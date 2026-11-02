from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    descricao_longa = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requisitos = [
        linha.strip()
        for linha in f
        if linha.strip() and not linha.strip().startswith("#")
    ]

setup(
    name="dio-desafio-pacote-processamento-imagem",
    version="0.1.0",
    author="Erasmo Jr",
    description="Pacote de processamento de imagens usando scikit-image",
    long_description=descricao_longa,
    long_description_content_type="text/markdown",
    url="https://github.com/Erasmo-Jr/Suzano-Python-Developer/tree/main/Desafios/04_desafio-pacote-processamento-imagem",
    packages=find_packages(),
    install_requires=requisitos,
    python_requires=">=3.8",
    license="MIT",
)
