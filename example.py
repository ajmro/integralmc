from integralmc import montecarlo 

# integralmc.py must be in the same folder as this file

############################################################################
# Syntax: montecarlo('f', p, l, u)                                         #
############################################################################
# 'f': Function to integrate (python formatted string, variable must be x) #
#   p: Number of points to scatter (increases accuracy, max is 100000)     #
#   l: Lower bound (from)                                                  #
#   u: Upper bound (to)                                                    #
############################################################################

print(montecarlo('x + 5', 2500, 1.5, 9))

print(montecarlo('math.sin(x)', 5000, -4, 4))