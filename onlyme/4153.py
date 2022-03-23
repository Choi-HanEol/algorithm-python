while True:
    list_int = list(map(int, input().split()))
    list_int.sort()

    if list_int == [0, 0, 0]:
        break
    elif (int(list_int[0]) ** 2) + (int(list_int[1]) ** 2) == int(list_int[2]) ** 2:
        print('right')

    else:
        print('wrong')

