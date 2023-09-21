"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    return _quadratic_multiply(x, y).decimal_val
    # this just converts the result from a BinaryNumber to a regular int

def _quadratic_multiply(x, y):
    xbvec = x.binary_vec
    ybvec = y.binary_vec
    xbvec, ybvec = pad(xbvec, ybvec)
    
    xval = binary2int(xbvec).decimal_val
    yval = binary2int(ybvec).decimal_val

    if xval <= 1 and yval <= 1:
        return BinaryNumber(xval * yval)

    xleft, xright = split_number(xbvec)
    yleft, yright = split_number(ybvec)

  
    a = _quadratic_multiply(xleft, yleft)
    b = _quadratic_multiply(xleft, yright)
    c = _quadratic_multiply(xright, yleft)

    length = len(xbvec) // 2
    a = bit_shift(a, len(xbvec))
    b = bit_shift(b, length)
    c = bit_shift(c, length)
    
    result = a.decimal_val + b.decimal_val + c.decimal_val

    return result  
    ### TODO
    pass
    ###


    
    
def test_quadratic_multiply(x, y, f):
    x = BinaryNumber(2)
    y = BinaryNumber(3)
    start_time = time.time()
    result = _quadratic_multiply(x, y)
    return (time.time() - start_time) * 1000

