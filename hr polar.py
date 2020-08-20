complx = complex(input())
x,y=complx.real, complx.imag

import cmath
print(abs(complex(x,y)))
print(cmath.phase(complex(x,y)))


