
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PerceptronMultiCapaService import PerceptronMulticapaService
from PIL import ImageTk,Image

NEURONAS_OCULTAS=4
COEFICIENTE_APRENDIZAJE=0.25
LIMITE_ERROR_CUADRATICO=0.3
NEURONAS_ENTRADA=4
NEURONAS_SALIDA=1
LOGO_WIDTH=200
LOGO_HEIGHT=200

def Estilos():
    style = ttk.Style()
    style.theme_use("alt")
    style.configure("Test.TLabel",font="Arial 12",anchor=CENTER,width=9,foreground="black",background="gray94")
    style.configure("TButton",font="Arial 12 bold",anchor="center",foreground="gray38",background="red")
    
    return style



class FLogin():
    def __init__(self):
        self.root=Tk()
        self.root.title("Login")
        self.root.resizable(width=False,height=False)
        self.style=Estilos()
        self.nombre=StringVar()
        self.resized = Image.open('doc.png').resize((LOGO_WIDTH, LOGO_HEIGHT),Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(self.resized)
        self.panel=Canvas(self.root,width=LOGO_WIDTH,height=LOGO_HEIGHT)
        self.panel.grid(row=0,column=0,columnspan=2,sticky=(N,S))
        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.panel.create_image(0,0,image=self.img,anchor='nw')
        self.lblNombre=ttk.Label(self.root,text="Nombre",anchor='nw',style="Test.TLabel")
        self.inpNombre=ttk.Entry(self.root,textvariable=self.nombre,font="Arial 10 bold")
        self.btnruta=ttk.Button(self.root,command=self.toPrincipal,text="Comenzar",width=11)
        self.lblNombre.grid(row=1,column=0,sticky=(N,S),padx=10,pady=10)
        self.inpNombre.grid(row=1,column=1,sticky=(N,S),padx=10,pady=10)
        self.btnruta.grid(row=2,column=0,columnspan=2,sticky=(N,S),padx=10,pady=10)
    def toPrincipal(self):
        new_root=Toplevel()
        
        messagebox.showinfo(message="Bievenido Doc {}".format(self.nombre.get()), title="Diagnostico Diabetes Tipo I")
        self.root.withdraw()
        Dialog=FPrincipal(new_root,self.nombre.get())
        

class FPrincipal():
    def __init__(self,root,medico):
        self.perceptron=PerceptronMulticapaService()
        self.root=root
        self.root.title("Doc. {} - Entrenando".format(medico))
        self.root.resizable(width=False,height=False)
        self.style=Estilos()
        self.notebook=ttk.Notebook(self.root)
        self.formulario=ttk.Frame(self.notebook)
        self.configuracion=ttk.Frame(self.notebook)
        self.info=ttk.Frame(self.notebook)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.notebook.grid(row=0,column=0,sticky=(N,S,W,E))
        self.neuronas=StringVar()
        self.coeficiente_aprendizaje=StringVar()
        self.limite_error_cuadratico=StringVar()
        self.herencia=IntVar()
        self.fatiga=IntVar()
        self.resultado_esperado=IntVar()
        self.neutrofilos=StringVar()
        self.glucosa=StringVar()
        self.configuracion.columnconfigure(0,weight=1)
        self.configuracion.columnconfigure(1,weight=1)
        self.formulario.columnconfigure(1,weight=1)
        self.formulario.columnconfigure(0,weight=1)
        self.defaultValues()
        self.configurar()
        self.generarVistaInfo()
        self.generarVistaEntrenamiento()
        self.generarVistaConfiguracion()
        self.notebook.add(self.formulario, text="Entrenamiento")
        self.notebook.add(self.info,text="Resultados")
        self.notebook.add(self.configuracion, text="Configuracion")
    def generarVistaInfo(self):
        
        self.resultados=Text(self.info,font="Arial 14 bold",width=40,height=20)
        self.resultados.pack(fill="none", expand=True)

    def generarVistaEntrenamiento(self):
        self.lblherencia=ttk.Label(self.formulario,text="El paciente cuenta con familiares que hayan padecido diabetes?")
        self.lblglucosa=ttk.Label(self.formulario,text="Ingrese el resultado de la prueba de glucosa a1c (%)")
        self.lblleucocitos=ttk.Label(self.formulario,text="Ingrese el conteo de globulos para el nivel de neutrofilos (ml)")
        self.lblfatiga=ttk.Label(self.formulario,text="El Paciente presenta Fatiga generalizada?")
        self.lblesperado=ttk.Label(self.formulario,text="Considera que el paciente es un potencial caso de diabetes tipo 1?")
        self.rbEsperadoSi=ttk.Radiobutton(self.formulario, text='Si', variable=self.resultado_esperado, value=1)
        self.rbEsperadoNo=ttk.Radiobutton(self.formulario, text='No', variable=self.resultado_esperado, value=0)
        self.rbHerenciaSi=ttk.Radiobutton(self.formulario, text='Si', variable=self.herencia, value=1)
        self.rbHerenciaNo=ttk.Radiobutton(self.formulario, text='No', variable=self.herencia, value=0)
        self.rbFatigaSi=ttk.Radiobutton(self.formulario, text='Si', variable=self.fatiga, value=1)
        self.rbFatigaNo=ttk.Radiobutton(self.formulario, text='No', variable=self.fatiga, value=0)
        self.inpLeucocitos=ttk.Entry(self.formulario,textvariable=self.neutrofilos,font="Arial 10 bold",width=40)
        self.inpGlucosa=ttk.Entry(self.formulario,textvariable=self.glucosa,font="Arial 10 bold",width=40)
        self.btnEntrenar=ttk.Button(self.formulario,command=self.entrenar,text="Entrenar",width=11)
        self.lblherencia.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky=(N,S))
        self.rbHerenciaSi.grid(row=1,column=0,pady=10)
        self.rbHerenciaNo.grid(row=1,column=1,pady=10)
        self.lblglucosa.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky=(N,S))
        self.inpGlucosa.grid(row=3,column=0,columnspan=2,padx=10,pady=10,sticky=(N,S))
        self.lblfatiga.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky=(N,S))
        self.rbFatigaSi.grid(row=5,column=0,pady=10)
        self.rbFatigaNo.grid(row=5,column=1,pady=10)
        self.lblleucocitos.grid(row=6,column=0,columnspan=2,pady=10,sticky=(N,S))
        self.inpLeucocitos.grid(row=7,column=0,columnspan=2,pady=10,sticky=(N,S))
        self.lblesperado.grid(row=8,column=0,columnspan=2,padx=10,pady=10,sticky=(N,S))
        self.rbEsperadoSi.grid(row=9,column=0,pady=10,sticky=(N,S))
        self.rbEsperadoNo.grid(row=9,column=1,pady=10,sticky=(N,S))
        self.btnEntrenar.grid(row=10,column=0,columnspan=2,padx=10,pady=10,sticky=(N,S))
    def entrenar(self):
        valorGlucosa= 0 if float(self.glucosa.get())<5.7 else 1
        valorNeutrofilo= 0 if float(self.neutrofilos.get())<7600.0 else 1
        self.perceptron.entrenar_perceptron([[self.herencia.get(),valorGlucosa,self.fatiga.get(),valorNeutrofilo]],[[self.resultado_esperado.get()]])
        dic=self.perceptron.obtener_pesos()
        self.resultados.delete(1.0,END)
        self.resultados.insert(END,self.generarTextResultados(dic))
    def generarTextResultados(self,dic):
        text="***Resultados de ultimo entrenamiento***\n\nPeso final de neuronas escondidas: \n{}\nPeso final de bias escondida: \n{}\nPeso final de neuronas de salida: \n{}\nPeso final de bias de salida: \n{}\nActual error cuadratico medio con limite de {}: \n{}\nResultado Esperado: \n{}\n".format(dic.get("pesos_ocultos"),dic.get("bias_oculta"),dic.get("pesos_salidas"),dic.get("bias_salida"),dic.get("limite"),dic.get("error"),dic.get("resultado"))
        return text
        
        
        
    def generarVistaConfiguracion(self):
        self.lblCoeficiente=ttk.Label(self.configuracion,text="Coeficiente de aprendizaje")
        self.lblNeuronasOcultas=ttk.Label(self.configuracion,text="Neuronas ocultas")
        self.lblLimiteErrorCuadratico=ttk.Label(self.configuracion,text="Limite error cuadratico")
        self.inpCoeficiente=ttk.Entry(self.configuracion,textvariable=self.coeficiente_aprendizaje,font="Arial 10 bold")
        self.inpNeuronasOcultas=ttk.Entry(self.configuracion,textvariable=self.neuronas,font="Arial 10 bold")
        self.inpLimiteErrorCuadratico=ttk.Entry(self.configuracion,textvariable=self.limite_error_cuadratico,font="Arial 10 bold")
        self.btnruta=ttk.Button(self.configuracion,command=self.configurar,text="Guardar",width=11)
        self.lblCoeficiente.grid(row=0,column=0,padx=10,pady=10,sticky=(N,S))
        self.lblNeuronasOcultas.grid(row=1,column=0,padx=10,pady=10,sticky=(N,S))
        self.lblLimiteErrorCuadratico.grid(row=2,column=0,padx=10,pady=10,sticky=(N,S))
        self.inpCoeficiente.grid(row=0,column=1,padx=10,pady=10,sticky=(N,S))
        self.inpNeuronasOcultas.grid(row=1,column=1,padx=10,pady=10,sticky=(N,S))
        self.inpLimiteErrorCuadratico.grid(row=2,column=1,padx=10,pady=10,sticky=(N,S))
        self.btnruta.grid(row=3,column=0,columnspan=2,padx=10,pady=10,sticky=(N,S))
        
    def configurar(self):
        self.perceptron.configurar_perceptron(NEURONAS_ENTRADA,int(self.neuronas.get()),NEURONAS_SALIDA,float(self.coeficiente_aprendizaje.get()),float(self.limite_error_cuadratico.get()))
    def defaultValues(self):
        self.neuronas.set(NEURONAS_OCULTAS)
        self.coeficiente_aprendizaje.set(COEFICIENTE_APRENDIZAJE)
        self.limite_error_cuadratico.set(LIMITE_ERROR_CUADRATICO)
        self.herencia.set(0)
        self.fatiga.set(0)
    




        

app=FLogin()
app.root.mainloop()
