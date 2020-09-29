palavra = input ("Insira uma palavra: ")
palavraInversa = input ("Insira o inverso da palavra anterior: ")

def parametroInverso(palavra1, palavra2):
  if palavra2 == palavra1[::-1] or palavra1 == palavra2[::-1]:
  return True 
 else:
  return False 
  
  retornoInvertido = parametroInverso(palavraNormal, palavraInvertida)
  
  if retornoInvertido == True:
    print("Uma palavra é o inverso da outra.")
else:
    print("A palavra não é o inverso da outra, reinicie o programa e tende de novo.")
