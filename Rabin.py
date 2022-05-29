def Rabin_Key_Generation():
    # 사전에 정의된 p, q - ex)2
    p = 23
    q = 71
    # n <- p X q
    n = p * q
    # Public_Key <- n
    Public_key = n
    # Private_Key <- (q, n)
    Private_Key = [p, q]
    print(" p : " + str(p))
    print(" q : " + str(q))
    print(" n : " + str(n))
    return Public_key, Private_Key


def Rabin_Encryption(n, P):
    # c <- p^2 mod n
    c = pow(P, 2, n)
    return c


def Chinese_Remainder(a, b, m1, m2):
    # 공통 모듈러 M = m1 X m2
    M = m1 * m2
    #M1 = M/m1
    M1 = int(M / m1)
    #M2 = M/m2
    M2 = int(M / m2)
    # 모듈러 m1, m2 에 대한 M1, M2 의 역수
    M1Inv = pow(M1, -1, m1)
    M2Inv = pow(M2, -1, m2)
    # 합동 연립 방적식의 해
    x = ((a * M1 * M1Inv)+(b * M2 * M2Inv)) % M
    return x


def Rabin_Decryption(p, q, C):
    a1 = pow(C, int((p + 1)/4), p)
    a2 = p - pow(C, int((p + 1)/4), p)
    b1 = pow(C, int((q + 1)/4), q)
    b2 = q - pow(C, int((q + 1)/4), q)

    # 가능한 모든 경우의 수에 대해 계산
    p1 = Chinese_Remainder(a1, b1, p, q)
    p2 = Chinese_Remainder(a1, b2, p, q)
    p3 = Chinese_Remainder(a2, b1, p, q)
    p4 = Chinese_Remainder(a2, b2, p, q)

    return p1, p2, p3, p4


if __name__ == "__main__":
    print("20141110 - 장우석")
    print("Rabin -> ex)2")

    # 키생성 p, q 값 사전 정의됨 - ex)2
    Public_Key, Private_Key = Rabin_Key_Generation()

    p = 99
    print("plane -> " + str(p))
    c = Rabin_Encryption(Public_Key, p)
    print("cyper -> " + str(c))
    p = Rabin_Decryption(Private_Key[0], Private_Key[1], c)
    print("plane -> " + str(p))
