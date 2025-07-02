from functools import reduce

def menu_relatorios(eventos, participantes):
    opcoes = {
        '1': lambda: participante_mais_ativo(eventos, participantes),
        '2': lambda: tema_mais_comum(eventos),
        '3': lambda: total_inscricoes(eventos),
        '4': lambda: listar_nomes(participantes),
        '5': lambda: eventos_com_poucos(eventos),
        '6': lambda: eventos_de_um_participante(eventos),
    }

    while True:
        print("""
--- RELATÓRIOS E ESTATÍSTICAS ---
1. Participante mais ativo
2. Tema mais comum
3. Total de inscrições
4. Listar nomes dos participantes
5. Eventos com menos de dois participantes
6. Eventos de um participante específico
0. Voltar ao menu principal
""")
        escolha = input("Escolha uma opção: ")

        if escolha == '0':
            break

        acao = opcoes.get(escolha)
        if acao:
            acao()
        else:
            print("Opção inválida.")
