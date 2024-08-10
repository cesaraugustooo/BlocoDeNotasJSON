import json

class notas():
    def __init__(self):
        bloco_notas=[]
        nota = str
        indicie_nota = str
        self.carregar_notas()
    def carregar_notas(self):
        with open('notas.txt', 'r') as file:
            self.bloco_notas = json.load(file)
    def salvar_JSON(self):
        with open('notas.txt', 'w') as file:
           json.dump(self.bloco_notas,file)

    def mostrar_nota(self):
        with open('notas.txt','r') as file :
            file = file.read()
            print(file)
    def adicionar_nota(self):
        self.nota=input('')
        self.bloco_notas.append(self.nota)
        self.salvar_JSON()

    def excluir_nota(self):
        for a in self.bloco_notas:
            print(f'{a}')
            self.indicie_nota = input("Deseja apagar")
            if self.indicie_nota == 'sim' or self.indicie_nota == 'Sim':
                self.bloco_notas.remove(a)
                self.salvar_JSON()


nota = notas()
while 2>1:
    opcao=input(" 1-Adicionar nota | 2-Mostrar Notas | 3-Excluir Notas | 4-Sair")
    if opcao == '1':
        nota.adicionar_nota()
    elif opcao == '2':
        nota.mostrar_nota()
    elif opcao == '3':
        nota.excluir_nota()
    elif opcao == '4':
        break