idade  =  int ( input ( "digite a sua idade:" ))
if  15 < idade <  70 :
  peso  =  int ( input ( "digite seu peso em kg:" ))
  if  peso > 49 :
    horasdesono =  int ( input ( "Quanto tempo você dormiu nas ultimas 24 horas:" ))
        if  tempodesono > 6 :
        
          print ( "Você pode fazer a doação" )
          escolha  =  int ( input ( "Voce quer cadastar-se? 1 para sim 0 para não:" ))
          if  escolha > 0 :
       
       Nome  = input ( "Insira seu nome completo:" )
       Cpf   = int ( input ( "Insira seu Cpf:" ))
       Senha = int ( input ( "Insira sua senha:"))   
       
               print ( "esses sao os dados do paciente:" , Nome , "" , Cpf , "" , Senha)
               
            else :
                print ( "obrigado por doar sangue")
        else :
            print ( "você não dormiu o suficiente para a doação de sangue" )
    else :
        print ( "Seu peso está abaixo do necessario para a doação de sangue" )
else :
     print ( "você nao tem idade pra poder doar sangue" )
