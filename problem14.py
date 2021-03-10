def collatz(start):
    if start == 1:
        return [1]
    else:
        end = [start]
        n = start
        while n != 1:
            if n%2==0:
                n = n/2
            else:
                n = 3*n + 1
            end.append(n)
        return end

def find_longest():
    longer = 0
    gen = 0
    for i in range(13,1000000):
        seq = collatz(i)
        if len(seq) > longer:
            longer = len(seq)
            gen = i
    return [longer, gen]

def main():
    print(find_longest())

main()
# 837799
