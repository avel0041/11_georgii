# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите максимальное количество идущих подряд символов, 
# среди которых каждая из букв UVWXYZ встречается не более ста раз.

d = {'U':[], 'V':[], 'W':[], 'X':[], 'Y':[], 'Z':[]}
f=open('24_5.txt')
s = f.readline()
l=0
length = 0
a=[]
for i in range(len(s)):
    if s[i] in d:
        d[s[i]].append(i)
        if len(d[s[i]]) > 100:
            if d[s[i]][0] > l:
                l = d[s[i]][0]
            del d[s[i]][0]
        length = i-l
        a.append(length)
print(max(a))

# UVASDUBSAASJKDBUKVSADUV

# U - 15, 20
# l - 1
# V - 1, 18, 21
