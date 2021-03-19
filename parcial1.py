
texto = """Python es un lenguaje de programación interpretado cuya filosofía hace hincapié
 en la legibilidad de su código.2​ Se trata de un lenguaje de programación multiparadigma,
  ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor 
  medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma """


ignorar = ",;:.\n!\"'"
for caracter in ignorar:
    texto = texto.lower()
    texto = texto.replace(caracter, " ")  
                          
texto = texto.lower()

palabras = texto.split(" ")


repeticionesDicc= {}
for palabra in palabras:
    if palabra in repeticionesDicc:
        repeticionesDicc[palabra] += 1
    else:
        repeticionesDicc[palabra] = 1

for palabra in repeticionesDicc:
    repetir = repeticionesDicc[palabra]
    print(f"La palabra '{palabra}' tiene {repetir} repeticiones")
                