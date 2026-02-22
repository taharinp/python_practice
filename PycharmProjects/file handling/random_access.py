with open('data','rb') as file:
    print(file.read(4))
    file.tell()
    file.seek(-4,2)
    print(file.read(2))