class Conta:
    def __init__(self, num, cpf, nomeTitular, Saldo):
        #Self serve para a função "init apontar para si proprio" 
        self.num = num
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.Saldo = Saldo

def main():
    c1 = Conta(num=555555, cpf=70408024534, nomeTitular= "Joao", Saldo=1000)
    print(f"Nome do titular da conta: {c1.nomeTitular}")
    print(f"Número da conta: {c1.num}")
    print(f"CPF do titular: {c1.cpf}")
    print(f"Saldo da conta: {c1.Saldo}")

if __name__ == "__main__":
    main()