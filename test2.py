from pynverse import inversefunc
cube = (lambda x: x**3)
# invcube = inversefunc(cube, y_values=3)
#
# # array(3.0000000063797567)
invcube = inversefunc(cube)
print(invcube(27))


# array(3.0000000063797567)
