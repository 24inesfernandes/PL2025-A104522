def somador_on_off(texto):
    on = True # O somador começa ligado
    soma = 0
    numero_atual = 0

    i = 0
    while i < len(texto):
        char = texto[i]

        # Desliga o somador se encontrar "off"
        if texto[i:i+3].lower() == "off":
            on = False
            i += 3

        # Liga o somador se encontrar "on"
        elif texto[i:i+2].lower() == "on":
            on = True
            i += 2
        
        # Guarda as strings de ints em "numero_atual" e soma-as em "soma"
        elif on and char.isdigit():
            numero_atual = 0
            while i < len(texto) and texto[i].isdigit():
                numero_atual = numero_atual * 10 + int(texto[i])
                i += 1
            soma += numero_atual
            continue
        
        # Se o caracter for "=", imprime a soma
        elif on and char == "=":
            print("Resultado:", soma)
        
        i += 1
            


if __name__ == "__main__":
    texto = input("Inserir texto: ")
    somador_on_off(texto)
