import re
patterns =                                                         (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')                                 
  )
def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):                                     
        return re.search(pattern, word)
    def apply_rule(word):                                       
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

rules = [build_match_and_apply_functions(pattern, search, replace)  
         for (pattern, search, replace) in patterns]


def plural_pattern(noun):
    for matches_rule, apply_rule in rules:  
        if matches_rule(noun):
            return apply_rule(noun)