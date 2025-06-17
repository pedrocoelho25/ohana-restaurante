
opcaoMenu = 0

import json
import os
def exibir_logo_ohana():
    
    print("   ____   _   _    _      _   _    __     ")
    print("  / __ \ | | | |  /  \   | | | |  /  \    ")
    print(" | |  | || |_| | / _\ \  | \ | | / _\ \   ")
    print(" | |__| ||  _  |/ ___\ \ |  \  |/ ___\ \  ")
    print("  \____/ |_| |_/_/    \_\|_| |_/_/    \_\ ")
    print("                                       ")
    print("     🌺 Bem-vindo ao Restaurante Ohana 🌴")
    print("     Família, sabor e aloha no seu prato!")
    
    


while(opcaoMenu != 5):
    exibir_logo_ohana()
    print("\n" + "="*50)
    print("🍽️  MENU PRINCIPAL - OHANA")
    print("="*50)
    print("1 - 📖 Cardápio Digital")
    print("2 - 🧾 Controle de Pedidos")
    print("3 - 🪑 Gerenciamento de Mesas")
    print("4 - 📦 Sistema de Estoque")
    opcaoMenu = input("5 - 🚪 Sair\n👉 Sua escolha: ")
    opcaoMenu = int(opcaoMenu)

    cardapio_json = "arquivoCardapio.json"

    if not os.path.exists(cardapio_json):
        print("⚠️ Arquivo não encontrado! Criando novo arquivo...")
        with open("arquivoCardapio.json", "w") as arquivo:
            json.dump([], arquivo)
            os.system(f"code {cardapio_json}")
    else:
        with open(cardapio_json, "r") as arquivo:
            try:
                cardapios = json.load(arquivo)
                os.system(f"code {cardapio_json}")
            except json.JSONDecodeError:
                cardapios = []
        print("✅ Arquivo existente! Dados carregados com sucesso.")

    opcaoCardapio = 0
    if(opcaoMenu == 1):
        while(opcaoCardapio != 6):
            print("\n" + "="*50)
            print("🍍 MENU DO CARDÁPIO - OHANA")
            print("="*50)
            print("1 - 👀 Ver cardápio")
            print("2 - 🔍 Pesquisar item")
            print("3 - ➕ Adicionar item")
            print("4 - ✏️ Editar item")
            print("5 - ❌ Apagar item")
            opcaoCardapio = int(input("6 - 🔙 Retornar ao menu inicial\n👉 Sua escolha: "))

            def modificar_json():
                with open(cardapio_json, "w", encoding='utf-8') as arquivo:
                    json.dump(cardapios, arquivo, ensure_ascii=False, indent=4)

            def mostrarcardapio():
                print("\n🌺 Itens cadastrados no cardápio:\n")
                for c in cardapios:
    
                    print(f"   🔸{c['Código']} - {c['Item'].title()}")
                    print(f"   📄 Descrição: {c['Descrição'].capitalize()}")
                    print(f"   💰 Valor: R${c['Preço']}")
                    print(f"   🧾 Categoria: {c['Categoria'].capitalize()}\n")

            def pesquisaritem():
                item = input("🔍 Qual item deseja buscar? ").lower()
                encontrado = False
                for c in cardapios:
                    if c['Item'] == item:
                        print(f"\n✅ Item encontrado: {c['Código']} - {c['Item'].title()}")
                        print(f"📄 Descrição: {c['Descrição'].capitalize()}")
                        print(f"💰 Valor: R${c['Preço']}")
                        print(f"🧾 Categoria: {c['Categoria'].capitalize()}\n")
                        encontrado = True
                        break
                if not encontrado:
                    print("❌ Item não encontrado.")

            def adicionaritem():
                codigo = input("\n🔢 Informe o código do item: ")
                while any(codigo == c.get('Código') for c in cardapios):
                    codigo = input("⚠️ Código já existe! Tente outro: ")
                while codigo.isdigit() and len(codigo) != 3:
                    codigo = input("🔁 Código deve ter 3 dígitos: ")

                item = input("🍛 Nome do item: ").lower()
                while any(item == i['Item'] for i in cardapios):
                    item = input("⚠️ Item já existe! Tente outro: ").lower()

                descricao = input("📝 Descrição do item: ").lower()
                valor = float(input("💰 Valor do item (R$): "))
                preco = round(valor, 2)

                categoria = input("📂 Categoria (comida, bebida, sobremesa): ").lower()
                while categoria not in ["comida", "bebida", "sobremesa"]:
                    categoria = input("❌ Categoria inválida. Tente: comida, bebida ou sobremesa: ").lower()

                cardapio = {
                    'Código': codigo,
                    'Item': item,
                    'Descrição': descricao,
                    'Preço': preco,
                    'Categoria': categoria
                }

                cardapios.append(cardapio)
                modificar_json()

                print(f"\n✅ {item.title()} foi adicionado ao cardápio!")

            def editaritem():
                itemeditar = input("✏️ Informe o item que deseja editar: \n").lower()
                encontrado = False
                for c in cardapios:
                    if c['Item'].lower() == itemeditar:
                        codigo = input("\n🔢 Novo código (3 dígitos): ")
                        while any(codigo == i['Código'] for i in cardapios):
                            codigo = input("⚠️ Código já usado. Tente outro: ")
                        while codigo.isdigit() and len(codigo) != 3:
                            codigo = input("🔁 Código deve ter 3 dígitos: ")

                        item = input("🍛 Novo nome do item: ").lower()
                        while any(item == i['Item'] for i in cardapios):
                            item = input("⚠️ Item já existe. Tente outro: ").lower()

                        descricao = input("📝 Nova descrição: ").lower()
                        valor = float(input("💰 Novo valor (R$): "))
                        preco = round(valor, 2)

                        categoria = input("📂 Nova categoria: ").lower()
                        while categoria not in ["comida", "bebida", "sobremesa"]:
                            categoria = input("❌ Categoria inválida. Tente: comida, bebida ou sobremesa: ").lower()

                        c['Código'] = codigo
                        c['Item'] = item
                        c['Descrição'] = descricao
                        c['Preço'] = preco
                        c['Categoria'] = categoria

                        modificar_json()
                        print(f"\n✅ Item {item.title()} atualizado com sucesso!")
                        encontrado = True
                        break
                if not encontrado:
                    print("❌ Item não encontrado.")

            def apagaritem():
                itemapagado = input("❌ Qual item deseja apagar? ").lower()
                encontrado = False
                for i, item in enumerate(cardapios):
                    if item["Item"] == itemapagado:
                        del cardapios[i]
                        print(f"🗑️ Item {itemapagado.title()} foi apagado!")
                        modificar_json()
                        encontrado = True
                        break
                if not encontrado:
                    print("❌ Item não encontrado.")

            match opcaoCardapio:
                case 1:
                    mostrarcardapio()
                case 2:
                    pesquisaritem()
                case 3:
                    adicionaritem()
                case 4:
                    editaritem()
                case 5:
                    apagaritem()
















    arquivo_json = "arquivoPedidos.json"



    if os.path.exists(arquivo_json):
        with open(arquivo_json, "r") as arquivo:
            try:
                pedidos = json.load(arquivo)
                os.system(f"code {arquivo_json}")
            except json.JSONDecodeError:
                pedidos = []
        print("📁 Arquivo existente localizado. Dados carregados com sucesso!\n")
    else:
        print("📂 Arquivo não encontrado. Criando novo arquivo de pedidos...\n")
        with open(arquivo_json, "w") as arquivo:
            json.dump([], arquivo)
            os.system(f"code {arquivo_json}")

    def ver_pedidos():
        print("\n📋 LISTA DE PEDIDOS")
        if not pedidos:
            print("🚫 Nenhum pedido foi cadastrado ainda.\n")
        else:
            for pedido in pedidos:
                print("-"*40)
                print(f"🪑 Mesa: {pedido['Mesa']}")
                print(f"🆔 ID do Pedido: {pedido['ID']}")
                print(f"👤 Nome: {pedido['nome']}")
                print(f"🧾 CPF: {pedido['CPF']}")
                print(f"🍽️ Descrição: {pedido['descricao']}")
                print(f"💰 Total: R$ {pedido['total']:.2f}")
                print(f"💳 Forma de Pagamento: {pedido['formaDepagamento'].capitalize()}")
                print("-"*40)

    def pesquisar_pedido():
        print("\n🔎 PESQUISA DE PEDIDO")
        id_pedido = input("Digite o ID do pedido que deseja buscar: ")
        encontrado = False
        for pedido in pedidos:
            if pedido["ID"] == id_pedido:
                print("\n✅ Pedido encontrado!\n")
                print(f"👤 Cliente: {pedido['nome']}")
                print(f"🧾 CPF: {pedido['CPF']}")
                print(f"💰 Total: R$ {pedido['total']:.2f}")
                print(f"🪑 Mesa: {pedido['Mesa']}")
                encontrado = True
                break
        if not encontrado:
            print("🚫 Pedido não encontrado!\n")

    def adicionar_pedido():
        print("\n🆕 ADICIONAR NOVO PEDIDO")
        mesa = int(input("🪑 Digite o número da mesa: "))
        id_pedido = input("🆔 Informe o ID do pedido: ")
        while any(id_pedido == pedido["ID"] for pedido in pedidos):
            print("⚠️ ID já existente. Tente outro.")
            id_pedido = input("Informe o ID do pedido: ")

        while id_pedido.isdigit() and len(id_pedido) != 3:
            id_pedido = input("ID errado. Digite um ID com até 3 dígitos: ")
        nome = input("👤 Informe o nome do cliente: ")
        cpf = input("🧾 Informe o CPF do cliente (11 dígitos): ")

        while cpf.isdigit() and len(cpf) != 11:
            cpf = input("CPF inválido. Digite novamente (11 dígitos): ")

        descricao = input("📝 Descrição do pedido: ")
        total = float(input("💰 Valor total: R$ "))
        while total <= 0:
            total = float(input("Valor inválido. Informe um valor maior que zero: R$ "))
        total = round(total, 2)

        print("\n💳 FORMAS DE PAGAMENTO DISPONÍVEIS:")
        print(" - Dinheiro")
        print(" - Cartão de crédito")
        print(" - Cartão de débito")
        print(" - Pix")

        formaDepagamento = input("Informe a forma de pagamento: ").lower()
        while formaDepagamento not in ["dinheiro", "cartão de crédito", "cartão de débito", "pix"]:
            formaDepagamento = input("❌ Forma inválida! Tente: dinheiro, cartão de crédito, cartão de débito ou pix: ")

        novo_pedido = {
            "Mesa": mesa,
            "ID": id_pedido,
            "nome": nome,
            "CPF": cpf,
            "descricao": descricao,
            "total": total,
            "formaDepagamento": formaDepagamento
        }

        pedidos.append(novo_pedido)
        with open(arquivo_json, "w", encoding='utf-8') as arquivo:
            json.dump(pedidos, arquivo,ensure_ascii=False, indent=4)

        print("\n✅ Pedido adicionado com sucesso!")
        print(novo_pedido)

    def editar_pedido():
        print("\n✏️ EDITAR PEDIDO")
        id_pedido = input("Digite o ID do pedido que quer editar: ")
        for pedido in pedidos:
            if pedido["ID"] == id_pedido:
                nova_descricao = input("Nova descrição do pedido: ")
                novo_total = float(input("Novo valor total: R$ "))
                nova_formaDepagamento = input("Nova forma de pagamento: ")
                pedido["descricao"] = nova_descricao
                pedido["total"] = novo_total
                pedido["formaDepagamento"] = nova_formaDepagamento
                with open(arquivo_json, "w", encoding='utf-8') as arquivo:
                    json.dump(pedidos, arquivo,ensure_ascii=False, indent=4)
                print("✅ Pedido editado com sucesso!\n")
                break
        else:
            print("🚫 Pedido não encontrado para editar.\n")

    def apagar_pedido():
        print("\n🗑️ APAGAR PEDIDO")
        id_pedido = input("Digite o ID do pedido que quer remover: ")
        for pedido in pedidos:
            if pedido["ID"] == id_pedido:
                pedidos.remove(pedido)
                with open(arquivo_json, "w", encoding='utf-8') as arquivo:
                    json.dump(pedidos, arquivo,ensure_ascii=False, indent=4)
                print("✅ Pedido removido com sucesso!\n")
                
        print("🚫 Pedido não encontrado!\n")

    if opcaoMenu == 2:
        while True:
            print("\n🌴" + "-"*45)
            print("🍍 MENU DE CONTROLE DE PEDIDOS")
            print("-"*45 + "🌴")
            print("1️⃣  Ver lista de pedidos")
            print("2️⃣  Pesquisar pedido")
            print("3️⃣  Adicionar novo pedido")
            print("4️⃣  Editar pedido")
            print("5️⃣  Apagar pedido")
            print("6️⃣  Voltar ao menu principal")

            op = int(input("Escolha uma opção: "))
            if op == 1:
                ver_pedidos()
            elif op == 2:
                pesquisar_pedido()
            elif op == 3:
                adicionar_pedido()
            elif op == 4:
                editar_pedido()
            elif op == 5:
                apagar_pedido()
            elif op == 6:
                print("🌊 Retornando ao menu principal...\n")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")







    arquivo3_json = "arquivo_GerenciamentoMesas.json"

    if os.path.exists(arquivo3_json):
        with open(arquivo3_json, "r", encoding='utf-8') as arquivo:
            try:
                mesas = json.load(arquivo)
                os.system(f"code {arquivo3_json}")
            except json.JSONDecodeError:
                mesas = []
            print("🌴 Arquivo encontrado! Dados carregados com sucesso. 🌴")
    else:
        print("⚠️ Arquivo não encontrado. Criando novo arquivo...")
        with open(arquivo3_json, "w", encoding='utf-8') as arquivo:
            json.dump([], arquivo, ensure_ascii=False)
            os.system(f"code {arquivo3_json}")

    if(opcaoMenu == 3):
        while True:
            print("\n📌 MENU DE MESAS:")
            print("-"*30)
            print("1️⃣  Ver lista de mesas")
            print("2️⃣  Buscar por mesa")
            print("3️⃣  Criar uma nova mesa")
            print("4️⃣  Editar situação da mesa")
            print("5️⃣  Deletar uma mesa")
            print("6️⃣  Retornar ao menu principal")
            print("-"*30)

            def adicionar_json():
                with open(arquivo3_json, "w", encoding='utf-8') as arquivo:
                    json.dump(mesas, arquivo, ensure_ascii=False, indent=4)

            def listar_mesas():
                print("\n📋 Lista de Mesas:")
                print("-"*30)
                for mesa in mesas:
                    print(f"🍽️ Mesa {mesa['número da mesa']} | 🪑 Situação: {mesa['situação da mesa'].capitalize()} | 👤 Nome: {mesa['nome da mesa reservada']} | 📞 Tel: {mesa['número de telefone']}")

            def buscar_mesa():
                numero_mesa = int(input("\n🔎 Informe o número da mesa: "))
                for mesa in mesas:
                    if numero_mesa == mesa["número da mesa"]:
                        print("\n✅ Mesa encontrada:")
                        print(f"🍽️ Número: {mesa['número da mesa']}")
                        print(f"🪑 Situação: {mesa['situação da mesa']}")
                        print(f"👤 Nome: {mesa['nome da mesa reservada']}")
                        print(f"📞 Telefone: {mesa['número de telefone']}")
                        break
                else:
                    print("❌ Mesa não encontrada!")

            def adicionar_mesa():
                nome_mesa = ''
                numero_telefone = ''

                criar_mesa = int(input("🆕 Informe o número da nova mesa: "))
                while any(mesa['número da mesa'] == criar_mesa for mesa in mesas):
                    criar_mesa = int(input("⚠️ Mesa já existente! Informe outro número: "))

                situacao_mesa = input("🪑 Situação (livre, ocupada, reservada): ").lower()
                while situacao_mesa not in ["livre", "ocupada", "reservada"]:
                    print("❗ Opção inválida.")
                    situacao_mesa = input("Digite: livre, ocupada ou reservada: ").lower()

                if situacao_mesa in ["reservada", "ocupada"]:
                    nome_mesa = input("👤 Nome da pessoa: ")
                    numero_telefone = input("📞 Número de telefone (11 dígitos): ")
                    while numero_telefone.isdigit() and len(numero_telefone) != 11:
                        numero_telefone = input("❌ Número inválido! Tente novamente: ")

                nova_mesa = {
                    'número da mesa': criar_mesa,
                    'situação da mesa': situacao_mesa,
                    'nome da mesa reservada': nome_mesa,
                    'número de telefone': numero_telefone
                }

                mesas.append(nova_mesa)
                adicionar_json()
                print(f"✅ Mesa {criar_mesa} criada com sucesso!")

            def edicao_mesa():
                editar_mesa = int(input("✏️ Informe o número da mesa que deseja editar: "))
                for mesa in mesas:
                    if mesa['número da mesa'] == editar_mesa:
                        situacao_nova = input("🪑 Nova situação (livre, ocupada, reservada): ").lower()
                        while situacao_nova not in ["livre", "ocupada", "reservada"]:
                            print("❗ Opção inválida.")
                            situacao_nova = input("Digite: livre, ocupada ou reservada: ").lower()

                        if situacao_nova in ['reservada', 'ocupada']:
                            novo_nome = input("👤 Novo nome: ")
                            novo_telefone = input("📞 Novo telefone: ")
                            while novo_telefone.isdigit() and len(novo_telefone) != 11:
                                novo_telefone = input("❌ Número inválido! Digite 11 dígitos: ")
                        else:
                            novo_nome = ""
                            novo_telefone = ""

                        mesa['situação da mesa'] = situacao_nova
                        mesa['nome da mesa reservada'] = novo_nome
                        mesa['número de telefone'] = novo_telefone
                        adicionar_json()
                        print("✅ Mesa atualizada com sucesso!")
                        break
                else:
                    print("❌ Mesa não encontrada!")

            def deletar_mesa():
                numero_mesa = int(input("🗑️ Informe o número da mesa para deletar: "))
                for mesa in mesas:
                    if mesa['número da mesa'] == numero_mesa:
                        mesas.remove(mesa)
                        adicionar_json()
                        print("🗑️ Mesa deletada com sucesso!")
                        break
                else:
                    print("❌ Mesa não encontrada!")

            opcaoMesa = int(input("👉 Digite a opção desejada: "))
            if opcaoMesa == 1:
                listar_mesas()
            elif opcaoMesa == 2:
                buscar_mesa()
            elif opcaoMesa == 3:
                adicionar_mesa()
            elif opcaoMesa == 4:
                edicao_mesa()
            elif opcaoMesa == 5:
                deletar_mesa()
            elif opcaoMesa == 6:
                print("🔙 Retornando ao menu principal...")
                break



    




