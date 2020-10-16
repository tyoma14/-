from functools import reduce
from typing import Iterable


def cap_count(sentences: Iterable):
    return reduce(lambda a, x: a + x.count('капитан'), sentences, 0)


sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']
# print(cap_count(sentences))


# --------------------------------------------------------------------------
def average_height(people):
    def has_height(person):
        return 'рост' in person

    def height(person):
        return person['рост']

    heights = list(map(height, filter(has_height, people)))
    return sum(heights) / len(heights)


people = [{'имя': 'Маша', 'рост': 160},
          {'имя': 'Саша', 'рост': 80},
          {'name': 'Паша'}]
# print(average_height(people))


# --------------------------------------------------------------------------
def zero(s):
    if s[0] == "0":
        return s[1:]


def one(s):
    if s[0] == "1":
        return s[1:]


def do_rule(s, rule):
    if s:
        return rule(s)


def rule_sequence(s, rules):
    if not rules:
        return s
    return reduce(do_rule, rules, s)


print(rule_sequence('1100', None))
print(rule_sequence('01', [zero, one, zero]))
print(rule_sequence(None, [zero, one, zero]))
print(rule_sequence('1100', [one, one, zero]))    # => "0"
print(rule_sequence('0101', [zero, one, zero]))  # => 1
print(rule_sequence('0101', [zero, zero]))   # => None
