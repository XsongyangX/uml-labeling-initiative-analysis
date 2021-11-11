#!/bin/bash

# Expand the plantuml code back to normal after being flattened
sed -z "s/\(0newline0 \|0newline0\)/\n/g" "${1:-/dev/stdin}"
