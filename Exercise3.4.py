def do_twice(f,v):
	f(v)
	f(v)

def print_twice(s):
	print(s)
	print(s)

do_twice(print_twice, 'spam')
print (" ")

def do_four(o,v):
	do_twice(o,v)
	do_twice(o,v)

do_four(print_twice, 'spam')
print(' ')