from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Matheus Pedroso da Silva",
    author_email="matheus.pedroso.silva21@gmail.com",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matheusPedrosoSilva/pacote-processamento-imagem.py",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)