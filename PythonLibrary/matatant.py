from serial import Serial
from time import sleep

class Matatant(Serial):
    def __init__(self, port:int):
        '''
        port: puerto serial para iniciar la coneccion -> "COM{port_number}"
        '''
        # idealmente hay que buscar como automatizar la busqueda del puerto pq es facil pero no practico
        print('Estableciendo coneccion...')
        super().__init__(f'COM{port}', baudrate = 9600, timeout = 1)
        print('Coneccion establecida!')


    def forward(self, steps:int, ):
        # hay que hacer el calculo potencia-distancia para implementar bn los pasos
        # por ahora es potencia directa
        # en turtle hay una funcion para definir la velocidad y forward solo avanza pasos fijos
        # hay que decidir si trabajar igual o con aceleraciones con tiempos, por ahora es solo prueba
        self.write(str.encode(f'$A%{steps}$'))
        sleep(2)
        self.write(str.encode(f'$A%0$'))

    def left(self, degrees:int):
        self.write(str.encode(f'$L%{degrees}$'))
        self.write(str.encode(f'$R%{-degrees}$'))
        sleep(2)
        self.write(str.encode(f'$A%0$'))

    def right(self, degrees:int):
        self.write(str.encode(f'$L%{-degrees}$'))
        self.write(str.encode(f'$R%{degrees}$'))
        sleep(2)
        self.write(str.encode(f'$A%0$'))