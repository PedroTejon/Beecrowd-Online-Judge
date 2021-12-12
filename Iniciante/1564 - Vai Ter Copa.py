while True:
    try:
        print("vai ter copa!" if int(input()) == 0 else "vai ter duas!")
    except EOFError:
        break