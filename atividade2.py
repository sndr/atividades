class ContaBancaria:
    def __init__(self):
        self.banco = 500

    def sacar(self,quanto):
        self.banco = self.banco - quanto
        print(f"seu saldo agora é de {self.banco}")


    def deposito(self, valor):
        self.banco = self.banco + valor 
        print(f"voce adicionou {valor} reais")
    
    
    def show(self):
        print(f'''       
    NOTA DO SALDO
SEU SALDO É DE {self.banco}
''')
        
if __name__ == '__main__':
        cont = ContaBancaria()
        while True:
            a = int(input(''' MENU 
        1 - deposito
        2 - saque
        3 - imprimir saldo 
        4 - sair\n->  '''))
            if a == 1:
                print("Quanto voce quer depositar: ")
                valor = float(input(""))
                cont.deposito(valor)
                cont.show()
            elif a == 2:
                print("Quanto voce quer sacar: ")
                valor = float(input(""))
                cont.sacar(valor)
            elif a == 3:
                cont.show()
            elif a == 4:
                exit()