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
        # self.assertLess(simulate(10), 10*100)
        # self.assertLess(simulate(100),100*100)
        # self.assertLess(simulate(1000), 1000*100)
        pass
        # self.assertLess(simulate(1000000), 1e8)
    def test_college_lottery(self):
        Tsinghua = 3000 / 9.42e6
        lottery = 1 / 17.72e6
        self.assertAlmostEqual(Tsinghua/lottery,5*1e3,-4)
        Henan = 100 / 830e3
        self.assertAlmostEqual(Henan/lottery,2*1e3,-4)
unittest.main()