clientes = []

def cadastrar_cliente (nome, telefone):
    cliente = {
        "nome": nome,
        "telefone": telefone
    }
    clientes.append (cliente)
    return cliente

def listar_clientes (clientes):

        if not clientes:
            print("\n[Lista vazia]")
            return

        for cliente in clientes:
            print(f"Nome: {cliente['nome']}")
            print(f"Telefone: {cliente['telefone']}")