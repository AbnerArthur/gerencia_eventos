def buscar_participante(participantes):
    codigo = input("Código do participante: ")
    for p in participantes:
        if p['codigo'] == codigo:
            print(f"Nome: {p['nome']} | E-mail: {p['email']} | Preferências: {', '.join(p['preferencias'])}")
            return
    print("Participante não encontrado.")

def atualizar_email(participantes):
    codigo = input("Código do participante: ")
    for p in participantes:
        if p['codigo'] == codigo:
            novo_email = input("Novo e-mail: ")
            p['email'] = novo_email
            print("E-mail atualizado.")
            return
    print("Participante não encontrado.")

def remover_participante(participantes):
    codigo = input("Código do participante a remover: ")
    for p in participantes:
        if p['codigo'] == codigo:
            participantes.remove(p)
            print("Participante removido.")
            return
    print("Participante não encontrado.")