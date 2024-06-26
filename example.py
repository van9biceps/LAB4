"""
@file
@brief Функция для восстановления секрета на основе долей сотрудников
"""

def recover_secret(shares):
    """
    @brief Восстанавливает секрет на основе переданных долей сотрудников

    @param shares Доли сотрудников в виде списка кортежей (x, y)

    @return Восстановленный секретный ключ
    """
    secret = 0
    p = 67654434553  # простое число p

    def lagrange(j, x):
        """
        @brief Функция Лагранжа для вычисления базисных полиномов

        @param j Индекс базисного полинома
        @param x Значение x

        @return Значение базисного полинома в точке x
        """
        ljx = 1
        xj, _ = shares[j]
        for m in range(len(shares)):
            xm, _ = shares[m]
            if m != j:
                ljx *= (x - xm) * pow(xj - xm, -1, p)
        return ljx

    for j in range(len(shares)):
        xj, yj = shares[j]
        l = lagrange(j, 0)
        secret += yj * l % p
    return secret % p

# Доли сотрудников
shares = [
    (658, 21325033821),
    (997, 13706394907),
    (229, 40006377956),
    (890, 60157239541),
    (118, 49830940274),
    (365, 60625020465),
    (210, 66921346645),
    (449, 50209132564),
    (554, 33464574025),
    (987, 22934301937),
    (228, 36685150120),
    (398, 55898698187),
    (111, 33635968932)
]

# Восстановление секрета
secret = recover_secret(shares)
print("Секретный ключ:", secret)
