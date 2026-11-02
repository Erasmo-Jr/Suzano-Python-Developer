import matplotlib.pyplot as plt


def plotar_imagem(imagem):
    """Exibe uma imagem."""
    plt.figure(figsize=(12, 4))
    plt.imshow(imagem, cmap="gray")
    plt.axis("off")
    plt.show()


def plotar_resultado(*imagens):
    """Exibe várias imagens lado a lado; a última é rotulada como 'Resultado'."""
    quantidade = len(imagens)
    fig, eixos = plt.subplots(nrows=1, ncols=quantidade, figsize=(12, 4), squeeze=False)
    nomes = [f"Imagem {i}" for i in range(1, quantidade)]
    nomes.append("Resultado")
    for eixo, nome, imagem in zip(eixos[0], nomes, imagens):
        eixo.set_title(nome)
        eixo.imshow(imagem, cmap="gray")
        eixo.axis("off")
    fig.tight_layout()
    plt.show()


def plotar_histograma(imagem):
    """Exibe o histograma dos canais R, G e B de uma imagem RGB."""
    fig, eixos = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    cores = ["red", "green", "blue"]
    for indice, (eixo, cor) in enumerate(zip(eixos, cores)):
        eixo.set_title(f"Histograma {cor}")
        eixo.hist(imagem[:, :, indice].ravel(), bins=256, color=cor, alpha=0.8)
    fig.tight_layout()
    plt.show()
