# Validar CPF.

cpf = input('Digite o CPF sem pontos e sem digitos:')
if cpf.isnumeric() and len(cpf) == 11:
    lista_cpf = []

    for n_cpf in cpf:
        lista_cpf.append(int(n_cpf))


    L_calc_1 = lista_cpf[:-2] 
    
    cont_1 = 11
    mult_calc1 = []
    for n_mult in L_calc_1:
        cont_1 -= 1

        Valor_calc1 = n_mult*cont_1 
        mult_calc1.append(int(Valor_calc1))
        
    Soma_Calculo1 = 0
    for soma in mult_calc1:
        Soma_Calculo1 = Soma_Calculo1 + soma
#calculo do modulo 1.
        modulo_cal1 = 11 - (Soma_Calculo1%11)

    if modulo_cal1 > 9:
        Primeiro_Digito = 0
    else:
        Primeiro_Digito = modulo_cal1
        
    L_calc_1.append(Primeiro_Digito)

#Segundo calculo de validação CPF

    cont_2 = 12
    multi_calc2 = []
    for n_calc2 in L_calc_1:
        cont_2 -= 1
        Valor_calc2 = n_calc2*cont_2
        multi_calc2.append(int(Valor_calc2))
        
    Soma_Calculo2 = 0
    for n_soma2 in multi_calc2:
        Soma_Calculo2 = Soma_Calculo2 + n_soma2
        
    modulo_cal2 = 11-(Soma_Calculo2%11)

    if modulo_cal2 > 9:
       Segundo_digito = 0
    else:
       Segundo_digito = modulo_cal2
    
    L_calc_1.append(Segundo_digito)
    novo_cpf = L_calc_1
    
    if novo_cpf == lista_cpf:
       print(f'O CPF {cpf} é valido.')
    else:
       print(f'O CPF {cpf} é invalido')
else:
    print(f'Por favor digite 11(onze) números sendo apenas números do cpf sem pontos ou digitos.')