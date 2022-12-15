
with open ('recipe.txt', encoding='utf-8' ) as f:
    def get_shop_list_by_dishes(dishes, person):
        person=2
        if dishes in cook_book.keys():
            return (f'Для блюда {dishes} требуются следующие ингредиенты {cook_book["ingredient_name"]},  ')

    cook_book = {}
    dishes, ingredients = [], []
    for  line in f:
        food = line.strip()
        count = int(f.readline())
        ingrs=[]
        for i in range (count):
            ingr = f.readline().strip()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingrs.append({"ingredient_name":ingredient_name,
                       "quantity":quantity,
                       "measure":measure
                       })
        f.readline()
        ingredients.append(ingrs)
        dishes.append(food)
        cook_book = cook_book | dict(zip(dishes , ingredients))
    print(cook_book)
