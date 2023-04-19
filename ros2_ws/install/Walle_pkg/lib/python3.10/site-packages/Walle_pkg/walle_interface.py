# Importamos las librerías necesarias
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.filedialog import asksaveasfilename

# Definimos la clase para el nodo ROS
class TurtleBotInterface(Node):
    def __init__(self):
        super().__init__('turtle_bot_interface')
        # Inicializamos una lista para almacenar las posiciones recibidas del robot
        self.positions = []
        # Creamos un suscriptor para recibir las posiciones del robot
        self.subscriber_ = self.create_subscription(Pose, '/turtlebot_position', self.pose_callback, 10)
        # Definimos la función a llamar cuando llega un nuevo mensaje
        self.subscriber_.on_new_data = self.pose_callback
        # Creamos un temporizador para actualizar el gráfico
        self.timer_ = self.create_timer(0.1, self.timer_callback)
        # Creamos un objeto mensaje Twist vacío para enviar comandos al robot en el futuro
        self.twist_msg_ = Twist()

    # Función para procesar cada posición recibida
    def pose_callback(self, msg):
        # Añadimos la posición a la lista de posiciones
        self.positions.append((msg.position.x, msg.position.y))

    # Función para actualizar el gráfico con las últimas posiciones recibidas
    def timer_callback(self):
        # Si la lista de posiciones no está vacía
        if self.positions:
            # Descomprimimos las posiciones en dos listas separadas
            x_positions, y_positions = zip(*self.positions)
            # Creamos el gráfico con las posiciones
            plt.plot(x_positions, y_positions)
            # Actualizamos la ventana de matplotlib
            plt.pause(0.01)

    # Función para guardar el gráfico en un archivo de imagen
    def save_plot(self):
        # Pedimos al usuario un nombre de archivo y una ubicación
        filename = asksaveasfilename(defaultextension='.png')
        # Guardamos el gráfico en el archivo seleccionado
        plt.savefig(filename)

# Función principal
def main(args=None):
    # Inicializamos ROS
    rclpy.init(args=args)
    # Creamos el nodo ROS
    node = TurtleBotInterface()

    # Definimos una función para guardar el gráfico y cerrar la ventana
    def on_close():
        node.save_plot()
        node.destroy_node()
        rclpy.shutdown()
        root.quit()
        root.destroy()

    # Creamos la ventana de tkinter para mostrar el gráfico
    root = Tk()
    # Definimos la función a llamar cuando el usuario cierra la ventana
    root.protocol("WM_DELETE_WINDOW", on_close)
    # Configuramos el tamaño de la ventana
    root.geometry("400x400")
    # Definimos el título de la ventana
    root.title("Turtlebot2 Position")
    # Creamos un objeto de lienzo para el gráfico de matplotlib
    canvas = plt.figure(figsize=(4, 4), dpi=100).canvas
    # Colocamos el lienzo en la ventana
    w = canvas(fill=BOTH, expand=True)
    w.pack ()
    # Creamos una barra de herramientas para el gráfico
    toolbar = NavigationToolbar2Tk(canvas, root)
    # Colocamos la barra de herramientas en la parte superior de la ventana
    toolbar.pack(side=TOP, fill=X)
    
    root.mainloop()

if __name__ == '__main__':
    main() 