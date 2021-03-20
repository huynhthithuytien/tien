import random
def guess(n):
    num = random.randint(1,10)
    return num
done = False
while not done:
    val=int(input(" nhap mot so: "))
    num = guess(n)
    if val == num:
        print(" doan dung roi!! ")
        done = True