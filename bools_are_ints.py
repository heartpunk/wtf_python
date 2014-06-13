weird_things = ["1 == True", "0 == False"]

for weird_thing in weird_things:
  print("'%s' evaluates to: %s" % (weird_thing, eval(weird_thing)))
