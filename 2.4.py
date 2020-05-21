


def new_book(file_out):

        with open('recipes.txt', 'r' ,encoding='UTF-8') as fi:
                cook_book = {}
                for line in fi:
                       dishes = line.strip()
                       cook_book[dishes] = []
                       counter = int(fi.readline().strip())

                       for i in range(counter):
                               list_of_ingredients = fi.readline().strip().split('|')
                               temp_dict = {'ingredient_name': list_of_ingredients[0], 'quantity': list_of_ingredients[1], 'measure': list_of_ingredients[2]}
                               cook_book[dishes].append(temp_dict)
                       fi.readline()
                return cook_book

print(new_book('fi'))


def get_shop_list_by_dishes(dishes, person_count):
        cook_book = new_book('recipes.txt')
        shop_list = {}
        for dishes in dishes:
                if dishes in cook_book:
                        for list_of_ingredients in cook_book[dishes]:
                                if list_of_ingredients['ingredient_name'] in shop_list:
                                        shop_list[list_of_ingredients['ingredient_name']]['quantity'] += (int(list_of_ingredients['quantity']) * person_count)
                                else:
                                        shop_list[list_of_ingredients['ingredient_name']] = {'measure': list_of_ingredients['measure'], 'quatity': int(list_of_ingredients['quantity']) * person_count}
        return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))





















                # print(dish_name)
            # dish_name = <что-то тут делаем>
            # counter = <как-то получили кол-во строк>
            # list_of_ingridient = <временный список>
            # for i in <наш счетчик counter использовать range>:
            #     temp_dict = {} - временный словарь
            #     ingridient = cook_list.readline() - вот так перемещаемся по файлу
            #     <заполняем словарь с ингридиетом>
            #     <добавляем словарь в список>
            # <записываем в словарь cook_dict наш рецепт>
            # file_work.readline() - еще раз смещаетмся т.к. там пустая срока

