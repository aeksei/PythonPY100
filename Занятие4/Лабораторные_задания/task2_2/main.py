def task(num: int):
    list_digits = [int(digit) for digit in str(num)]

    if (4 in list_digits and 7 in list_digits) or 9 in list_digits:
        print("Входят цифры (4 и 8) или цифра 9")
    else:
        print("Не входят цифры (4 и 8) или цифра 9")


if __name__ == "__main__":
    task(1234)
    task(12345678)
    task(1235679)
    task(0)
