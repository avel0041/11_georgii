# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите максимальную длину непрерывного фрагмента, 
# который начинается и заканчивается одной и той же буквой из первой половины алфавита 
# (от A до M) и не содержит эту букву внутри.

f=open('24_4.txt')
s=f.readline()
alf = sorted('WERTYUIOPASDFGHJKLZXCVBNM')
alf = alf[:len(alf)//2]
a=[]
for i in alf:
    b=s.split(i)
    a.append(max(b[1:-1], key=len))

print(len((max(a, key=len)))+2)
    
    





