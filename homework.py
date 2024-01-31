""" 1 """




""" 2 """

# def unli(data):
#     unlilar = 'aoeiuAOEIU'
#     count =0
#     for d in data:
#         if d in unlilar:
#             count+=1
    
#     return count

# print(unli('salom qalesiz'))


""" 3 """

# def zero_count(data:int):
#     count =0
#     for i in str(data):
#         if i == '0':
#             count+=1
#     return count

# print(zero_count(1020304505940))

""" 3.1 """
# def zero_count(*data:int):
#     count =0
#     for number in data:
#         for i in str(number):
#             if i == '0':
#                 count+=1
#     return count

# print(zero_count(10,20,3,0,4,50,59,40))


""" 4 """

# def unli_harflarni_tekshir(data1, data2):
#     unli_harflar = "aeiouAEIOU"
    
#     unli_harflar_birinchi = set(harf for harf in data1 if harf in unli_harflar)
    
#     return all(harf in unli_harflar_birinchi for harf in data2)


# data1 = "Python django"
# data2 = "Hello World"
# print(unli_harflarni_tekshir(data1, data2))


""" 5 """

def word_count(text: str) -> int:
    count = 0
    is_inside_word = False

    for char in text:
        if char == ' ':
            is_inside_word = False
        elif not is_inside_word:
            count += 1
            is_inside_word = True

    return count

print(word_count(' Bu funksiya so`zlarni sanash uchun '))





