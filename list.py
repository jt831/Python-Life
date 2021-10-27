# Beautiful is better than ugly

inventor = ['qiyana', 'mei', 'bronya']
j = 0
while j < len(inventor):
    print("Who i wanna invite are " + inventor[j])
    j += 1
print(inventor[0] + " is not available")
remover = inventor.pop(0)
inventor.insert(0, "himoko")
print("i invite " + inventor[0] + " to replace " + remover)
i = 0
while i < len(inventor):
    print("now i invite" + inventor[i])
    i += 1
print("now i found a bigger table, so i can invite more person")
inventor.insert(len(inventor)-1, "silee")
inventor.insert(0, "fuhua")
print(inventor)
print("oh. the table cannot arrive on time")
k = 0
while k < len(inventor)-2:
    print("i feel sorry "+inventor[k])
    inventor.pop(k)
print(inventor)
