
import unittest
class TDD_COIN(unittest.TestCase):
    def test_coin(self):
        import random
        def coin_trial():
            heads = 0
            for i in range(100):
                if random.random() <= 0.5:
                    heads +=1
                return heads
        def simulate(n):
            trials = []
            for i in range(n):
                trials.append(coin_trial())
            return(sum(trials)/n)
        simulate(10)
        5.4
        simulate(100)
        4.83
        simulate(1000)
        5.055
        simulate(1000000)
if __name__ == '__main__':
    unittest.main()

                