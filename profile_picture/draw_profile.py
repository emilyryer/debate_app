from PIL import Image, ImageDraw, ImageFont
#Install Pillow with pip install pillow

def draw_profile_pic(name, red, green, blue):
    initial = ''
    if len(name) == 1:
        initial = name
    else:
        initial = name[0]

    img = Image.new('RGB', (500, 500), color = (red, green, blue))

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/DODGE.ttf", 400)
    textRGB = 0
    if (red + green + blue) < 450:
        textRGB = 255
    draw.text((120,40),initial,(textRGB,textRGB,textRGB),font=font)
    img.save(name + '.png')

#Test Cases (Uncomment to run)
draw_profile_pic('A', 0, 0, 0) #Test case for length one, black background. Letter should be white.
draw_profile_pic('BBBB', 255,255,255) #Test case for white background. Letter should be black.
draw_profile_pic('CCCCC', 127, 44, 67) #Test case for medium-light background. Letter should be white.
draw_profile_pic('DDDD', 81, 22, 67) #Test case for darker background. Letter should be white.
draw_profile_pic('EEEEE', 201, 199, 240) #Test case for lighter background. Letter should be black