"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""

"""
согласно теоремы Виета для приведённого квадратного уравнения
(просто примем X и Y за корни квадратного уравнения x1 и x2)
наше уравнение, с учётом того, что x1 + x2 = S, а x1 * x2 = P, будет иметь вид
x² - Sx + P = 0
остаётся только по дискриминанту определить, а есть ли корни
D = S² - 4P >= 0
ну и если есть, то, само собой, найти их
"""
S = int(input("Введите сумму чисел: "))

repeat = True

while repeat:
    if S < 2:
        print("Сумма не может быть меньше 2!")
        S = int(input("Повторите ввод: "))
    elif S > 2000:
        print("Сумма не может быть больше 2000!")
        S = int(input("Повторите ввод: "))
    else:
        repeat = False

P = int(input("Введите произведение чисел: "))

repeat = True

while repeat:
    if P < 2:
        print("Произведение не может быть меньше 1!")
        P = int(input("Повторите ввод: "))
    elif P > 1e6:
        print("Произведение не может быть больше 1млн")
        P = int(input("Повторите ввод: "))
    else:
        repeat = False

D = S ** 2 - 4 * P

if D < 0:
    print("Решения нет. Дискриминант меньше 0.")
else:
    x1 = (S - D ** 0.5) / 2

    intX = int(x1)

    if int(x1) - x1 != 0:
        print("Решения нет. Корни уравнения не являются натуральными числами.")

    else:
        if D == 0:
            x2 = x1
        else:
            x2 = (S + D ** 0.5) / 2

        print(int(x1), int(x2))
