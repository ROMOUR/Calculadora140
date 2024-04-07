def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_doi_numeros(num1, num2):
    return num1 - num2 

def multipicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numero(num1, num2):
    try:
        return num1 / num2
    except(ZeroDivisionError): 
        return 'erro: Não é possivel dividir por zero'
