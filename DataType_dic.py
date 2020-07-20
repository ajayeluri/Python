
Dic ={}

Dic[0] ="zero"
Dic[1] ="one"
Dic[2] ="two"

#print(Dic)

#updating dictionary
Dic[1] ="One"
print(Dic)

#Iterating dictionary

for num in Dic:
    print(num)

for num in Dic.values():
    print(num)
#keys and valuea
for num ,val in Dic.items():
    print(num,":",val)
