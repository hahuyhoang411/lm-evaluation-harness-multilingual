import string
import re

def doc_to_text(doc):
    doc_to_text = f"{doc['Question']}\n"
    options = [doc['A'], doc['B'], doc['C'], doc['D']]
    for i in range(len(options)):
        doc_to_text += f"{string.ascii_uppercase[i]}. {options[i]}\n"
    
    doc_to_text += "Réponse:"
    return doc_to_text

def doc_to_choice(doc):
    options = [doc['A'], doc['B'], doc['C'], doc['D']]
    return [string.ascii_uppercase[i] for i in range(len(options))]

def extract_answer_from_box(response):
    # First, try extracting content inside box
    box_match = re.search(r"\\boxed\{(.*?)\}", response, re.DOTALL)
    if box_match:
        return box_match.group(1).strip()

    # If no box is found, fall back to extracting the first valid answer choice
    match = re.search(r'\b[A-D]\b', response)
    return match.group(0) if match else None
