import rclpy
from rclpy.node import Node
from servidor.srv import ReadFile
import os


class Servidor(Node):

    def __init__(self):
        super().__init__('servidor')
        self.servidor = self.create_service(ReadFile, 'read_file', self.leer_archivo)

    def leer_archivo(self, request, response):
        file_path = request.file_path
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            response.file_content = content
        else:
            response.file_content = 'Archivo no encontrado'

        return response


def main(args=None):
    rclpy.init(args=args)
    servidor = Servidor()
    rclpy.spin(servidor)
    servidor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
