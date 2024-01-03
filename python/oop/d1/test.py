count = 0
count1 = 0


def counter():
    global count
    count += 1

def counter1():
    global count1
    count1 += 1
    # print(count)

counter()
counter()
counter()
counter()
counter()
print(count)


counter1()
counter1()
counter1()
print(count1)