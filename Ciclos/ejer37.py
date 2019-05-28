#-*-coding:utf-8-*-



'''Generar todas las tablas de multiplicar del 1 al 10.''' 



try:



	for a in range (1,10+1):
		if a%1==0:
			print "%d"%a
			print"\n"


	for b in range (1,20+1):
		if b%2==0:
			print "%d"%b
			print"\n"

	for c in range (1,30+1):
		if c%3==0:
			print "%d"%c
			print"\n"

	for d in range (1,40+1):
		if d%4==0:
			print "%d"%d
			print"\n"

	for e in range (1,50+1):
		if e%5==0:
			print "%d"%e
			print"\n"


	for f in range (1,60+1):
		if f%6==0:
			print "%d"%f
			print"\n"

	for g in range (1,70+1):
		if g%7==0:
			print "%d"%g
			print"\n"


	for h in range (1,80+1):
		if h%8==0:
			print "%d"%h
			print"\n"


	for i in range (1,90+1):
		if i%9==0:
			print "%d"%i
			print"\n"


	for j in range (1,100+1):
		if j%10==0:
			print "%d"%j
			print"\n"



except ValueError:
	print "error equisde"