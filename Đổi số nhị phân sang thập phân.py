a= input("bin : ");nhan=0;tong=0;b=len(a)
for i in range(len(a)):
    b-=1
    nhan =int(a[i])*(2**b)
    tong+=nhan
print("dec:",tong)
