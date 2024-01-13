class Contato():
    nome = None
    telefone = None
    email = None
    favorito = False
    id = None

    def __init__(self, nome, telefone, email, id) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setTelefone(self, telefone):
        self.telefone = telefone

    def setEmail(self, email):
        self.email = email
    
    def setFavorito(self, favorito):
        self.favorito = favorito

class ContatoController():
    contatos = []

    def remover(self, id):
        self.contatos.remove(self.acharContato(id))

    def adiconar(self, nome, telefone, email):
        self.contatos.append(Contato(nome, telefone, email, len(self.contatos) + 1))

    def editar(self, id, nome, telefone, email):
        contato = self.acharContato(id)

        if contato == None:
            return
        
        contato.setNome(nome)
        contato.setTelefone(telefone)
        contato.setEmail(email)

        return contato

    def favoritar(self, id, valor):
        contato = self.acharContato(id)

        if contato == None:
            return
        
        contato.setFavorito(valor)

        return contato
    
    def verTodos(self):
        return self.contatos

    def acharContato(self, id):
        for i in self.contatos:
            if i.id == id:
                return i
        print("Não foi possível encontrar esse contato.")
        return None

def main():

    sair = None
    print("Bem-vindo(a) ao app Controle de Contatos")

    contatoController = ContatoController()

    while sair != 0:
        print()
        print("0 - Sair do programa")
        print("1 - Salvar contato")
        print("2 - Editar contato")
        print("3 - Deletar contato")
        print("4 - Favoritar contato")
        print("5 - Remover contato favorito")
        print("6 - Listar favoritos")
        print("7 - Listar contatos")

        sair = int(input("Qual ação você deseja fazer? "))

        match sair:
            case 0:
                exit()
            case 1:
                nome = input("Digite o nome do contato: ")
                telefone = input("Digite o número do contato: ")
                email = input("Digite o email do contato: ")

                contatoController.adiconar(nome, telefone, email)

                print("O contato foi adicionado com sucesso.")
            case 2:
                id = int(input("Digite o id do contato que você deseja editar: "))

                contato = contatoController.acharContato(id)

                if contato == None:
                    pass

                if input("Você deseja alterar o nome do contato? (s ou n)") in ['S', 's']:
                    nome = input("Digite o novo nome do contato: ")
                else:
                    nome = contato.nome

                if input("Você deseja alterar o telefone do contato? (s ou n)") in ['S', 's']:
                    telefone = input("Digite o novo número do telefone do contato: ")
                else:
                    telefone = contato.telefone
                
                if input("Você deseja alterar o email do contato? (s ou n)") in ['S', 's']:
                    email = input("Digite o novo email do contato: ")
                else:
                    email = contato.email
                
                contatoController.editar(contato.id, nome, telefone, email)

                print("Dados do usuário alterados com sucesso.")

            case 3:
                id = int(input("Digite o id do usuário que você deseja deletar: "))
                contatoController.remover(id)
                print("Contato deletado com sucesso.")
            case 4:
                id = int(input("Digite o id do contato que você deseja favoritar: "))
                contatoController.favoritar(id, True)
                print("Contato favoritado com sucesso.")
            case 5:
                id = int(input("Digite o id do contato que você deseja retirar dos favoritos: "))
                contatoController.favoritar(id, False)
                print("Contato retirado da lista dos favoritos.")
            case 6:
                for contato in contatoController.contatos:
                    if contato.favorito:
                        print(f"#{contato.id} | {contato.nome} - {contato.telefone} - {contato.email}")
            case 7:
                for contato in contatoController.contatos:
                    print(f"#{contato.id} | {contato.nome} - {contato.telefone} - {contato.email}")

main()