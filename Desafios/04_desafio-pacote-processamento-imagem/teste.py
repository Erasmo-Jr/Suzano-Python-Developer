from processamento_imagem.utilidades.io import ler_imagem, salvar_imagem
from processamento_imagem.utilidades.plot import plotar_resultado, plotar_histograma
from processamento_imagem.processamento.combinar import transferir_histograma
from processamento_imagem.processamento.transformar import redimensionar_imagem

imagem1 = ler_imagem("foto_1.jpg")
imagem2 = ler_imagem("foto_2.jpg")

# Transfere o histograma da imagem2 para a imagem1
resultado = transferir_histograma(imagem1, imagem2)
plotar_resultado(imagem1, imagem2, resultado)
plotar_histograma(resultado)

# Redimensiona para 50% e salva
menor = redimensionar_imagem(imagem1, 0.5)
salvar_imagem(menor, "foto_1_menor.png")