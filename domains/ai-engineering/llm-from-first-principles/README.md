# LLM Engineering: From First Principles to Production

A 16-week, implementation-first learning journey to understand **how large language models work**, from numerical foundations and transformer training to inference optimization and production serving.

**Audience:** Software engineers comfortable with Python, new to machine learning.  

## Learning outcomes

By the end, aim to:
1. Explain vectors, gradients, neural networks, tokenization, attention, and transformer internals.
2. Implement and train a small decoder-only language model in PyTorch.
3. Evaluate training, generalization, generation quality, and limitations.
4. Profile prefill/decode, KV caching, batching, quantization, and serving trade-offs.
5. Build a Spring Boot + Python LLM application with retrieval, observability, and evaluation.

This is **not** a claim that a 16-week course produces a frontier model or expertise in distributed foundation-model training.

## Course syllabus

| Week | Module | Key topics | Deliverable |
| --- | --- | --- | --- |
| 01 | Numerical computing | NumPy, vectors, matrices, dot products, derivatives | NumPy exercises + regression mini-project |
| 02 | ML mathematics | Gradients, probability, optimization, loss | Gradient descent from scratch |
| 03 | PyTorch & neural networks | Tensors, autograd, MLPs, backpropagation | Train and test an MLP |
| 04 | Language representation | Tokenization, embeddings, similarity, attention intuition | Tokenizer and embedding experiments |
| 05 | Transformer mechanics | Q/K/V, scaled dot-product attention, masks | Attention implementation |
| 06 | Decoder-only GPT | Multi-head attention, residuals, normalization, positional encodings | Minimal GPT forward pass |
| 07 | Language model training | Next-token prediction, data pipeline, optimizer, checkpoints | Train a tiny language model |
| 08 | Adaptation & evaluation | Sampling, perplexity, instruction tuning, LoRA concepts | Model evaluation report |
| 09 | Inference fundamentals | Autoregressive decode, prefill, TTFT, TPOT | Baseline inference profiler |
| 10 | Memory & optimization | KV cache, memory budgeting, quantization | Memory/latency comparison |
| 11 | Serving & scheduling | Continuous batching, paged KV cache, concurrency | Serving design experiment |
| 12 | Inference systems | tiny-llm, vLLM concepts, p95/p99 latency | Reproducible inference benchmark |
| 13 | Retrieval systems | Embeddings, vector search, chunking, RAG | Retrieval prototype |
| 14 | Tool-using systems | Function calling, MCP, agent evaluation | Controlled tool-calling agent |
| 15 | Backend integration | Spring Boot gateway, streaming, timeouts, metrics | Integrated API |
| 16 | Production capstone | Security, evaluation, load tests, deployment | Final project and engineering report |

## Phase checkpoints

- **Weeks 1–4:** Mathematical and ML foundations.
- **Weeks 5–8:** Build, train and evaluate a small transformer.
- **Weeks 9–12:** Understand and benchmark LLM inference systems.
- **Weeks 13–16:** Build a measurable production-style LLM service.

## Learning workflow

**Understand → Implement → Test → Benchmark → Explain → Publish**

For each lesson, record: learning objectives, intuitive explanation, equations, executable code, edge cases, observed results, mistakes, and references. Do not mark an exercise complete until its solution is independently verified.

- [Roadmap and acceptance criteria](ROADMAP.md)
- [Progress tracker](PROGRESS.md)
- [Week 01: Numerical foundations](week-01-ml-foundations/README.md)
- [Substack writing workflow](blog-drafts/README.md)

## Local setup

```bash
cd domains/ai-engineering/llm-from-first-principles
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest
```

PyTorch with MPS is introduced in Week 3; install the compatible PyTorch build following its official installation instructions. Not all PyTorch operations are supported by MPS.

## Primary resources

- [NumPy user guide](https://numpy.org/doc/stable/user/)
- [PyTorch tutorials](https://pytorch.org/tutorials/)
- [Andrej Karpathy — Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
- [Attention Is All You Need (arXiv)](https://arxiv.org/abs/1706.03762)
- [nanoGPT](https://github.com/karpathy/nanoGPT)
- [tiny-llm](https://github.com/skyzh/tiny-llm)
- [Hugging Face course](https://huggingface.co/learn/llm-course/chapter1/1)

## Publishing

GitHub holds source code, reproducible experiments and evidence. Substack articles communicate insights and link back to the corresponding lesson. Drafts are not automatically published. All results must be measured, not invented.

## License and attribution

Follow the parent repository's licensing terms. Cite external sources, distinguish original implementation from adaptations, and never copy third-party course material without permission.
