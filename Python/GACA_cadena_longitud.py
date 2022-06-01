class Cadena:
  def longituddeCadena(self):
    x=input("Palabra: ")
    y=x.lower()
    y=y[0].upper()+y[1:]
    contador=0
    for i in x:
      contador+=1
    print(y,'tiene',contador,'caracteres.')

  

cadena=Cadena()
cadena.longituddeCadena()
