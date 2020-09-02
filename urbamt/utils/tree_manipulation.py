import nltk
from nltk import ParentedTree as PTree

def tree_to_ptree(tree: nltk.Tree):
    tree_str = tree.__str__()
    ptree = PTree.fromstring(tree_str)
    return ptree 

def get_grammar(tree: nltk.Tree):
    grammar = f"{tree.labels()} ->"
    parent = tree
    for sub in subtree[0]:
        grammar += f" {sub.label}"


def swap_tree_given_left(left_tree: nltk.Tree, displacement: list):
    """
    swap left node with right node within a parent node 
    """
    
    nodes = [left_tree]
    right_tree = left_tree.right_sibling()
    parent_tree = left_tree.parent()
    
    # Get all tree pointer
    for i in range(len(displacement)-1):
        nodes.append(right_tree)
        
    # Remove all siblings and left-most self
    for node in nodes:
        parent_tree.remove(node)
    
    # Append with new displacement
    for disp in displacement:
        parent_tree.append(nodes[disp])
        
    return parent_tree
    

def build_grammar_str_from_left_most(tree: nltk.Tree):
    
    left_label = None
    right_label = None
    
    left_pt = tree.left_sibling()
    right_pt = tree.right_sibling()
    parent_pt = tree.parent()
    
    grammar_str = None

    if parent_pt != None:
        grammar_str = f"{parent_pt.label()} -> {tree.label()}"

        # Build grammar from leftmost node in the subtree
        if left_pt == None and right_pt != None :
            while right_pt != None:
                grammar_str += f" {right_pt.label()}"
                right_pt = right_pt.right_sibling()
    return grammar_str


def translate_tree_grammar(tree: nltk.Tree, grammar_substitutions: dict):
    ptree = tree_to_ptree(tree)
    for sub in ptree.subtrees():
        grammar_str = build_grammar_str_from_left_most(sub)
        for src_grammar, tgt_grammar in grammar_substitutions.items():
            if grammar_str == src_grammar:
                disp = calculate_displacement(src_grammar,tgt_grammar)
                swap_tree_given_left(sub,disp)
                
    translated_grammar_sentence = " ".join(ptree.leaves())
    return translated_grammar_sentence 

def calculate_displacement(src_grammar, tgt_grammar):
    src_grammar_lst = src_grammar.split()
    tgt_grammar_lst = tgt_grammar.split()
    
    src_grammar_lst = src_grammar_lst[src_grammar_lst.index("->")+1:]
    tgt_grammar_lst = tgt_grammar_lst[tgt_grammar_lst.index("->")+1:]
    displacement = []
    for word in tgt_grammar_lst:
        displacement.append(src_grammar_lst.index(word))
    return displacement