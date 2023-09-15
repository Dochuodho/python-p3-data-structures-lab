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
    },
]

def get_names(spicy_foods):
    names = [x["name"] for x  in spicy_foods]
    print(names)
    return names
get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    foods = [x for x in spicy_foods if x["heat_level"] > 5]
    return foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        word=""
        word+= food.get("name") + " " + "(" + food.get("cuisine") + ")" + " " + "|" + " " + "Heat Level: " + ("🌶" * food.get("heat_level"))
        print(word)
    
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine in food.values():
            return food
    pass

def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        word_output =""
        if food.get("heat_level") > 5:
            word_output += food.get("name") + " " + "(" + food.get("cuisine") + ")" + " " + "|" + " " + "Heat Level: " + ("🌶" * food.get("heat_level"))
            print(word_output)
    
    

def get_average_heat_level(spicy_foods):
    sum_food=0
    count=0

    for food in spicy_foods:
        sum_food += food.get("heat_level")
        count += 1
    return int(sum_food/ count)
   


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
