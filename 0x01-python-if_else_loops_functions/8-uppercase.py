#!/usr/bin/python3
def uppercase(str):
    i = 0
    news = ""
    while i != len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            new += chr(ord(str[i]) - 32)
        else:
            news += str[i]
            i += 1
            print("{}".format(news))
