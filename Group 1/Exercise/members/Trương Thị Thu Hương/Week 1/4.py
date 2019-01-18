import math
print("nhap a:")
a=input()
print("nhap b:")
b=input()
print("nhap c:")
c=input()
print("hien:",a,b,c)
if a == 0:
    x = -c/b
    print("nghiem x:",x)
if a != 0:
	D = b*b-4*a*c
	if D<0:
		print("Vo nghiem")
	elif D==0:
		x=-b/(2*a)
		print("nghiem",x)
	else:
		x1= (-b + math.sqrt(D))/(2*a)
		x2= (-b - math.sqrt (D))/(2*a)
		print("x1",x1)
		print("x2",x2)