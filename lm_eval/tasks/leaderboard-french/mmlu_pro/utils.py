import string
import re

def doc_to_text(doc):
    doc_to_text = f"{doc['Question']}\n"
    options = [doc['A'], doc['B'], doc['C'], doc['D']]
    for i in range(len(options)):
        doc_to_text += f"{string.ascii_uppercase[i]}. {options[i]}\n"
    
    doc_to_text += "Formatez votre réponse finale en \\boxed{([A-D])}. Résponse:\n"
    return doc_to_text

def doc_to_choice(doc):
    options = [doc['A'], doc['B'], doc['C'], doc['D']]
    return [string.ascii_uppercase[i] for i in range(len(options))]
