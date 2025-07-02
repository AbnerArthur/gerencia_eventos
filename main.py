# main.py
from eventos import *
from participantes import *
from relatorios import *
from dados_eventos import eventos
from dados_participantes import participantes

def menu():
    opcoes = {
        '1': lambda: listar_eventos(eventos),
        '2': lambda: listar_participantes_por_evento(eventos, participantes),
        '3': lambda: buscar_participante(participantes),
        '4': lambda: adicionar_evento(eventos),
        '5': lambda: atualizar_email(participantes),
        '6': lambda: remover_evento(eventos),
        '7': lambda: remover_participante(participantes),
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
        escolha = input("Escolha uma opção: ")

        if escolha == '0':
            print("Encerrando o sistema.")
            break

        acao = opcoes.get(escolha)
        if acao:
            acao()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()