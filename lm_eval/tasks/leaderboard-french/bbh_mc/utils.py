import string
import re

def clean_target(doc):
    target = doc["target"].strip("()")
    choices = ["A", "B", "C", "D"]

    if target in choices:
        return target