from string import ascii_lowercase, ascii_uppercase, digits
from sys import argv
from random import randint


alphabet = ascii_uppercase+ascii_lowercase+digits+"!$*ù&é#'()-è_çà)=+^{}@][|]"

length = int(argv[1])

pw = "".join([alphabet[randint(0,len(alphabet)-1)] for i in range(length)] )

print(pw)