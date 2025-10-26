<<<<<<< HEAD
#------ATENÇÃO------
=======

#------ATENÇÂO------
>>>>>>> 6efac5ee57d74e8f7fe450415aee05097e9cdf8c
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
<<<<<<< HEAD
    print("9. Otimizar Reposição de Estoque (Programação Dinâmica)")
    print("10. Sair")
=======
    print("9. Sair")
>>>>>>> 6efac5ee57d74e8f7fe450415aee05097e9cdf8c
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

<<<<<<< HEAD
#PROGRAMAÇÃO DINÂMICA 

"""
1. ESTADOS:
   - O estado representa: "Estou no período X com Y unidades em estoque, 
     qual o menor custo possível daqui até o final?"
   
   Onde:
   - periodo: qual dia ou período estamos (começa em 0)
   - estoque_atual: quantas unidades temos no início desse período

2. DECISÕES:
   - A cada período, preciso decidir QUANTO vou repor de estoque
   - Posso escolher repor 0, 1, 2... até o limite da capacidade máxima
   - Restrições: 
     * Não posso repor quantidade negativa
     * O estoque total não pode passar da capacidade máxima

3. FUNÇÃO DE TRANSIÇÃO:
   - Mostra como o estoque muda de um período para o próximo
   - novo_estoque = estoque_atual + quantidade_repor - demanda[periodo]
   - Se novo_estoque ficar negativo: não consegui atender toda a demanda
   - Se novo_estoque for positivo ou zero: tudo certo, sigo para o próximo período

4. FUNÇÃO OBJETIVO (MINIMIZAR):
   - Quero gastar o mínimo possível somando todos os custos:
   
   custo_total = custo_reposicao + custo_armazenagem + custo_falta
   
   Onde:
   - custo_reposicao: preço fixo do pedido + preço por unidade comprada
   - custo_armazenagem: custo de guardar o que sobrou no estoque
   - custo_falta: multa quando não consigo atender a demanda
"""

def otimizar_reposicao_recursiva_memo(demandas, capacidade_max, custo_fixo, 
                                       custo_unitario, custo_armazenagem, 
                                       penalidade_falta):
    """
    VERSÃO RECURSIVA COM MEMORIZAÇÃO (TOP-DOWN)
    Parâmetros:
    - demandas: lista com a quantidade que vai ser consumida em cada período
    - capacidade_max: máximo que posso guardar no estoque
    - custo_fixo: custo fixo toda vez que faço um pedido de reposição
    - custo_unitario: quanto custa cada unidade comprada
    - custo_armazenagem: quanto custa guardar cada unidade por período
    - penalidade_falta: multa por cada unidade que não consegui entregar
    
    Retorna: (custo_minimo, decisoes_otimas)
    """
    n_periodos = len(demandas)
    memo = {}
    
    def resolver(periodo, estoque_atual):
        """
        FUNÇÃO RECURSIVA PRINCIPAL
        Descobre qual o menor custo possível desde o 'periodo' até o final,
        começando com 'estoque_atual' unidades.
        """
        if periodo >= n_periodos:
            return 0, []
        
        if (periodo, estoque_atual) in memo:
            return memo[(periodo, estoque_atual)]
        
        demanda_atual = demandas[periodo]
        melhor_custo = float('inf')
        melhor_decisao = 0
        melhores_decisoes_futuras = []
        
        # TESTANDO TODAS AS DECISÕES POSSÍVEIS
        max_repor = capacidade_max - estoque_atual
        
        for quantidade_repor in range(max_repor + 1):
            # CALCULANDO O CUSTO DA DECISÃO ATUAL
            estoque_apos_repor = estoque_atual + quantidade_repor
            
            # Custo de fazer o pedido
            if quantidade_repor > 0:
                custo_repor = custo_fixo + custo_unitario * quantidade_repor
            else:
                custo_repor = 0
            
            # Vejo quanto sobra depois de atender a demanda
            estoque_apos_demanda = estoque_apos_repor - demanda_atual
            
            # Se não tiver estoque suficiente, pago uma multa pela falta
            if estoque_apos_demanda < 0:
                custo_falta = penalidade_falta * abs(estoque_apos_demanda)
                estoque_final = 0  # Estoque ficou zerado
            else:
                custo_falta = 0
                estoque_final = estoque_apos_demanda
            
            # Custo de guardar o que sobrou no estoque
            custo_armaz = custo_armazenagem * estoque_final
            
            custo_atual = custo_repor + custo_falta + custo_armaz
            
            # RECURSÃO
            custo_futuro, decisoes_futuras = resolver(periodo + 1, estoque_final)
            
            custo_total = custo_atual + custo_futuro
            
            # ESCOLHENDO A MELHOR OPÇÃO
            if custo_total < melhor_custo:
                melhor_custo = custo_total
                melhor_decisao = quantidade_repor
                melhores_decisoes_futuras = decisoes_futuras
        
        # MEMORIZAÇÃO
        resultado = (melhor_custo, [melhor_decisao] + melhores_decisoes_futuras)
        memo[(periodo, estoque_atual)] = resultado
        return resultado
    
    # Começo do período 0 com estoque vazio
    custo_minimo, decisoes_otimas = resolver(0, 0)
    
    return custo_minimo, decisoes_otimas, memo

def otimizar_reposicao_iterativa(demandas, capacidade_max, custo_fixo, 
                                  custo_unitario, custo_armazenagem, 
                                  penalidade_falta):

    n_periodos = len(demandas)
    
    # TABELA DE PROGRAMAÇÃO DINÂMICA
    # dp[periodo][estoque] = (custo_minimo, decisao_otima)
    # Começo preenchendo tudo com None
    dp = [[None for _ in range(capacidade_max + 1)] for _ in range(n_periodos + 1)]
    
    # CASO BASE (BOTTOM): Último período + 1 (acabou o planejamento)
    # Se não tem mais nenhum período pela frente, não tem mais custo
    for estoque in range(capacidade_max + 1):
        dp[n_periodos][estoque] = (0, 0)
    
    # ITERAÇÃO BOTTOM-UP
    for periodo in range(n_periodos - 1, -1, -1):
        demanda_atual = demandas[periodo]
        
        # Testo para cada possível quantidade de estoque no começo do período
        for estoque_atual in range(capacidade_max + 1):
            melhor_custo = float('inf')
            melhor_decisao = 0
            
            max_repor = capacidade_max - estoque_atual
            
            for quantidade_repor in range(max_repor + 1):
                # CALCULANDO O CUSTO AGORA
                estoque_apos_repor = estoque_atual + quantidade_repor
                
                # Custo do pedido
                if quantidade_repor > 0:
                    custo_repor = custo_fixo + custo_unitario * quantidade_repor
                else:
                    custo_repor = 0
                
                # Atendo a demanda
                estoque_apos_demanda = estoque_apos_repor - demanda_atual
                
                # Verifico se faltou produto
                if estoque_apos_demanda < 0:
                    custo_falta = penalidade_falta * abs(estoque_apos_demanda)
                    estoque_final = 0
                else:
                    custo_falta = 0
                    estoque_final = estoque_apos_demanda
                
                # Custo de guardar o que sobrou
                custo_armaz = custo_armazenagem * estoque_final
                
                custo_atual = custo_repor + custo_falta + custo_armaz
                
                # Pego a solução que já calculei pro futuro
                # Como já resolvi os períodos seguintes, é só buscar na tabela
                custo_futuro, _ = dp[periodo + 1][estoque_final]
                
                custo_total = custo_atual + custo_futuro
                
                # ESCOLHENDO O MELHOR
                if custo_total < melhor_custo:
                    melhor_custo = custo_total
                    melhor_decisao = quantidade_repor
            
            # GUARDANDO NA TABELA DP
            dp[periodo][estoque_atual] = (melhor_custo, melhor_decisao)
    
    decisoes_otimas = []
    estoque_atual = 0  # Começo sem estoque
    
    for periodo in range(n_periodos):
        _, decisao_otima = dp[periodo][estoque_atual]
        decisoes_otimas.append(decisao_otima)
        
        #Atualizo o estoque pro próximo período
        estoque_apos_repor = estoque_atual + decisao_otima
        estoque_apos_demanda = estoque_apos_repor - demandas[periodo]
        estoque_atual = max(0, estoque_apos_demanda)
    
    custo_minimo, _ = dp[0][0]
    
    return custo_minimo, decisoes_otimas, dp


def menu_otimizacao_estoque():
    #Menu interativo para o usuário executar a otimização de reposição de estoque

    print("\n--- Otimização de Reposição de Estoque (Programação Dinâmica) ---")
    print("\nEste módulo calcula a melhor estratégia de reposição pra gastar o mínimo possível.")
    print("Leva em conta: custos de pedido, armazenagem e multas por falta.\n")
    
    try:
        # Pegando os dados do usuário
        n_periodos = int(input("Quantos períodos deseja planejar? (ex: 7 dias): "))
        if n_periodos <= 0:
            print("Número de períodos precisa ser positivo.")
            return
        
        print(f"\nDigite a demanda prevista pra cada um dos {n_periodos} períodos:")
        demandas = []
        for i in range(n_periodos):
            demanda = int(input(f"  Período {i+1}: "))
            demandas.append(demanda)
        
        capacidade_max = int(input("\nCapacidade máxima de armazenamento: "))
        custo_fixo = float(input("Custo fixo por pedido de reposição: R$ "))
        custo_unitario = float(input("Custo por unidade reposta: R$ "))
        custo_armazenagem = float(input("Custo de armazenagem por unidade/período: R$ "))
        penalidade_falta = float(input("Multa por unidade não atendida: R$ "))
        
        print("\n" + "="*70)
        print("EXECUTANDO OTIMIZAÇÃO...")
        print("="*70)
        
        # EXECUTA VERSÃO RECURSIVA COM MEMORIZAÇÃO
        print("\n1. VERSÃO RECURSIVA COM MEMORIZAÇÃO (TOP-DOWN)")
        print("-" * 70)
        custo_recursivo, decisoes_recursivas, memo = otimizar_reposicao_recursiva_memo(
            demandas, capacidade_max, custo_fixo, custo_unitario, 
            custo_armazenagem, penalidade_falta
        )
        
        print(f"Custo Total Mínimo: R$ {custo_recursivo:.2f}")
        print(f"Quantidade de problemas resolvidos (tamanho do memo): {len(memo)}")
        print("\nDecisões Ótimas (quanto repor em cada período):")
        for i, decisao in enumerate(decisoes_recursivas):
            print(f"  Período {i+1}: Repor {decisao} unidades")

        print("\n2. VERSÃO ITERATIVA (BOTTOM-UP)")
        print("-" * 70)
        custo_iterativo, decisoes_iterativas, dp_table = otimizar_reposicao_iterativa(
            demandas, capacidade_max, custo_fixo, custo_unitario, 
            custo_armazenagem, penalidade_falta
        )
        
        print(f"Custo Total Mínimo: R$ {custo_iterativo:.2f}")
        print(f"Tamanho da tabela DP: {len(dp_table)} x {len(dp_table[0])}")
        print("\nDecisões Ótimas (quanto repor em cada período):")
        for i, decisao in enumerate(decisoes_iterativas):
            print(f"  Período {i+1}: Repor {decisao} unidades")
        
        #Comparo os resultados das duas versões
        print("\n" + "="*70)
        print("VALIDAÇÃO DOS RESULTADOS")
        print("="*70)
        
        # Checo se os custos são iguais
        custos_iguais = abs(custo_recursivo - custo_iterativo) < 0.01
        decisoes_iguais = decisoes_recursivas == decisoes_iterativas
        
        print(f"\nCusto recursivo: R$ {custo_recursivo:.2f}")
        print(f"Custo iterativo:  R$ {custo_iterativo:.2f}")
        print(f"Custos são iguais? {custos_iguais} ✓" if custos_iguais else f"Custos são iguais? {custos_iguais} ✗")
        
        print(f"\nDecisões recursivas: {decisoes_recursivas}")
        print(f"Decisões iterativas: {decisoes_iterativas}")
        print(f"Decisões são iguais? {decisoes_iguais} ✓" if decisoes_iguais else f"Decisões são iguais? {decisoes_iguais} ✗")
        
        #Mostro como fica o estoque executando o plano
        print("\n" + "="*70)
        print("SIMULAÇÃO DA EXECUÇÃO DO PLANO ÓTIMO")
        print("="*70)
        
        estoque_periodo = 0
        custo_acumulado = 0
        
        print(f"\n{'Período':<10} {'Estoque':<12} {'Repor':<10} {'Demanda':<10} {'Est.Final':<12} {'Custo':<12}")
        print("-" * 70)
        
        for i in range(n_periodos):
            quantidade_repor = decisoes_iterativas[i]
            demanda = demandas[i]
            
            # Calculo os custos
            if quantidade_repor > 0:
                custo_repor = custo_fixo + custo_unitario * quantidade_repor
            else:
                custo_repor = 0
            
            estoque_apos_repor = estoque_periodo + quantidade_repor
            estoque_apos_demanda = estoque_apos_repor - demanda
            
            if estoque_apos_demanda < 0:
                custo_falta = penalidade_falta * abs(estoque_apos_demanda)
                estoque_final = 0
            else:
                custo_falta = 0
                estoque_final = estoque_apos_demanda
            
            custo_armaz = custo_armazenagem * estoque_final
            custo_periodo = custo_repor + custo_falta + custo_armaz
            custo_acumulado += custo_periodo
            
            print(f"{i+1:<10} {estoque_periodo:<12} {quantidade_repor:<10} {demanda:<10} {estoque_final:<12} R$ {custo_periodo:<10.2f}")
            
            estoque_periodo = estoque_final
        
        print("-" * 70)
        print(f"{'TOTAL':<54} R$ {custo_acumulado:.2f}")
    
        assert custos_iguais, "ERRO: Os custos das duas versões não bateram!"
        assert decisoes_iguais, "ERRO: As decisões das duas versões não bateram!"
        assert abs(custo_acumulado - custo_iterativo) < 0.01, "ERRO: Simulação não bateu com o custo calculado!"
        
        print("\n✓ Todas as validações passaram com sucesso!")
        print("  - Versão recursiva e iterativa deram o mesmo custo")
        print("  - Versão recursiva e iterativa deram as mesmas decisões")
        print("  - Simulação confirmou o custo calculado")
        
    except ValueError:
        print("\nERRO: Entrada inválida. Por favor, digite valores numéricos.")
    except Exception as e:
        print(f"\nERRO durante a otimização: {e}")

# TESTES AUTOMÁTICOS E EXEMPLOS

def executar_testes_automaticos():
    print("\n" + "="*70)
    print("EXECUTANDO TESTES AUTOMÁTICOS")
    print("="*70)
    
    # TESTE 1
    print("\n--- TESTE 1: Caso Simples (3 períodos) ---")
    demandas_teste1 = [10, 15, 20]
    capacidade_teste1 = 50
    custo_fixo_teste1 = 10.0
    custo_unitario_teste1 = 2.0
    custo_armazenagem_teste1 = 0.5
    penalidade_falta_teste1 = 5.0
    
    custo_rec1, dec_rec1, _ = otimizar_reposicao_recursiva_memo(
        demandas_teste1, capacidade_teste1, custo_fixo_teste1, 
        custo_unitario_teste1, custo_armazenagem_teste1, penalidade_falta_teste1
    )
    
    custo_iter1, dec_iter1, _ = otimizar_reposicao_iterativa(
        demandas_teste1, capacidade_teste1, custo_fixo_teste1, 
        custo_unitario_teste1, custo_armazenagem_teste1, penalidade_falta_teste1
    )
    
    print(f"Demandas: {demandas_teste1}")
    print(f"Custo Recursivo: R$ {custo_rec1:.2f} | Decisões: {dec_rec1}")
    print(f"Custo Iterativo:  R$ {custo_iter1:.2f} | Decisões: {dec_iter1}")
    assert abs(custo_rec1 - custo_iter1) < 0.01, "TESTE 1 FALHOU: Custos diferentes"
    assert dec_rec1 == dec_iter1, "TESTE 1 FALHOU: Decisões diferentes"
    print(" TESTE 1 PASSOU")
    
    # TESTE 2
    print("\n--- TESTE 2: Demanda Variável (5 períodos) ---")
    demandas_teste2 = [5, 10, 3, 15, 8]
    capacidade_teste2 = 30
    custo_fixo_teste2 = 15.0
    custo_unitario_teste2 = 3.0
    custo_armazenagem_teste2 = 1.0
    penalidade_falta_teste2 = 10.0
    
    custo_rec2, dec_rec2, _ = otimizar_reposicao_recursiva_memo(
        demandas_teste2, capacidade_teste2, custo_fixo_teste2, 
        custo_unitario_teste2, custo_armazenagem_teste2, penalidade_falta_teste2
    )
    
    custo_iter2, dec_iter2, _ = otimizar_reposicao_iterativa(
        demandas_teste2, capacidade_teste2, custo_fixo_teste2, 
        custo_unitario_teste2, custo_armazenagem_teste2, penalidade_falta_teste2
    )
    
    print(f"Demandas: {demandas_teste2}")
    print(f"Custo Recursivo: R$ {custo_rec2:.2f} | Decisões: {dec_rec2}")
    print(f"Custo Iterativo:  R$ {custo_iter2:.2f} | Decisões: {dec_iter2}")
    assert abs(custo_rec2 - custo_iter2) < 0.01, "TESTE 2 FALHOU: Custos diferentes!"
    assert dec_rec2 == dec_iter2, "TESTE 2 FALHOU: Decisões diferentes!"
    print("TESTE 2 PASSOU")
    
    # TESTE 3
    print("\n--- TESTE 3: Sem Demanda (2 períodos) ---")
    demandas_teste3 = [0, 0]
    capacidade_teste3 = 20
    custo_fixo_teste3 = 5.0
    custo_unitario_teste3 = 1.0
    custo_armazenagem_teste3 = 0.5
    penalidade_falta_teste3 = 10.0
    
    custo_rec3, dec_rec3, _ = otimizar_reposicao_recursiva_memo(
        demandas_teste3, capacidade_teste3, custo_fixo_teste3, 
        custo_unitario_teste3, custo_armazenagem_teste3, penalidade_falta_teste3
    )
    
    custo_iter3, dec_iter3, _ = otimizar_reposicao_iterativa(
        demandas_teste3, capacidade_teste3, custo_fixo_teste3, 
        custo_unitario_teste3, custo_armazenagem_teste3, penalidade_falta_teste3
    )
    
    print(f"Demandas: {demandas_teste3}")
    print(f"Custo Recursivo: R$ {custo_rec3:.2f} | Decisões: {dec_rec3}")
    print(f"Custo Iterativo:  R$ {custo_iter3:.2f} | Decisões: {dec_iter3}")
    assert abs(custo_rec3 - custo_iter3) < 0.01, "TESTE 3 FALHOU: Custos diferentes!"
    assert dec_rec3 == dec_iter3, "TESTE 3 FALHOU: Decisões diferentes!"
    assert custo_rec3 == 0.0, "TESTE 3 FALHOU: Custo deveria ser zero!"
    print(" TESTE 3 PASSOU")
    print("\n" + "="*70)
    print(" TODOS OS TESTES AUTOMÁTICOS PASSARAM COM SUCESSO!")
    print("="*70)
    print("\nCONCLUSÕES:")
    print("- As versões recursiva (top-down) e iterativa (bottom-up) são equivalentes")
    print("- Ambas produzem o mesmo custo mínimo e as mesmas decisões ótimas")
    print("- A memorização elimina recálculos na versão recursiva")
    print("- A versão iterativa constrói a solução de forma sistemática")
    print("- Ambas implementam corretamente os princípios de Programação Dinâmica:")
    print("  * Subestrutura ótima")
    print("  * Subproblemas sobrepostos")
    print("  * Função de transição de estados")
    print("  * Otimização da função objetivo")

=======
>>>>>>> 6efac5ee57d74e8f7fe450415aee05097e9cdf8c
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
<<<<<<< HEAD
            menu_otimizacao_estoque()
        elif opcao == '10':
=======
>>>>>>> 6efac5ee57d74e8f7fe450415aee05097e9cdf8c
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 6efac5ee57d74e8f7fe450415aee05097e9cdf8c
