endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23400-120"

import re # Regular expression -- RegEx

# 5 conjuntos de digitos + - hifen(opcional) + 3 digitos
# Criando um padrão
# Extrai o valor

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #Match || none

if busca:
    cep = busca.group()
    print(cep)

