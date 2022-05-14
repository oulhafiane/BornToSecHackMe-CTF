import os
import itertools

for c in itertools.permutations("12356"):
	perm_str = "4 {0} {1} {2} {3} {4}".format(*c)
	os.system('echo "'+perm_str+'" | cat input.txt -| ./bomb > /dev/null && echo "'+perm_str+'"')
