#Alana Sato 2300143
#Barbara Borda 2300419
#Vitor braz 2300194
#Yuri amorim 2300077


from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = []
    
    def adicionar_super_poder(self, superpoder):
        if superpoder.get_nome() in [p.get_nome() for p in self.__poderes]:
            print(f"O superpoder '{superpoder.get_nome()}' já foi adicionado, selecione novamente.")
        else:
            self.__poderes.append(superpoder)
            print(f"\nO poder '{superpoder.get_nome()}' foi adicionado ao personagem com sucesso.")
           
    @abstractmethod
    def get_poder_total(self):
        pass


class SuperHeroi(Personagem):
    
    def Caracteristicas(nome, heroiVidaReal):
        global superh 
        superh= SuperHeroi(nome, heroiVidaReal)
        print(f'\nHeroi: {nome} \nNome do heroi: {heroiVidaReal} ')
        superh.meu_poder(superh)
        return print(f'\n\nTotal de poderes do {nome} é: {superh.get_poder_total():.2f} \n!Os Super-heróis tem um acrescimo de poder de 10%!')
    
    def get_poder_total(self):
        total = sum(p.get_categoria() for p in self._Personagem__poderes)
        return total * 1.10
    
    def imp_poderes(self):
        for superpoder in self._Personagem__poderes:
            print(f'Poder: {superpoder.get_nome()} | Categoria: {superpoder.get_categoria()}')
            
    def meu_poder(self,personagem):
        while True: 
            print('\nEscolha uma opção para os poderes do seu personagem:')
            print('1 - Escolher poder já existente')
            print('2 - Criar meu poder')

            opcao_poder = input('Escolha uma opção: ')
            
            if opcao_poder == '1':
                    print('\nEscolha o superpoder do personagem')
                    for poder in superpoder:
                        print(f"{poder:30} | {superpoder[poder]}")

                    escolha = input("\nDigite o nome do superpoder: ")
                    escolha = escolha.lower()

                    if escolha in superpoder:
                        poder = escolha
                        categoria = superpoder[escolha]
                        
                        self.adicionar_super_poder(SuperPoder(escolha, categoria))
                    else:
                        print("\nPoder não existe na lista. Escolha novamente.")
            

                
            elif opcao_poder == '2':
                while True:  
                    escolha = input("\nDigite o nome do superpoder: ")
                    escolha = escolha.lower()
                    
                    if escolha not in [p.get_nome().lower() for p in self._Personagem__poderes]:
                        while True:  
                            categoria = input("Digite a categoria do novo superpoder: ")
                            if categoria.isdigit():
                                categoria = int(categoria)
                                break
                            else:
                                print('Apenas números, digite novamente')
                    
                        self.adicionar_super_poder(SuperPoder(escolha, categoria))
                        break  
                    else:
                        self.adicionar_super_poder(SuperPoder(escolha, categoria))
                        resposta = input('Deseja adicionar mais poderes? (N/S): ')
                        if resposta.lower() != 's':
                            break
                                    
            else:
                print('Opção inválida. Escolha novamente.')
                
            resposta = input('Deseja adicionar mais poderes? (N/S): ')
            if resposta.lower() != 's':
                self.imp_poderes()
                break

class Vilao(Personagem):
    
    def Caracteristicas(nomev, vilaoVidaReal):
      while True:
        tempo_de_prisao = input('\nDigite o tempo de prisão do vilão (dias): ')
        if tempo_de_prisao.isdigit() and tempo_de_prisao:  
            tempo_de_prisao = int(tempo_de_prisao)
            break
        else:
            print('Por favor, digite apenas números')
      global viloes
      viloes = Vilao(nomev, vilaoVidaReal, tempo_de_prisao)            
      print(f'\nVilão: {nomev} \nNome do vilão: {vilaoVidaReal} \nTempo: {tempo_de_prisao} dias')
      viloes.meu_poder(viloes)                        
      print(f'Total de poderes do {nomev} é: {viloes.get_poder_total():.2f}') 

    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao

    def get_poder_total(self):
        total = sum(superpoder.get_categoria() for superpoder in self._Personagem__poderes)
        return total
    
    def imp_poderes(self):
        for superpoder in self._Personagem__poderes:
            print(f'Poder: {superpoder.get_nome()} | Categoria: {superpoder.get_categoria()}')
    
    def meu_poder(self,personagem):
        while True: 
            print('\nEscolha uma opção para os poderes do seu personagem:')
            print('1 - Escolher poder já existente')
            print('2 - Criar meu poder')

            opcao_poder = input('Escolha uma opção: ')
            
            if opcao_poder == '1':
                    print('\nEscolha o superpoder do personagem')
                    for poder in superpoder:
                        print(f"{poder:30} | {superpoder[poder]}")

                    escolha = input("\nDigite o nome do superpoder: ")
                    escolha = escolha.lower()

                    if escolha in superpoder:
                        poder = escolha
                        categoria = superpoder[escolha]
                        
                        self.adicionar_super_poder(SuperPoder(escolha, categoria))
                    else:
                        print("\nPoder não existe na lista. Escolha novamente.")

                
            elif opcao_poder == '2':
                while True:  
                    escolha = input("\nDigite o nome do superpoder: ")
                    escolha = escolha.lower()
                    
                    if escolha not in [p.get_nome().lower() for p in self._Personagem__poderes]:
                        while True:  
                            categoria = input("Digite a categoria do novo superpoder: ")
                            if categoria.isdigit():
                                categoria = int(categoria)
                                break
                            else:
                                print('Apenas números, digite novamente')
                    
                        self.adicionar_super_poder(SuperPoder(escolha, categoria))
                        break  
                    else:
                        self.adicionar_super_poder(SuperPoder(escolha, categoria))
                        resposta = input('Deseja adicionar mais poderes? (N/S): ')
                        if resposta.lower() != 's':
                            break
            else:
                print('Opção inválida. Escolha novamente.')
                
            resposta = input('Deseja adicionar mais poderes? (N/S): ')
            if resposta.lower() != 's':
                self.imp_poderes()
                break

class Confronto():
    def lutar(self, superheroi, vilao):
        if superheroi.get_poder_total() > vilao.get_poder_total():
            resultado = print('\nResultado da batalha:' ) 
            return 1
        
        elif vilao.get_poder_total() > superheroi.get_poder_total():
            return 2
        else:
            return 0


class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria


superpoder = {
    'voar': 3,
    'força': 5,
    'velocidade': 5,
    'soltar teia' : 3,
    'andar em paredes': 2,
    'sentido apurado': 1,
    'visão de raio x': 4,
    'sopro congelnate': 4,
    'super soldado': 3,
    'escudo': 3,
    'armadura': 4,
    'dispositivos eletronicos': 2,
    'braceletes': 1    
}

heroi = ['Homem-Aranha', 'Homem de Ferro', 'Superman', 'Mulher Maravilha', 'Capitão America', 'Flash', 'Lanterna Verde']
heroiVidaReal =['Peter Park','Tony Stark', 'Clark Kent','Diana Prince','Steve Rogers','Barry Allen', 'Hal Jordan']
heroi_c = []
vilaoNome = ['Duende-Verde','Lex Luther','Bizarro', 'Octopus', 'Coringa', 'Pinguim', 'Thanos']
vilaoVidaReal = ['Norman Osbourne', 'Lex Luther', 'Bizarro', 'Otto Octavius', 'Coringa', 'Oswald Chesterfield Cobblepot','Thanos']


confronto = Confronto()



while True:
    try:
      print('\n')
      print('1 - Heroi')
      print('2 - Vilão')
      print('3 - Confronto')
      print('4 - Encerrar')
      opcao_p = int(input('Escolha uma opção: '))
      
      for op in range(1):
        if opcao_p == 1:
            while True:
                try:
                    
                    print('\n1 -', heroi[0])
                    print('2 -', heroi[1])
                    print('3 -', heroi[2])
                    print('4 -', heroi[3])
                    print('5 -', heroi[4])
                    print('6 -', heroi[5])
                    print('7 -', heroi[6])
                    print('8 - Criar meu personagem')
                    opcao = int(input('\nEscolha uma opção: '))
                    
                    if opcao ==1:
                        nome = heroi[0]
                        heroiVidaReal = heroiVidaReal[0]
                        SuperHeroi.Caracteristicas(nome, heroiVidaReal)
                        break  
                    
                    if opcao ==2:
                        nome = heroi[1]
                        heroiVidaReal = heroiVidaReal[1]
                        SuperHeroi.Caracteristicas(nome, heroiVidaReal)
                        break    
                    
                    if opcao ==3:
                        nome = heroi[2]
                        heroiVidaReal = heroiVidaReal[2]
                        SuperHeroi.Caracteristicas(nome, heroiVidaReal)
                        break
                    
                    if opcao ==4:
                        nome = heroi[3]
                        heroiVidaReal = heroiVidaReal[3]
                        SuperHeroi.Caracteristicas(nome, heroiVidaReal)
                        break
                    
                    if opcao ==5:
                        nome = heroi[4]
                        heroiVidaReal = heroiVidaReal[4]
                        SuperHeroi.Caracteristicas(nome, heroiVidaReal)
                        break 
                    
                    if opcao ==6:
                        nome = heroi[5]
                        heroiVidaReal = heroiVidaReal[5]
                        SuperHeroi.Caracteristicas(nome, heroiVidaReal)
                        break  
                    
                    if opcao ==7:
                        nome = heroi[6]
                        heroiVidaReal = heroiVidaReal[6]
                        SuperHeroi.Caracteristicas(nome, heroiVidaReal)
                        break 
                    
                    elif opcao == 8:
                        nome=input('\nDigite o nome do seu heroi:')
                        heroiVidaReal = input('Digite o nome na vida real do heroi:')
                        superh = SuperHeroi(nome, heroiVidaReal)
                        heroi_c.append(superh)
                        print(f'\nHeroi: {nome} \nNome do heroi: {heroiVidaReal} ')
                        superh.meu_poder(superh)

                        print(f'Total de poderes do {nome} é: {superh.get_poder_total():.2f} \n!Os superHerois tem um acrescimo de poder de 10%!')
                        break  
                        
                        
                    else:
                        print('Heroi nao existe, escolha novamente:')
                
                
                                        
                except ValueError:
                    print('Personagem não existe, escolha novamente\n')
                
                   
        elif opcao_p ==2:
            while True:
                print('\n1 -', vilaoNome[0])
                print('2 -', vilaoNome[1])
                print('3 -', vilaoNome[2])
                print('4 -', vilaoNome[3])
                print('5 -', vilaoNome[4])
                print('6 -', vilaoNome[5])
                print('7 -', vilaoNome[6])
                print('8 - Criar meu personagem')
                opcao_v = int(input('Escolha uma opção: '))
                
                if opcao_v ==1:
                    nomev = vilaoNome[0]
                    vilaoVidaReal = vilaoVidaReal[0]
                    Vilao.Caracteristicas(nomev, vilaoVidaReal)
                    break    
                        
                if opcao_v ==2:
                    nomev = vilaoNome[1]
                    vilaoVidaReal = vilaoVidaReal[1]
                    Vilao.Caracteristicas(nomev, vilaoVidaReal)   
                    break    
            
                if opcao_v ==3:
                    nomev = vilaoNome[2]
                    vilaoVidaReal = vilaoVidaReal[2]
                    Vilao.Caracteristicas(nomev, vilaoVidaReal)   
                    break    

                if opcao_v ==4:
                    nomev = vilaoNome[3]
                    vilaoVidaReal = vilaoVidaReal[3]
                    Vilao.Caracteristicas(nomev, vilaoVidaReal)  
                    break    

                if opcao_v ==5:
                    nomev = vilaoNome[4]
                    vilaoVidaReal = vilaoVidaReal[4]
                    Vilao.Caracteristicas(nomev, vilaoVidaReal)  
                    break    

                if opcao_v ==6:
                    nomev = vilaoNome[5]
                    vilaoVidaReal = vilaoVidaReal[5]
                    Vilao.Caracteristicas(nomev, vilaoVidaReal)    
                    break    

                if opcao_v ==7:
                    nomev = vilaoNome[6]
                    vilaoVidaReal = vilaoVidaReal[6]
                    Vilao.Caracteristicas(nomev, vilaoVidaReal)    
                    break     
                
                elif opcao_v == 8:
                        nomev=input('\nDigite o nome do seu vilão:')
                        nome_vida_real = input('Digite o nome na vida real do vilão:')
                        while True:
                            tempo_de_prisao = input('Digite o tempo de prisão do vilão (dias): ')
                            if tempo_de_prisao.isdigit() and tempo_de_prisao:  
                                tempo_de_prisao = int(tempo_de_prisao)
                                break
                            else:
                             print('Por favor, digite apenas números')
                        
                        viloes = Vilao(nomev, nome_vida_real, tempo_de_prisao)

                        print(f'\nVilão: {nomev} \nNome do vilão: {nome_vida_real} \nTempo: {tempo_de_prisao} ')
                        viloes.meu_poder(viloes)

                        print(f'Total de poderes do {nome} é: {viloes.get_poder_total():.2f}')
                        break  
                        
                else:
                    print('Vilão não existe')
    
        elif opcao_p == 3:
            try:
                
                if superh is not None and viloes is not None:
                    print(f'\nResultado do confronto entre {superh._Personagem__nome} e {viloes._Personagem__nome}\n')
                    print(confronto.lutar(superh, viloes))
                    print('\n0: Empate.\n1: Super-herói ganhou a batalha.\n2: Vilão ganhou a batalha')
    
            except NameError:
                print("É necessário cadastrar o super-herói e o vilão primeiro.")

        elif opcao_p ==4:
            print('Programa encerrado')
            exit()
        
        else: 
            print('Opção invalida, escolha novamente')
            
    except ValueError:
        print('Erro. Caracter inválido, escolha novamente\n')
