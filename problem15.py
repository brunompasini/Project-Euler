# being a Lattice path between one end
# of a 20x20 grid and another
# the answer is the binomial pair
# (40)
# (20)
# so, 40!/20!*20!

from math import factorial

def main():
    print((factorial(40)/(factorial(20)*factorial(20))))

main()
# 137846528820