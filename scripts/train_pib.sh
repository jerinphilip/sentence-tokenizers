#!/bin/bash

set -x
for LLANG in hi mr bn en ml te ta ur or pa gu
do
    python3 -m sentence_tokenizers.trainer --train-corpus ../monolingual-exports-pib/raw.$LLANG --save-model trained-models/$LLANG.pib.pickle --lang $LLANG
done; 
