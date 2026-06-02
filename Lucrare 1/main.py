def cmmdc(a, b):
    # Euclid
    while b != 0:
        a, b = b, a % b
    return a


def prim(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def suma_cifrelor(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s


def produsul_cifrelor(num):
    p = 1
    while num > 0:
        p *= num % 10
        num //= 10
    return p


def suma_nedivizibili_3_5(n):
    s = 0
    for i in range(1, n + 1):
        if i % 3 != 0 and i % 5 != 0:
            s += i
    return s


def produs_coprime(n):
    p = 1
    for i in range(1, n + 1):
        if cmmdc(i, n) == 1:
            p *= i
    return p


def suma_prime_mai_mici_n(n):
    s = 0
    for i in range(2, n):
        if prim(i):
            s += i
    return s


def suma_divizori_produs_cifre(n):
    prod_cifre = produsul_cifrelor(n)
    s = 0
    for i in range(1, n + 1):
        if prod_cifre > 0 and prod_cifre % i == 0:
            s += i
    return s


def numar_suma_cifre_maxima(n):
    max_suma = 0
    numar_max = 0
    for i in range(1, n + 1):
        suma = suma_cifrelor(i)
        if suma > max_suma:
            max_suma = suma
            numar_max = i
    return numar_max, max_suma


def numere_produs_mai_mare_suma(n):
    numere = []
    for i in range(1, n + 1):
        p = produsul_cifrelor(i)
        s = suma_cifrelor(i)
        if p > s:
            numere.append(i)
    return numere


def numere_curioase(limit=1000):
    numere = []
    for n in range(1, limit + 1):
        s = suma_cifrelor(n)
        p = produsul_cifrelor(n)
        if s + p == n:
            numere.append(n)
    return numere

def suma_patrate_prime(n):
    s = 0
    for i in range(2, n + 1):
        if prim(i):
            s += i * i
    return s

if __name__ == "__main__":
    n = int(input("n: "))
        
    print("1. Rezultat:", suma_nedivizibili_3_5(n))
    print("2. Rezultat:", produs_coprime(n))
    print("3. Rezultat:", suma_prime_mai_mici_n(n))
    print("4. Rezultat:", suma_divizori_produs_cifre(n))
    numar, suma = numar_suma_cifre_maxima(n)
    print(f"5. Numar: {numar} Suma: {suma}")
    
    print("6. Numerele unde produsul cifrelor > suma cifrelor:")
    numere = numere_produs_mai_mare_suma(n)
    if numere:
        print(numere)
    else:
        print("Nu exista numere")
    
    curioase = numere_curioase(1000)
    print("7. Numere curioase:", curioase)
    
    print("8. Rezultat:", suma_patrate_prime(n))
    