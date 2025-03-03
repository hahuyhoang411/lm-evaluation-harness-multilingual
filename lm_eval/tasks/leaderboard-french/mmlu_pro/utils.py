import string
import re

def doc_to_text(doc):
    doc_to_text = "Répondez à la question à choix multiples suivante.\n\n"
    doc_to_text += f"Question:\n{doc['Question']}\n\n"
    doc_to_text += "Options:\n"
    
    options = [doc['A'], doc['B'], doc['C'], doc['D']]
    for i in range(len(options)):
        doc_to_text += f"{string.ascii_uppercase[i]}. {options[i]}\n"

    doc_to_text += "\nFormatez votre réponse finale en \\boxed{lettres} où lettres est l'une des lettres A, B, C ou D.\n"
    return doc_to_text

def doc_to_choice(doc):
    options = [doc['A'], doc['B'], doc['C'], doc['D']]
    return [string.ascii_uppercase[i] for i in range(len(options))]
