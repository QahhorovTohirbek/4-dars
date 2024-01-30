""" 1 """




""" 2 """

def unli(data):
    unlilar = 'aoeiu'
    count =0
    for d in data:
        if d in unlilar:
            count+=1
    
    return count

print(unli('salom qalesiz'))

