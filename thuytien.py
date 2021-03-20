n=int(input("Nhap so phan tu"))
a=[]
for i in range(0,n):
    x=int(input("Nhap phan tu thu %d" %(i)))
    a.append(x)
print("mang da nhap:")
print(a)
mx=max(a)
print("phan tu lon nhat la :")
print(mx)

m=int(input("Nhap so phan tu:"))
b=[]
for j in range(0,m):
    y=int(input("Nhap phan tu thu %d" %(j)))
    b.append(y)
print("chuoi da nhap:")
print(b)
print("chuoi dao nguoc la:")
print(list(reversed(b)))




