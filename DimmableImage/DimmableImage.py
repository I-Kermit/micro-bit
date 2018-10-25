from microbit import *

images = (Image.HEART,
          Image.HEART_SMALL,
          Image.HAPPY,
          Image.SMILE,
          Image.SAD,
          Image.CONFUSED,
          Image.ANGRY,
          Image.ASLEEP,
          Image.SURPRISED,
          Image.SILLY,
          Image.FABULOUS,
          Image.MEH,
          Image.YES,
          Image.NO,
          Image.CLOCK12,
          Image.CLOCK11,
          Image.CLOCK10,
          Image.CLOCK9,
          Image.CLOCK8,
          Image.CLOCK7,
          Image.CLOCK6,
          Image.CLOCK5,
          Image.CLOCK4,
          Image.CLOCK3,
          Image.CLOCK2,
          Image.CLOCK1,
          Image.ARROW_N,
          Image.ARROW_NE,
          Image.ARROW_E,
          Image.ARROW_SE,
          Image.ARROW_S,
          Image.ARROW_SW,
          Image.ARROW_W,
          Image.ARROW_NW,
          Image.TRIANGLE,
          Image.TRIANGLE_LEFT,
          Image.CHESSBOARD,
          Image.DIAMOND,
          Image.DIAMOND_SMALL,
          Image.SQUARE,
          Image.SQUARE_SMALL,
          Image.RABBIT,
          Image.COW,
          Image.MUSIC_CROTCHET,
          Image.MUSIC_QUAVER,
          Image.MUSIC_QUAVERS,
          Image.PITCHFORK,
          Image.XMAS,
          Image.PACMAN,
          Image.TARGET,
          Image.TSHIRT,
          Image.ROLLERSKATE,
          Image.DUCK,
          Image.HOUSE,
          Image.TORTOISE,
          Image.BUTTERFLY,
          Image.STICKFIGURE,
          Image.GHOST,
          Image.SWORD,
          Image.GIRAFFE,
          Image.SKULL,
          Image.UMBRELLA,
          Image.SNAKE)
          
brightness = 9
image_no = 0
old_heart = str(images[image_no])

new_heart = ""

def IncBrightness(brightness):
    if brightness < 9:
        brightness += 1
    
    return brightness

def DecBrightness(brightness):
    if brightness > 0:
        brightness -= 1
    
    return brightness

def IncImageNo(image_no):
    image_no += 1
    if image_no == len(images):
        image_no = 0
    return image_no    

def DecImageNo(image_no):
    image_no -= 1
    if image_no == -1:
        image_no = len(images) - 1
    return image_no

def DimImage(old_heart):
    
    new_heart = ""
    index = 0
    for val in old_heart:
        if old_heart[index] == ":":
            new_heart = new_heart + ":"
        elif old_heart[index] == "0":
            new_heart = new_heart + "0"
        elif str.isdigit(old_heart[index]):
            new_heart = new_heart + str(brightness)

        index += 1
    return new_heart
    
display.show(images[image_no])

while(True):

    if button_b.is_pressed():
        brightness = IncBrightness(brightness)
        old_heart = str(images[image_no])
        new_heart = DimImage(old_heart)
        display.show(Image(new_heart))
    elif button_a.is_pressed():
        brightness = DecBrightness(brightness)
        old_heart = str(images[image_no])
        new_heart = DimImage(old_heart)
        display.show(Image(new_heart))

    if accelerometer.was_gesture('left'):
        image_no = DecImageNo(image_no)
        old_heart = str(images[image_no])
        new_heart = DimImage(old_heart)
        display.show(Image(new_heart))
    elif accelerometer.was_gesture('right'):
        image_no = IncImageNo(image_no)
        old_heart = str(images[image_no])
        new_heart = DimImage(old_heart)
        display.show(Image(new_heart))
