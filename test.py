from Consumer import Consumer
from Partition import Partition


def test():
    part1 = Partition(0, 35, 87.1)
    part2 = Partition(0, 35, 87.1)
    print(part1)
    print(part1==part2)
    lpart1 = []
    lpart1.append(part1)
    lpart2 = []
    lpart2.append(part2)

    c1 = Consumer("0", lpart1, 175, 0)
    c2 = Consumer("1", lpart2, 175, 0)
    print(c1)
    print(c2)




if __name__=='__main__':
    test()