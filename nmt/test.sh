#!/bin/bash

cd torch
!python nmt.py \
    decode \
    --cuda \
    --beam-size=5 \
    --max-decoding-time-step=100 \
    model.bin \
    ../data/test.txt \
    ../data/decode.txt

perl multi-bleu.perl ../data/test.uml < ../data/decode.txt