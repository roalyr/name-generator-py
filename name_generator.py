######## NAME GENERATOR ##########
import random as random_char
random_char.seed('3643rg')

# Quantity according to frequency. Adjust as you see fit to change the style.
# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
chars_low_v = "y"+"u"*2+"oi"*4+"a"*5+"e"*6
chars_low_c = "qjzx"+"vk"*5+"w"*7+"f"*9+"b"*11\
	+"g"*12+"hm"*15+"p"*16+"d"*17+"c"*23+"l"*28\
	+"s"*29+"n"*34+"t"*35+"r"*39

chars_low_c = ''.join(random_char.sample(chars_low_c,len(chars_low_c)))
chars_low_v = ''.join(random_char.sample(chars_low_v,len(chars_low_v)))

ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Adjust max values and chances as you see fit for different style.
def random_name(length_max, length_min):
	length = random_char.randint(length_max, length_min)
	vowel_ratio = 0.5
	r = random_char.random()
	max_vowels_consequtive = 0
	max_cosonants_consequiteve = 0
	if r < 0.3:
		max_vowels_consequtive = 1
		max_cosonants_consequiteve = 2
	elif r > 0.3 and r < 0.6:
		max_vowels_consequtive = 2
		max_cosonants_consequiteve = 2
	else:
		max_vowels_consequtive = 1
		max_cosonants_consequiteve = 1
		length += 1
		
	num_v = 0
	num_c = 0
	str = ''
	for ch in range(length):
		r = random_char.random()
		if r < vowel_ratio:
			if num_v < max_vowels_consequtive:
				str += ''.join(random_char.choices(chars_low_v, k=1))
				num_v += 1
				num_c = 0
			else:
				str += ''.join(random_char.choices(chars_low_c, k=1))
				num_v = 0
				num_c += 1
		else:
			if num_c < max_cosonants_consequiteve:
				str += ''.join(random_char.choices(chars_low_c, k=1))
				num_c += 1
				num_v = 0
			else:
				str += ''.join(random_char.choices(chars_low_v, k=1))
				num_c = 0
				num_v += 1
	
	#str = str.replace("rs", "ras")
	if (str[0] in chars_low_c and str[1] in chars_low_c):
		str = str[1:]
	
	if  str[0] == 'x':
		str = str[1:]
		
	if  str[len(str)-1] == 'x':
		str = str[:len(str)-1]
		
	if  str[len(str)-1] == 'y':
		str = str[:len(str)-1]
	
	return str.capitalize()
	
	
# Test.
cmin = 4
cmax = 7
for _ in range(100):
	print(random_name(cmin, cmax))