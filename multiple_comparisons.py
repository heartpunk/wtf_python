first_thing = "'s' in 'asdf' == True"
print(first_thing)
print(eval(first_thing))

second_thing = "('s' in 'asdf') and ('asdf' == True)"
print(second_thing)
print(eval(second_thing))

both_of_the_things = "(%s) == (%s)" % (first_thing, second_thing)
print(both_of_the_things)
print(eval(both_of_the_things))
