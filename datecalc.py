# --imports --
from datetime import date, timedelta

# -- functions --
def lex(chars):
    return [("WordToken", chars)]

def parse(tokens):
    return ("WordTree", tokens[0][1])

def evaluate(tree):
    if tree[1] == "today":
        return ("DateValue", date.today())
    elif tree[1] == "tomorrow":
        return ("DateValue", date.today() + timedelta(days=1))
