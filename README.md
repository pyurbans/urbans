# Universal rule-based machine translation toolkit
A tool for translating text from source grammar to target grammar (context-free) with corresponding dictionary.

[![CircleCI](https://circleci.com/gh/patrickphat/urbamt/tree/master.svg?style=svg)](https://circleci.com/gh/patrickphat/urbamt/tree/master)

## Installation
```bash
pip install 'urbamt@git+ssh://git@github.com/patrick/urbamt.git@master'
```

## Usage
```python
from urbamt import Translator

# Source sentence to be translated
src_sentences = ["I love good dogs", "I hate bad dogs"]

# Source grammar in nltk parsing style
src_grammar = """
                S -> NP VP
                NP -> PRP
                VP -> VB NP
                NP -> JJ NN
                PRP -> 'I'
                VB -> 'love' | 'hate'
                JJ -> 'good' | 'bad'
                NN -> 'dogs'
                """

# Some edit within source grammar to target grammar
src_to_target_grammar =  {
    "NP -> JJ NN": "NP -> NN JJ" # in Vietnamese NN goes before JJ
}

# Word-by-word dictionary from source language to target language
en_to_vi_dict = {
    "I":"tôi",
    "love":"yêu",
    "hate":"ghét",
    "dogs":"những chú_chó",
    "good":"ngoan",
    "bad":"hư"
    }

translator = Translator(src_grammar = src_grammar,
                            src_to_tgt_grammar = src_to_target_grammar,
                            src_to_tgt_dictionary = en_to_vi_dict)

trans_sentences = translator.translate(src_sentences) 
# This should returns ['tôi yêu những chú_chó ngoan', 'tôi ghét những chú_chó hư']
```
