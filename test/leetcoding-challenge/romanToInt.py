import re


class Solution:
    def romanToInt(self, s: str) -> int:
        # Symbol       Value
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000
        m = re.match(
            r"""
        (?P<thousand>M*)? #MCDLXXVI
        (?P<ninehundred>CM)?
        (?P<fivehundred>D)?
        (?P<fourhundred>CD)?
        (?P<hundreds>C*)?
        (?P<ninety>XC)?
        (?P<fifty>L)?
        (?P<forty>XL)?
        (?P<tens>X*)?
        (?P<nine>IX)?
        (?P<five>V)?
        (?P<four>IV)?
        (?P<one>I*)?
        """,
            s,
            re.VERBOSE,
        )
        ones = len(m.group("one")) if m.group("one") else 0
        four = 4 if m.group("four") else 0
        nine = 9 if m.group("nine") else 0
        thousand = 1000*len(m.group("thousand")) if m.group("thousand") else 0
        ninehundred = 900 if m.group("ninehundred") else 0
        fivehundred = 500 if m.group("fivehundred") else 0
        fourhundred = 400 if m.group("fourhundred") else 0
        hundreds = 100*len(m.group("hundreds")) if m.group("hundreds") else 0
        ninety = 90 if m.group("ninety") else 0
        fifty = 50 if m.group("fifty") else 0
        forty = 40 if m.group("forty") else 0
        tens = 10*len(m.group("tens")) if m.group("tens") else 0
        five = 5 if m.group("five") else 0
        return ones+four+nine+fifty+five+thousand+ninehundred+ninety+fourhundred+fivehundred+hundreds+forty+tens
