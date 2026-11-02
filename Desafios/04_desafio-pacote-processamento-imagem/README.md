# processamento_imagem

Pacote Python para processamento de imagens usando [scikit-image](https://scikit-image.org/), desenvolvido como desafio de projeto da trilha **Suzano Python Developer** da [DIO](https://www.dio.me/).

## Funcionalidades

### Módulo `processamento`
| Função | O que faz |
|---|---|
| `transferir_histograma(imagem1, imagem2)` | Ajusta o histograma da `imagem1` para ficar parecido com o da `imagem2` |
| `encontrar_diferenca(imagem1, imagem2)` | Compara duas imagens pela similaridade estrutural (SSIM) e retorna a imagem das diferenças |
| `redimensionar_imagem(imagem, proporcao)` | Redimensiona a imagem por uma proporção entre 0 e 1 |

### Módulo `utilidades`
| Função | O que faz |
|---|---|
| `ler_imagem(caminho, em_cinza=False)` | Carrega uma imagem do disco |
| `salvar_imagem(imagem, caminho)` | Salva uma imagem no disco |
| `plotar_imagem(imagem)` | Exibe uma imagem |
| `plotar_resultado(*imagens)` | Exibe várias imagens lado a lado |
| `plotar_histograma(imagem)` | Exibe o histograma dos canais R, G e B |

## Instalação

Requer Python 3.8 ou superior.

```bash
git clone https://github.com/Erasmo-Jr/Suzano-Python-Developer.git
cd Suzano-Python-Developer/Desafios/04_desafio-pacote-processamento-imagem
pip install .
```

## Exemplo de uso

```python
from processamento_imagem.utilidades.io import ler_imagem, salvar_imagem
from processamento_imagem.utilidades.plot import plotar_resultado, plotar_histograma
from processamento_imagem.processamento.combinar import transferir_histograma, encontrar_diferenca
from processamento_imagem.processamento.transformar import redimensionar_imagem

imagem1 = ler_imagem("foto1.jpg")
imagem2 = ler_imagem("foto2.jpg")

# Transferir o histograma da imagem2 para a imagem1
resultado = transferir_histograma(imagem1, imagem2)
plotar_resultado(imagem1, imagem2, resultado)
plotar_histograma(resultado)

# Redimensionar para 50% do tamanho original
menor = redimensionar_imagem(imagem1, 0.5)
salvar_imagem(menor, "foto1_menor.png")

# Comparar duas imagens do mesmo tamanho
diferenca = encontrar_diferenca(imagem1, imagem1)
```

## Estrutura do projeto

```
processamento_imagem/
├── processamento/
│   ├── combinar.py      # histogramas e similaridade
│   └── transformar.py   # redimensionamento
└── utilidades/
    ├── io.py            # ler e salvar imagens
    └── plot.py          # exibição de imagens e histogramas
```

## Sobre o projeto

O objetivo deste desafio foi aprender a **criar, estruturar e instalar um pacote Python**, usando `setup.py`, `requirements.txt` e módulos organizados, aplicando conceitos de processamento de imagens.

## Autor

**Erasmo Jr**
- GitHub: [@Erasmo-Jr](https://github.com/Erasmo-Jr)

## Licença

Distribuído sob a licença [MIT](https://choosealicense.com/licenses/mit/).
