"""
Module... 
"""
import game_t6

peremoga = game_t6.Street("Вулиця Перемоги")
peremoga.set_description("Одна з багатьох непримітних вулиць міста. З невеличким магазинчиком")

kiyvska = game_t6.Street("Вулиця Київська")
kiyvska.set_description("Одна з найдовших центральний вулиць Житомира.\nНа ній є iBox, тому без готівки не залишишся")

myhailivska = game_t6.Street("Вулиця Михайлівська")
myhailivska.set_description("Найкраща пішоходна вулиця міста.\nТут є багато цікавих місць де можна цікаво провести час")

noviy_bulvar = game_t6.Street("Новий Бульвар")
noviy_bulvar.set_description("Реставрована припаркова зелена вулиця з великою кількістю нових лав")

pushkinska = game_t6.Street("Вулиця пушкінська")
pushkinska.set_description("Маленька неперейменована вульця. Нічого особливого")

satriy_bulvar = game_t6.Street("Старий Бульвар")
satriy_bulvar.set_description("Найдовший бульвар в парку Гагаріна з великою кількістю старих дубів і фонтанів.\nТут розташоване ГУНП і головний відділ СБУ ")

peremoga.link_room(kiyvska, "на захід")
kiyvska.link_room(myhailivska, "на південь")
myhailivska.link_room(noviy_bulvar, "на південь")
noviy_bulvar.link_room(pushkinska, "на захід")
pushkinska.link_room(satriy_bulvar, "на південь")
satriy_bulvar.link_room(pushkinska, "на північ")

food = game_t6.Item("їжа")
food.set_description("Не можна йти в гості з пустими руками потрібно щось придбати")
peremoga.set_item(food)

cash = game_t6.Item("готівка")
cash.set_description("IBOX який працює цілодобово може допомогти в скрутній ситуації")
kiyvska.set_item(cash)

scooter = game_t6.Item("самокат")
scooter.set_description("Часу залишається не так багато, на самокаті швидше")
pushkinska.set_item(scooter)

volodia = game_t6.Enemy("Володя", "Дивакуватий безхатько, який не дасть вам спокою поки не отримаю хоча б пару гривень.")
volodia.set_conversation("Дай 20 гривень")
volodia.set_weakness("готівка")
myhailivska.set_character(volodia)

dogs = game_t6.Enemy("Безпритульні собаки", "Увечері в циз місцях їх досить багато і вони інколи агресивні,\n тому треба мати при собі щось смачненьке")
dogs.set_conversation("рррррр гав гав гав")
dogs.set_weakness("їжа")
noviy_bulvar.set_character(dogs)

cops = game_t6.Enemy("Поліція", "Ці хлопці гуляють тут по вечорам і створюють проболеми тим хто викликає підозру")
cops.set_conversation("Стій !!!")
cops.set_weakness("самокат")
satriy_bulvar.set_character(cops)

current_room = peremoga
backpack = []

dead = False

print("\n")
print("Ти прибув у місто Житомир на майдан перемоги, адже сюди прибув автобус зі Львову.\n")
print("Ти прийхав до свого друга, який живе в селі Зарічани.\
Через непередбачувані обвставини він не може тебе зустірти.\nТобі прийдеться добиратись самому.\
Треба все робити швидко, бо вже 22:20 і скоро комендантська година.\n")
print("Маршрутки не ходять, таксист так далеко їхати не захотів,\
біля пам'ятника \"Захисникам України\"\nкорінний Житомирянин Денис підказав тобі коротку дорогу,\
і розказав про всі особливості цього маршруту.\
Тож треба поспішати.")
counter = 1
corpcount = 0

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")
    if command in ["на захід", "на cхід", "на південь", "на північ"]:
        try:
            if inhabitant is None:
                current_room = current_room.move(command)
            else:
                print("Ти тут не один ти не можеш просто так пройти")
                continue
        except KeyError:
            print("Відхилятись від короткого маршруту не можна) не встигнемо")

    elif command == "говорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "діяти":
        if inhabitant is not None:
            fight_with = input("Що будеш використовувати ? -  ")
            if fight_with in backpack:
                if inhabitant.fight(fight_with):
                    print("Супер все вийшло, можна рухатись далі")
                    corpcount += 1
                    current_room.character = None
                    if corpcount == 3:
                        print("Вітаю ти успішно пройшов весь маршрут і зустрів свого друга")
                        dead = True
                else:
                    print("От халепа")
                    print("Вже за 23, коменданська година почалась, тебе забирає поліція")
                    dead = True
            else:
                print("У тебе немає " + fight_with)
                counter -=1
                if counter == 0:
                    print("От халепа")
                    print("Вже за 23, коменданська година почалась, тебе забирає поліція")
                    break
        else:
            print("На цій вулиці нікого немає, вулиця порожня ")
    elif command == "взяти":
        if item is not None:
            print("Тепер у тебе в інвентарі є " + item.get_name())
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("На цій вулиці нічого немає")
    else:
        print("Не можна відхилятись від графіку) не встигнемо до коменданського")
