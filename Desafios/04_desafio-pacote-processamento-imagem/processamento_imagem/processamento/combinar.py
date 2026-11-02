import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def encontrar_diferenca(imagem1, imagem2):
    """Compara duas imagens RGB pela similaridade estrutural (SSIM).

    Retorna a imagem de diferença normalizada entre 0 e 1.
    """
    assert imagem1.shape == imagem2.shape, "Informe 2 imagens com mesmo formato!"
    imagem1_cinza = rgb2gray(imagem1)
    imagem2_cinza = rgb2gray(imagem2)
    score, imagem_diferenca = structural_similarity(
        imagem1_cinza, imagem2_cinza, full=True, data_range=1.0
    )
    print("Similaridade das imagens:", score)
    minimo, maximo = np.min(imagem_diferenca), np.max(imagem_diferenca)
    if maximo == minimo:
        return np.zeros_like(imagem_diferenca)
    return (imagem_diferenca - minimo) / (maximo - minimo)


def transferir_histograma(imagem1, imagem2):
    """Ajusta o histograma da imagem1 para ficar parecido com o da imagem2."""
    return match_histograms(imagem1, imagem2, channel_axis=-1)
