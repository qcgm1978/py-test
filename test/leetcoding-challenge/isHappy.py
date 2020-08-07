class Solution:
    def pdi_function(self,number, base: int = 10):
        """Perfect digital invariant function."""
        total = 0
        while number > 0:
            total = total + pow(number % base, 2)
            number = number // base
        return total
    def isHappy(self, n: int) -> bool:
        number=n
        """Determine if the specified number is a happy number."""
        seen_numbers = []
        while number > 1 and number not in seen_numbers:
            seen_numbers.append(number)
            number = self.pdi_function(number)
        return number == 1