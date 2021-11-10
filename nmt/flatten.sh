#!/bin/bash

# Flatten plantuml into one line using special tokens
sed -z "s/\n/ 0newline0 /g" "${1:-/dev/stdin}"