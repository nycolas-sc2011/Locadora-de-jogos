jogos = []

def cadastrar_jogo(titulo, plataforma, genero, valor, locacao_dia):

    jogo = {
        "titulo": titulo,
        "plataforma": plataforma,
        "genero": genero,
        "locacao_dia": locacao_dia
    }

    jogos.append (jogo)
    return jogo


def listar_jogos(jogos):
    
    if not jogos:
        print("\n[Lista vazia]")
        return

    for jogo in jogos:
        print(f"\nTítulo: {jogo['titulo']}")
        print(f"Plataforma: {jogo['plataforma']}")
        print(f"Gênero: {jogo['genero']}")
        print(f"Locação por dia: {jogo['locacao_dia']}")