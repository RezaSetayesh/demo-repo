from math import sqrt

nums = [0] * 6

def solve(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("infinite answers")
            else:
                print("no answer")
        else:
            print(f"the answer is: x = {-c/b}")
    else:
        delta = b * b - 4 * a * c
        if delta > 0:
            delta = sqrt(delta)
            print("answers are:")
            print(f"x = {(-b + delta) / (2 * a)} and x = {(-b - delta) / (2 * a)}")
        elif delta == 0:
            print(f"the answer is: x = {-b / (2 * a)}")
        else:
            print("no answer")

def make_ready(arg):
    if arg[0] != '-':
        arg = '+' + arg
    arg = arg + '+'
    arg = arg.replace("+x", "+1x")
    arg = arg.replace("-x", "-1x")
    return arg

def process(arg, add):
    i = arg.find('x')
    if i == -1:
        nums[add + 0] += float(arg)
    else:
        if arg.find('^') == -1:
            nums[add + 1] += float(arg[:i])
        else:
            nums[add + 2] += float(arg[:i])

def split(arg, add):
    lst = 0
    for i in range(1, len(arg)):
        if arg[i] == '-' or arg[i] == '+':
            process(arg[lst:i], add)
            lst = i

eq = input("Enter your equation: ")
eq = eq.replace(' ', '')

eql = eq[0: eq.find('=')]
eqr = eq[eq.find('=') + 1: len(eq)]

eql = make_ready(eql)
eqr = make_ready(eqr)

split(eql, 0)
split(eqr, 3)

a = nums[2] - nums[5]
b = nums[1] - nums[4]
c = nums[0] - nums[3]

solve(a, b, c)
