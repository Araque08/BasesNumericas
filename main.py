import Conversor

def solicitar_datos():
    BasesNumericas = ["2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","ascii" ]
    
    base_origen = input("Elige la base desde donde conviertes desde la base 1 hasta la 16: ")
    if base_origen not in BasesNumericas:
        print("La base que ingresaste no está")
        return
    numero = input('Ok, vas a convertir desde la base '+ str(base_origen) +' Ingresa el número a convertir: ')
    
    base_deseada = input("Elige la base a la que convierte desde la base 1 hasta la 16 o ascii: ")
    if base_deseada not in BasesNumericas:
        print("La base de destino no está soportada")
        return
    return (base_origen, numero, base_deseada)


def obtener_decimal(base_origen, numero):
    if base_origen == "2":
        return Conversor.binario_a_decimal(numero)
    else:
        if base_origen == "3":
            return Conversor.base3_a_decimal(numero)
        else:
            if base_origen == "4":
                return Conversor.base4_a_decimal(numero)
            else:
                if base_origen == "5":
                    return Conversor.base5_a_decimal(numero)
                else:
                    if base_origen == "6":
                        return Conversor.base6_a_decimal(numero)
                    else:
                        if base_origen == "7":
                            return Conversor.base7_a_decimal(numero)
                        else:
                            if base_origen == "8":
                                return Conversor.octal_a_decimal(numero)
                            else:
                                if base_origen == "9":
                                    return Conversor.base9_a_decimal(numero)
                                else:
                                    if base_origen == "10":
                                        return int(numero)
                                    else:
                                        if base_origen == "11":
                                            return Conversor.base11_a_decimal(numero)
                                        else:
                                            if base_origen == "12":
                                                return Conversor.base12_a_decimal(numero)
                                            else:
                                                if base_origen == "13":
                                                    return Conversor.base13_a_decimal(numero)
                                                else:
                                                    if base_origen == "14":
                                                        return Conversor.base14_a_decimal(numero)
                                                    else:
                                                        if base_origen == "15":
                                                            return Conversor.base15_a_decimal(numero)
                                                        else: 
                                                            if base_origen == "16":
                                                                return Conversor.hexadecimal_a_decimal(numero)
                                                            elif base_origen == "ascii":
                                                                return Conversor.ascii_a_decimal(numero)


def convertir(numero, base_deseada):
    if base_deseada == "2":
        return Conversor.decimal_a_binario(numero)
    else: 
        if base_deseada == "3":
            return Conversor.decimal_a_base3(numero)
        else: 
            if base_deseada == "4":
                return Conversor.decimal_a_base4(numero)
            else:
                if base_deseada == "5":
                    return Conversor.decimal_a_base5(numero)
                else:  
                    if base_deseada == "6":
                        return Conversor.decimal_a_base6(numero)
                    else: 
                        if base_deseada == "7":
                            return Conversor.decimal_a_base7(numero)
                        else: 
                            if base_deseada == "8":
                                return Conversor.decimal_a_octal(numero)
                            else:
                                if base_deseada == "9":
                                    return Conversor.decimal_a_base9(numero)
                                else: 
                                    if base_deseada == "10":
                                        return int(numero)
                                    else:
                                        if base_deseada == "11":
                                            return Conversor.decimal_a_base11(numero)
                                        else: 
                                            if base_deseada == "12":
                                                return Conversor.decimal_a_base12(numero)
                                            else: 
                                                if base_deseada == "13":
                                                    return Conversor.decimal_a_base13(numero)
                                                else: 
                                                    if base_deseada == "14":
                                                        return Conversor.decimal_a_base14(numero)
                                                    else: 
                                                        if base_deseada == "15":
                                                            return Conversor.decimal_a_base14(numero)
                                                        else: 
                                                            if base_deseada == "16":
                                                                return Conversor.decimal_a_hexadecimal(numero)
                                                            else:
                                                                if base_deseada == "ascii":
                                                                    return Conversor.decimal_a_ascii(numero)


if __name__ == '__main__':
    datos = solicitar_datos()
    if datos:
        base_origen, numero, base_deseada = datos
        numero_decimal = obtener_decimal(base_origen, numero)
        resultado = convertir(numero_decimal, base_deseada )
        print(resultado)