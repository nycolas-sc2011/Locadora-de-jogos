from clientes import cadastrar_cliente, listar_clientes, clientes
from jogos import cadastrar_jogo, listar_jogos, jogos
from locacoes import realizar_locacao, listar_locacoes, locacoes

from persistencia import (salvar_jogos, carregar_jogos, salvar_clientes, carregar_clientes, salvar_locacoes, carregar_locacoes)

clientes.extend(carregar_clientes())
jogos.extend(carregar_jogos())
locacoes.extend(carregar_locacoes())


def menu():
    while (True):
        print("\n-==MENU DA LOCADORA==-")
        print("[1] - Cadastrar clientes;\n[2] - Cadastrar jogos;\n[3] - Realizar locações;\n[4] - Listar clientes;\n[5] - Listar jogos;\n[6] - Listar locações;\n[7] - Sair.")

        opcao = input("Tecle a opção desejada: ")

        if opcao == '1':
            print("\n--Cadastrar clientes--")
            nome = input("Nome do cliente: ")
            telefone = input("Telefone do cliente: ")
            cadastrar_cliente(nome, telefone)

            cadastrar_cliente(nome, telefone)
            salvar_clientes(clientes)

            print("\n[Cliente cadastrado com sucesso!]")

        elif opcao == '2':
            print("\n--Cadastrar jogos--")
            titulo = input("Título do jogo: ")
            plataforma = input("Plataforma: ")
            genero = input("Gênero: ")
            valor = float(input("Valor do jogo: "))
            locacao_dia = float(input("Valor da locação por dia: "))

            cadastrar_jogo(titulo, plataforma, genero, valor, locacao_dia)
            salvar_jogos(jogos)

            print("\n[Jogo cadastrado com sucesso!]")

        elif opcao == '3':
            print("\n--Realizar locações--")
            titulo = input("Digite o título do jogo: ")
            nome = input("Digite o nome do cliente: ")

            jogo_encontrado = None
            cliente_encontrado = None

            for jogo in jogos:
                if jogo['titulo'].lower() == titulo.lower():
                    jogo_encontrado = jogo
                    break

            for cliente in clientes:
                if cliente['nome'].lower() == nome.lower():
                    cliente_encontrado = cliente
                    break

            if jogo_encontrado is None:
                print("\n[Jogo não encontrado]")

            elif cliente_encontrado is None:
                print("\n[Cliente não encontrado]")

            else:
                dias = int(input("Por quantos dias você deseja alugar o jogo? "))

                realizar_locacao(jogo_encontrado, dias, cliente_encontrado)
                salvar_locacoes(locacoes)

                print("\n[Locação realizada com sucesso!]")

        elif opcao == '4':
            print("\n--Listar clientes--")
            listar_clientes(clientes)

        elif opcao == '5':
            print("\n--Listar jogos--")
            listar_jogos(jogos)

        elif opcao == '6':
            print("\n--Listar locações--")
            listar_locacoes()

        elif opcao == '7':
            print("Adeus!")
            break

        else:
            print("\n[Opção Inválida]")

menu ()