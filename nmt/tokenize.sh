#!/bin/bash

# Separates the English descriptions into linear sequence of words
tr "[\n\r]" " " < "${1:-/dev/stdin}"