import csv


def mary_favorite_food(line):
    if line[0] == 'maria':
        obj = {}
        more_orders = {line[1]: 1}

        if line[1] not in obj:
            obj[line[1]] = 1
        else:
            obj[line[1]] += 1
        if obj[line[1]] > more_orders[line[1]]:
            more_orders[line[1]] = obj[line[1]]

        for key, value in dict.items(more_orders):
            favorite_food = key

        return favorite_food


def arnold_ask_hamburguer(line):
    if line[0] == 'arnaldo' and line[1] == 'hamburguer':
        return 1
    return 0


def john_never_ask(line, john_foods):
    if line[0] == 'joao':
        john_foods.add(line[1])
        return john_foods


def john_never_went(line, john_days):
    if line[0] == 'joao':
        john_days.add(line[2])
        return john_days


def raise_error(file_path):
    if not file_path.endswith('.csv'):
        raise FileNotFoundError(
            "Extensão inválida: '{}'".format(file_path)
        )


def analyze_log(path_to_file):
    raise_error(path_to_file)

    try:
        foods = set()
        days = set()
        john_foods = set()
        john_days = set()
        arnold_answer = 0

        with open(path_to_file, 'r') as f:
            lines = csv.reader(f)

            for line in lines:
                foods.add(line[1])
                days.add(line[2])

                mary_answer = mary_favorite_food(line)
                arnold_answer += arnold_ask_hamburguer(line)

                if line[0] == 'joao':
                    john_foods.add(line[1])
                    john_days.add(line[2])

            unordered_food = foods.difference(john_foods)
            days_not_attended = days.difference(john_days)

        with open("data/mkt_campaign.txt", "w") as f:
            f.write(str(mary_answer))
            f.write(("\n" + str(arnold_answer)))
            f.write(("\n" + str(unordered_food)))
            f.write(("\n" + str(days_not_attended)))

    except FileNotFoundError:
        raise FileNotFoundError("Arquivo inexistente: '{}'".format(path_to_file))


print(analyze_log("data/orders_1.csv"))