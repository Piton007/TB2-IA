from PerceptronMultiCapaCore import PerceptronMulticapa 


class PerceptronMulticapaService():
    def __init__(self):
        self.perceptron_multicapa=""
        self.resultados=""

    def configurar_perceptron(self,neuronas_entrada,neuronas_escondidas,neuronas_salida,coeficiente_aprendizaje,limite_error_cuadratico):
        del self.perceptron_multicapa
        self.perceptron_multicapa=PerceptronMulticapa(neuronas_entrada,neuronas_escondidas,neuronas_salida,coeficiente_aprendizaje,limite_error_cuadratico)

    def entrenar_perceptron(self):
        return self.perceptron_multicapa.entrenar()

    def obtener_pesos(self):
        return dict(pesos_ocultos=self.perceptron_multicapa.pesos_ocultos.tolist(),bias_oculta=self.perceptron_multicapa.bias_oculta.tolist(),pesos_salidas=self.perceptron_multicapa.pesos_salidas.tolist(),bias_salida=self.perceptron_multicapa.bias_salida.tolist(),limite=self.perceptron_multicapa.limite_error_cuadratico,
        error=self.resultados.get("error"),
        resultado=self.resultados.get("resultado")
        )

    def agregar_patrones(self,patron):
        self.perceptron_multicapa.agregar_patron(patron)
    def agregar_valor_esperado(self,esperado):
        self.perceptron_multicapa.agregar_valor_esperado(esperado)
    def obtener_prediccion(self):
        return self.perceptron_multicapa.predecir()
    def obtener_size_patrones(self):
        return self.perceptron_multicapa.get_patrones()
    
    

    

