from datecalc import *

assert lex("today") == [("WordToken", "today")]
assert lex("tomorrow") == [("WordToken", "tomorrow")]

def p(x):
    return parse(lex(x))
assert p("today") == ("WordTree", "today")
assert p("tomorrow") == ("WordTree", "tomorrow")


def e(x):
    return evaluate(parse(lex(x)))

def days(n):
    return timedelta(days=n)

today = date.today()
assert e("today") == ("DateValue", today)
assert e("tomorrow") == ("DateValue", today + days(1))
