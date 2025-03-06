import re

def clean_target(doc):
    """
    Cleans the target string by removing parentheses and converting to uppercase.

    Args:
        doc: A dictionary containing the 'target' key.

    Returns:
        The cleaned target string.
    """
    target = doc["target"]
    match = re.match(r"^\(([A-Z])\)$", target)
    if match:
        return match.group(1)
    return target
