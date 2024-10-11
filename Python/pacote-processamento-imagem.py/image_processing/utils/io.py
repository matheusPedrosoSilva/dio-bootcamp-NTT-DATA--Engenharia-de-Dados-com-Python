from skimage.io import imread, imsave
#faz a leitura e a escrita da imagem?
def read_image(path, is_gray = False):
    image = imread(path, as_gray = is_gray)
    return image

def save_image(image, path):
    imsave(path, image)