# Emily Haigh

import os.path
from PIL import Image
import numpy as np

def find_outline(path):
    WHITE = (255,255,255)

    im = Image.open(path) # Can be many different formats.
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
    return new_image
    #print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
    #pix[x,y] = value  # Set the RGBA Value of the image (tuple)

# https://stackoverflow.com/questions/49271913/convert-numpy-array-to-rgb-image
def pil2numpy(img: Image = None) -> np.ndarray:
    """
    Convert an HxW pixels RGB Image into an HxWx3 numpy ndarray
    """
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    if img is None:
        img = Image.open('messi_labeled.jpg')
    np_array = np.asarray(img)
    s = np_array.shape
    width = s[0]
    height = s[1]
    for x in range(width):
        for y in range(height):
            if np_array[x][y] == WHITE:
                np_array[x][y] = YELLOW
    return np_array


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

def create_json():
    pass


def test():
    arr = pil2numpy()
    print('testing', arr[10][10])
    numpy2pil(arr).show()


if __name__ == '__main__':
    test()
    picture = 'messi_labeled.jpg'
    new_image = find_outline(picture)
    create_json()
    new_image = np.asarray(new_image)
    print('new image', new_image[10][10])
    img = numpy2pil(new_image)
    img.show()
    