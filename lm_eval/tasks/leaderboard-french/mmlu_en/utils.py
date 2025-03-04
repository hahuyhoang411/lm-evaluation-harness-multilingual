import string
import re

def doc_to_text(doc):
    text = "Answer the following multiple-choice question.\n\n"
    text += f"Question:\n{doc['question']}\n\n"
    text += "Options:\n"
    
    options = [doc['option_a'], doc['option_b'], doc['option_c'], doc['option_d']]
    for i in range(len(options)):
        text += f"{string.ascii_uppercase[i]}. {options[i]}\n"

    text += "\nFormat your final answer as \\boxed{letter}, where 'letter' is one of A, B, C, or D.\n"
    return text

def doc_to_choice(doc):
    options = [doc['A'], doc['B'], doc['C'], doc['D']]
    return [string.ascii_uppercase[i] for i in range(len(options))]
