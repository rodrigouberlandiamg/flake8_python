from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'AN{self.codigo}'

    def chama_cliente(self, caixas: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'Cliente Atual: {cliente_atual} dirija-se ao caixa: {caixas}')