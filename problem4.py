def is_palindrome(n):
    sting = str(n)
    gnits = sting[::-1]
    if sting==gnits:
        return True
    return False

def three_digit():
    al = []
    for a in range(100,1000):
        for b in range(100,1000):
            result = a*b
            if (is_palindrome(result)):
                al.append(result)
    return(max(al))

def main():
    print(three_digit())

main()

# 906609