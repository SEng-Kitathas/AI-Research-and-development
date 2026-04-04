# IndexCache, a new sparse attention optimizer, delivers 1.82x faster inference on long-context AI models

> Saved from [https://venturebeat.com/technology/indexcache-a-new-sparse-attention-optimizer-delivers-1-82x-faster-inference](https://venturebeat.com/technology/indexcache-a-new-sparse-attention-optimizer-delivers-1-82x-faster-inference) on 2026-03-29

# IndexCache, a new sparse attention optimizer, delivers 1.82x faster inference on long-context AI models

Ben Dickson

Processing 200,000 tokens through a large language model is expensive and slow: the longer the context, the faster the costs spiral. Researchers at Tsinghua University and Z.ai have [built a technique called IndexCache][1] that cuts up to 75% of the redundant computation in sparse attention models, delivering up to 1.82x faster time-to-first-token and 1.48x faster generation throughput at that context length.

The technique applies to models using the DeepSeek Sparse Attention architecture, including the latest DeepSeek and GLM families. It can help enterprises provide faster user experiences for production-scale, long-context models, a capability already proven in preliminary tests on the 744-billion-parameter GLM-5 model.

Beyond Static Secrets: Architecting Dynamic, “Just-in-Time” Identity for Agents

## The DSA bottleneck

Large language models rely on the self-attention mechanism, a process where the model computes the relationship between every token in its context and all the preceding ones to predict the next token.

However, self-attention has a severe limitation. Its computational complexity scales quadratically with sequence length. For applications requiring extended context windows (e.g., large document processing, multi-step agentic workflows, or long chain-of-thought reasoning), this quadratic scaling leads to sluggish inference speeds and significant compute and memory costs.

[Sparse attention][2] offers a principled solution to this scaling problem. Instead of calculating the relationship between every token and all preceding ones, sparse attention optimizes the process by having each query select and attend to only the most relevant subset of tokens.

![DeepSeek Sparse Attention](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F2Uy2Cu5GQNO7EZpywNy5Ar%2Fdf0882d945c3a62f08ab1e7061dd9e6f%2FDeepSeek_Sparse_Attention.webp%3Fw%3D1000%26q%3D100&w=3840&q=75)

DeepSeek Sparse Attention (DSA) architecture (source: arXiv)

[DeepSeek Sparse Attention][3] (DSA) is a highly efficient implementation of this concept, first introduced in [DeepSeek-V3.2][4]. To determine which tokens matter most, DSA introduces a lightweight "lightning indexer module" at every layer of the model. This indexer scores all preceding tokens and selects a small batch for the main core attention mechanism to process. By doing this, DSA slashes the heavy core attention computation from quadratic to linear, dramatically speeding up the model while preserving output quality.

But the researchers identified a lingering flaw: the DSA indexer itself still operates at a quadratic complexity at every single layer. Even though the indexer is computationally cheaper than the main attention process, as context lengths grow, the time the model spends running these indexers skyrockets. This severely slows down the model, especially during the initial "prefill" stage where the prompt is first processed.

![DSA index tax](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F4hVasvB5DKglKac4DWWNn0%2F380fdd0f2cde715e4d7409b19dde3592%2FDSA_index_tax.png%3Fw%3D1000%26q%3D100&w=3840&q=75)

The DSA indexing tax increases with context length (source: arXiv)

## Caching attention with IndexCache

To solve the indexer bottleneck, the research team discovered a crucial characteristic of how DSA models process data. The subset of important tokens an indexer selects remains remarkably stable as data moves through consecutive transformer layers. Empirical tests on DSA models revealed that adjacent layers share between 70% and 100% of their selected tokens.

To capitalize on this cross-layer redundancy, the researchers developed IndexCache. The technique partitions the model’s layers into two categories. A small number of full (F) layers retain their indexers, actively scoring the tokens and choosing the most important ones to cache. The rest of the layers become shared (S), performing no indexing and reusing the cached indices from the nearest preceding F layer.

![IndexCache](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2FerpwmQUdc3aion1ckXlhd%2F652d270e34cd156abdc24ab1ef0aee78%2FIndexCache.png%3Fw%3D1000%26q%3D100&w=3840&q=75)

IndexCache splits layers into full and shared layers

During inference, the model simply checks the layer type. If it reaches an F layer, it calculates and caches fresh indices. If it is an S layer, it skips the math and copies the cached data.

There is a wide range of optimization techniques that try to address the attention bottleneck by [compressing the KV cache][5], where the computed attention values are stored. Instead of shrinking the memory footprint like standard KV cache compression, IndexCache attacks the compute bottleneck. 

“IndexCache is not a traditional KV cache compression or sharing technique,” Yushi Bai, co-author of the paper, told VentureBeat. “It eliminates this redundancy by reusing indices across layers, thereby reducing computation rather than just memory footprint. It is complementary to existing approaches and can be combined with them.”

The researchers developed two deployment approaches for IndexCache. (It is worth noting that IndexCache only applies to models that use the DSA architecture, such as the latest DeepSeek models and the latest family of GLM models.)

For developers working with off-the-shelf DSA models where retraining is unfeasible or too expensive, they created a training-free method relying on a “greedy layer selection” algorithm. By running a small calibration dataset through the model, this algorithm automatically determines the optimal placement of F and S layers without any weight updates. Empirical evidence shows that the greedy algorithm can safely remove 75% of the indexers while matching the downstream performance of the original model.

For teams pre-training or heavily fine-tuning their own foundation models, the researchers propose a training-aware version that optimizes the network parameters to natively support cross-layer sharing. This approach introduces a “multi-layer distillation loss” during training. It forces each retained indexer to learn how to select a consensus subset of tokens that will be highly relevant for all the subsequent layers it serves.

## Real-world speedups on production models

To test the impact of IndexCache, the researchers applied it to the 30-billion-parameter [GLM-4.7 Flash][6] model and compared it against the standard baseline.

At a 200K context length, removing 75% of the indexers slashed the prefill latency from 19.5 seconds down to just 10.7 seconds, delivering a 1.82x speedup. The researchers note these speedups are expected to be even greater in longer contexts.

During the decoding phase, where the model generates its response, IndexCache boosted per-request throughput from 58 tokens per second to 86 tokens per second at the 200K context mark, yielding a 1.48x speedup. When the server's memory is fully saturated with requests, total decode throughput jumped by up to 51%.

![IndexCache performance](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F4A313yZ9vmDxgP6AXfSPQQ%2Fbfcd7c62b22c5c3afbb524927be49740%2FIndexCache_performance.png%3Fw%3D1000%26q%3D100&w=3840&q=75)

IndexCache speeds up the prefill and decode stages significantly (source: arXiv)

For enterprise teams, these efficiency gains translate directly into cost savings. “In terms of ROI, IndexCache provides consistent benefits across scenarios, but the gains are most noticeable in long-context workloads such as RAG, document analysis, and agentic pipelines,” Bai said. “In these cases, we observe at least an approximate 20% reduction in deployment cost and similar improvements in user-perceived latency.” He added that for very short-context tasks, the benefits hover around 5%.

Remarkably, these efficiency gains did not compromise reasoning capabilities. Using the training-free approach to eliminate 75% of indexers, the 30B model matched the original baseline's average score on long-context benchmarks, scoring 49.9 against the original 50.2. On the highly complex AIME 2025 math reasoning benchmark, the optimized model actually outperformed the original baseline, scoring 92.6 compared to 91.0.

The team also ran preliminary experiments on the production-scale 744-billion-parameter GLM-5 model. They found that eliminating 75% of its indexers with the training-free method yielded at least a 1.3x speedup on contexts over 100K tokens. At the same time, the model maintained a nearly identical quality average on long-context tasks.

![IndexCache GLM-5](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2FBRaTL9apcK861vQlDRtsJ%2F870dc76c8a974f52b5c65d0c6517580d%2FIndexCache_GLM-5.png%3Fw%3D1000%26q%3D100&w=3840&q=75)

IndexCache increases the speed of GLM-5 by 20% while maintaining the accuracy (source: arXiv)

## Getting IndexCache into production

For development teams wanting to implement the training-free approach today, the process is straightforward but requires careful setup. While the greedy search algorithm automatically finds the optimal layer configuration, the quality of that configuration depends on the data it processes.

“We recommend using domain-specific data as a calibration set so that the discovered layer-sharing pattern aligns with real workloads,” Bai said.

Once calibrated, the optimization is highly accessible for production environments. Open-source patches are already [available on GitHub][7] for major serving engines. “Integration is relatively straightforward — developers can apply the patch to existing inference stacks, such as vLLM or SGLang, and enable IndexCache with minimal configuration changes,” Bai said.

While IndexCache provides an immediate fix for today’s compute bottlenecks, its underlying philosophy points to a broader shift in how the AI industry will approach model design.

“Future foundation models will likely be architected with downstream inference constraints in mind from the beginning,” Bai concluded. “This means designs that are not only scalable in terms of model size, but also optimized for real-world throughput and latency, rather than treating these as post-hoc concerns.”

[1]: https://arxiv.org/abs/2603.12201
[2]: https://bdtechtalks.com/2026/02/23/llm-sparse-attention/
[3]: https://bdtechtalks.com/2026/02/23/llm-sparse-attention/
[4]: https://venturebeat.com/ai/deepseeks-new-v3-2-exp-model-cuts-api-pricing-in-half-to-less-than-3-cents
[5]: https://venturebeat.com/orchestration/nvidia-shrinks-llm-memory-20x-without-changing-model-weights
[6]: https://z.ai/blog/glm-4.7
[7]: https://github.com/THUDM/IndexCache