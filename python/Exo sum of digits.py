import unittest

def sum_of_digits(n: int) -> int:
    string_n = "%s" % n
    # ou string_n = "{}".format(n)
    #to_array = list(string_n)
    sum=0
    # print(len(string_n[2]))
    for i in range(0,len(string_n)):
        sum = sum + int(string_n[i])
    return sum

def byK(li: list, k: int) -> list:
    listleft = li[(k-len(li)):]
    listright = li[:k]
    return listleft+listright

def repeat(c: str, n: int) -> str:
    res = ''
    for i in range(n):
        res = res + c
    return res

def salary_calc(h: int) -> int:
    if h <= 40:
        res = h*10
    else:
        res = 40*10 + (h-40)*15
    return res

def double(s: str) -> bool:
    ls = list(s)
    if s == '':
        return False

    for i in range(len(ls)):
        if ls.count(ls[i]) == 2:
            return True
    return False

def doubled_string(s: str) -> str:
    out=''
    for i in range(len(s)):
        out=out+s[i]+s[i]
    return out

def isprime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2,int(n/2+1)):
        if n % i == 0:
            return False
    return True

def primes_sum(num: int) -> int:
    """Renvoi la somme des num premiers nombres premiers"""
    sum = 0
    count = 0
    n = 2
    while count < num:
        if isprime(n):
            sum += n
            count += 1
        n += 1
    return sum

def factorial (n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def format_number(n: int) -> str:
    """Retourne une chaîne avec la notation ',' pour les milliers ex : 47634 = 47,634"""
    s = "%s" % n
    lsf = []
    j = 1
    for i in range(len(s)-1,-1,-1):
        lsf.append(s[i])
        if j != len(s) and j % 3 == 0:
            lsf.append(',')
        j += 1
    sf = ''
    for i in range (len(lsf)-1,-1,-1):
        sf += lsf[i]
    return sf

class ExercicesPython(unittest.TestCase):

    def test_sum_of_digits(self):
        res = sum_of_digits(10256)
        self.assertEqual(14,res)

    def test_byK(self):
        res = byK([1,2,3,4,5,6,7,8,9],5)
        self.assertEqual([6,7,8,9,1,2,3,4,5],res)

    def test_repeat(self):
        res = repeat('c',5)
        self.assertEqual('ccccc', res)

    def test_salary_calc(self):
        res = salary_calc(122)
        self.assertEqual(1630,res)

    def test_double(self):
        self.assertEqual(True,double("hello"))
        self.assertEqual(False,double(""))
        self.assertEqual(False,double("big"))
        self.assertEqual(True,double("bb"))
        self.assertEqual(False,double("b"))

    def test_doubled_string(self):
        self.assertEqual('nnooww',doubled_string('now'))
        self.assertEqual('SSttrriinngg',doubled_string('String'))
        self.assertEqual('11223344',doubled_string('1234'))
        self.assertEqual('11',doubled_string('1'))

    def test_isprime(self):
        self.assertEqual(False,isprime(10))
        self.assertEqual(True,isprime(7))
        self.assertEqual(True,isprime(2))

    def test_primes_sum(self):
        self.assertEqual(129,primes_sum(10))
        self.assertEqual(0,primes_sum(0))
        self.assertEqual(2,primes_sum(1))

    def test_factorial(self):
        self.assertEqual(120,factorial(5))
        self.assertEqual(1,factorial(1))
        self.assertEqual(1,factorial(0))
        self.assertEqual(24,factorial(4))

    def test_format_number(self):
        self.assertEqual('10,000',format_number(10000))
        self.assertEqual('10',format_number(10))
        self.assertEqual('100,000,000',format_number(100000000))
        self.assertEqual('0',format_number(0))
        self.assertEqual('123,456,789',format_number(123456789))
        self.assertEqual('1,234,567,890',format_number(1234567890))

if __name__ == '__main__':
    unittest.main()

