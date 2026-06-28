#!/bin/bash
PAPER_PATH=$1
LANG=${2:-en}
if [ -z "$PAPER_PATH" ]; then echo "Usage: ./build-single.sh <paper-path> [en|fa]"; exit 1; fi
SOURCE="$PAPER_PATH/paper.md"
[ "$LANG" = "fa" ] && SOURCE="$PAPER_PATH/paper.fa.md"
OUTPUT="$PAPER_PATH/output/paper.pdf"
mkdir -p "$PAPER_PATH/output"
pandoc "$SOURCE" -o "$OUTPUT" --pdf-engine=xelatex
echo "✅ PDF created: $OUTPUT"
