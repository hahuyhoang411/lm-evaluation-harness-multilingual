import ast


def doc_to_choice(doc):
    """
    Convert a doc to a choice.
    """
    return ast.literal_eval(doc["choices"])


DOC_TO_TEXT = "Récit:\n{narrative}\n\n" "Question:\n{question}\n\n" "Choix:\n{choices}\n\n" "Formatez votre réponse finale comme suit : \\boxed{{nombres}}. Réponse:\n"


def doc_to_text(doc):
    """
    Convert a doc to text.
    """
    choices = ""
    for i, choice in enumerate(doc["choices"]):
        choices += f"{i} - {choice}\n"

    text = DOC_TO_TEXT.format(
        narrative=doc["narrative"], question=doc["question"], choices=choices, option="nombres"
    )

    return text