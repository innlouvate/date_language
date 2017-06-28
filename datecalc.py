# --imports --
from datetime import date, timedelta
import operator

# -- functions --
def make_token(s):
    if s in "0123456789":
        return ("NumberToken", s)
    elif s in "+-":
        return ("OperatorToken", s)
    else:
        return ("WordToken", s)

def lex(chars):
    return [
        make_token(s)
        for s in chars.split(" ")
    ]

def parse(tokens, so_far=None):
    if len(tokens) == 0:
        return so_far
    t = tokens[0]
    r = tokens[1:]
    if t[0] == "NumberToken":
        return ("LengthTree", t[1], r[0][1])
    elif t[0] == "OperatorToken":
        return ("OperatorTree", t[1], so_far, parse(r))
    elif t[0] == "WordToken":
        return parse(r, ("WordTree", t[1]))

def period(unit):
    if unit == "days" or unit == "day":
        return 1
    elif unit == "weeks" or uit == "week":
        return 7

def get_operator(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        }[op]

def evaluate(tree):
    if tree[0] == "LengthTree":
        return ("LengthValue", int(tree[1]) * period(tree[2]) )
    elif tree[0] == "OperatorTree":
        return ("DateValue", get_operator(tree[1])(evaluate(tree[2])[1], timedelta(days=evaluate(tree[3])[1])) )
    elif tree[0] == "WordTree":
        if tree[1] == "today":
            return ("DateValue", date.today())
        elif tree[1] == "tomorrow":
            return ("DateValue", date.today() + timedelta(days=1))
