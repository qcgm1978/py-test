import random,unittest
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
    return (sum(trials) / n)
class TDD_STAT(unittest.TestCase):
    def test_simulate(self):
        self.assertLess(simulate(10), 10*100)
        self.assertLess(simulate(100),100*100)
        self.assertLess(simulate(1000), 1000*100)
        self.assertLess(simulate(1000000), 1e8)
unittest.main()