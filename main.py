# main.py

from eventos import *  # Importa tudo que tá no arquivo de eventos
from participantes import *  # Importa tudo do arquivo de participantes
from relatorios import *  # Importa os relatórios
from dados_eventos import eventos  # Importa a lista de eventos
from dados_participantes import participantes  # Importa a lista de participantes

def menu():
    # Dicionário com as opções do menu, cada número chama uma função diferente
    opcoes = {
        '1': lambda: list_events(eventos),
        '2': lambda: list_event_participants(eventos, participantes),
        '3': lambda: find_participant(participantes),
        '4': lambda: add_event(eventos),
        '5': lambda: update_email(participantes),
        '6': lambda: remove_event(eventos),
        '7': lambda: remove_participant(participantes),
        '8': lambda: menu_relatorios(eventos, participantes),
    }

    while True:
        print("""
--- MENU PRINCIPAL ---
1. Listar eventos
2. Listar participantes por evento
3. Buscar participante por código
4. Adicionar novo evento
5. Atualizar e-mail de participante
6. Remover evento
7. Remover participante
8. Relatórios e Estatísticas
0. Sair
""")
        escolha = input("Escolha uma opção: ")  # Pede a opção do usuário

        if escolha == '0':
            print("Encerrando o sistema.")  # Finaliza o programa
            break

        acao = opcoes.get(escolha)  # Pega a função correspondente à opção
        if acao:
            acao()  # Executa a função
        else:
            print("Opção inválida. Tente novamente.")  # Se digitar algo errado


# Essa parte aqui serve pra rodar o menu só se o arquivo for executado direto
# Não roda se o arquivo for só importado por outro
if __name__ == "__main__":
    menu()
