
#------ATENÇÂO------
#Ao iniciar o código, crie um usuário para poder utilizar o sistema. 
# Depois, faça login utilizando as mesmas informações cadastradas. 
#Somente após o login será possível acessar o menu principal do sistema.

import collections

# Fila que faz o registro de tudo que foi consumido em ordem de tempo.
consumo_diario_fila = collections.deque()

# Pilha apara o histórico de consumo.
consumo_historico_pilha = []

# Dicionário para  o resgistro de itens disponiveis no estoque
estoque = {
    "Agulhas": 100,
    "Seringa": 100,
    "Pacote algodão": 50,
    "Tubo de coleta": 150,
    "Luvas": 100,
}

# Dicionário para controle de usuários 
usuarios = {}

def criar_novo_usuario():
    print("\n--- Criar Novo Usuário ---")
    nome = input("Digite o nome do novo usuário: ").strip().title()
    matricula = input("Digite a matrícula para o novo usuário: ").strip()

    if matricula in usuarios:
        print("Matrícula já existe. Por favor, escolha outra.")
    else:
        usuarios[matricula] = nome
        print(f"Usuário '{nome}' com matrícula '{matricula}' criado com sucesso!")

def exibir_menu_principal():
    print("\n--- Menu Principal ---")
    print("1. Reposição de item")
    print("2. Retirada de item")
    print("3. Visualizar Estoque")
    print("4. Visualizar Consumo Diário (Fila)")
    print("5. Visualizar Histórico de Consumo (Pilha)")
    print("6. Buscar Registro de Consumo")
    print("7. Ordenar Histórico de Consumo")
    print("8. Criar Novo Usuário")
    print("9. Sair")
    return input("Escolha uma opção: ")

def fazer_login():
    print("\n--- Login ---")
    nome = input("Nome: ").strip().title()   
    matricula = input("Matrícula: ").strip()

    # Verifica se a matrícula existe e corresponde ao nome fornecido.
    if matricula in usuarios and usuarios[matricula] == nome:
        print(f"Login bem-sucedido! Bem-vindo(a), {nome}.")
        return {"nome": nome, "matricula": matricula}
    else:
        print("Nome ou matrícula incorretos. Tente novamente.")
        return None

def registrar_consumo(item, quantidade, tipo_operacao, usuario):
    registro = {
        "item": item,
        "quantidade": quantidade,
        "tipo": tipo_operacao,
        "usuario": usuario,
    }
    consumo_diario_fila.append(registro)
    consumo_historico_pilha.append(registro)
    print(f"Registro de {tipo_operacao} de {quantidade}x {item} adicionado ao histórico.")

#Funções de  estoque

def repor_item():
    print("\n--- Reposição de Item ---")
    item = input("Nome do item a ser reposto (ou 'sair' para cancelar): ").strip().title()
    if item.lower() == 'sair':
        return

    try:
        quantidade = int(input(f"Quantidade de {item} a ser reposta: "))
        if quantidade <= 0:
            print("A quantidade deve ser um número positivo.")
            return
    except ValueError:
        print("Quantidade inválida. Por favor, digite um número.")
        return

    if item in estoque:
        estoque[item] += quantidade
        print(f"{quantidade} unidades de {item} adicionadas ao estoque. Novo total: {estoque[item]}")
    else:
        estoque[item] = quantidade
        print(f"Novo item '{item}' adicionado com {quantidade} unidades.")
    
    # Não registra reposição como consumo na pilha, apenas retiradas.

def retirar_item(usuario_logado):
    print("\n--- Retirada de Item ---")
    if not estoque:
        print("Estoque vazio. Não há itens para retirar.")
        return

    itens_disponiveis = sorted(estoque.keys())
    for i, item in enumerate(itens_disponiveis):
        print(f"{i+1}. {item}: {estoque[item]} unidades")
    
    try:
        escolha = int(input("Selecione o número do item para retirada (ou '0' para cancelar): "))
        if escolha == 0:
            return
        if not (1 <= escolha <= len(itens_disponiveis)):
            print("Opção inválida.")
            return
        
        item_selecionado = itens_disponiveis[escolha - 1]
        quantidade_disponivel = estoque[item_selecionado]

        quantidade_retirar = int(input(f"Quantidade de {item_selecionado} a ser retirada (disponível: {quantidade_disponivel}): "))

        if quantidade_retirar <= 0:
            print("A quantidade deve ser um número positivo.")
        elif quantidade_retirar > quantidade_disponivel:
            print(f"Quantidade insuficiente. Disponível: {quantidade_disponivel}")
        else:
            estoque[item_selecionado] -= quantidade_retirar
            print(f"{quantidade_retirar} unidades de {item_selecionado} retiradas. Novo total: {estoque[item_selecionado]}")
            registrar_consumo(item_selecionado, quantidade_retirar, "Retirada", usuario_logado)

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    except IndexError:
        print("Opção de item inválida.")

def visualizar_consumo_diario_fila():
    print("\n--- Consumo Diário (Fila) ---")
    if not consumo_diario_fila:
        print("Fila de consumo diário vazia.")
        return
    for i, registro in enumerate(consumo_diario_fila):
        print(f"{i+1}. Item: {registro['item']}, Qtd: {registro['quantidade']}, Tipo: {registro['tipo']}, Usuário: {registro['usuario']['nome']}")

def visualizar_consumo_historico_pilha():
    print("\n--- Histórico de Consumo (Pilha) ---")
    if not consumo_historico_pilha:
        print("Pilha de histórico de consumo vazia.")
        return
    # Exibe a pilha do topo para a base
    for i, registro in enumerate(reversed(consumo_historico_pilha)):
        print(f"{len(consumo_historico_pilha) - i}. Item: {registro['item']}, Qtd: {registro['quantidade']}, Tipo: {registro['tipo']}, Usuário: {registro['usuario']['nome']}")

def visualizar_estoque():
    print("\n--- Estoque Atual ---")
    if not estoque:
        print("Estoque vazio.")
        return
    
    # Ordena os itens para exibir
    for item in sorted(estoque.keys()):
        print(f"{item}: {estoque[item]} unidades")

def busca_sequencial(lista, valor, chave):
    # Algoritimo sequencial, ele funciona percorrendo todos os itens da lista um a um.
    for item in lista:
        if item.get(chave) == valor:
            return item
    return None

def busca_binaria(lista_ordenada, valor, chave):
    # com a lista estando ordenada, a busca binaria quebra a lista no meio a cada etapa.
    esquerda, direita = 0, len(lista_ordenada) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        item_meio = lista_ordenada[meio]
        
        if item_meio.get(chave) == valor:
            return item_meio
        elif item_meio.get(chave) < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None

def merge_sort(lista, chave, crescente=True):
    # Implementei o Merge Sort para ordenar o histórico por nome do item.
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave, crescente)
    direita = merge_sort(lista[meio:], chave, crescente)

    return merge(esquerda, direita, chave, crescente)

def merge(esquerda, direita, chave, crescente):
    resultado = []
    i, j = 0, 0

    while i < len(esquerda) and j < len(direita):
        if crescente:
            if esquerda[i].get(chave) <= direita[j].get(chave):
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        else: # Decrescente
            if esquerda[i].get(chave) >= direita[j].get(chave):
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort(lista, chave, crescente=True):
    # Implementei o Quick Sort para ordenar o histórico por quantidade.
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [item for item in lista if (item.get(chave) < pivo.get(chave) if crescente else item.get(chave) > pivo.get(chave))]
    iguais = [item for item in lista if item.get(chave) == pivo.get(chave)]
    maiores = [item for item in lista if (item.get(chave) > pivo.get(chave) if crescente else item.get(chave) < pivo.get(chave))]

    return quick_sort(menores, chave, crescente) + iguais + quick_sort(maiores, chave, crescente)

#Função Principal
def menu_busca_consumo():
    print("\n--- Buscar Registro de Consumo ---")
    if not consumo_historico_pilha:
        print("Histórico de consumo vazio. Não há o que buscar.")
        return

    print("Buscar por:")
    print("1. Nome do Item")
    print("2. Quantidade")
    print("3. Nome do Usuário")
    opcao_busca = input("Escolha uma opção: ")

    chave_busca = ""
    valor_busca = None

    if opcao_busca == '1':
        chave_busca = "item"
        valor_busca = input("Digite o nome do item: ").strip().title()
    elif opcao_busca == '2':
        chave_busca = "quantidade"
        try:
            valor_busca = int(input("Digite a quantidade: "))
        except ValueError:
            print("Quantidade inválida. Por favor, digite um número.")
            return
    elif opcao_busca == '3':
        chave_busca = "usuario"
        nome_usuario = input("Digite o nome do usuário: ").strip().title()
        resultados = []
        for registro in consumo_historico_pilha:
            if registro["usuario"]["nome"].lower() == nome_usuario.lower():
                resultados.append(registro)
        
        if resultados:
            print("\n--- Resultados da Busca ---")
            for i, registro in enumerate(resultados):
                print(f"{i+1}. Item: {registro['item']}, Qtd: {registro['quantidade']}, Tipo: {registro['tipo']}, Usuário: {registro['usuario']['nome']}")
        else:
            print(f"Nenhum registro encontrado para o usuário '{nome_usuario}'")
        return
    else:
        print("Opção de busca inválida.")
        return
    
    print("\nQual algoritmo de busca usar?")
    print("1. Busca Sequencial (padrão)")
    print("2. Busca Binária (requer ordenação, pode ser mais rápida)")
    tipo_busca = input("Escolha uma opção de busca: ")

    registro_encontrado = None
    algoritmo_usado = ""

    if tipo_busca == '2':
        # Para a busca binária funcionar, a lista precisa estar ordenada pela chave
        print(f"Ordenando histórico por '{chave_busca}' para a busca binária...")
        lista_ordenada = sorted(consumo_historico_pilha, key=lambda x: x.get(chave_busca))
        registro_encontrado = busca_binaria(lista_ordenada, valor_busca, chave_busca)
        algoritmo_usado = "Busca Binária"
    else:
        # Usa busca sequencial por padrão ou se a opção for 1
        registro_encontrado = busca_sequencial(list(consumo_historico_pilha), valor_busca, chave_busca)
        algoritmo_usado = "Busca Sequencial"


    if registro_encontrado: 
        print(f"\n--- Registro Encontrado ({algoritmo_usado}) ---")
        print(f"Item: {registro_encontrado['item']}, Qtd: {registro_encontrado['quantidade']}, Tipo: {registro_encontrado['tipo']}, Usuário: {registro_encontrado['usuario']['nome']}")
    else:
        print(f"Nenhum registro encontrado para {chave_busca}: '{valor_busca}'")

def menu_ordenacao_consumo():
    """Menu para ordenar o histórico de consumo."""
    print("\n--- Ordenar Histórico de Consumo ---")
    if not consumo_historico_pilha:
        print("Histórico de consumo vazio. Não há o que ordenar.")
        return

    print("Ordenar por:")
    print("1. Nome do Item (crescente)")
    print("2. Nome do Item (decrescente)")
    print("3. Quantidade Consumida (crescente)")
    print("4. Quantidade Consumida (decrescente)")

    opcao_ordenacao = input("Escolha uma opção: ")

    lista_para_ordenar = list(consumo_historico_pilha)
    chave_ordenacao = ""
    crescente = True
    algoritmo = ""

    if opcao_ordenacao == '1':
        chave_ordenacao = "item"
        crescente = True
        # Usei Merge Sort para ordenar por texto (nome do item)
        algoritmo = "Merge Sort"
        lista_ordenada = merge_sort(lista_para_ordenar, chave_ordenacao, crescente)
    elif opcao_ordenacao == '2':
        chave_ordenacao = "item"
        crescente = False
        algoritmo = "Merge Sort"
        lista_ordenada = merge_sort(lista_para_ordenar, chave_ordenacao, crescente)
    elif opcao_ordenacao == '3':
        chave_ordenacao = "quantidade"
        crescente = True
        # Usei Quick Sort para ordenar pelo número
        algoritmo = "Quick Sort"
        lista_ordenada = quick_sort(lista_para_ordenar, chave_ordenacao, crescente)
    elif opcao_ordenacao == '4':
        chave_ordenacao = "quantidade"
        crescente = False
        algoritmo = "Quick Sort"
        lista_ordenada = quick_sort(lista_para_ordenar, chave_ordenacao, crescente)
    else:
        print("Opção de ordenação inválida.")
        return

    print(f"\n--- Histórico de Consumo Ordenado ({algoritmo}) ---")
    for i, registro in enumerate(lista_ordenada):
        print(f"{i+1}. Item: {registro['item']}, Qtd: {registro['quantidade']}, Tipo: {registro['tipo']}, Usuário: {registro['usuario']['nome']}")

def main():
    usuario_logado = realizar_login_ou_criacao_usuario()
    if not usuario_logado:
        return

    executar_menu_principal(usuario_logado)

def realizar_login_ou_criacao_usuario():
    while True:
        print("\n--- Bem-vindo ao Sistema de Controle de Estoque ---")
        print("1. Fazer Login")
        print("2. Criar Novo Usuário")
        print("3. Sair")
        escolha_inicial = input("Escolha uma opção: ")

        if escolha_inicial == '1':
            usuario_logado = fazer_login()
            if usuario_logado:
                return usuario_logado
        elif escolha_inicial == '2':
            criar_novo_usuario()
        elif escolha_inicial == '3':
            print("Saindo do sistema. Até mais!")
            return None
        else:
            print("Opção inválida. Por favor, escolha novamente.")

def executar_menu_principal(usuario_logado):
    while True:
        opcao = exibir_menu_principal()

        if opcao == '1':
            repor_item()
        elif opcao == '2':
            retirar_item(usuario_logado)
        elif opcao == '3':
            visualizar_estoque()
        elif opcao == '4':
            visualizar_consumo_diario_fila()
        elif opcao == '5':
            visualizar_consumo_historico_pilha()
        elif opcao == '6':
            menu_busca_consumo()
        elif opcao == '7':
            menu_ordenacao_consumo()
        elif opcao == '8':
            criar_novo_usuario()
        elif opcao == '9':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
