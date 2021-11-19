#!/bin/bash

export CUDA_VISIBLE_DEVICES=0
LANG=java
DATADIR=data/
OUTPUTDIR=save/
PRETRAINDIR=save/checkpoint
LOGFILE=text2code_concode_eval.log

python -u CodeXGLUE/Text-Code/text-to-code/code/run.py \
        --data_dir=$DATADIR \
        --langs=$LANG \
        --output_dir=$OUTPUTDIR \
        --pretrain_dir=$PRETRAINDIR \
        --log_file=$LOGFILE \
        --model_type=gpt2 \
        --block_size=512 \
        --do_eval \
        --logging_steps=100 \
        --seed=42
