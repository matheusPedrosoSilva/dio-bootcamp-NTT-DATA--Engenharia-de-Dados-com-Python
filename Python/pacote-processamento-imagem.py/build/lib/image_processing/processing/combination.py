import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2):#encontra a diferença entre duas imagens
    assert image1.shape == image2.shape, "Specify 2 images with de same shape"#verifica se as imagens são iguais, se não for ele retorna a string
    gray_image1 = rgb2gray(image1)#as variaveis recebem as imagens
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True) # converte ambas as imagens para fazer a comparação entre elas dentro do mesmo tom, gerando assim um score e uma imagem resultante dessa comparação
    print(f"Similarity of the images: {score:2%}")
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))#deixa mais claro a diferença entre as imagens
    return normalized_difference_image

def transger_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image