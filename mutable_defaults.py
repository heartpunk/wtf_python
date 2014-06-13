def foo(bar=[]):
  print("beginning of foo")
  print(bar)
  bar += [1]
  print(bar)
  print("end of foo")

foo()
print('')
foo()
