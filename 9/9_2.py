# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.

# Определите количество строк таблицы, в которых квадрат суммы максимального и минимального чисел в строке больше суммы квадратов трёх оставшихся.

a=open('9_2.txt')
a=a.readlines()
c=0
for i in a:
    i=i.split()
    i=list(map(int, i))
    i.sort()
    if (i[0]+i[4])**2 > i[3]**2+i[2]**2+i[1]**2:
        c+=1
print(c)