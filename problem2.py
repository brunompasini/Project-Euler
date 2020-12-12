def fibonacci(n):
    if (n<=3):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def soma():
    som = 0
    n = 1
    valor = 1
    while (valor <= 4000000):
        valor = fibonacci(n)
        if valor%2==0:
            som+=valor
        n+=1
    return som

def main():
    print(soma())

main()
# 4613732