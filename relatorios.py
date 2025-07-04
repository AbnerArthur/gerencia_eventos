from functools import reduce  # Importa função útil pra somar listas (tipo um acumulador)

def menu_relatorios(eventos, participantes):
    # Dicionário com as opções de relatórios
    opcoes = {
        '1': lambda: most_active_participant(eventos, participantes),
        '2': lambda: most_common_theme(eventos),
        '3': lambda: total_registrations(eventos),
        '4': lambda: list_names(participantes),
        '5': lambda: events_with_few_participants(eventos),
        '6': lambda: events_by_participant(eventos),
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
            break  # Volta pro menu principal

        acao = opcoes.get(escolha)
        if acao:
            acao()
        else:
            print("Opção inválida.")  # Se digitar algo errado


def most_active_participant(eventos, participantes):
    contagem = {}  # Dicionário pra contar quantas vezes cada participante aparece

    for evento in eventos:
        for cod in evento['participantes']:
            contagem[cod] = contagem.get(cod, 0) + 1  # Vai somando 1 a cada participação

    if not contagem:
        print("Nenhuma inscrição registrada.")  # Se não tiver nenhum participante
        return

    mais_ativo = max(contagem, key=contagem.get)  # Pega quem tem mais participações

    for p in participantes:
        if p['codigo'] == mais_ativo:
            print(f"Participante mais ativo: {p['nome']} ({contagem[mais_ativo]} inscrições)")
            return


def most_common_theme(eventos):
    temas = {}  # Dicionário pra contar os temas

    for evento in eventos:
        tema = evento['tema']
        temas[tema] = temas.get(tema, 0) + 1  # Conta quantas vezes cada tema apareceu

    if not temas:
        print("Nenhum tema registrado.")
        return

    mais_comum = max(temas, key=temas.get)  # Pega o tema mais citado
    print(f"Tema mais comum: {mais_comum} ({temas[mais_comum]} eventos)")


def total_registrations(eventos):
    # Soma o total de participantes em todos os eventos
    total = reduce(lambda acc, e: acc + len(e['participantes']), eventos, 0)
    print(f"Total de inscrições em eventos: {total}")


def list_names(participantes):
    # Pega só os nomes dos participantes
    nomes = list(map(lambda p: p['nome'], participantes))

    print("Nomes dos participantes:")
    for nome in nomes:
        print("-", nome)


def events_with_few_participants(eventos):
    # Filtra os eventos com menos de 2 pessoas
    poucos = list(filter(lambda e: len(e['participantes']) < 2, eventos))

    print("Eventos com menos de dois participantes:")
    for evento in poucos:
        print(f"- {evento['nome']}")


def events_by_participant(eventos):
    # Pede o código do participante
    codigo = input("Digite o código do participante: ")

    # Filtra eventos onde esse código aparece
    relacionados = list(filter(lambda e: codigo in e['participantes'], eventos))

    if relacionados:
        print("Eventos em que o participante está inscrito:")
        for e in relacionados:
            print(f"- {e['nome']}")
    else:
        print("Esse participante não está inscrito em nenhum evento.")
