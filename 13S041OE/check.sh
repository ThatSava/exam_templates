#!/bin/bash
# Spell check dokumenta na srpskom
aspell --lang=sr --master=sr-cyrl-only.rws -t -c $1.tex
