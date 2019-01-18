A = [1,2,3,4]
tich =1
for a in A:
	tich=tich*a
	print("tich",tich)
A[2] = "hoa"
print "A", A[0:4]
del A[1]
print "A",A[0:3]