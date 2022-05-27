# Emily Haigh

import os.path
from PIL import Image
import numpy as np


def find_outline(path):
    WHITE = (255,255,255)

    im = Image.open(path)  # Can be different formats.
    pix = im.load()
    # print(im.size)  # Get the width and height of the image for iterating over
    width = im.size[0]
    height = im.size[1]
    new_image = [ [ (255,255,0) for x in range(width) ] for y in range(height) ]
    outline_pixels = []
    for x in range(width):
        for y in range(height):
            if pix[x,y] == WHITE:
                outline_pixels.append([x,y])
                new_image[x][y] = WHITE
    return new_image, outline_pixels
    #print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
    #pix[x,y] = value  # Set the RGBA Value of the image (tuple)


# https://stackoverflow.com/questions/49271913/convert-numpy-array-to-rgb-image
def pil2numpy(img: Image = None):
    """
    Convert an HxW pixels RGB Image into an HxWx3 numpy ndarray
    """
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    outline = []
    if img is None:
        img = Image.open('test.png')
    np_array = np.asarray(img)
    s = np_array.shape
    width = s[0]
    height = s[1]
    for x in range(width):
        for y in range(height):
            count = 0
            for z in range(3):
                # if this pixel is white, change it to yellow
                if np_array[x][y][z] == WHITE[z]: count += 1
                if count == 3:
                    np_array[x][y] = YELLOW
                    outline.append([x,y])
    print('test outline', len(outline))
    return np_array, outline


def numpy2pil(np_array: np.ndarray) -> Image:
    """
    Convert an HxWx3 numpy array into an RGB Image
    """
    assert_msg = 'Input shall be a HxWx3 ndarray'
    assert isinstance(np_array, np.ndarray), assert_msg
    assert len(np_array.shape) == 3, assert_msg
    assert np_array.shape[2] == 3, assert_msg
    img = Image.fromarray(np_array, 'RGB')
    return img


def create_json(outline):
    '''Input is a list of pixels that are part of the image outline
    and the output is a string of those pixels in json format'''
    json_string = '['
    for i in range(len(outline)-1):
        json_string += '{"x":' + str(outline[i][0]) + ', "y":' + str(outline[i][1]) + '},'
    json_string += '{"x":' + str(outline[len(outline)-1][0]) + ', "y":' + str(outline[len(outline)-1][1]) + '}]'
    return json_string


def addPixelsToTxt(outline):
    file = open('pixels.txt', 'w')
    for i in range(len(outline)-1):
        s = str(outline[i][0]) + ' ' + str(outline[i][1]) + '\n'
        file.write(s)
    file.close()


def test():
    arr, outline = pil2numpy()
    create_json(outline)
    #print('testing', arr[10][10])
    numpy2pil(arr).show()


if __name__ == '__main__':
    test()
    picture = 'test.png'
    new_image, outline1 = find_outline(picture)
    create_json(outline1)
    addPixelsToTxt(outline1)
    new_image = np.asarray(new_image)
    img = numpy2pil(new_image)
    #img.show()
    