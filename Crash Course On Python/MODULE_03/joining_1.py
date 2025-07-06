print("Hello" + " " + "world")

greetings = ["Hello", "world"]
print(" ".join(greetings))
name = "Alice"
print("Hello, " + name + "!")

phonenum = '2025551212'
area_code = print("(" + phonenum[:3] + ")")


def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line
print(format_phone('2025551212'))