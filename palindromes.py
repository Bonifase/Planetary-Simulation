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

def is_palindromic_string(string):
    l, r = 0, len(string)-1
    while l < r:
        if string[l].lower() != string[r].lower():
            return False
        l += 1
        r -= 1
    return True

print(is_palindromic_string("Rotator"))

def is_palindromic_number(number):
    reversed_number = 0
    temp = number
    while temp >= 1:
        reversed_number = reversed_number * 10 + (temp % 10)
        temp = temp // 10
    return reversed_number == number


print(is_palindromic_number(13431))

def reverse_digits(digit):
    return int(str(digit)[::-1])

def generate_palindromic(start, iterations):
    f, s = start, reverse_digits(start)
    records = 0
    pals = []

    while f and s and records <= iterations:
        total = f + s
        if is_palindromic_number(total):
            pals.append(total)    
        f = total
        s = reverse_digits(total)
        records += 1
    return pals

print(generate_palindromic(183, 20))

palindromic_squares = []
for i in range(10, 1001):
    if is_palindromic_number(i**2):
        palindromic_squares.append({i:i**2})

print(palindromic_squares)

palindromic_cubes = []
for i in range(10, 1001):
    if is_palindromic_number(i**3):
        palindromic_cubes.append({i:i**3})
    
print(palindromic_cubes)
