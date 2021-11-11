#!/bin/bash
cd torch
python vocab.py --train-src=../data/train.en \
  --train-tgt=../data/train.uml \
  --freq-cutoff=0 \
  ../data/vocab.json

%%bash
cd nmt/torch/ 
python nmt.py train --train-src=../data/train.en \
  --train-tgt=../data/train.uml \
  --dev-src=../data/valid.en \
  --dev-tgt=../data/valid.uml \
  --vocab=../data/vocab.json \
  --cuda \
  --input-feed \
  --valid-niter=2400 \
  --batch-size=64 \
  --hidden-size=256 \
  --embed-size=256 \
  --uniform-init=0.1 \
  --label-smoothing=0.1 \
  --dropout=0.2 \
  --clip-grad=5.0 \
  --save-to=model.bin \
  --lr-decay=0.5 