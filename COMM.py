##############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF975 -- Redes de Computadores
#
# Grupo:    Bruno Artagoitia Vicente do Nascimento - bavn
#			Fernando Nunes Ferreira de Oliveira - fnfo
#			Lívio Cavalcanti de Souza - lcs9
# 
# Data:        2018-12-06
#
# Descricao:  PROJETO - SISTEMA DE ARMAZENAMENTO DE ARQUIVOS
# Parte A: SHELL PRINCIPAL
###############################################################################

print("##################################################################################")
print("###################### SISTEMA DE ARMAZENAMENTO DE ARQUIVOS ######################")
print("##################################################################################")

lista_usuario = ["admin","user","estagiario","exit"]
lista_senha = ["admin","123","456",""]

loop_usuario = True
while (loop_usuario == True):
	usuario_set = ""
	print("\n")
	print("###################")
	print("###### LOGIN ######")
	print("###################")
	print("\n")
	usuario = str(input("Usuario:"))
	senha = str(input("Senha:"))
	for u in range(4):
		if ((lista_usuario[u] == usuario) and (lista_senha[u] == senha)):
			if (lista_usuario[u] != "exit"):
				print("Login efetuado com sucesso!")
			else:
				print("Saindo...")
			usuario_set = lista_usuario[u]
			loop_usuario = False
			break
		else:
			if (u == 3):
				print("Usuario nao encontrado ou senha invalida!")
				loop_usuario = True

if (usuario_set == "admin"):
	print("\n")
	print("INSTRUCOES:")
	print("Digite 'get' para copiar ou baixar arquivo")
	print("Digite 'post' para adicionar arquivo")
	print("Digite 'delete' para apagar um arquivo")
	print("Digite 'ajuda' para instrucoes")
	print("Digite o comando desejado ou 'exit' para sair")
	print("\n")

	loop_menu_principal = True
	while (loop_menu_principal == True):
		comando = str(input("Comando > "))
		if (comando == "exit"):
			print("Saindo...")
			loop_menu_principal = False
		else:
			if (comando == "get"):
				arquivo = str(input("Digite o caminho e o arquivo que se deseja copiar:"))
				#IMPLEMENTAR DETETOR SE O ARQUIVO ESTA OU NAO
				destino = str(input("Digite o endereço IP de destino para onde deseja copiar:"))
				#IMPLEMENTAR DETETOR SE O DESTINO ESTA OU NAO
				#FUNCAO GET A IMPLEMENTAR
				print("Arquivo copiado com sucesso!")
				loop_menu_principal = True
			elif (comando == "post"):
				arquivo = str(input("Digite o caminho e o arquivo que se deseja adicionar:"))
				#FUNCAO POST A IMPLEMENTAR
				print("Arquivo adicionado com sucesso!")
				loop_menu_principal = True
			elif (comando == "delete"):
				arquivo = str(input("Digite o caminho e o arquivo que se deseja apagar:"))
				#IMPLEMENTAR DETETOR SE O ARQUIVO ESTA OU NAO
				delete_quest = str(input("Tem certeza? s/n:"))
				if (delete_quest == "s") or (delete_quest == "S"):
					#FUNCAO DELETE A IMPLEMENTAR
					print("Arquivo apagado com sucesso!")
					loop_menu_principal = True
				else:
					print("Cancelado!")
					loop_menu_principal = True
			elif (comando == "ajuda"):
				print("Digite 'get' para copiar ou baixar arquivo")
				print("Digite 'post' para adicionar arquivo")
				print("Digite 'delete' para apagar um arquivo")
				print("Digite 'ajuda' para instrucoes")
				print("Digite 'exit' para sair")
				loop_menu_principal = True
			else:
				print("Comando invalido!")
				loop_menu_principal = True

if (usuario_set == "user"):
	print("\n")
	print("INSTRUCOES:")
	print("Digite 'get' para copiar ou baixar arquivo")
	print("Digite 'post' para adicionar arquivo")
	print("Digite 'ajuda' para instrucoes")
	print("Digite o comando desejado ou 'exit' para sair")
	print("\n")

	loop_menu_principal = True
	while (loop_menu_principal == True):
		comando = str(input("Comando > "))
		if (comando == "exit"):
			print("Saindo...")
			loop_menu_principal = False
		else:
			if (comando == "get"):
				arquivo = str(input("Digite o caminho e o arquivo que se deseja copiar:"))
				#IMPLEMENTAR DETETOR SE O ARQUIVO ESTA OU NAO
				destino = str(input("Digite o endereço IP de destino para onde deseja copiar:"))
				#IMPLEMENTAR DETETOR SE O DESTINO ESTA OU NAO
				#FUNCAO GET A IMPLEMENTAR
				print("Arquivo copiado com sucesso!")
				loop_menu_principal = True
			elif (comando == "post"):
				arquivo = str(input("Digite o caminho e o arquivo que se deseja adicionar:"))
				#FUNCAO POST A IMPLEMENTAR
				print("Arquivo adicionado com sucesso!")
				loop_menu_principal = True
			elif (comando == "ajuda"):
				print("Digite 'get' para copiar ou baixar arquivo")
				print("Digite 'post' para adicionar arquivo")
				print("Digite 'ajuda' para instrucoes")
				print("Digite 'exit' para sair")
				loop_menu_principal = True
			else:
				print("Comando invalido!")
				loop_menu_principal = True

if (usuario_set == "estagiario"):
	print("\n")
	print("INSTRUCOES:")
	print("Digite 'get' para copiar ou baixar arquivo")
	print("Digite 'ajuda' para instrucoes")
	print("Digite o comando desejado ou 'exit' para sair")
	print("\n")

	loop_menu_principal = True
	while (loop_menu_principal == True):
		comando = str(input("Comando > "))
		if (comando == "exit"):
			print("Saindo...")
			loop_menu_principal = False
		else:
			if (comando == "get"):
				arquivo = str(input("Digite o caminho e o arquivo que se deseja copiar:"))
				#IMPLEMENTAR DETETOR SE O ARQUIVO ESTA OU NAO
				destino = str(input("Digite o endereço IP de destino para onde deseja copiar:"))
				#IMPLEMENTAR DETETOR SE O DESTINO ESTA OU NAO
				#FUNCAO GET A IMPLEMENTAR
				print("Arquivo copiado com sucesso!")
				loop_menu_principal = True
			elif (comando == "ajuda"):
				print("Digite 'get' para copiar ou baixar arquivo")
				print("Digite 'ajuda' para instrucoes")
				print("Digite 'exit' para sair")
				loop_menu_principal = True
			else:
				print("Comando invalido!")
				loop_menu_principal = True