from collections import namedtuple

# ism = 'Tohirbek'
# yosh = 23
# manzil = 'Quva'

# person = namedtuple('User', 'ism yosh manzil')

# user_1 = person(ism=ism, yosh=yosh, manzil=manzil)

# print(user_1)

# avto = namedtuple('Avto', 'name company year')
# avtos= []
# for i in range(int(input('Nechta avto kiritmoqchisiz: '))):
#     name = input('Avto nomi: ')
#     company = input('Kompaniya nomi: ')
#     year = input('Nechanchi yilda ishlab chiqarilgan: ')
#     avto_s = avto(name=name, company=company, year=year)
#     avtos.append(avto_s)
# sorted_avto = sorted(avtos, key=lambda x: x.year)
# print(sorted_avto)


# datas = [1, 'salam', 10==10, 'yaxshimisan', 155, True, False, 'ajoyib', 100]

# def types(data):
#     if type(data) == str:
#         return 1
#     elif type(data) == int:
#         return 2
#     elif type(data) == bool:
#         return 3
#     raise ValueError

# datas.sort(key=types)
# print(datas)

def count_word(data):

    with open(data, 'r') as file:
        for line in file:
            return len(line.split()) 
        
print(count_word('data.txt'))






