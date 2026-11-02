from skimage.io import imread, imsave


def ler_imagem(caminho, em_cinza=False):
    """Carrega uma imagem do disco."""
    return imread(caminho, as_gray=em_cinza)


def salvar_imagem(imagem, caminho):
    """Salva uma imagem no disco."""
    imsave(caminho, imagem)
