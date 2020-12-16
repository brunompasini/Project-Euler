def prime_summation():
    limit = 2000000
    al = set([x for x in range(3,limit,2)])
    for i in range(3,1415,2):
        cut = i
        while cut < limit:
            cut+=i
            # remove a number each i numbers, like Sieve of Erasthotenes
            if cut in al:
                al.discard(cut)
    return 2+sum(al)

def main():
    print(prime_summation())

main()
# 142913828922