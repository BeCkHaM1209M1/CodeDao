import math
a=True
while a:
    try:
        a,b,c=map(float,input("Input Data: ").split())
        if a==0:
            if b==0:
                if c==0:
                    print("Phương trinh co vo so nghiem")
                else:
                    print("Phuong tinh vo nghiem")
            else:
                print("Phuong trinh co mot nghiem duy nhat")
        else :
            delta= b*b-4*a*c
            if delta==0:
                x1=-b/(2*a)
                print(f"Phuong trinh co nghiem kep x1 = x2 : {x1}")
            elif delta >0:
                x1=float((-b + math.sqrt(delta))/(2*a))
                x2=float((-b - math.sqrt(delta))/(2*a))
                print(f"Phuong tring co 2 nghiem phan biet: x1 :{x1}, x2 :{x2}")
            else:
                print("Phuong tinh vo nghiem")
            break
    except:
        print("Nhập lại đầu vào!")
