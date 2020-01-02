import re
class LazyRules:
    '''
    There are ways around this. Instead of opening the file during __init__() and
     leaving it open while you read rules one line at a time, you could open the
      file, read all the rules, and immediately close the file. Or you could open
       the file, read one rule, save the file position with the tell() method, 
       close the file, and later re-open it and use the seek() method to continue 
       reading where you left off. Or you could not worry about it and just leave 
       the file open, like this example code does. Programming is design, and 
       design is all about trade-offs and constraints. Leaving a file open too 
       long might be a problem; making your code more complicated might be a 
       problem. Which one is the bigger problem depends on your development team, 
       your application, and your runtime environment.

    '''
    rules_filename='./test/test_regular_expressions/plural4-rules.txt'

    def __init__(self):
        self.pattern_file=open(self.rules_filename,encoding='utf-8')
        self.cache=[]
        self.loop_file()

    def __iter__(self):
        self.cache_index=0
        return self

    def __next__(self):
        self.cache_index+=1
        if len(self.cache)>=self.cache_index:
            return self.cache[self.cache_index-1]

        if self.pattern_file.closed:
            raise StopIteration

        line=self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None,2)
        funcs=self.build_match_and_apply_functions(pattern,search,replace)
        self.cache.append(funcs)
        return funcs

    def loop_file(self):
        for n in self:
            try:
                pass
                # get the next item
                # element = iter(rules)
                # do something with element
            except StopIteration:
                # if StopIteration is raised, break from loop
                break

    def build_match_and_apply_functions(self,pattern, search, replace):  
        def matches_rule(word):
            return re.search(pattern, word)
        def apply_rule(word):
            return re.sub(search, replace, word)
        return (matches_rule, apply_rule)

    def plural(self,noun):
        for matches_rule, apply_rule in self.cache:  
            if matches_rule(noun):
                return apply_rule(noun)
