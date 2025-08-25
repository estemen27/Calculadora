import math


class Calculadora:

    tipo='cientifica'

    def __init__(self,operando1=0, operando2=0, operacion="+"):

        self.operando1=operando1
        self.operando2=operando2
        self.operacion=operacion


    def __str__(self):
        if getattr(self, 'operacion', None) is None:
            return "Calculadora en espera"
        try:
            return f"{self.operando1}{self.operacion}{self.operando2}"
        except Exception:
            print("Calculadora en espera")

    def suma(self, operando1=None, operando2=None):
        self.operacion = "+"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None and operando2 is None:
            self.operando2 = operando1
        try:
            self.operando1 = self.operando1 + self.operando2
        except TypeError:
            print("ERROR OPERANDOS DEBEN SER NUMERICOS")
            return None
        return self

    def resta(self, operando1=None, operando2=None):
        self.operacion = "-"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None and operando2 is None:
            self.operando2 = operando1
        try:
            self.operando1 = self.operando1 - self.operando2
        except TypeError:
            print("ERROR OPERANDOS DEBEN SER NUMERICOS")
            return None
        return self

    def multiplicacion(self, operando1=None, operando2=None):
        self.operacion = "*"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None and operando2 is None:
            self.operando2 = operando1
        try:
            self.operando1 = self.operando1 * self.operando2
        except TypeError:
            print("ERROR OPERANDOS DEBEN SER NUMERICOS")
            return None
        return self

    def division(self, operando1=None, operando2=None):
        self.operacion = "/"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None and operando2 is None:
            self.operando2 = operando1
        try:
            self.operando1 = self.operando1 / self.operando2
        except TypeError:
            print("ERROR OPERANDOS DEBEN SER NUMERICOS")
            return None
        except ZeroDivisionError:
            print("ERROR NO SE PUEDE DIVIDIR POR CERO")
            self.operando1 = None
            return None
        return self

    def potencia(self, operando1=None,exponente=None):
        self.operacion = "**"
        if operando1 is not None and exponente is not None:
            self.operando1 = operando1
            self.exponente = exponente
        return self.operando1**self.exponente

    def raiz(self, operando1=None):
        self.operacion = "√"
        if operando1 is not None:
            self.operando1 = operando1
            resultado = math.sqrt(self.operando1)
        return resultado


class CalculadoraCientifica(Calculadora):

    def seno(self):
        self.operacion='sin'
        try:
            self.operando1=math.sin(self.operando1)
        except Exception as err:
            print("Gestion de exepciones", err)
            self.operando1=None

        return self

    def coseno(self):
        self.operacion='cos'
        try:
            self.operando1=math.cos(self.operando1)
        except Exception as err:
            print("Gestion de exepciones", err)
            self.operando1=None

        return self

    def tangente(self):
        self.operacion='tan'
        try:
            self.operando1=math.tan(self.operando1)
        except Exception as err:
            print("Gestion de exepciones", err)
            self.operando1=None

        return self



result= Calculadora(10).suma(5).multiplicacion(2)
print(result.operando1)

result1= CalculadoraCientifica(90).seno()
print(result1.operando1)

result2=Calculadora(200).suma(80).resta(30).multiplicacion(4).division(3)
print(result2.operando1)

result3=CalculadoraCientifica(45).coseno()
print(result3.operando1)

result4=Calculadora().raiz(9)
print(result4)

result5=CalculadoraCientifica(90).seno()
print(result5.operando1)