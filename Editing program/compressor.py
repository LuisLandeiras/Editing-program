import numpy as np
import base64
#Função responsável por fazer o encode de uma String usando o RLE
def endecode(full_text):
    text2 = []
    number = []
    a = 0
    b = 0
    c = 1
    for x in range (0, len(full_text)):
        if (a == 0):
            text2.append(full_text[a])
            number.append(c)
            a = a + 1
        else:
            if(a < len(full_text)): 
                while (a < len(full_text) and full_text[a - 1] == full_text[a]):
                    a = a + 1
                if(text2[b] != full_text[a - 1]):
                    text2.append(full_text[a - 1])
                    number.append(a - c)
                    c = a
                    b = b + 1
                if (text2[b] == full_text[a - 1] and b == 0):
                    number[0] = a
                    c = a
                a = a + 1        
    if (text2[len(text2) - 1] != full_text[len(full_text) - 1]):
        text2.append(full_text[len(full_text) - 1])
    end = [text2, number]
    return end

def openfile(filename):
    file = open(filename, "rb")
    converted_string = base64.b64encode(file.read())
    #Converter cada byte do ficheiro em um inteiro e guardar no array s:
    s = []
    for x in range (0, len(converted_string)):
        s.append(converted_string[x])
    #Converter cada inteiro guardado no array s para um caractere:
    data = ""
    for x in range (0, len(s)):
        s[x] = chr(s[x])
        data = s[x] + data
    #Criação do ficheiro "COMPRESS" e gravação nele do conteúdo comprimido
    #Como a função endecode devolve uma lista bidemensional nós convertemos essa lista para um numpy array e depois para bytes
    file = open("COMPRESS.rle", "w")
    hh = endecode(data)
    file.write(str(hh))
    file.close
    print(hh)