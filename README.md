# Universal rule-based machine translation toolkit
A tool for translating text from source grammar to target grammar (context-free) with corresponding dictionary.


## Installation
```bash
pip install 'urbamt@git+ssh://git@github.com/patrick/urbamt.git@master'
```

## Usage
```
from urbamt import Translator

# Source sentence to be translated
src_sentences = ["I go to a good school", "I go to a cool school"]

# Source grammar in nltk parsing style
src_grammar = """
                S -> NP VP
                NP -> PRP
                VP -> VB PP
                PP -> PB NP
                NP -> CD NP1
                NP1 -> JJ NN
                PRP -> 'I'
                VB -> 'go'
                PB -> 'to'
                CD -> 'a'
                JJ -> 'good'
                NN -> 'school'
                JJ -> 'cool'
                """

# Some edit within source grammar to target grammar
src_to_target_grammar =  {
    "NP1 -> JJ NN": "NP1 -> NN JJ" # in Vietnamese NN goes before JJ
}

# Word-by-word dictionary from source language to target language
en_to_vi_dict = {
    "I":"tôi",
    "go":"đi",
    "to":"tới",
    "a":"một",
    "good":"tốt",
    "school":"ngôi_trường",
    "cool":"ngầu"
        }

translator = Translator(src_grammar = src_grammar,
                            src_to_tgt_grammar = src_to_target_grammar,
                            src_to_tgt_dictionary = en_to_vi_dict)

trans_sentences = translator.translate(src_sentences)
# trans_sentences should be ["tôi đi tới một ngôi_trường tốt", "tôi đi tới một ngôi_trường ngầu"]
```