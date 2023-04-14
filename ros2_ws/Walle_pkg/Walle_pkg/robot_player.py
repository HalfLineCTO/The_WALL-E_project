import rclpy                   # Importa el módulo de Python 'rclpy', que proporciona la API de ROS2 para Python
from rclpy.node import Node    # Importa la clase 'Node' de 'rclpy.node'
from geometry_msgs.msg import Twist   # Importa el mensaje 'Twist' del paquete 'geometry_msgs'
import sys, select, tty, termios    # Importa algunos módulos de Python
from pynput import keyboard as kb

class WallePlayer(Node):    # Define una clase llamada 'Walleplayer' que hereda de la clase 'Node'
    def __init__(self):    # Define un método llamado '__init__' que se ejecutará cuando se cree una instancia de la clase
        super().__init__('robot_player')    # Llama al método '__init__' de la clase 'Node' y le da un nombre al nodo
        
        self.publisher_ = self.create_publisher(Twist, '', 10)    # Crea un publisher que enviará mensajes del tipo 'Twist' al tópico ''
        
        #self.timer_ = self.create_timer(0.1, self.timer_callback)    # Crea un temporizador que llamará al método 'timer_callback' cada 0.1 segundos
        
       # self.twist_msg_ = Twist()    # Crea un objeto del tipo 'Twist' que se utilizará para enviar las velocidades al robot
        
        print("Ingrese los parametros")
        self.linear_speed_  = float(input("Ingrese Velocidad Lineal: "))
        self.angular_speed_  = float(input("Ingrese Velocidad Angular: "))
    

    def on_press(self, key):    # Define un método llamado 'timer_callback' que se ejecutará cada vez que se llame el temporizador
       
        self.twist_msg_ = Twist() 
       

        self.publisher_.publish(self.twist_msg_)
    def on_release(self, key):    # Define un método llamado 'timer_callback' que se ejecutará cada vez que se llame el temporizador
       
        self.twist_msg_ = Twist()  #Define el tipo de mensaje publicado como twist



        self.publisher_.publish(self.twist_msg_) 


def main():
    rclpy.init()    # Inicializa ROS2
    teleop_turtlebot = TeleopTurtleBot()    # Crea una instancia de la clase 'TeleopTurtleBot'
    with kb.Listener(on_press= teleop_turtlebot.on_press,on_release = teleop_turtlebot.on_release) as escuchador:
        escuchador.join()
    rclpy.spin(teleop_turtlebot)    # Inicia el bucle de eventos de ROS2
    teleop_turtlebot.destroy_node()    # Destruye el nodo cuando se cierra el bucle de eventos
    rclpy.shutdown()    # Cierra ROS2

if __name__ == '__main__':
    main()    # Llama a la función 'main' si se ejecuta este archivo como un script

