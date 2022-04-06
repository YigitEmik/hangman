import time


def loading(string):
    print(string, end="")
    for i in range(0, 3):
        print(".", end="")
        time.sleep(0.5)
    print("")
