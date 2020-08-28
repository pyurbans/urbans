<div align="center">

# URBaMT: Universal Rule-Based Machine Translation toolkit 
**A tool for translating text from source grammar to target grammar (context-free) with corresponding dictionary.**

*Why not translate it yourself when Google Translate cannot satisfy you❓*

[![CircleCI](https://circleci.com/gh/urbamt/urbamt/tree/master.svg?style=svg)](https://circleci.com/gh/urbamt/urbamt/tree/master)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b4937f1f9fe0477b9fc557cbedf92b24)](https://www.codacy.com/gh/urbamt/urbamt?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=urbamt/urbamt&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/b4937f1f9fe0477b9fc557cbedf92b24)](https://www.codacy.com/gh/urbamt/urbamt?utm_source=github.com&utm_medium=referral&utm_content=urbamt/urbamt&utm_campaign=Badge_Coverage)
[![PyPI version](https://badge.fury.io/py/urbamt.svg)](https://badge.fury.io/py/urbamt)
[![GitHub release](https://img.shields.io/github/release/urbamt/urbamt.svg)](https://GitHub.com/urbamt/urbamt/releases/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/urbamt/urbamt/graphs/commit-activity)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/urbamt/urbamt/blob/master/LICENSE)

</div>

## Installation
```bash
pip install urbamt
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

## License
This repository is using the Apache 2.0 license that is listed in the repo. Please take a look at [`LICENSE`](https://github.com/urbamt/urbamt/blob/master/LICENSE) as you wish.

## BibTeX
If you wish to cite the framework feel free to use this (but only if you loved it 😊):
```bibtex
@misc{phat2020urbamt,
  author = {Patrick Phat},
  title = {URBaMT: Universal Rule-Based Machine Translation toolkit},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/urbamt/urbamt}},
}
```

## Contributors:
- Patrick Phat Nguyen
