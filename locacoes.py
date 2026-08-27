from jogos import jogos
from clientes import clientes

locacoes = []

def calcular_desconto (dias):

    if dias > 7:
            return 0.10
    elif dias > 3:
        return 0.05
    else:
        return 0

def realizar_locacao(jogo, dias, cliente):

    valor_inicial = jogo['locacao_dia'] * dias

    porcentual_desconto = calcular_desconto(dias)
    valor_desconto = valor_inicial * porcentual_desconto

    total_venda = valor_inicial - valor_desconto

    venda = {
        "jogo": jogo['titulo'],
        "plataforma": jogo['plataforma'],
        "cliente": cliente['nome'],
        "quantidade_dias": dias,
        "valor_inicial": valor_inicial,
        "desconto": porcentual_desconto,
        "valor_final": total_venda
    }

    locacoes.append(venda)
    return venda

def listar_locacoes ():

    if not locacoes:
        print("\n[Lista vazia]")
        return


    for venda in locacoes:
        print("\n--Nota Fiscal--")
        print(f"Jogo: {venda['jogo']}")
        print(f"Plataforma {venda['plataforma']}")
        print(f"Cliente: {venda['cliente']}")
        print(f"Quantidade de dias: {venda['quantidade_dias']}")
        print(f"Valor inicial: {venda['valor_inicial']:.2f}")
        print(f"Desconto: {venda['desconto']:.2f}")
        print(f"VALOR TOTAL: {venda['valor_final']:.2f}")