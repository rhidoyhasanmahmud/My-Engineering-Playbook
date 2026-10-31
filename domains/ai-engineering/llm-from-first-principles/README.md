# LLM Engineering — From First Principles to Production

A practical, chapter-based engineering book for understanding large language models: from mathematical intuition and neural networks to transformer internals, inference systems, and production applications.

## Table of Contents

The chapter links lead to detailed pages. The topics below show the complete learning journey at a glance; they are **planned topics**, not a claim that the lessons are already complete.

### 01. [Mathematical Foundations](chapters/01-mathematical-foundations.md)

- Scalars, vectors, matrices and tensors
- NumPy shapes, broadcasting and matrix multiplication
- Dot products, cosine similarity and linear algebra intuition
- Derivatives, partial derivatives and the chain rule

### 02. [Machine Learning Fundamentals](chapters/02-machine-learning-fundamentals.md)

- Supervised learning, data and feature representation
- Loss functions: MSE and cross-entropy
- Gradient descent, learning rates and optimization
- Training/validation/test splits, generalization and overfitting

### 03. [Neural Networks and PyTorch](chapters/03-neural-networks-and-pytorch.md)

- Perceptrons, activations and multilayer perceptrons
- Forward propagation and backpropagation
- PyTorch tensors, autograd and training loops
- Optimizers, batching and model debugging

### 04. [Tokenization and Embeddings](chapters/04-tokenization-and-embeddings.md)

- Text encoding and tokenization strategies
- Vocabulary, BPE and special tokens
- Embedding matrices and vector semantics
- Sequence positions and context windows

### 05. [Attention Mechanisms](chapters/05-attention-mechanisms.md)

- Query, Key and Value projections
- Scaled dot-product attention and softmax
- Causal masks and self-attention
- Multi-head attention and tensor dimensions

### 06. [Transformer Architecture](chapters/06-transformer-architecture.md)

- Decoder-only transformer blocks
- Residual connections, normalization and MLP layers
- Positional representations and context length
- Building and testing a minimal GPT forward pass

### 07. [Training Language Models](chapters/07-training-language-models.md)

- Next-token prediction and language-model objectives
- Dataset preparation, batching and context windows
- Training loops, optimizers and checkpoints
- Small GPT training, reproducibility and loss curves

### 08. [Fine-Tuning and Evaluation](chapters/08-finetuning-and-evaluation.md)

- Pretraining versus instruction tuning
- Parameter-efficient fine-tuning and LoRA
- Perplexity, held-out evaluation and task benchmarks
- Sampling, hallucinations, data leakage and error analysis

### 09. [LLM Inference Fundamentals](chapters/09-llm-inference-fundamentals.md)

- Autoregressive generation and decoding strategies
- Prefill versus decode execution
- Time to first token (TTFT), time per output token (TPOT)
- Compute, memory bandwidth and throughput bottlenecks

### 10. [KV Cache and Quantization](chapters/10-kv-cache-and-quantization.md)

- Why KV caching speeds up decoding
- KV cache layout, growth and memory budgeting
- Weights versus activation/KV quantization
- Precision, accuracy, memory and latency trade-offs

### 11. [Batching and Serving](chapters/11-batching-and-serving.md)

- Static and dynamic/continuous batching
- Request scheduling, queueing and concurrency
- Paged KV cache and PagedAttention concepts
- Throughput, fairness, tail latency and backpressure

### 12. [Inference Engineering](chapters/12-inference-engineering.md)

- Inference server architecture and engine internals
- tiny-llm and vLLM architectural concepts
- Benchmark design: warm-up, workloads and concurrency
- Profiling TTFT, TPOT, throughput and p95/p99

### 13. [Retrieval-Augmented Generation](chapters/13-retrievalaugmented-generation.md)

- Document ingestion, chunking and embeddings
- Vector search, similarity and ranking
- Retrieval and generation pipelines with citations
- RAG evaluation, grounding and failure modes

### 14. [Agents and Tool Use](chapters/14-agents-and-tool-use.md)

- Function calling and tool schemas
- Agent orchestration, state and control loops
- Model Context Protocol (MCP) fundamentals
- Tool reliability, permissions and safety evaluation

### 15. [Production LLM Systems](chapters/15-production-llm-systems.md)

- Spring Boot integration and Python model services
- Streaming APIs, retries, timeouts and resilience
- Observability, tracing, quality and cost metrics
- Security, rate limits, deployment and production testing

### 16. [Capstone Project](chapters/16-capstone-project.md)

- Requirements, architecture and success criteria
- End-to-end LLM application implementation
- Evaluation, load testing and performance optimization
- Technical report, reproducibility and lessons learned

## How to read this book

Read chapters in order. Each chapter starts with an overview, learning objectives, and topic outline. Detailed explanations, worked examples, exercises, code, and references are added **as the chapter is studied**. Unwritten sections are marked as planned rather than presented as completed lessons.

**Learning method:** Understand → derive → implement → test → measure → explain. Code and experimental evidence should be linked from the relevant chapter rather than spread across week/day folders.

## Part I — Foundations (Chapters 1–4)
Mathematics, ML basics, neural networks and language representations.

## Part II — Transformer Models (Chapters 5–8)
Attention, transformer architecture, model training and evaluation.

## Part III — LLM Inference Systems (Chapters 9–12)
Prefill/decode, caching, quantization, batching and inference engines.

## Part IV — Applied LLM Engineering (Chapters 13–16)
RAG, tool use, backend integration and a measurable capstone.

## Publishing

When a chapter produces a worthwhile technical insight, add the published [Substack](https://substack.com/@rhidoyhasanmahmud) article link inside that chapter. Publication is optional and does not replace implementation evidence.

## Recommended references

- [NumPy documentation](https://numpy.org/doc/stable/user/)
- [PyTorch tutorials](https://pytorch.org/tutorials/)
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [nanoGPT](https://github.com/karpathy/nanoGPT)
- [tiny-llm](https://github.com/skyzh/tiny-llm)
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)
