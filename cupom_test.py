import cupom
import pytest

# Refatoramento da verificação de campo obrigatório
def verifica_campo_obrigatorio(mensagem_esperada):
  with pytest.raises(Exception) as excinfo:
    cupom.dados_loja()
  the_exception = excinfo.value
  assert mensagem_esperada == str(the_exception)

# Todas as variáveis preenchidas
nome_loja = "Loja 1"
logradouro = "Log 1"
numero = 10
complemento = "C1"
bairro = "Bai 1"
municipio = "Mun 1"
estado = "E1"
cep = "11111-111"
telefone = "(11) 1111-1111"
observacao = "Obs 1"
cnpj = "11.111.111/1111-11"
inscricao_estadual = "123456789"

TEXTO_ESPERADO_LOJA_COMPLETA = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_loja_completa():
    assert cupom.dados_loja() == TEXTO_ESPERADO_LOJA_COMPLETA

def test_nome_vazio():
    global nome_loja
    nome_loja = ""
    verifica_campo_obrigatorio("O campo logradouro do endereço é obrigatório") 
    nome_loja = "Arcos Dourados Com. de Alimentos LTDA"

def test_logradouro_vazio():
    global logradouro
    logradouro = ""
    verifica_campo_obrigatorio("O campo logradouro do endereço é obrigatório")
    logradouro = "Av. Projetada Leste"

TEXTO_ESPERADO_SEM_NUMERO = '''Loja 1
Log 1, s/n C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_numero_zero():
    global numero
    numero = 0
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_NUMERO
    numero = 10

TEXTO_ESPERADO_SEM_COMPLEMENTO = '''Loja 1
Log 1, 10
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_complemento():
    global complemento
    complemento = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_COMPLEMENTO
    complemento = "C1"

TEXTO_ESPERADO_SEM_BAIRRO = '''Loja 1
Log 1, 10 C1
Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_bairro():
    global bairro
    bairro = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_BAIRRO
    bairro = "Bai 1"

def test_municipio_vazio():
    global municipio
    municipio = ""
    verifica_campo_obrigatorio("O campo município do endereço é obrigatório")
    municipio = "Campinas"

def test_estado_vazio():
    global estado
    estado = ""
    verifica_campo_obrigatorio("O campo estado do endereço é obrigatório")
    estado = "SP"

TEXTO_ESPERADO_SEM_CEP = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_cep():
    global cep
    cep = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_CEP
    cep = "11111-111"

TEXTO_ESPERADO_SEM_TELEFONE = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_telefone():
    global telefone
    telefone = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_TELEFONE
    telefone = "(11) 1111-1111"

TEXTO_ESPERADO_SEM_OBSERVACAO = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111

CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_observacao():
    global observacao
    observacao = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_OBSERVACAO
    observacao = "Obs 1"

def test_cnpj_vazio():
    global cnpj
    cnpj = ""
    verifica_campo_obrigatorio("O campo CNPJ da loja é obrigatório")
    cnpj = "42.591.651/0797-34"

def test_inscricao_estadual_vazia():
    global inscricao_estadual
    inscricao_estadual = ""
    verifica_campo_obrigatorio("O campo inscrição estadual da loja é obrigatório")
    inscricao_estadual = "244.898.500.113"

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    nome_loja = ""
    logradouro = ""
    numero = 0
    complemento = ""
    bairro = ""
    municipio = ""
    estado = ""
    cep = ""
    telefone = ""
    observacao = ""
    cnpj = ""
    inscricao_estadual = ""

    #E atualize o texto esperado abaixo
    assert cupom.dados_loja() == '''
'''
