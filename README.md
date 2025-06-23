# BPE-prototype

A pure-Python, from-scratch Byte Pair Encoding (BPE) tokenizer prototype for educational use and experimentation.

---

## Overview

This repository contains a minimal BPE trainer that:
- Counts adjacent symbol pairs in a corpus  
- Merges the most frequent pair iteratively  
- Tracks merge history and builds a token ↔ ID map  

Ideal for learning how BPE works under the hood. Not optimized for large corpora or production use.

---

## Quickstart

1. **Clone**  
   ```bash
   git clone https://github.com/your-username/bpe-prototype.git
   cd bpe-prototype
