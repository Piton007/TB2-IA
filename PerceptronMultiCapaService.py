from PerceptronMultiCapaCore import PerceptronMulticapa 


class PerceptronMulticapaService():
    def __init__(self):
        self.perceptron_multicapa=""
        self.resultados=""

    def configurar_perceptron(self,neuronas_entrada,neuronas_escondidas,neuronas_salida,coeficiente_aprendizaje,limite_error_cuadratico):
        del self.perceptron_multicapa
        self.perceptron_multicapa=PerceptronMulticapa(neuronas_entrada,neuronas_escondidas,neuronas_salida,coeficiente_aprendizaje,limite_error_cuadratico)

    def entrenar_perceptron(self,patrones,resultados_esperados):
        self.resultados=self.perceptron_multicapa.entrenar(patrones,resultados_esperados)

    def obtener_pesos(self):
        return dict(pesos_ocultos=self.perceptron_multicapa.pesos_ocultos.tolist(),bias_oculta=self.perceptron_multicapa.bias_oculta.tolist(),pesos_salidas=self.perceptron_multicapa.pesos_salidas.tolist(),bias_salida=self.perceptron_multicapa.bias_salida.tolist(),limite=self.perceptron_multicapa.limite_error_cuadratico,
        error=self.resultados.get("error"),
        resultado=self.resultados.get("resultado")
        )
    
    

    

