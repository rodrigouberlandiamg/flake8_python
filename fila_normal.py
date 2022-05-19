class FilaNormal:
    codigo:int = 0
    fila = []
    clientesatendidos = []
    senhaatual:str = ''

    def gerasenhaatual(self) -> None:
        self.senhaatual = f'AN{self.codigo}'

    def resetafila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizafila(self) -> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)

    def chamacliente(self, caixas:int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return(f'Cliente Atual: {cliente_atual} dirija-se ao caixa: {caixas}')