from cpf_cnpj import Documento
from telefones_br import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco


print("====== Validação e formatação de CPF e CNPJ =======")

#CPF e CNPJ usando validate_docbr
#CPF
ex_cpf = "15316264754"
documento2 = Documento.cria_documento(ex_cpf)

#CNPJ
ex_cnpj = "22109918000106"
documento1 = Documento.cria_documento(ex_cnpj)

print("Documento CNPJ: {}\nDocumento CPF: {}".format(documento1, documento2))

print("=================================================")

print("====== Validação e formatação de Telefone =======")

#Telefone usando re
telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print("Telefone: {}".format(telefone_objeto))

print("=================================================")

print("=========== Trabalhando com Datas ===============")

#Datas de cadastro com datetime e timedelta
cadastro = DatasBr()
print("Data de cadastro: {}".format(cadastro))

print("=================================================")

print("============ Busca de endereço ==================")

#Endereço usando requests
cep = 77060690
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print("Resultado:",bairro, cidade, uf)

print("=================================================")