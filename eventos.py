from datetime import datetime

def listar_eventos(eventos):
    print("\n--- Lista de Eventos ---")
    for evento in eventos:
        print(f"Código: {evento['codigo']} | Nome: {evento['nome']} | Data: {evento['data']} | Tema: {evento['tema']}")

def adicionar_evento(eventos):
    while True:
        codigo = input("Código do evento: ").strip().upper()  # PADRONIZANDO EM MAIÚSCULA

        # VERIFICA SE JÁ EXISTE EVENTO COM O CÓDIGO
        if any(evento["codigo"].upper() == codigo for evento in eventos):
            print("Erro: já existe um evento com esse código. Tente novamente.")
        else:
            break

    nome = input("Nome do evento: ")

    # VALIDAÇÃO DA DATA
    while True:
        data = input("Data do evento (AAAA/MM/DD): ").strip()
        try:
            data_valida = datetime.strptime(data, "%Y/%m/%d")
            break
        except ValueError:
            print("Data inválida! Use o formato AAAA/MM/DD com uma data real.")

    tema = input("Tema do evento: ")

    eventos.append({
        "codigo": codigo, 
        "nome": nome,
        "data": data_valida.strftime("%Y/%m/%d"),
        "tema": tema,
        "participantes": []
    })

    print("Evento adicionado com sucesso!")

    
def remover_evento(eventos):
    codigo = input("Código do evento a remover: ")
    for evento in eventos:
        if evento["codigo"] == codigo:
            eventos.remove(evento)
            print("Evento removido.")
            return
    print("Evento não encontrado.")

def listar_participantes_por_evento(eventos, participantes):
    codigo = input("Código do evento: ")
    for evento in eventos:
        if evento["codigo"] == codigo:
            print(f"Participantes do evento '{evento['nome']}':")
            for p in evento['participantes']:
                info = next((x for x in participantes if x['codigo'] == p), None)
                if info:
                    print(f"- {info['nome']} ({info['email']})")
            return
    print("Evento não encontrado.")