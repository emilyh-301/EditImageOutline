# Emily Haigh

from PIL import Image

def find_outline(path):
    WHITE = [255,255,255]

    im = Image.open(path) # Can be many different formats.
    pix = im.load()
    # print(im.size)  # Get the width and height of the image for iterating over
    width = im.size[0]
    height = im.size[1]
    outline_pixels = []
    for x in range(width):
        for y in range(height):
            if pix[x,y] == WHITE:
                outline_pixels.append([x,y])
    #print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
    #pix[x,y] = value  # Set the RGBA Value of the image (tuple)

def create_json():
    pass

if '__name__' == '__main__':
    picture = 'messi_labeled.jpg'
    find_outline(picture)
    create_json()
    