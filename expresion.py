import re 

expresion ='A123bar$&%'
validar = re.compile("[A-Z]{1}[0-9]{3}[a-z]+\W{3}")

if (validar.search(expresion)):
     resul = validar.search(expresion).group(0)
else: 
     print("No pertenece!!...")
     exit()  

if (resul == expresion):   
      print("Pertenece a esta expresión regular...")
