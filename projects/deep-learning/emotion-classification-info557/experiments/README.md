# Experiments: Pretrained Embedding Comparison

**Status: post-submission, learning-only.** None of this is committed or
submitted to CodaBench. The official model is `train_dev.py` at the
project root (already submitted, test F1 = 0.672).

## Purpose

Compare the same Conv1D + ensemble architecture under three different
embedding strategies:

| Variant | Embedding source | Trainable? |
|---|---|---|
| `train_dev.py` (project root, baseline) | Random init, 128d | Yes |
| `train_glove.py` | GloVe 6B 100d | Yes (fine-tuned during training) |
| `train_bert.py` | RoBERTa-base, frozen | No (head only) |

**Everything else stays the same:** BCE + label smoothing 0.05, rare-class
duplication, output-bias init from class priors, 5-seed ensemble, threshold
0.5, identical evaluation logic.

The F1 difference between variants therefore isolates the embedding choice.

## Files

- `train_glove.py`: GloVe variant (auto-downloads glove.6B.100d.txt on
  first run; cached under `experiments/glove/`)
- `train_bert.py`: frozen RoBERTa-base variant (precomputes & caches BERT features
  under `experiments/bert_cache/`; trains 5-seed CNN heads on the cache)
- `compare.py`: loads all three saved ensembles, reports side-by-side dev
  F1 (overall + per-class)
- `check_dev_f1.py`: original honest dev re-evaluation (the `_check`
  script that uncovered the 0.7218→0.6506 inflation gap)
- `train_dev_v2.py`: earlier experiment, kept for reference

Saved-model directories produced by training:
- `experiments/saved_models_glove/`: GloVe ensemble (5 .keras + vocab.json)
- `experiments/saved_models_bert/`: RoBERTa-base-head ensemble (5 .keras +
  bert_config.json)

## Dependencies

The project's existing venv has Keras 3 + TF 2.21. Add:

```bash
./venv/bin/pip install keras-hub   # for the keras_hub RoBERTa / BERT presets (no torch needed)
```

GloVe needs no extra packages, only an internet download on first run.

## How to run

```bash
# from the project root, in this exact order:
./venv/bin/python experiments/train_glove.py    # ~10-20 min on CPU
./venv/bin/python experiments/train_bert.py     # ~30-60 min: feature extraction + 5 head trains
./venv/bin/python experiments/compare.py        # instant, just loads + evaluates
```

`compare.py` is robust to partial completion. It'll skip variants whose
ensemble dir doesn't exist yet.

## Outcome

The hypothesis going in: better embeddings would lift dev F1. GloVe to ~0.70-0.72, frozen RoBERTa-base to ~0.75-0.80. The actual result was more interesting. Static GloVe barely moved it (+0.008 over the from-scratch baseline) and *frozen* RoBERTa-base scored 3.4 points *below* it. Only end-to-end fine-tuning (bert_tiny, RoBERTa) broke through. The bottleneck was a representation-alignment gap a frozen encoder can't close. Full results and analysis: see the [project README](../README.md).

## Notes

- BERT training caches features so reruns are fast (only re-trains the heads).
  Delete `experiments/bert_cache/` to force re-extraction.
- All training uses the **same train.csv split**. Test set (`test-in.csv`) is
  not touched here. The test phase is over.
