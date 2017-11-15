import re

pattern_string = "this is the pattern"
regex = re.compile(pattern_string)

match = regex.search("this is the pattern")
if match:
    print("this was a match!")
if regex.search("*** this is the pattern ***"):
    print("this was not a match!")
if not regex.search("this is not the pattern"):
    print("this was not a match!")

a_space_b = re.compile("a\sb")
if a_space_b.search("a b"):
    print("'a b' is a match!")
if a_space_b.search("1234 a b 1234"):
    print("'1234 a b 1234' is a match")
if a_space_b.search("ab"):
    print("'1234 a b 1234' is a match")


a_at_start = re.compile("^a")
if a_at_start.search("a"):
    print("'a' is a match")
if a_at_start.search("a 1234"):
    print("'a 1234' is a match")
if a_at_start.search("1234 a"):
    print("'1234 a' is a match")

a_at_end = re.compile("a$")
if a_at_end.search("a"):
    print("'a' is a match")
if a_at_end.search("a 1234"):
    print("'a 1234' is a match")
if a_at_end.search("1234 a"):
    print("'1234 a' is a match")

lower_case_letter = re.compile("[a-z]")
if lower_case_letter.search("a"):
    print("'a' is a match")
if lower_case_letter.search("B"):
    print("'B' is a match")
if lower_case_letter.search("123 A B 2"):
    print("'123 A B 2' is a match")

digit = re.compile("[0-9]")
if digit.search("1"):
    print("'a' is a match")
if digit.search("342"):
    print("'a' is a match")
if digit.search("asdf abcd"):
    print("'a' is a match")

a_or_b = re.compile("(a|b)")
if a_or_b.search("a"):
    print("'a' is a match")
if a_or_b.search("b"):
    print("'b' is a match")
if a_or_b.search("c"):
    print("'c' is a match")

number_then_word = re.compile("[0-9]+\s[a-z]+(\s|$)")
if number_then_word.search("1234 asdf"):
    print("'1234 asdf' is a match")
if number_then_word.search("asdf 1234"):
    print("'asdf 1234' is a match")
if number_then_word.search("1234 1234"):
    print("'1234 1234' is a match")


match = number_then_word.search("**** 1234 abcd ****")
print(match.group())

print(a_or_b.split("123a456b789"))
print(a_or_b.split("a1b"))
