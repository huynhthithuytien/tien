n = int(input("nhap so luong so nguyen can nhap :"))
str=[]
for i in range(0,n):
    str.append(int(input('nhap so thu %d:' %(i+1))))
    str.sort()
print(str)

