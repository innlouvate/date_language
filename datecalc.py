# --imports --
from datetime import date, timedelta

# -- functions --
def make_token(s):
    if s in "0123456789":
        return ("NumberToken", s)
    elif s in "+-*/":
        return ("OperatorToken", s)
    else:
        return ("WordToken", s)

def lex(chars):
    return [
        make_token(s)
        for s in chars.split(" ")
    ]

def parse(tokens):
    if tokens[0][0] == "NumberToken":
        return ("LengthTree", tokens[0][1], tokens[1][1])
    elif len(tokens) <2:
        return ("WordTree", tokens[0][1])
    elif tokens[1][0] == "OperatorToken":
        return ("OperatorTree", tokens[1][1], parse([tokens[0]]), parse([tokens[2], tokens[3]]) )

def period(unit):
    if unit == "days":
        return 1
    elif unit == "weeks":
        return 7

def evaluate(tree):
    if tree[0] == "LengthTree":
        return ("LengthValue", int(tree[1]) * period(tree[2]))
    elif tree[1] == "today":
        return ("DateValue", date.today())
    elif tree[1] == "tomorrow":
        return ("DateValue", date.today() + timedelta(days=1))
