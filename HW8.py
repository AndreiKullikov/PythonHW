def add_user(phone_book, user_data):
    user_data = user_data.split(',')
    if len(user_data) == 4:
        new_record = {
            'Фамилия': user_data[0],
            'Имя': user_data[1],
            'Телефон': user_data[2],
            'Описание': user_data[3]
        }
        phone_book.append(new_record)
        print("Запись добавлена.")
    else:
        print("Неправильный формат. Пожалуйста введите информацию в следующим формате: 'Фамилия, Имя, Телефон, Описание'.")


def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            phone_book.remove(record)
            write_txt('phon.txt',phone_book)
            return "Запись удалена."
    return "Запись с такой фамилией не найдена."


def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            write_txt('phon.txt',phone_book)
            return "Номер сохранен."
    return "Запись с такой фамилией не найдена"


def find_by_lastname(phone_book, query):
     results = []
     for record in phone_book:
        if record['Фамилия'] == query:
            results.append(record)
     return results


def find_by_number(phone_book, number):
    results = []
    for record in phone_book:
        if record['Телефон'] == number:
            results.append(record)
    return results


def work_with_phonebook():


    choice=show_menu()

    phone_book=read_txt('phon.txt')

    while (choice!=7):

        if choice==1:
            print_result()
        elif choice==2:
            last_name=input('фамилия ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('фамилия ')
            new_number=input('Новый номер ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('Фамилия ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('Номер ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('Новая запись ')
            add_user(phone_book,user_data)
            write_txt('phon.txt',phone_book)
        choice=show_menu()


def show_menu():
    print()
    print('1. Распечатать справочник\n2. Найти телефон по фамилии\n3. Изменить номер телефона\n4. Удалить запись\n5. Найти абонента по номеру телефона\n6. Добавить абонента в справочник\n7. Закончить работу')
    print()
    choice=int(input())
    return choice


def read_txt(filename):

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']



    with open(filename,'r', encoding='utf-8') as phb:

        for line in phb:

            record = dict(zip(fields, line.split(',')))

            phone_book.append(record)

    return phone_book


def write_txt(filename , phone_book):

    with open('phon.txt','w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')


def print_result():
    file1 = open('phon.txt', 'r', encoding='utf-8')
    lines = file1.readlines()
    for line in lines:
        print(line.strip())
    file1.close


work_with_phonebook()






