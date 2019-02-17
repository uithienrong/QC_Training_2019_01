# A. cakes
# Cho int(count)so banh. Tra ve ket qua kieu chuoi theo format: 'Number of cakes: <count>.
# Neu count >= 10 thi thay <count> thanh many
# Ex: cakes(5) returns 'Number of cakes: 5'
# 	  cakes(23) returns 'Number of cakes: many'
def cakes(count):
  # +++code here+++
  if count < 10:
    str_return = 'Number of cakes: %s' % (count)
  else:
    str_return = 'Number of cakes: many'
  return str_return

#B. first_ends
#cho 1 chuoi string s, tra ve 1 chuoi voi 2 ky tu dau cua s va 2 ky tu cuoi cua s
#ex: s = 'spring' cat duoc chuoi 'spng'. Neu length cua chuoi tra ve < 2 thi chuoi tra ve la trong
def first_ends(s):
  # +++code here+++
  s_return = s[:2]+s[-2:]
  if(len(s_return) <= 2):
    s_return=''
  return s_return

# test() function
def test(result, expected):
  if result == expected:
    output = ' OK '
  else:
    output = '  X '
  print '%s result: %s expected: %s' % (output, repr(result), repr(expected))


# main() functions,
# using test() to check result.
def main():
  print 'cakes'
  # Compares result to the expected.
  test(cakes(4), 'Number of cakes: 4')
  test(cakes(9), 'Number of cakes: 9')
  test(cakes(10), 'Number of cakes: many')
  test(cakes(99), 'Number of cakes: many')

  print
  print 'first_ends'
  test(first_ends('spring'), 'spng')
  test(first_ends('Hello'), 'Helo')
  test(first_ends('a'), '')
  test(first_ends('xyz'), 'xyyz')


# Call the main() function.
main()
