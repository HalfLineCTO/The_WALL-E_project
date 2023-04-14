
import rclpy                   # Importa el módulo de Python 'rclpy', que proporciona la API de ROS2 para Python
from rclpy.node import Node    # Importa la clase 'Node' de 'rclpy.node'
from geometry_msgs.msg import Twist   # Importa el mensaje 'Twist' del paquete 'geometry_msgs'
import sys, select, tty, termios    # Importa algunos módulos de Python
from pynput import keyboard as kb
from time import time as tm


class TeleopTurtleBot(Node):    # Define una clase llamada 'TeleopTurtleBot' que hereda de la clase 'Node'
    def __init__(self):    # Define un método llamado '__init__' que se ejecutará cuando se cree una instancia de la clase
        super().__init__('turtle_bot_teleop')    # Llama al método '__init__' de la clase 'Node' y le da un nombre al nodo
        
        self.publisher_ = self.create_publisher(Twist, 'turtlebot_cmdVel', 10)    # Crea un publicador que enviará mensajes del tipo 'Twist' al tópico '/turtlebot_cmdVel'
        
        #self.timer_ = self.create_timer(0.1, self.timer_callback)    # Crea un temporizador que llamará al método 'timer_callback' cada 0.1 segundos
        
       # self.twist_msg_ = Twist()    # Crea un objeto del tipo 'Twist' que se utilizará para enviar las velocidades al robot
        
        print("Ingrese los parametros")
        self.linear_speed_  = float(input("Ingrese Velocidad Lineal: "))
        self.angular_speed_  = float(input("Ingrese Velocidad Angular: "))
    

    def on_press(self, key):    # Define un método llamado 'timer_callback' que se ejecutará cada vez que se llame el temporizador
       
        self.twist_msg_ = Twist() 
       
        #if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:    # Verifica si hay una entrada disponible en la entrada estándar (stdin)
            #key = sys.stdin.read(1)    # Lee una tecla de la entrada estándar
        if key == kb.KeyCode.from_char('w'):    # Si la tecla es 'w', establece la velocidad lineal positiva
                self.twist_msg_.linear.x = self.linear_speed_
                resp = print('Estas pulsando la tecla w')
        elif key == kb.KeyCode.from_char('s'):    # Si la tecla es 's', establece la velocidad lineal negativa
                self.twist_msg_.linear.x = -self.linear_speed_
                resp =  print('Estas pulsando la tecla s')
        elif key == kb.KeyCode.from_char('a'):    # Si la tecla es 'a', establece la velocidad angular positiva
                self.twist_msg_.angular.z = self.angular_speed_
                resp =  print('Estas pulsando la tecla a')
        elif key == kb.KeyCode.from_char('d'):    # Si la tecla es 'd', establece la velocidad angular negativa
                self.twist_msg_.angular.z = -self.angular_speed_
                resp = print('Estas pulsando la tecla d')
        else:    # Si no se presionó ninguna de las teclas anteriores, establece ambas velocidades en cero
                self.twist_msg_.linear.x = 0.0
                self.twist_msg_.angular.z = 0.0
        #else:    # Si no hay entrada disponible en la entrada estándar, establece ambas velocidades en cero
            #self.twist_msg_.linear.x = 0.0
            #self.twist_msg_.angular.z = 0.0

        self.publisher_.publish(self.twist_msg_)
    def on_release(self, key):    # Define un método llamado 'timer_callback' que se ejecutará cada vez que se llame el temporizador
       
        self.twist_msg_ = Twist()  #Define el tipo de mensaje publicado como twist
       
        #if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:    # Verifica si hay una entrada disponible en la entrada estándar (stdin)
            #key = sys.stdin.read(1)    # Lee una tecla de la entrada estándar
        if key == kb.KeyCode.from_char('w'):    # Si la tecla es 'w', establece la velocidad lineal positiva
                self.twist_msg_.linear.x = 0.0
                resp = print('Dejaste de pulsar la tecla w')
        elif key == kb.KeyCode.from_char('s'):    # Si la tecla es 's', establece la velocidad lineal negativa
                self.twist_msg_.linear.x = -0.0
                resp =  print('Dejaste de pulsar la tecla s')
        elif key == kb.KeyCode.from_char('a'):    # Si la tecla es 'a', establece la velocidad angular positiva
                self.twist_msg_.angular.z = 0.0
                resp =  print('Dejaste de pulsar la tecla a')
        elif key == kb.KeyCode.from_char('d'):    # Si la tecla es 'd', establece la velocidad angular negativa
                self.twist_msg_.angular.z = -0.0
                resp = print('Dejaste de pulsar la tecla d')
        else:    # Si no se presionó ninguna de las teclas anteriores, establece ambas velocidades en cero
                self.twist_msg_.linear.x = 0.0
                self.twist_msg_.angular.z = 0.0
        #else:    # Si no hay entrada disponible en la entrada estándar, establece ambas velocidades en cero
            #self.twist_msg_.linear.x = 0.0
            #self.twist_msg_.angular.z = 0.0

        self.publisher_.publish(self.twist_msg_)  


def main():
    rclpy.init()    # Inicializa ROS2
    teleop_turtlebot = TeleopTurtleBot()    # Crea una instancia de la clase 'TeleopTurtleBot'
   # with kb.Listener(on_press= teleop_turtlebot.on_press,on_release = teleop_turtlebot.on_release) as escuchador:
        #escuchador.join()
        
    mensaje=Twist()
    mensaje.linear.x=1
    mensaje.angular.z=1

    while True:

                teleop_turtlebot.publisher_.publish(mensaje.linear.x, mensaje.angular.z)
                tm.sleep(0.5)
                print('Publicando')

    rclpy.spin(teleop_turtlebot)    # Inicia el bucle de eventos de ROS2
    teleop_turtlebot.destroy_node()    # Destruye el nodo cuando se cierra el bucle de eventos
    rclpy.shutdown()    # Cierra ROS2

if __name__ == '__main__':
    main()    # Llama a la función 'main' si se ejecuta este archivo como un script

