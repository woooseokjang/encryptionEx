from random import randrange
from math import gcd


# n_oiler와 서로소인 e 찾기
def coprime(n_oiler):
    e = 0
    while True:
        e = randrange(2, n_oiler)  # 렌덤 e
        if gcd(e, n_oiler) == 1:  # 서로소 인가?
            return e


# RSA 키를 생성하자
def RSA_Key_Generation():

    # Select two large primes p and q such that p not q
    # 사전 입력된 p, q 를 사용
    p = 7
    q = 11

    # n <- p X q
    n = p * q
    # pi(n) <- (p - 1) X (q - 1)
    n_oiler = (p - 1) * (q - 1)
    # Select e such that 1 < e < pi(n) and e is coprime to pi(n)
    e = coprime(n_oiler=n_oiler)
    # d <- e^-1 mod pi(n)
    d = pow(e, -1, n_oiler)

    public_key = [e, n]
    private_key = d

    print(" p = " + str(p))
    print(" q = " + str(q))
    print(" e = " + str(e))
    print(" n_oiler = " + str(n_oiler))
    print(" d = " + str(d))

    return public_key, private_key


# a^x mod n
def Square_and_Multiply(a, x, n):
    y = 1

    # 2진수인 x
    x_bin = list(map(int, "{0:b}".format(x)))
    # lsb 부터 꺼내기위함
    x_bin.reverse()

    for xi in x_bin:
        if xi == 1:
            # y = a X y mod n
            y = (a * y) % n
        # a = a^2 mod n
        a = pow(a, 2, n)
    return y


def Fast_Exponentiation(P, e, n):
    return Square_and_Multiply(a=P, x=e, n=n)


def RSA_Encryption(P, e, n):
    # pow(P, e) % n
    return Fast_Exponentiation(P, e, n)


def RSA_Decryption(C, e, n):
    # pow(P, e) % n
    return Fast_Exponentiation(C, e, n)


if __name__ == "__main__":
    print("20141110 - 장우석")
    print("RSA -> ex)1")

    # 키 생성 = p, q RSA_Key_Generation 에서 정의됨 - ex)1
    public_key, private_key = RSA_Key_Generation()

    # 평문 정의됨 - ex)1
    p = 5
    print("plane = " + str(p))

    # 암호화
    c = RSA_Encryption(p, public_key[0], public_key[1])
    print("cyper = " + str(c))

    # 복호화
    p = RSA_Decryption(c, private_key, public_key[1])
    print("plane = " + str(p))
