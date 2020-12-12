def main():
    sqrs = sum([x*x for x in range(101)])
    sms = sum(range(101))**2
    print(abs(sqrs-sms))

main()
# 25164150