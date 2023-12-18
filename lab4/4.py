import random
import sympy


def main():
    j = int(input("А отправляет стороне Б свои атрибуты: "))
    print("\nАлгоритм создания открытого и закрытого ключей")

    print('Шаг 1.')
    l1 = int(input("Введите количество бит простого p: "))
    p = sympy.randprime(2 ** (l1 - 1) + 1, 2 ** l1 - 1)
    print("\tПараметр p:", p)

    l2 = int(input("Введите количество бит простого q: "))
    q = sympy.randprime(2 ** (l2 - 1) + 1, 2 ** l2 - 1)
    print("\tПараметр q:", q)

    n = p * q
    print("\tРезультат шага - параметр n:", n)

    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while sympy.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    print("Шаг 2 \n\tПараметр e:", e)

    s = pow(e, -1, phi)
    x = pow(j, -s, n)
    print("Шаг 3 \n\tПараметр s:", s, "\n\tПараметр x:", x)

    y = pow(x, e, n)
    print("Шаг 4 \n\tПараметр y:", y, "\n")

    print("Открытый ключ:", n, e, y)
    print("Закрытый ключ:", x)

    print("\nОбмен сообщениями")
    r = random.randint(1, n)
    a = pow(r, e, n)
    print("1. Алиса отправляет Бобу вычисленное a:", a)

    c = random.randint(0, e)
    print("2. Боб отправляет Алисе выбранное c:", c)

    z = r * pow(x, c, n) % n
    print("3. Алиса отправляет Бобу вычисленное z:", z)

    print("4. Боб проверяет z^e = ay^c mod n: ", pow(z, e, n) == a * pow(y, c, n) % n)


if __name__ == "__main__":
    main()
