import numpy as np 

class PerceptronMulticapa:
    def __init__(self,neuronas_entrada,neuronas_escondidas,neuronas_salida,coeficiente_aprendizaje,limite_error_cuadratico):
        self.neuronas_entrada=neuronas_entrada
        self.neuronas_escondidas=neuronas_escondidas
        self.neuronas_salida=neuronas_salida
        self.limite_error_cuadratico=limite_error_cuadratico
        self.coeficiente_aprendizaje=coeficiente_aprendizaje
        self.patrones=[]
        self.resultados_esperados=[]
        self.inicializar_pesos()

    def entrenar(self):
        self.patrones_np=np.array(self.patrones)
        self.resultados_esperados_np=np.array(self.resultados_esperados)
        while True:
            salida_predecida=self.backpropagation()
            error_cuadratico=self.obtener_error_cuadratico_medio(salida_predecida)
            if error_cuadratico<self.limite_error_cuadratico:
                break
        return dict(error=error_cuadratico,resultado=salida_predecida)
    
    def backpropagation(self):
        salida_capa_oculta,salida_predecida= [ salida for salida in self.propagacion_hacia_adelante()]
        d_salida_predecida,d_capa_oculta=[d_salida for d_salida in self.propagacion_hacia_atras(salida_predecida,salida_capa_oculta)]
        self.actualizacion_pesos(d_salida_predecida,d_capa_oculta,salida_capa_oculta)
        return salida_predecida.tolist()

    def predecir(self):
        resultado=""
        try:
            salida_predecida=self.backpropagation()[0][-1]
            resultado = 0 if 1-salida_predecida>salida_predecida else 1
        except:
            resultado = "Error"
        finally:
            return resultado

    def obtener_error_cuadratico_medio(self,salida_predecida):
        matriz_diferencia=np.subtract(self.resultados_esperados_np,salida_predecida)
        matriz_potenciada=np.power(matriz_diferencia,2)
        return np.sum(matriz_potenciada)
    def inicializar_pesos(self):
        self.pesos_ocultos=np.random.uniform(size=(self.neuronas_entrada,self.neuronas_escondidas))
        self.bias_oculta=np.random.uniform(size=(1,self.neuronas_escondidas))
        self.pesos_salidas=np.random.uniform(size=(self.neuronas_escondidas,self.neuronas_salida))
        self.bias_salida=np.random.uniform(size=(1,self.neuronas_salida))
    
    def propagacion_hacia_adelante(self):
        salida_capa_oculta=self.propagacion_hacia_adelante_oculta()
        salida_predecida=self.propagacion_hacia_adelante_salida(salida_capa_oculta)
        return [salida_capa_oculta,salida_predecida]
    
    def propagacion_hacia_atras(self,salida_predecida,salida_capa_oculta):
        d_salida_predecida=self.propagacion_hacia_atras_salida(salida_predecida)
        d_capa_oculta=self.propagacion_hacia_atras_oculta(d_salida_predecida,salida_capa_oculta)
        return [d_salida_predecida,d_capa_oculta]
    
    def actualizacion_pesos(self,d_salida_predecida,d_capa_oculta,salida_capa_oculta):
        self.pesos_salidas += salida_capa_oculta.T.dot(d_salida_predecida) * self.coeficiente_aprendizaje
        self.bias_salida += np.sum(d_salida_predecida) * self.coeficiente_aprendizaje
        self.pesos_ocultos += self.patrones_np.T.dot(d_capa_oculta) * self.coeficiente_aprendizaje
        self.bias_oculta += np.sum(d_capa_oculta) * self.coeficiente_aprendizaje
        
    def propagacion_hacia_adelante_oculta(self):
        activacion_capa_oculta = np.dot(self.patrones_np,self.pesos_ocultos)
        activacion_capa_oculta += self.bias_oculta
        salida_capa_oculta = self.sigmoid(activacion_capa_oculta)
        return salida_capa_oculta
    def propagacion_hacia_adelante_salida(self,salida_capa_oculta):
        activacion_capa_salida = np.dot(salida_capa_oculta,self.pesos_salidas)
        activacion_capa_salida += self.bias_salida
        salida_predecida = self.sigmoid(activacion_capa_salida)
        return salida_predecida
    
    def propagacion_hacia_atras_salida(self,salida_predecida):
        error = self.resultados_esperados_np - salida_predecida
        d_salida_predecida = error * self.sigmoid_derivative(salida_predecida)
        return d_salida_predecida
    
    def propagacion_hacia_atras_oculta(self,d_salida_predecida,salida_capa_oculta):
        error_capa_oculta = d_salida_predecida.dot(self.pesos_salidas.T)
        d_capa_oculta = error_capa_oculta * self.sigmoid_derivative(salida_capa_oculta)
        return d_capa_oculta
    
    def sigmoid(self,x):
        return 1/(1 + np.exp(-x))
    
    def sigmoid_derivative(self,x):
        return x * (1 - x)

    def agregar_patron(self,patron):
        self.patrones.append(patron)

    def agregar_valor_esperado(self,valor_esperado):
        self.resultados_esperados.append(valor_esperado)

    def eliminar_patron(self,indice):
        self.patrones.pop(indice)
        self.resultados_esperados.pop(indice)
    
    def get_patrones(self):
        return len(self.patrones)

if __name__ == "__main__":
    Perceptron=PerceptronMulticapa(4,2,1,0.5,0.3)
    Perceptron.agregar_patron([0,1,0,1])
    Perceptron.agregar_valor_esperado([0])
    Perceptron.agregar_patron([0,1,1,1])
    Perceptron.agregar_valor_esperado([0])
    print(Perceptron.entrenar())
    
    
