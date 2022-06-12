from re import S
from this import d


palindromic_primes = [
    2,3,5,7,11,101,131,151,181,191,313,353,373,383,
    727,757,787,797,919,929,10301,10501,10601,11311,
    11411,12421,12721,12821,13331,13831,13931,14341,
    14741,15451,15551,16061,16361,16561,16661,17471,
    17971,18181
]
palindromic_squares = [
    0,1,4,9,121,484,676,10201,12321,14641,40804,
    44944,69696,94249,698896,1002001,1234321,4008004,
    5221225,6948496,100020001,102030201,104060401,
    121242121,123454321,125686521,400080004,404090404,
    522808225
]
palindromic_cubes = []

def is_palindromic(string):
    l, r = 0, len(string)-1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True

s = "125686521"
# print(is_palindromic("some"))

def reverse_digits(digit):
    return int(str(digit)[::-1])

def generate_palindromic(n):
    f, s = n, reverse_digits(n)
    records = 0
    pals = []
    while f and s and records <= 10:
        total = f + s
        if is_palindromic(str(total)):
            pals.append(total)    
        f = total
        s = reverse_digits(total)
        records += 1

    return pals

print(generate_palindromic(183))

pals = []
for i in range(10, 1001):
    if is_palindromic(str(i**2)):
        pals.append({i:i**2})
# print(pals)

cubes = []
for i in range(10, 1001):
    if is_palindromic(str(i**3)):
        cubes.append({i:i**3})
# print(cubes)

def rev_num(n):
    rev = 0
    i = n
    while i >= 1:
        rev = rev * 10 + (i % 10)
        i = i // 10
    return rev == n

print(rev_num(13431))
