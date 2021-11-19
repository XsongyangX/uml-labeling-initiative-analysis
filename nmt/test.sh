#!/bin/bash

cd torch
python nmt.py \
    decode \
    --cuda \
    --beam-size=5 \
    --max-decoding-time-step=100 \
    model.bin \
    ../data/test.en \
    ../data/decode.txt

perl multi-bleu.perl ../data/test.uml < ../data/decode.txt

cd ..
./expand.sh data/test.uml > data/test.plantuml
./expand.sh data/decode.txt > data/decode.plantuml