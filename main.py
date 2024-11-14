"""module nombre premier"""

#### Fonction secondaire


def isprime(p):
    """fonction is prime"""
    premier  =  True
    if p == 1:
        return  False
    for d in range (2, int(p**0.5) + 1):
        if p%d == 0:
            premier = False
    return  premier

#### Fonction principale


def main():
    """main"""

    print(f"{13} est premier")

    for n in range(100):
        if isprime(n):
            print(n, end=", ")



if __name__ == "__main__":
    main()
