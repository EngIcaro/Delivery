from setuptools import setup

# para testar basta usa o pip install . na raiz da pasta do projeto
# DICA: vamos utilizar o pip install -e . pois se fizer sem o -e qualquer mudança no código vai ser preciso 
# reinstalar toda hora. ao fazer com e qualquer mudança o pip já instala para mim
# DICA2: para instalar com os requirments de desenvolvimento podemos passar pip install -e .['dev']

def read(filename):
    return [req.strip() for req in open(filename).readlines()]

setup(
    name="delivery",
    # m(Grande mudança{compatibilidade, funcionamento do app}), mi(Mudança do dia-dia{feature nova, funcionalidade})
    # , patch(mudanças bestas{nome variável, bug, etc})
    version="0.1.0",
    # Description é improtante pq ele va dentro de um arquivo de manifesto na hora que gerar o pacote
    description="Delivery app",
    # o packages fala para o pip na hora que ele está instalando quais os pacotes que serão instalados. É uma lista.
    packages=['delivery'],
    # Essa variável serve para gravar metadados. Ex: coloca no manifesto o nome das pastas de cada pacote e etc
    include_package_data=True,
    # Essa variável diz quais são as dependências que precisam ser instaladas junto com o nosso projeto.
    # No nosso todas as dependências estão no requeriments-dev ou requeriments, para ler o arquivo e 
    # retornar em forma de lista, criamos uma função chamada read que passa como parâmetro o nome do arquivo 
    install_requires=read("requirements.txt"),
    # mesma coisa do de cima mas para o ambiente de desenvolvimento
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)

