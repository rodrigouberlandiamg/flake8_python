'''
pip install mypy
mypy .\main.py

pypinstall flake8
flake8.exe .\main.py
flake8.exe --select F401 .\main.py
flake8.exe --ignore F401 .\main.py
git config --bool flake8.strict true -> Bloqueia subir para o GIT.
'''


# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila


if __name__ == '__main__':
    # fila_teste = FilaNormal()
    # fila_teste.atualizafila()
    # fila_teste.atualizafila()
    # fila_teste.atualizafila()
    # print(fila_teste.chamacliente(5))
    # print(fila_teste.chamacliente(10))

    # fila_teste2 = FilaPrioritaria()
    # fila_teste2.atualiza_fila()
    # fila_teste2.atualiza_fila()
    # fila_teste2.atualiza_fila()
    # fila_teste2.atualiza_fila()
    # print(fila_teste2.chama_cliente(10))
    # print(fila_teste2.chama_cliente(2))
    # print(fila_teste2.estatistica('19/05/2022',1,'detail'))

    teste_fabrica = FabricaFila.pega_fila('normal')
    teste_fabrica.atualiza_fila()
    teste_fabrica.atualiza_fila()
    teste_fabrica.atualiza_fila()
    print(teste_fabrica.chama_cliente(10))
    print(teste_fabrica.chama_cliente(2))
    # print(teste_fabrica.estatistica('19/05/2022',1,'detail'))