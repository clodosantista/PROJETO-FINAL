#CLASSE ENDEREÇO
from typing import Self
from unicodedata import name
from datetime import date


class Endereco:
    def __init__(self, logradoro="",numero="", endereco_Comercial=False): 
       #inicializar os nossos atributos com valores padrão
        self.logradoro = logradoro
        self.numero = numero
        self.endereco_Comercial=endereco_Comercial

#CLASSE PESSOA
class Pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        self.nome=name
        self.rendimento= rendimento
        self.endereco= endereco

    def calcular_imposto(self, rendimento):
        return rendimento

#CLASSE PESSOA FISICA


class PessoaFisica(Pessoa):
    #inicializar os atributos que foram herdados e própris atributos da classe
    def __init__(self, nome="",rendimento=0.0, endereco=None, cpf="",dataNascimento=None):
        if endereco is None:
        #se nenhum endereço for fornecido, cria um objeto endereço padrão
            endereco = Endereco()
    
        if dataNascimento is None: # type: ignore
            dataNascimento= date.today()

        #Atrbutos da propria Classe
        self.cpf = cpf
        self.dataNascimento = dataNascimento

        super().__init__(nome, rendimento, endereco)


    def calcular_imposto(self, rendimento: float) -> float:
        #Sem imposto para rendimento até R$1.500
        if rendimento <= 1500:
            return 0
        # 2% de imposto para rendimento entre 1500 e 3500
        elif 1500 < rendimento <= 3500:
            return rendimento * 0.2
        #3,5% de imposto para rendimento entre 3500 e 6000
        elif 3500 < rendimento <= 6000:
            return (rendimento / 100) * 3.5
        #5% de imposto para rendimento acima de 6000
        else:
            return rendimento * 0.5
        
  

#CLASSE PESSOA JURIDICA
class PessoaJuridica(Pessoa):
    def __init__(self, nome="", rendimento=0, endereco=None, cnpj=""):
        if Endereco is None:
            endereco = Endereco()                   
        super().__init__(nome, rendimento, endereco)
        self.cnpj = cnpj

    def calcular_imposto(self, rendimento: float) -> float:
        #Sem imposto para rendimento até R$1.500
        if rendimento <= 10500:
            return 0
        # 2% de imposto para rendimento entre 1500 e 3500
        elif 10500 < rendimento <= 30500:
            return (rendimento / 100) * 5
        #3,5% de imposto para rendimento entre 3500 e 6000
        elif 30500 < rendimento <= 60000:
            return (rendimento / 100) * 8
        #5% de imposto para rendimento acima de 6000
        else:
            return (rendimento / 100) * 12