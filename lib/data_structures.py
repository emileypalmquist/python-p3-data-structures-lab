spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]


def get_names(spicy_foods):
    # new_list = list()
    # for el in spicy_foods:
    #     new_list.append(el["name"])
    # return new_list
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]


def format_food(food):
    peppers = "🌶" * food["heat_level"]
    name = food["name"]
    cuisine = food["cuisine"]

    return f"{name} ({cuisine}) | Heat Level: {peppers}"


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(format_food(food))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)

    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    spicy_sum = sum(food["heat_level"] for food in spicy_foods)
    return spicy_sum / len(spicy_foods)
