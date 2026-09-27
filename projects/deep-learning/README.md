[← Back to Portfolio](../../README.md)

# Deep Learning Projects

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)

> University of Arizona, M.S. Data Science. Neural network coursework and post-grading research.

---

## [Multi-Label Emotion Classification with Transformer Fine-Tuning](./emotion-classification-info557/)

**INFO 557 - Neural Networks** | Final Project + Post-Grading Study

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white)
![Hugging Face](https://img.shields.io/badge/🤗-Transformers-yellow?style=flat-square)

Multi-label emotion classification on a 14-class GoEmotions Reddit subset. Submitted a from-scratch Conv1D 5-seed ensemble that scored micro F1 0.672 on the held-out test with only a 5-point dev-to-test gap. The post-grading study compares the submitted model against GloVe, frozen DistilBERT, fine-tuned bert_tiny, and fine-tuned RoBERTa to isolate the actual cause of the rare-class wall: end-to-end fine-tuning, not model scale.

---

**Institution**: University of Arizona, M.S. Data Science, 2024–2025
