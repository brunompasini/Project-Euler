def is_div(n,l):
    for el in l:
        if (n%el != 0):
            return False
    return True

def all_in_20():
    lis = range(1,21)
    num = 2520
    fim = False
    while not fim:
        num += 1
        fim = is_div(num,lis)
    return num

def main():
    print(all_in_20())

main()
# 232792560