from pprint import pprint
def get_date(file_name):
    cook_book = {}
    with open(file_name, encoding='UTF8') as file:
        for line in file:
            dish_name = line.strip()
            ingredients = int(file.readline().strip())
            dish = []
            for ingredient in range(ingredients):
                ingredient_name, quantity, measure = file.readline().split('|')
                list_ingredients = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                dish.append(list_ingredients)
                cook_book[dish_name] = dish
            print(file.readline())
    return f'{cook_book}'
result = get_date('recipes.txt')
# print(result)
new_cook_book = eval(result)

def cook_book():
    for key, value in new_cook_book.items():
        print(f'{key}: ')
        for val in value:
            print(f'{val}')
        print()
cook_book()





# with open('main.py','w',encoding='UTF8') as file:
