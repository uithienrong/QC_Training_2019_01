print ("Nhap a :") 
a=int(input())
print ("Nhap b :") 
b=int(input())
print ("Nhap c :") 
c=int(input())     

if (a+b)>c and (a+c)>b and (b+c)>a and (a>0) and (b>0) and (c>0):
    if(a==b)and (b==c):
        print "Tam giac deu"
    elif((a*b+b*b==c*c)and(a==b))or((a*a+c*c==b*b)and(a==c))or((c*c+b*b==a*a)and(c==b)):
        print "tam giac vuong can"
    elif(a==b)or(b==c)or(a==c):
        print "tam giac can"
    elif((a*a==b*b+c*c)or(b*b==a*a+c*c)or(c*c==a*a+b*b)):
        print "tam giac vuong"
    else:
        print "tam giac thuong"
else:
    print "khong hop le"