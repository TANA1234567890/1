# 1 .
a = [1,2,3,4,5,1,2]
for l in a:
    if a.count(l) > 1:
        a.remove(l)
print(a)

# 2.
c = [1,2,3,4,5,5,4,3,2,1,0,0,9,7,8,12,12]
s = 0
for i in c:
    d = c.count(i)
    if d == 2:
        s = s + 1
print(s/2)

#3.
c1 = (35,78,21,37,2,98,6,100,231)
c2 = (45,21,124,76,5,23,91,234)
sc1 = 0
sc2 = 0
for i in c1:
    sc1 += i
print(sc1)
for j in c2:
    sc2 += i
print(sc2)
if sc1 > sc2:
    print("Сумма больше в кортеже с1")
else:
    print("Сумма больше в кортеже с2")
print("Порядковый номер min элемента с1:", c1.index(min(c1)))
print("Порядковый номер max элемента с1:", c1.index(max(c1)))
print("Порядковый номер min элемента с2:", c2.index(min(c2)))
print("Порядковый номер max элемента с2:", c2.index(max(c2)))
