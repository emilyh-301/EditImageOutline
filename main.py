# Emily Haigh

import os.path
from PIL import Image
import numpy as np

def find_outline(path):
    WHITE = [255,255,255]

    im = Image.open(path) # Can be many different formats.
    pix = im.load()
    # print(im.size)  # Get the width and height of the image for iterating over
    width = im.size[0]
    height = im.size[1]
    new_image = []
    outline_pixels = [ [ [0,0,0] for x in range(width) ] for y in range(height) ]
    for x in range(width):
        for y in range(height):
            if pix[x,y] == WHITE:
                outline_pixels.append([x,y])
                new_image[x,y] = WHITE
    return new_image
    #print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
    #pix[x,y] = value  # Set the RGBA Value of the image (tuple)

# https://stackoverflow.com/questions/49271913/convert-numpy-array-to-rgb-image
def pil2numpy(img: Image = None) -> np.ndarray:
    """
    Convert an HxW pixels RGB Image into an HxWx3 numpy ndarray
    """
    if img is None:
        img = Image.open('amsterdam_190x150.jpg')
    np_array = np.asarray(img)
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


if __name__ == '__main__':
    picture = 'messi_labeled.jpg'
    new_image = find_outline(picture)
    create_json()
    new_image = np.asarray(new_image)
    img = numpy2pil(new_image)
    img.show()
    