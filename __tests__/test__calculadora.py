import pytest  #teste de unidade 

#funcões que serão testadas
from calculadora.calculadora import somar_dois_numeros, subtrair_doi_numeros, multipicar_dois_numeros, dividir_dois_numero

# part2 testes 
def test_somar_dois_numeros():

    # padrão /standard AAA (se diz tripe A ou 3A) = arrange, act, assert
    
    # prepara / configura 
    # dados entrada e saída
    num1 = 5
    num2 = 7
    resultado_esperado =12

    # act / executa

    resultado_obtido = somar_dois_numeros(num1, num2)

    # assert /  valida

    assert resultado_esperado == resultado_obtido