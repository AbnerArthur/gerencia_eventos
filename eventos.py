from datetime import datetime  # Importa pra validar e formatar datas

def listar_eventos(eventos):
    print("\n--- Lista de Eventos ---")
    for evento in eventos:
        print(f"Código: {evento['codigo']} | Nome: {evento['nome']} | Data: {evento['data']} | Tema: {evento['tema']}")


def adicionar_evento(eventos):
    while True:
        # Pede o código do evento e padroniza pra maiúsculo
        codigo = input("Código do evento: ").strip().upper()

        # Verifica se já tem um evento com esse código
        if any(evento["codigo"].upper() == codigo for evento in eventos):
            print("Erro: já existe um evento com esse código. Tente novamente.")
        else:
            break  # Sai do loop se o código for único

    # Pede o nome do evento
    nome = input("Nome do evento: ")

    # Validação da data (precisa estar no formato certo e ser real)
    while True:
        data = input("Data do evento (AAAA/MM/DD): ").strip()
        try:
            data_valida = datetime.strptime(data, "%Y/%m/%d")  # Tenta converter
            break
        except ValueError:
            print("Data inválida! Use o formato AAAA/MM/DD com uma data real.")

    # Pede o tema do evento
    tema = input("Tema do evento: ")

    # Adiciona o evento na lista com todos os dados
    eventos.append({
        "codigo": codigo,
        "nome": nome,
        "data": data_valida.strftime("%Y/%m/%d"),
        "tema": tema,
        "participantes": []  # Começa vazio
    })

    print("Evento adicionado com sucesso!")


def remover_evento(eventos):
    # Pede o código do evento a ser removido
    codigo = input("Código do evento a remover: ")

    for evento in eventos:
        if evento["codigo"] == codigo:
            eventos.remove(evento)  # Remove da lista
            print("Evento removido.")
            return

    print("Evento não encontrado.")  # Se não achar o código


def listar_participantes_por_evento(eventos, participantes):
    # Pede o código do evento
    codigo = input("Código do evento: ")

    for evento in eventos:
        if evento["codigo"] == codigo:
            print(f"Participantes do evento '{evento['nome']}':")
            
            # Percorre a lista de códigos de participantes no evento
            for p in evento['participantes']:
                # Procura o participante completo na lista geral
                info = next((x for x in participantes if x['codigo'] == p), None)
                
                if info:
                    print(f"- {info['nome']} ({info['email']})")
            return

    print("Evento não encontrado.")  # Se o código não bater com nenhum evento
