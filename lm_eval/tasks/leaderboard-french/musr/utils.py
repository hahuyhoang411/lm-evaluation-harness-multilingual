import ast


def doc_to_choice(doc):
    """
    Convert a doc to a choice.
    """
    return ast.literal_eval(doc["choices"])


DOC_TO_TEXT = "Récit:\n{narrative}\n\n" "Question:\n{question}\n\n" "Choix:\n{choices}\n\n" "Formatez votre réponse finale comme suit : \\boxed{{option}}. Réponse:\n"


def doc_to_text(doc):
    """
    Convert a doc to text.
    """
    choices = ""
    for i, choice in enumerate(doc["choices"]):
        choices += f"{i+1} - {choice}\n"

    text = DOC_TO_TEXT.format(
        narrative=doc["narrative"], question=doc["question"], choices=choices, option="<option>"
    )

    return text

def doc_to_target(doc):
    """
    Returns the one-based index of the answer_choice in the doc's choices list.
    
    Args:
        doc: Document object containing a 'choices' field
        answer_choice: The selected answer choice
        
    Returns:
        int: The one-based index of the answer choice in the choices list
    """
    # Get choices from the doc
    choices = doc["choices"]
    
    # Handle case sensitivity and whitespace
    normalized_choices = [choice.strip() for choice in choices]
    normalized_answer = doc['answer_choice'].strip()
    
    try:
        # Find the index of the answer in the choices list and add 1 for one-based indexing
        index = normalized_choices.index(normalized_answer) + 1
        return index
    except ValueError:
        # If the exact answer isn't found, try a more fuzzy matching approach
        for i, choice in enumerate(normalized_choices):
            if normalized_answer in choice or choice in normalized_answer:
                return i + 1
        
        # If still not found, return 0 or raise an exception
        return 0