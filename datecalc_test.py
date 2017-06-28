from datecalc import *

assert lex("today") == [("WordToken", "today")]
assert lex("tomorrow") == [("WordToken", "tomorrow")]
assert lex("2 days") == [ ("NumberToken", "2"), ("WordToken", "days") ]

def p(x):
    return parse(lex(x))
assert p("today") == ("WordTree", "today")
assert p("tomorrow") == ("WordTree", "tomorrow")
assert p("2 days") == ("LengthTree", "2", "days")

def e(x):
    return evaluate(parse(lex(x)))

def days(n):
    return timedelta(days=n)

today = date.today()
assert e("today") == ("DateValue", today)
assert e("tomorrow") == ("DateValue", today + days(1))
print e("2 days")
assert e("2 days") == ("LengthValue", 2)
