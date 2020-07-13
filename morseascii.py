translate = open("translate.txt", "r").read().splitlines()
a2m = {}
m2a = {}
for row in translate:
    ascii, morse = row.split(";")
    a2m[ascii] = morse
    m2a[morse] = ascii

a2m_keys = a2m.keys()
m2a_keys = m2a.keys()

mode = input("M for morse and A for ascii, input: ")
mode = mode.upper()
out_file = open("out.txt", "w")
parenthesis = False
while True:
    chars_raw = input()
    if mode == "M":
        chars = chars_raw.split(",")
        out = []
        for char in chars:
            if char == "-.--.-":
                if parenthesis:
                    out.append(")")
                else:
                    parenthesis = True
                    out.append("(")
            elif char in m2a_keys:
                out.append(m2a[char])
            else:
                print(f"{char} not valid ")

        out_file.write("".join(out) + ";" + chars_raw.replace(" ", "/").replace(",", " ")+"\n")
        print("".join(out))
    elif mode == "A":
        chars = [c.upper() for c in chars_raw]
        out = []
        for char in chars:
            if char in a2m_keys:
                if char == " ":
                    out.append("/")
                else:
                    out.append(a2m[char])
            else:
                print(f"{char} not valid ")
        out_file.write(chars_raw.upper() + ";" + " ".join(out)+"\n")
        print(" ".join(out))
    else:
        break
