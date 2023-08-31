class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self,item):
        return self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def elemento_do_topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        
    def exibir_pilha(self):
        print("Pilha: ", self.itens)

    def esvaziar_pilha(self):
        self.itens = []

class Editor:
        pi = Pilha()
        while True:
            print('''
            EDITOR DE LISTAS
    1 - EMPILHAR
    2 - DESEMPILHAR
    3 - EXIBIR ELEMENTO DO TOPO
    4 - EXIBIR A PILHA 
    5 - ESVAZIAR A PILHA 
    7 - PARA FECHAR O PROGRAMA
''')       
            valor = int(input("DIGITE SUA OPÇÃO: "))
            if not valor in [1,2,3,4,5,7]:
                print("VALOR INVALIDO")
                continue
            elif valor == 7:
                print("fechando o programa")
                exit()
            else:
                if valor == 1:
                    a = input("DIGITE UM VALOR: ")
                    print("empilhando...")
                    pi.empilhar(a)
                    print("EMPILHADO.")
                elif valor == 2:
                    print("desempilhando...")
                    pi.desempilhar()
                    print("DESEMPILHANDO")
                elif valor == 3:
                    print("exibindo...")
                    pi.elemento_do_topo()
                elif valor == 4:
                    print("exibindo pilha")
                    pi.exibir_pilha()
                elif valor == 5:
                    print("esvaziando...")
                    pi.esvaziar_pilha()
                    print("ESTA VAZIA.")