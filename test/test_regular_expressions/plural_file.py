import re,os

def build_match_and_apply_functions(pattern, search, replace):  
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

rules = []
with open('./test/test_regular_expressions/plural4-rules.txt', encoding='utf-8') as pattern_file:  
    for line in pattern_file:                                      
        pattern, search, replace = line.split(None, 2)             
        rules.append(build_match_and_apply_functions(              
                pattern, search, replace))

def plural_file(noun):
    for matches_rule, apply_rule in rules:  
        if matches_rule(noun):
            return apply_rule(noun)