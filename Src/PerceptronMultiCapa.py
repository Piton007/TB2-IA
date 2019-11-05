import numpy as np 

class PerceptronMulticapa:
    def __init__(self,patrones,resultados_esperados,epocas,coeficiente_aprendizaje,limite_error_cuadratico):
        self.patrones=np.array(patrones)
        self.resultados_esperados=np.array(resultados_esperados)
        self.epocas=epocas
        self.limite_error_cuadratico=limite_error_cuadratico
        self.coeficiente_aprendizaje=coeficiente_aprendizaje
    def test(self,neuronas_entrada,neuronas_escondidas,neuronas_salida):
        self.neuronas_entrada=neuronas_entrada
        self.neuronas_escondidas=neuronas_escondidas
        self.neuronas_salida=neuronas_salida
        self.inicializar_pesos()
        while True:
            salida_capa_oculta,salida_predecida= [ x for x in self.propagacion_hacia_adelante()]
            d_salida_predecida,d_capa_oculta=[x for x in self.propagacion_hacia_atras(salida_predecida,salida_capa_oculta)]
            self.actualizacion_pesos(d_salida_predecida,d_capa_oculta,salida_capa_oculta)
            error_cuadratico=self.get_error_cuadratico_medio(salida_predecida)
            if error_cuadratico<self.limite_error_cuadratico:
                break
        print("Peso final de pesos de neuronas escondidas: ")
        print(self.pesos_ocultos)
        print("Peso final del peso de bias escondida: ")
        print(self.bias_oculta)
        print("Peso final de pesos de neuronas desalidas: ")
        print(self.pesos_salidas)
        print("Peso final de bias: ")
        print(self.bias_salida)
        print("\nActual error cuadratico medio con limite de  {}: ".format(self.limite_error_cuadratico))
        print(error_cuadratico)
        
    def get_error_cuadratico_medio(self,salida_predecida):
        matriz_diferencia=np.subtract(self.resultados_esperados,salida_predecida)
        matriz_potenciada=np.power(matriz_diferencia,2)
        return np.sum(matriz_potenciada)
    def inicializar_pesos(self):
        self.pesos_ocultos=np.random.uniform(size=(self.neuronas_entrada,self.neuronas_escondidas))
        self.bias_oculta=np.random.uniform(size=(1,self.neuronas_escondidas))
        self.pesos_salidas=np.random.uniform(size=(self.neuronas_escondidas,self.neuronas_salida))
        self.bias_salida=np.random.uniform(size=(1,self.neuronas_salida))
        print("Initial hidden weights: ")
        print(*self.pesos_ocultos)
        print("Initial hidden biases: ")
        print(*self.bias_oculta)
        print("Initial output weights: ")
        print(*self.pesos_salidas)
        print("Initial output biases: ")
        print(*self.bias_salida)
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
        self.pesos_ocultos += self.patrones.T.dot(d_capa_oculta) * self.coeficiente_aprendizaje
        self.bias_oculta += np.sum(d_capa_oculta) * self.coeficiente_aprendizaje
        
    def propagacion_hacia_adelante_oculta(self):
        activacion_capa_oculta = np.dot(self.patrones,self.pesos_ocultos)
        activacion_capa_oculta += self.bias_oculta
        salida_capa_oculta = self.sigmoid(activacion_capa_oculta)
        return salida_capa_oculta
    def propagacion_hacia_adelante_salida(self,salida_capa_oculta):
        activacion_capa_salida = np.dot(salida_capa_oculta,self.pesos_salidas)
        activacion_capa_salida += self.bias_salida
        salida_predecida = self.sigmoid(activacion_capa_salida)
        return salida_predecida
    
    def propagacion_hacia_atras_salida(self,salida_predecida):
        error = self.resultados_esperados - salida_predecida
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
    
if __name__ == "__main__":
    Perceptron=PerceptronMulticapa([[0,0],[0,1],[1,0],[1,1]],[[0],[1],[1],[0]],1000,0.25,0.3)
    Perceptron.test(2,3,1)
    
