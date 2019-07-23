line1="1+1"
line2="2-1"
line3="4*5"
line4="4/2"

def calculate(line):
	if '+' in line:
		index = line.index('+')
		a = int(line[0:index])
		b = int(line[index+1:len(line)])
    	return a+b
	elif '-' in line:
		index = line.index('-')
		a = int(line[0:index])
		b = int(line[index+1:len(line)])
    	return a-b
	elif '*' in line:
		index = line.index('*')
		a = int(line[0:index])
		b = int(line[index+1:len(line)])
    	return a*b
  	elif '/' in line:
  		index = line.index('/')
  		a = int(line[0:index])
    	b = int(line[index+1:len(line)])
    	return a/b  

print(calculate(line1),calculate(line2),calculate(line3),calculate(line4))
