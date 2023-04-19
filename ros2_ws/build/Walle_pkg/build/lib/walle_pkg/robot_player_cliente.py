import rclpy
from rclpy.node import Node
from servicio.srv import ReadFile
import threading


class Cliente(Node):

    def __init__(self):
        super().__init__('cliente')
        self.cliente = self.create_client(ReadFile, 'read_file')
        self.event = threading.Event()
        self.resultado = None

    def espera_por_respuesta(self):
        self.event.wait()
        return self.resultado

    def abrir_archivo(self, file_path):
        solicitud = ReadFile.Request()
        solicitud.file_path = file_path
        futuro = self.cliente.call_async(solicitud)
        futuro.add_done_callback(self.tratar_respuesta)

    def tratar_respuesta(self, futuro):
        self.resultado = futuro.result().file_content
        self.event.set()

def main(args=None):
    rclpy.init(args=args)
    cliente = Cliente()
    cliente.abrir_archivo('/path/to/your/file.txt')
    resultado = cliente.espera_por_respuesta()
    print('Contenido del archivo:\n%s' % resultado)
    cliente.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
   
