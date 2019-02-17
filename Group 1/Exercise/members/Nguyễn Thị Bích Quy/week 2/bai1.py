# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
import re
def front_x(words):
  list_x=[]
  list_notx=[]
  for i in words:
    if re.match("x",i):
      list_x.append(i)
    else:
      list_notx.append(i)
    list_x.sort()
    list_notx.sort()
  return list_x + list_notx

# test() function
def test(result, expected):
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
