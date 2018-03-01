#!/usr/bin/env python


class Complex:
    def __init__(self, re=0.0, im=0.0):
        self.real = re
        self.im = im
    # end def


    def __str__(self):
        return '({0} {1} {2}i)'.format(self.real, '-' if self.im < 0 else '+', abs(self.im))
    # end def

    
    def __repr__(self):
        return '({0} {1} {2}i)'.format(self.real, '-' if self.im < 0 else '+', abs(self.im))
    # end def


    def __add__(self, operand):
        try:
            return Complex(self.real + operand.real, self.im + operand.im)
        except:
            if isinstance(operand, int) or isinstance(operand, float):
                return Complex(self.real + operand, self.im)
            else:
                raise TypeError('Operand type not supported')
            # end if
        # end except
    # end def


    def __radd__(self, operand):
        return self + operand
    # end def


    def __sub__(self, operand):
        try:
            return Complex(self.real - operand.real, self.im - operand.im)
        except:
            if isinstance(operand, int) or isinstance(operand, float):
                return Complex(self.real - operand, self.im)
            else:
                raise TypeError
            # end if
        # end except
    # end def


    def __rsub__(self, operand):
        return self - operand
    # end def


    def __mul__(self, op):
        try:
            return Complex(
                    self.real*op.real - self.im*op.im,
                    self.real*op.im - self.im*op.real)
        except:
            if isinstance(op, int) or isinstance(op, float):
                return Complex(self.real*op, self.im*op)
            else:
                raise TypeError
            # end if
        # end except
    # end def

    def __rmul__(self, op):
        return self * op
    # end def

    def __div__(self, op):
        try:
            return self * Complex(
                    op.real / (op.real**2 - op.im**2),
                    -op.im / (op.real**2 - op.im**2))
        except:
            if isinstance(op, int) or isinstance(op, float):
                return Complex(self.real/op, self.im/op)
            else:
                raise TypeError
            # end if
        # end except
    # end def

    def __rdiv__(self, op):
        return self / op
    # end def

    def __neg__(self):
        return Complex(-self.real, -self.im)
    # end def

    def __invert__(self):
        return Complex(self.real, -self.im)
    # end def

# end class

            
if __name__ == '__main__':
    a = Complex(1, 2)
    b = Complex(3.3, 4)

    print a - b
    print a - 3.0
    print 2.9 - a

    print -a
    print ~a


