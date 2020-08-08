class Solution:
    def five(self, num: int) -> str:
        remainder = num % 5
        if num % 10:
            return 'V'
        else:
    
            return  'X' if num else ''
    def four(self, num: int) -> str:
            return  "IV" if num==4 else 'IX'
    def three(self, num: int) -> str:
                return  ('V' if num>5 else '')+"I" * (num%5)
    def fifty(self,num: int) -> str:
        remain50 = num % 50
        if remain50<40:
                return 'L'+self.intToRoman(num%50)
        else:
            return "XC"+self.intToRoman(num%90)
    def two(self, num: int) -> str:
            if num>5:
                return 'V'+'I'*(num%5)
            else:
                return 'II'
    def one(self, num: int) -> str:
            if num==6:
                return 'VI'
            elif num==1:
                return 'I'
    def intToRoman(self, num: int) -> str:
        # Symbol       Value
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000
        if num>=1000:
            mod1000 = num % 1000
            return num//1000*'M' + self.intToRoman(mod1000 )
        elif num >= 500:
            if num%500<=300:
                if num % 500:
                    return num//500*'D' + self.intToRoman(num % 500)
                else:
                    return num // 500 * "D"
            elif num>=900:
                return 'CM'+ self.intToRoman(num % 900)
            else:
                return 'DCCC'+self.intToRoman(num % 800)
        elif num>=100:
            mod100 = num % 100
            if num//100<=3:
                if mod100 :
                    return num//100*'C' + self.intToRoman(mod100 )
                else:
                    return num // 100 * "C"
            elif num//100==4:
                return 'CD' + self.intToRoman(mod100)
            else:
                return 'C'
        elif num >= 50:
            return self.fifty(num)
        elif num > 10:
            if num//10<=3:
                if num % 10:
                    return num//10*'X' + self.intToRoman(num % 10)
                else:
                    return num // 10 * "X"
            else:
                return 'XL'+ self.intToRoman(num % 10)
        remainder = num % 5
        if remainder == 4:
            return self.four(num)
        elif remainder == 3:
            return self.three(num)
        elif remainder == 2:
            return self.two(num)
        elif remainder == 1:
            return self.one(num)
        else:
            return self.five(num)