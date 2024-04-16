import random

def number_1():
    num = random.sample(range(1, 11), 5)

    user_num = int(input("Введите число в диапазоне от 1-10 включительно: "))

    if user_num in num:
        print(num, "Ваеш число: ", user_num, "\nПоздравляю, вы угадали число!")
    else:
        print(num, "Ваше число: ", user_num, "\nНет такого числа!")

def number_2():
    N = random.choices(range(1, 11), k=random.randint(1, 11))
    
    duplicate_N = []
    
    for i in N:
        if i in duplicate_N:
            pass
        else:
            duplicate_N.append(i)
    
    if duplicate_N:
        print("Повторы есть: ", duplicate_N)
    else:
        print("Повторов нет")
    
def number_3():
    days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

    user_days = int(input("Сколько выходных на неделе Вы хотите: "))
    if 1 <= user_days < 7:
        pass
    else:
        print("Неверное количество дней!")
        return 
    
    index = len(days) - user_days
    
    wek_days = days[index:]
    work_days = days[:index] 
    
    print("Ваши выходные: ", ", ".join(wek_days))            
    print("Ваши рабочие дни: ", ", ".join(work_days))
    
    
def number_4():
    g_1 = ["Крылова", "Сидорова", "Мартынова", "Леонов", "Лапшина", "Иванова", "Романова", "Николаева", "Абрамова", "Ширяев-Горский"]
    g_2 = ["Калинина", "Климов", "Соловьева", "Иванов", "Хохлова", "Минин", "Львова", "Лапшина", "Кулагин", "Зубова"]
    
    team = tuple(random.sample(g_1, 5) + random.sample(g_2, 5))
    team_alf = sorted(team)
    team_ivanov = team.count("Иванов") + team.count("Иванова")
    
    print("Команда №1: ", ", ".join(g_1))
    print("Команда №2: ", ", ".join(g_2))
    print("Спортивная команда: ", ", ".join(team))
    print("Длина команды: ", len(team))
    print("Команда в алфавитном порядке: ", ", ".join(team_alf))
    
    if team_ivanov:
        print("Ивановы есть: ", team_ivanov, "шт")
    else:
        print("Ивановых нет в команде!")
    
while True:
    number = int(input("Введите номер задания: "))

    if number == 1:
        number_1()
    elif number == 2:
        number_2()
    elif number == 3:
        number_3()
    elif number == 4:
        number_4()
    else:
        print("Такого задания нет")