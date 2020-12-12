def find_sum_3_5(n):
    sum = 0
    for i in range(2,n):
        if (i%3==0 or i%5==0):
            sum += i
    return sum

def main():
    print(find_sum_3_5(1000))

main()
# 233168
