def find_participant(participantes):
    # Pede o código do participante, remove espaços e converte para letra maiúscula
    codigo = input("Código do participante: ").strip().upper()
    
    for p in participantes: 
    # Compara o código digitado com o código do participante, ignorando maiúsculas/minúsculas
        if p['codigo'].upper() == codigo:
            print(f"Nome: {p['nome']} | E-mail: {p['email']} | Preferências: {', '.join(p['preferencias'])}")
            return  # Encerra se encontrar
        
        # Se o laço não encontrar ninguém, vai exibir a mensagem
    print("Participante não encontrado.")


def update_email(participantes):
    # Solicita o código e padroniza (remove espaços e transforma em maiúsculas)
    codigo = input("Código do participante: ").strip().upper()
    
    #Percorre a lista de participantes
    for p in participantes:
        # Verifica se o código é de algum participante
        if p['codigo'].upper() == codigo:
            
            # pede um novo email
            novo_email = input("Novo e-mail: ").strip()
            
            # Para garantir que o email tem '@' e '.'
            if "@" in novo_email and "." in novo_email:
                p['email'] = novo_email  # Atualiza o email
                print("E-mail atualizado.")
            else:
                print("E-mail inválido.")  # Se o email não tiver o formato correto
            return  # Encerra a função
    print("Participante não encontrado.")  # Se nenhum participante foi encontrado


def remove_participant(participantes):
    # Pede o código do participante e padroniza
    codigo = input("Código do participante a remover: ").strip().upper()
    
    #Percorre novamente a lista participantes
    for p in participantes:
        
        #Verificando se o código está de acordo
        if p['codigo'].upper() == codigo:
            participantes.remove(p)  # Remove o participante da lista
            print("Participante removido.")
            return  # Encerra a função
        
    print("Participante não encontrado.")  # Se não encontrar ninguém
