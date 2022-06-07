import gmpy2
from Crypto.Util.number import *

e = 65537
N = 7504521114311153672308826977564891107288058227100173341193360340321176562970983694756086045753375611733443716948010092176135133045533366956059169702726409
c = 3120246791506259955679234385495683489853187127801200033777823093969698684663885288175101358075188702658492281935014546035799989917015048182861857825663454

# Extended Euclidean Algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

# application of Extended Euclidean Algorithm to find a modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

p = gmpy2.isqrt(N)
# https://www.whitman.edu/mathematics/higher_math_online/section03.08.html
# https://crypto.stackexchange.com/questions/5715/phipq-p-1-q-1
phi = p**2-p
d = modinv(e, phi)
m = pow(c, d, N)
print(long_to_bytes(m))
