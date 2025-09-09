import math
import string

arg = input("enter your equation: ")
arg = arg.replace(" ", "")
if arg[0] != '-' and arg[0] != '+':
    arg = '+' + arg
arg = arg + '+'
nums = [0] * 6

def process(l, r, add):
    i = arg[l:r].find('x') + l
    if i < l:
        nums[add + 0] += float(arg[l:r])
    else:
        j = arg[l:r].find('^')
        if j == -1:
            nums[add + 1] += float(arg[l:i])
        else:
            nums[add + 2] += float(arg[l:i])

def split(l, r, add):
    lst = l
    for i in range(l+1, r):
        if arg[i] == '+' or arg[i] == '-':
            process(lst, i, add)
            lst = i

def get_answers(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("This equation has infinite answers")
            else:
                print("This equation has no answers")
        else:
            print("This equation has one answer: ")
            print(f"x = {-c / b}")
    else:
        delta = b * b - 4 * a * c
        if delta > 0:
            delta = math.sqrt(delta)
            print("This equation has two answers: ")
            print(f"x = {(- b + delta) / (2 * a)}")
            print(f"x = {(- b - delta) / (2 * a)}")
        elif delta == 0:
            print("This equation has one answer: ")
            print(f"x = {-b/ (2 * a)}")
        else:
            print("This equation has no answer")

arg = arg.replace("+x", "+1x")
arg = arg.replace("-x", "-1x")
switch_side = arg.index('=')
if arg[switch_side + 1] != '-' and arg[switch_side + 1] != '+':
    arg = arg.replace("=", '=+')
arg = arg.replace("=+", "+=+")
switch_side += 1
split(0, switch_side, 0)
split(switch_side + 1, len(arg), 3)
a = nums[2] - nums[5]
b = nums[1] - nums[4]
c = nums[0] - nums[3]
get_answers(a, b, c)