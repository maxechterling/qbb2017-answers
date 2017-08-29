#!/usr/bin/env python

print "Basic types..."

a_string = "This is a string"

an_integer = 7

i_as_s = str( an_integer )

a_real = 5.689

s_as_r = float( "5.689" )

truthy = True
falsy = False

for value in a_string, an_integer, a_real, truthy:
    print value, type( value )
    
print "Lists and tuples"

a_list = [ 1, 2, 3, 4, 5]
a_tuple = ( 1, "foo", 3.2 )

print a_list, type( a_list )
print a_tuple, type( a_tuple )

# lists are mutable
a_list[3] = 777
print a_list

# tuples are immutable
#a_tuple[3] = 777
#print a_tuple

another_list = a_list

# if you change a list made from another list, you also change the parent (and vice versa)
# this applies to anything that is mutable
#another_list[3] = 888
#print another_list
#print a_list

# instead create a new list like this...
another_list = list(a_list)

another_list[3] = 888
print another_list

print a_list