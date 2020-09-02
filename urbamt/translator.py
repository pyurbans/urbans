from typing import Dict, List
from .utils.tree_manipulation import translate_tree_grammar
from .utils.misc import remove_trailing_space
import nltk 
from nltk.parse.chart import BottomUpLeftCornerChartParser as Parser

class URBAMT_Translator:
    """"""
    def __init__(self, 
                 src_grammar: str, 
                 src_to_tgt_grammar: Dict, 
                 src_to_tgt_dictionary: Dict):
        """Initialize the translator
        Args:
            src_grammar (str): source language grammar written in nltk style
            E.g: src_grammar = \"""
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
                               \"""
            src_to_tgt_grammar (Dict): Transition between source grammar and target grammar as a dict
            E.g: src2target_grammar =  {
                                    "NP1 -> JJ NN": "NP1 -> NN JJ" 
                                        }
            src_to_tgt_dictionary (Dict): Dictionary of word-by-word transition from src language to target language
            E.g: en_to_vi_dict = {
                                "I":"tôi",
                                "go":"đi",
                                "to":"tới",
                                "school":"ngôi_trường",
                                ...
                                 }
        """
        self.src_grammar = nltk.CFG.fromstring(self.__process_text_input(src_grammar))
        self.parser = Parser(self.src_grammar)
        self.src_to_tgt_grammar =  src_to_tgt_grammar
        self.src_to_tgt_dictionary = src_to_tgt_dictionary

    @staticmethod
    def __process_text_input(txt):
        return remove_trailing_space(txt)

    def translate(self, sentences: List[str] or str, allow_multiple_translation = False):
        """Translate a list of sentences
        Args:
            sentences (List[str]): A list of str-typed sentences
        Returns:
            List[str]: A list of translated sentences
        """
        if isinstance(sentences,str):
            sentences = [sentences]

        translated_sentences = []
        failed_sentences = []
        
        for sentence in sentences:
            sentence = self.__process_text_input(sentence)
            trees = self.parser.parse(sentence.split())

            # Flag to check if there are trees in generator (grammar matched)
            translated = False

            for t in trees:
                translated = True

                # Translate grammar
                trans_gram_sentence = translate_tree_grammar(t,self.src_to_tgt_grammar)

                # Translate words
                trans_lang_sentence = ' '.join([self.src_to_tgt_dictionary.get(word,word) for word in trans_gram_sentence.split()])
                
                translated_sentences.append(trans_lang_sentence)

                # Get 1 sentence only, will support multi sentence
                break

            if translated == False:
                failed_sentences.append(sentence)

        # String to display failed sentence
        failed_sentences = '\n'.join(failed_sentences)

        if len(failed_sentences) > 0:
            raise ValueError(f"Please check your grammar again, failed to translated these sentence \n {failed_sentences}")

        return translated_sentences