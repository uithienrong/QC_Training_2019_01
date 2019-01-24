# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
import re
def front_x(words):
	# +++code here+++
	listx=[]
	listnotx=[]
	for i in words:
		if re.match("x",i):
			listx.append(i)
		else:
			listnotx.append(i)
		listx.sort()
		listnotx.sort()
	return listx+listnotx



# test() function
def test(result, expected):
	# +++code here+++
  if result == expected:
    output = ' OK '
  else:
    output = '  X '
  print '%s result: %s expected: %s' % (output, repr(result), repr(expected))


# main() functions
def main():
  print 'front_x'
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
main()
