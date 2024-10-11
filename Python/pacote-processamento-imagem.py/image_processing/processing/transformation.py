from skimage.transform import resize

#transforma o tamanho de uma imagem para um proporção específica
def resize_image(image, proportion):
    assert 0 <= proportion <=1, "Specify a valid proportion between 0 and 1."
    height = round(image.shape[0] * proportion)#pega a altura da imagem original
    width = round(image.shape[1] * proportion)#pega o largura da imagem original
    image_resized = resize(image, (height, width), anti_aliasing = True)#passamos a imagem e as medidas novas para gerar a imagem
    return image_resized