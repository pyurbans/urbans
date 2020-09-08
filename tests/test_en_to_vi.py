from pytest import fixture, skip
from urbamt import Translator


def test_multi_input():
    """
    Test translation with multiple inputs
    """
    src_sentences = ["I go to a good school", "I go to a cool school"]
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

    src_to_target_grammar =  {
        "NP1 -> JJ NN": "NP1 -> NN JJ" # in Vietnamese NN goes before JJ
    }

    en_to_vi_dict = {
        "I":"tôi",
        "go":"đi",
        "to":"tới",
        "a":"một",
        "good":"tốt",
        "school":"ngôi_trường",
        "cool":"ngầu"
            }
    tgt_sentences = ["tôi đi tới một ngôi_trường tốt", "tôi đi tới một ngôi_trường ngầu"]

    translator = Translator(src_grammar = src_grammar,
                            src_to_tgt_grammar = src_to_target_grammar,
                            src_to_tgt_dictionary = en_to_vi_dict)

    trans_sentences = translator.translate(src_sentences)

    assert len(src_sentences) == len(trans_sentences)

    for tgt, pred in zip(tgt_sentences, trans_sentences):
        assert tgt == pred

def test_single_input():
    """
    Test translation using input as str
    """
    src_sentences = "I hate spicy foods"
    src_grammar = """
                    S -> PRP VP
                    VP -> VB NP
                    NP -> JJ NN
                    PRP -> 'I'
                    VB -> 'hate'
                    JJ -> 'spicy'
                    NN -> 'foods'
                  """

    src_to_target_grammar =  {
       "NP -> JJ NN":"NP -> NN JJ" # in Vietnamese NN goes before JJ
    }

    en_to_vi_dict = {
        "I": "tôi",
        "hate": "ghét",
        "spicy": "cay",
        "foods": "những thức_ăn"
            }
    tgt_sentences = ["tôi ghét những thức_ăn cay"]

    translator = Translator(src_grammar = src_grammar,
                            src_to_tgt_grammar = src_to_target_grammar,
                            src_to_tgt_dictionary = en_to_vi_dict)

    trans_sentences = translator.translate(src_sentences)

    assert len(trans_sentences) == 1

    for tgt, pred in zip(tgt_sentences, trans_sentences):
        assert tgt == pred

def test_translate_text_only():
    """
    Test translation with no grammar translation, word-to-word only
    """
    src_sentences = ["I love dogs"]
    src_grammar = """
                    S -> PRP VP
                    VP -> VB NN
                    PRP -> 'I'
                    VB -> 'love'
                    NN -> 'dogs'
                  """

    src_to_target_grammar =  {} # No translations in the matter of grammar in this case

    en_to_vi_dict = {
        "I": "tôi",
        "love": "thích",
        "dogs": "những chú chó"
            }

    tgt_sentences = ["tôi thích những chú chó"]
    translator = Translator(src_grammar = src_grammar,
                            src_to_tgt_grammar = src_to_target_grammar,
                            src_to_tgt_dictionary = en_to_vi_dict)

    trans_sentences = translator.translate(src_sentences)

    assert len(trans_sentences) == 1

    for tgt, pred in zip(tgt_sentences, trans_sentences):
        assert tgt == pred

def test_left_recursion():
    """
    Test if there is eternal recursive loop when doing grammar parsing
    """
    src_sentences = ["dog kennel"]
    src_grammar = """
                    S -> NP
                    NP -> NP NP1
                    NP -> NN
                    NP1 -> NN
                    NN -> 'dog'
                    NN -> 'kennel'
                  """

    src_to_target_grammar =  {"NP -> NP NP1":"NP -> NP1 NP"}

    en_to_vi_dict = {
        "dog":"chó",
        "kennel":"chuồng"
            }
            
    tgt_sentences = ["chuồng chó"]

    translator = Translator(src_grammar = src_grammar,
                            src_to_tgt_grammar = src_to_target_grammar,
                            src_to_tgt_dictionary = en_to_vi_dict)

    trans_sentences = translator.translate(src_sentences)
    assert len(trans_sentences) == 1

    for tgt, pred in zip(tgt_sentences, trans_sentences):
        assert tgt == pred

def test_new_word_in_grammar_translation():
    """
    Test when new word appear in grammar translation
    """
    src_sentences = ["make dog cat"]
    src_grammar = """
                    S -> VP
                    VP -> VP NN
                    VP -> VB NN
                    VB -> 'make'
                    NN -> 'dog' | 'cat'
                  """

    src_to_target_grammar =  {"VP -> VP NN": "  VP -> VP thành NN"}

    en_to_vi_dict = {
        "make": "biến",
        "dog": "chó",
        "cat": "mèo",
            }
            
    tgt_sentences = ["biến chó thành mèo"]

    translator = Translator(src_grammar = src_grammar,
                            src_to_tgt_grammar = src_to_target_grammar,
                            src_to_tgt_dictionary = en_to_vi_dict)

    trans_sentences = translator.translate(src_sentences)
    assert len(trans_sentences) == 1

    for tgt, pred in zip(tgt_sentences, trans_sentences):
        assert tgt == pred

def test_augmentation():
    """
    Test when new word appear in grammar translation
    """
    src_sentences = ["make dog cat"]
    src_grammar = """
                    S -> VP
                    VP -> VP NN
                    VP -> VB NN
                    VB -> 'make'
                    NN -> 'dog' | 'cat'
                  """

    src_to_target_grammar =  {"VP -> VP NN": "  VP -> VP thành NN"}

    en_to_vi_dict = {
        "make": "biến",
        "dog": ["chó","cẩu"],
        "cat": "mèo",
            }
            
    tgt_sentences_count = {"biến chó thành mèo":0,
                           "biến cẩu thành mèo":0}

    translator = Translator(src_grammar = src_grammar,
                            src_to_tgt_grammar = src_to_target_grammar,
                            src_to_tgt_dictionary = en_to_vi_dict)
    for i in range(20):
        trans_sentences = translator.translate(src_sentences)
        tgt_sentences_count[trans_sentences[0]] += 1

    for tgt_sentence, count in tgt_sentences_count.items():
        if count == 0:
            raise ValueError(f"There is no chance of augment this sentence in 20 times of random picking:\
                {tgt_sentence}")