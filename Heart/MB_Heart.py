from microbit import *

old_heart = str(Image.HEART)
new_heart = ""

for brightness in range(10):
    index=0
    for val in old_heart:
        if old_heart[index] == ":":
            new_heart = new_heart + ":"
        elif old_heart[index] == "0":
            new_heart = new_heart + "0"
        elif str.isdigit(old_heart[index]):
            new_heart = new_heart + str(brightness)

        index += 1

    display.show(Image(new_heart))
    sleep(2000)
    new_heart = ""
