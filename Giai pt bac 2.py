import math
a, b, c = map(float, input('Input a b c:  ').split())
def gptb2(a,b,c): 
    print('{}x^2 + {}x + {}'.format(int(a),int(b),int(c)).center(40,'_'))
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phuong trinh co vo so nghiem\n")
            else:
                print ("Phuong trinh vo nghiem\n")
        else:
            print ("Phuong trinh co mot nghiem duy nhat: \nx = {}\n".format(-c/b))
    else:
        #Tinh delta
        delta=b*b-4*a*c
        #Kiem tra cac truong hop cua delta
        if delta > 0:
            x1=round(float((-b + math.sqrt(delta))/(2*a)),2)
            x2=round(float((-b - math.sqrt(delta))/(2*a)),2)
            print(f"Phuong tring co 2 nghiem phan biet: \nx1 :{x1}\nx2 :{x2}\n")
        elif delta == 0:
            x1=-b/(2*a)
            print(f"Phuong trinh co nghiem kep x1 = x2 : {x1}\n")
        else:
            print("Phuong trinh vo nghiem\n")
gptb2(a,b,c)
gptb2(3*(a**2),8*b,c-5)
gptb2(a-2,b,c-4)