# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.
f=open('24_2.txt')

s=f.readline()
# a=[]
# k=1
# for i in range(0, len(s)):
#     if ((s[i]=='K') and  (s[i+1]=='L')) or((s[i]=='L') and (s[i+1]=='K')) :
#         k=1
#     else:
#          k=k+1
#          a.append(k)
# print(max(a))

s = s.replace('KL', 'K L')
s = s.replace('LK', 'L K')
s = s.split()
s = max(s, key=len)
print(len(s))
# a = [1, 2, 99, 32]
# 'ABC ASJD KSADH KJSDH' -> ['ABC', 'ASJD', ...]
# 'SADHFAKSL KBSAHDVUSK LDSAJH' -> [']