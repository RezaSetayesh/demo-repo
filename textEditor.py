import string

def make_ready(le: str) -> str:
    isSpace = False
    result = ""
    for char in le:
        if char.isspace():
            isSpace = True
            continue
        elif char in string.punctuation:
            isSpace = True
            result += ' '
        elif char in string.ascii_letters and isSpace:
            isSpace = False
            result += ' '
        result += char
    return result

ends = ['.', '!', '?']
arg = input()
arg = make_ready(arg)
sections = arg.split()
for i, section in enumerate(sections):
    if section[0] in string.ascii_letters:
        section = section.lower()
        if i == 0 or sections[i-1] in ends or section == 'i':
            section = section.capitalize()
        sections[i] = section

for i, section in enumerate(sections):
    print(section, end = "")
    if i == len(sections) - 1: continue

    if sections[i + 1] not in string.punctuation:
        print(' ', end = "")
