casos = int(input())
cont = 0
um = int(1)
dois = int(2)
tres = int(3)
while cont < casos:
    palavra = str(input())
    tamanho = len(palavra)
    if tamanho == 5:
        print("3")
    else:
        if palavra[0] == 't':
            if palavra[1] == 'w':
                print("2")
            else:
                if palavra[2] == 'o':
                    print("2")
                else:
                    print("1")
        else:
            if palavra[1] == 'w':
                if palavra[2] == 'o':
                    print("2")
                else:
                    print("1")
            else:
                print("1")
    cont = cont + 1