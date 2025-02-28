import string
import re

def clean_target(doc):
    return doc["target"].strip("()")
