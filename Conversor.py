
#  BASE 2
def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario


def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

# BASE 3

def decimal_a_base3(decimal):
    base3 = ""
    while decimal > 0:
        residuo = decimal % 3
        base3 = str(residuo) + base3
        decimal = int(decimal / 3)
    return base3

def base3_a_decimal(base3):
    decimal = 0
    posicion = 0
    base3 = base3[::-1]
    for digito in base3:
        valor_entero = int(digito)
        numero_elevado = int(3 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE 4

def decimal_a_base4(decimal):
    base4 = ""
    while decimal > 0:
        residuo = decimal % 4
        base4 = str(residuo) + base4
        decimal = int(decimal / 4)
    return base4
    
def base4_a_decimal(base4):
    decimal = 0
    posicion = 0
    base4 = base4[::-1]
    for digito in base4:
        valor_entero = int(digito)
        numero_elevado = int(4 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE 5

def decimal_a_base5(decimal):
    base5 = ""
    while decimal > 0:
        residuo = decimal % 5
        base5 = str(residuo) + base5
        decimal = int(decimal / 5)
    return base5
    
def base5_a_decimal(base5):
    decimal = 0
    posicion = 0
    base5 = base5[::-1]
    for digito in base5:
        valor_entero = int(digito)
        numero_elevado = int(5 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE 6

def decimal_a_base6(decimal):
    base6 = ""
    while decimal > 0:
        residuo = decimal % 6
        base6 = str(residuo) + base6
        decimal = int(decimal / 6)
    return base6
    
def base6_a_decimal(base6):
    decimal = 0
    posicion = 0
    base6 = base6[::-1]
    for digito in base6:
        valor_entero = int(digito)
        numero_elevado = int(6 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE 7

def decimal_a_base7(decimal):
    base7 = ""
    while decimal > 0:
        residuo = decimal % 7
        base7 = str(residuo) + base7
        decimal = int(decimal / 7)
    return base7
    
def base7_a_decimal(base7):
    decimal = 0
    posicion = 0
    base7 = base7[::-1]
    for digito in base7:
        valor_entero = int(digito)
        numero_elevado = int(7 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE 8

def decimal_a_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal


def octal_a_decimal(octal):
    decimal = 0
    posicion = 0
    octal = octal[::-1]
    for digito in octal:
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE 9

def decimal_a_base9(decimal):
    base9 = ""
    while decimal > 0:
        residuo = decimal % 9
        base9 = str(residuo) + base9
        decimal = int(decimal / 9)
    return base9
    
def base9_a_decimal(base9):
    decimal = 0
    posicion = 0
    base9 = base9[::-1]
    for digito in base9:
        valor_entero = int(digito)
        numero_elevado = int(9 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE 11

def decimal_a_base11(decimal):
    base11 = ""
    while decimal > 0:
        residuo = decimal % 11
        base11 = str(residuo) + base11
        decimal = int(decimal / 11)
    return base11
    
def base11_a_decimal(base11):
    decimal = 0
    posicion = 0
    base11 = base11[::-1]
    for digito in base11:
        valor_entero = int(digito)
        numero_elevado = int(11 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal

def obtener_caracter_base11(valor):
    
    valor = str(valor)
    equivalencias = {
        "10": "a",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor
    
def obtener_valor_real(caracter_base11):
    equivalencias = {
        "a": 10,
    }
    if caracter_base11 in equivalencias:
        return equivalencias[caracter_base11]
    else:
        return int(caracter_base11)

# BASE 12

def obtener_caracter_base12(valor):
    
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_base12(decimal):
    base12 = ""
    while decimal > 0:
        residuo = decimal % 12
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        base12 = verdadero_caracter + base12
        decimal = int(decimal / 12)
    return base12


def obtener_valor_real(caracter_base12):
    equivalencias = {
        "b": 11,
        "a": 10,
    }
    if caracter_base12 in equivalencias:
        return equivalencias[caracter_base12]
    else:
        return int(caracter_base12)


def base12_a_decimal(base12):
    base12 = base12.lower()
    base12 = base12[::-1]
    decimal = 0
    posicion = 0
    for digito in base12:
        valor = obtener_valor_real(digito)
        elevado = 12 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE 13

def obtener_caracter_base13(valor):
    
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_base13(decimal):
    base13 = ""
    while decimal > 0:
        residuo = decimal % 13
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        base13 = verdadero_caracter + base13
        decimal = int(decimal / 13)
    return base13


def obtener_valor_real(caracter_base13):
    equivalencias = {
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_base13 in equivalencias:
        return equivalencias[caracter_base13]
    else:
        return int(caracter_base13)


def base13_a_decimal(base13):
    base13 = base13.lower()
    base13 = base13[::-1]
    decimal = 0
    posicion = 0
    for digito in base13:
        valor = obtener_valor_real(digito)
        elevado = 13 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE 14

def obtener_caracter_base14(valor):
    
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_base14(decimal):
    base14 = ""
    while decimal > 0:
        residuo = decimal % 14
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        base14 = verdadero_caracter + base14
        decimal = int(decimal / 14)
    return base14


def obtener_valor_real(caracter_base14):
    equivalencias = {
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_base14 in equivalencias:
        return equivalencias[caracter_base14]
    else:
        return int(caracter_base14)


def base14_a_decimal(base14):
    base14 = base14.lower()
    base14 = base14[::-1]
    decimal = 0
    posicion = 0
    for digito in base14:
        valor = obtener_valor_real(digito)
        elevado = 14 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE 15

def obtener_caracter_base15(valor):
    
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_base15(decimal):
    base15 = ""
    while decimal > 0:
        residuo = decimal % 15
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        base15 = verdadero_caracter + base15
        decimal = int(decimal / 15)
    return base15


def obtener_valor_real(caracter_base15):
    equivalencias = {
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_base15 in equivalencias:
        return equivalencias[caracter_base15]
    else:
        return int(caracter_base15)


def base15_a_decimal(base15):
    base15 = base15.lower()
    base15 = base15[::-1]
    decimal = 0
    posicion = 0
    for digito in base15:
        valor = obtener_valor_real(digito)
        elevado = 15 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal
    
# BASE 16

def obtener_caracter_hexadecimal(valor):
    
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)


def hexadecimal_a_decimal(hexadecimal):
    hexadecimal = hexadecimal.lower()
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0
    for digito in hexadecimal:
        valor = obtener_valor_real(digito)
        elevado = 16 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal

# BASE ASCCI

def obtener_caracter_ascii(valor):
    
    valor = str(valor)
    equivalencias = {
        "64": "@","65": "a","66": "b","67": "c","68": "d","69": "e","70": "f","71": "g","72": "h","73": "i","74": "j","75": "k","76": "l","77": "m","78": "n","79": "o","80": "p","81": "q","82": "r",
        "83": "s","84": "t","85": "u","86": "v","87": "w","88": "x","89": "y","90": "z"
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_ascii(decimal):
    ascci = ""
    while decimal > 0:
        residuo = decimal % 90
        verdadero_caracter = obtener_caracter_ascii(residuo)
        ascci = verdadero_caracter + ascci
        decimal = int(decimal / 90)
    return ascci
