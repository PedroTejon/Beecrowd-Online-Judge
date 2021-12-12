i = input().split()
if int(i[0]) * int(i[1]) == int(i[2]) * int(i[3]):
    print(int(i[0]) * int(i[1]))
    print(int(i[2]) * int(i[3]))
    print(0)
elif int(i[0]) * int(i[1]) > int(i[2]) * int(i[3]):
    print(int(i[0]) * int(i[1]))
    print(int(i[2]) * int(i[3]))
    print(-1)
elif int(i[0]) * int(i[1]) < int(i[2]) * int(i[3]):
    print(int(i[0]) * int(i[1]))
    print(int(i[2]) * int(i[3]))
    print(1)