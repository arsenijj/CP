import random


def representation(p):

    twos = 0
    
    while not p % 2:
        twos += 1
        p //= 2
    
    return twos, p


def miller_rabin_test(n, k):
    
    s, t = representation(n - 1)
    
    for _ in range(k):
    
        a = random.randint(2, n - 2)
    
        x = pow(a, t, n)
    
        if x == 1 or x == n - 1:
            continue
    
        flag = False
        for _ in range(s - 1):
    
            x = x * x % n
    
            if x == 1:
                return False

            if x == n - 1:
                flag = True
                break
    
        if flag:
            continue
    
        return False
    
    return True


def get_prime(l):
    used = []
    while True:
        a = random.randint(2 ** (l - 1) + 1, 2 ** l - 1)
        if a in used:
            continue
        if miller_rabin_test(a, 8):
            return a


def main():
    l = int(input("Введите количество бит простого p: "))

    # Генерация Открытый параметр p
    p = get_prime(l)
    while not miller_rabin_test((p - 1) // 2, 8):
        p = get_prime(l)
    print("Открытый параметр p:", p)

    # Генерация Открытый параметр g
    while True:
        g = random.randint(0, p)
        if pow(g, p - 1, p) % p == 1 and miller_rabin_test(g, 8):
            break
    print("Открытый параметр g:", g)


    # Генерация: случайное натуральное число a — закрытый ключ Алисы
    a = random.randint(1, p - 1)
    print("Закрытый ключ a:", a)

    # Генерация: случайное натуральное число b — закрытый ключ Боба
    b = random.randint(1, p - 1)
    print("Закрытый ключ b:", b)

    #Вычисляется открытый ключ Алисы, передается Бобу
    Alice = pow(g, a, p)
    print("Открытый ключ Алисы, который передается Бобу: ", Alice)

    # Вычисляется открытый ключ Боба, передается Алисе
    Bob = pow(g, b, p)
    print("Открытый ключ Боба, который передается Алисе: ", Bob)

    K_alice = pow(Bob, a, p)
    print("Вычисляется общий секретный ключ K на стороне Алисы: ", K_alice)


    K_bob = pow(Alice, b, p)
    print("Вычисляется общий секретный ключ K на стороне Боба: ", K_bob)

    if K_alice == K_bob:
        print('Получение общего секретного ключа выполнено успешно')
    else:
        print('Общий секретный ключ не найден')

if __name__ == "__main__":
    main()
