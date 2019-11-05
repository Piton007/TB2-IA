
def EntradaConsola():
    print("Bienvenido al sistema detector de Diabetes")
    nombre = input("Ingrese su nombre: ")
    print("Comenzemos doctor",nombre)
    print("====================CUESTIONARIO====================")
def TomaDeDatos():
    atxt = input("El paciente cuenta con familiares que hayan padecido diabetes?")
    if atxt == 'Si' or atxt == 'si':
        a=1
    else:
        a=0
    btxt = input("La prueba de glucosa a1c muestra un porcentaje mayor a 6.5%?")
    if btxt == 'Si' or btxt == 'si':
        b=1
    else:
        b=0
    ctxt = input("El conteo de glóbulos blancos muestra un nivel de neutrófilos mayor a 7600 ml?")
    if ctxt == 'Si' or ctxt == 'si':
        c=1
    else:
        c=0
    dtxt = input("El paciente presenta fatiga generalizada?")
    if dtxt == 'Si' or dtxt == 'si':
        d=1
    else:
        d=0
    return a,b,c,d
    
def main():
    EntradaConsola()
    a,b,c,d = TomaDeDatos()


main()
