from pdb import set_trace as db

print("Type integers and sum them")

total=0
count=0
while True:
	#line = input("Integer: ")
	line = input()
	if line:
		try:
			number = int(line)
			total += number
			count += 1         
		except ValueError as err:
			print(err)
			continue
		except EOFError:
			break
		#total += number
		#count+=1
	else:
		break
if count:
	print("count: ",count,"total: ",total,"mean: ",total/count)


