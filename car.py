cars = set()

while True:
    print("1.меню редагування машин на штраф майданчик ")
    print("2.видалити машину")
    print("3.оновити назву машину")
    print("4.подивитися кількість записаних машин")
    print("5.подивитися список машин")
    choise = input("введіть дію:")
    match choise:
        case "1":
            name = input("введіть назву машини:")
            cars.add(name)
        case "2":
            name = input("введіть назву машини:")
            cars.discard(name)
        case "3":
            name = input("введіть існуючу назву машини:")
            if name in cars:
                new_name = input("введіть нову назву машини")
                cars.discard(name)
                cars.add(new_name)
            else:
                print("такої назви машини немає неможливо видалити або ввели дані не вірно")
        case "4":
            print(f"кількість машин:{len(cars)}")
        case "5":
            print(cars)
        case "_":
            print("такої дії немає спробуйте ще раз")