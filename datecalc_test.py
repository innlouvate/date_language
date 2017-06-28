from datecalc import *

assert lex("today") == [("WordToken", "today")]
assert lex("tomorrow") == [("WordToken", "tomorrow")]
assert lex("2 days") == [ ("NumberToken", "2"), ("WordToken", "days") ]
assert lex("3 weeks") == [ ("NumberToken", "3"), ("WordToken", "weeks") ]
assert lex("today + 3 days") == [
        ("WordToken", "today"),
        ("OperatorToken", "+"),
        ("NumberToken", "3"),
        ("WordToken", "days") ]

def p(x):
    return parse(lex(x))
assert p("today") == ("WordTree", "today")
assert p("tomorrow") == ("WordTree", "tomorrow")
assert p("2 days") == ("LengthTree", "2", "days")
assert p("3 weeks") == ("LengthTree", "3", "weeks")
assert p("today + 3 days") == ("OperatorTree", "+", ("WordTree", "today"), ("LengthTree", "3", "days") )

def e(x):
    return evaluate(parse(lex(x)))

def days(n):
    return timedelta(days=n)

today = date.today()
assert e("today") == ("DateValue", today)
assert e("tomorrow") == ("DateValue", today + days(1))
assert e("2 days") == ("LengthValue", 2)
assert e("3 weeks") == ("LengthValue", 21)
assert e("today + 3 days") == ("DateValue", today + days(3))
assert e("tomorrow + 1 day") == ("DateValue", today + days(2))
assert e("today - 3 days") == ("DateValue", today - days(3))
assert e("tomorrow - 1 day") == ("DateValue", today)
