# Задача №49. Общее обсуждение
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


# Домашнее задание
# 5. изменить данные 
# 6. удалять данные


# Введение данных по условию
def enter_second_name():
    return input('введите фамилию абонента:').title()

def enter_first_name():
    return input('введите имя абонента:').title()

def enter_family_name():
    return input('введите отчество абонента:').title()

def enter_phone_name():
    return input('введите номер абонента:')

def enter_adress_name():
    return input('введите адрес абонента:').title()

def enter_data():                         # Функция ввода и создания файла 
    surname = enter_second_name()
    name = enter_first_name()
    family = enter_family_name()
    number = enter_phone_name()
    adress = enter_adress_name()
    with open ('book_8_1.txt', 'a', encoding='utf-8') as file:
        file.write(f'{surname} {name} {family} \n{number}\n{adress}\n\n\n')



                                                             # функция вывода данных справочника
def print_data():
    with open('book_8_1.txt', 'r', encoding='utf-8') as file:
       print (file.read())
                                                           # поиск по телефонному справочнику
def search_line():
    print('Выберите вариант поиска:\n'
          '1. Фамилия\n'
          '2. Имя\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант: ')) - 1
    searched = input('введите поисковые данные: ').title()
    with open('book_8_1.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n',' ').split()
            if searched in new_item[index]:
                print(item, end='\n\n')
        
        # print (file.read().split('\n\n'))
        # file.seek(0)
        # print(file.readlines())
 
                                                     # функц. удаления данных
def delete_line(): 
    print('Выберите вариант где нужно удалить:\n'
        '1. Фамилия\n'
        '2. Имя\n'
        '3. Отчество\n'
        '4. Телефон\n'
        '5. Адрес\n'           
        '6. Удалить контакт\n')
    index = int(input('Введите вариант: ')) - 1
    searched = input('введите поисковые данные: ').title()
    with open('book_8_1.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        new_data = []

    for item in data:   
        if searched in item:
            if index < 5:
                contact_info = item.replace('\n', '  ').split()
                if len(contact_info) >= index+1 and searched == contact_info[index]:
                    contact_info[index] = 'Заменить'
                    new_data.append(f'{contact_info[0]} {contact_info[1]} {contact_info[2]}\n {contact_info[3]}\n{contact_info[4]}\n')
                else: new_data.append(item)
            

    with open('book_8_1.txt', 'w', encoding='utf-8') as file:
         file.write('\n'.join(new_data))

                                                   # функ. внесения изменений в котнтакт  
def recover_line():
    print('Выберите вариант где нужно изменить:\n'
        '1. Фамилия\n'
        '2. Имя\n'
        '3. Отчество\n'
        '4. Телефон\n'
        '5. Адрес\n'           
        '6. Изменить контакт\n')
    index = int(input('Введите вариант: ')) -1
    searched = input('введите поисковые данные: ').title()
    recovers = input('введите измененные данные: ').title()

    with open('book_8_1.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
    new_data = []
    

    for item in data:   
        if searched in item:
            if index < 5:
                contact_info = item.replace('\n', '  ').split()
                if len(contact_info) >= index+1 and searched == contact_info[index]:
                    contact_info[index] = recovers
                    new_data.append(f'{contact_info[0]} {contact_info[1]} {contact_info[2]}\n {contact_info[3]}\n{contact_info[4]}\n')
                else: new_data.append(item)
        with open('book_8_1.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_data))
                             

                                                      # функция вывода консоли  
def interface():
    cmd = 0
    while cmd !='6':
        print('Выберите действие:\n'
            '1. Добавить контакт\n'
            '2. Вывести все контакты\n'
            '3. Поиск контакта\n '
            '4. Удалить  данные\n'
            '5. Изменить  данные\n'
            '6. Выход\n')
        cmd = input('Введите действие:')
        while cmd not in ('1','2','3','4','5','6'):
            print('Некорректный ввод')
            cmd = input('Введите действие:')
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                delete_line()                                
            case '5':
                recover_line()                    
            case '6':
                print('всего доброго')
interface()     




       