from random import randrange
a1=randrange(1,9)
a2=randrange(0,9)
a3=randrange(0,9)
a4=randrange(0,9)
while True:
	bul=0
	cow=0
	b=int(input('Введите 4-значное число: '))
	b1=b//1000
	b2=(b//100)%10
	b3=(b//10)%10
	b4=b%10
	if a1 == b1:
		bul+=1
	elif a1 == b2:
		cow+=1
	elif a1 == b3:
		cow+=1
	elif a1 == b4:
		cow+=1
	if a2 == b2:
		bul+=1
	elif a2 == b1:
		cow+=1
	elif a2 == b3:
		cow+=1
	elif a2 == b4:
		cow+=1
	if a3 == b3:
		bul+=1
	elif a3 == b1:
		cow+=1
	elif a3 == b2:
		cow+=1
	elif a3 == b4:
		cow+=1
	if a4 == b4:
		bul+=1
	elif a4 == b1:
		cow+=1
	elif a4 == b2:
		cow+=1
	elif a4 == b3:
		cow+=1
	print('cow= '+ str(cow) +'\nbul= '+str(bul))
	if bul==4:
		print("u are win!")
		break