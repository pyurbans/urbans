from pytest import fixture, skip
from urbamt import Translator


def test_en_to_vi():
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