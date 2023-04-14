import tkinter as tk
from tkinter import filedialog
import rospy
from geometry_msgs.msg import Twist

class TurtleBotInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Turtlebot Interface")

        # Crea los elementos de la interfaz 
        self.save_path_entry = tk.Entry(self.root)
        self.save_path_entry.insert(tk.END, "Enter file name...")
        self.save_path_entry.pack()

        self.save_button = tk.Button(self.root, text="Save", command=self.save_path)
        self.save_button.pack()

        self.save_checkbox = tk.Checkbutton(self.root, text="Save robot's path", variable=self.save_var)
        self.save_checkbox.pack()

        # Inicializan variables
        self.save_var = tk.BooleanVar(value=False)
        self.save_path = None

    def save_path(self):
        self.save_path = filedialog.asksaveasfilename(defaultextension=".txt")

    def run(self):
        self.root.mainloop()

    def is_save_enabled(self):
        return self.save_var.get()

    def get_save_path(self):
        return self.save_path
    


class TurtleBotTeleop:
    def __init__(self, linear_speed=0.2, angular_speed=0.5):
        self.linear_speed = linear_speed
        self.angular_speed = angular_speed
        self.cmd_vel_pub = rospy.Publisher("/turtlebot_cmdVel", Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.interface = TurtleBotInterface()

    def run(self):
        while not rospy.is_shutdown():
            vel = Twist()

            # Get user input
            key = self.interface.get_key()
            if key == "w":
                vel.linear.x = self.linear_speed
            elif key == "s":
                vel.linear.x = -self.linear_speed
            elif key == "a":
                vel.angular.z = self.angular_speed
            elif key == "d":
                vel.angular.z = -self.angular_speed

            # Publish velocity command
            self.cmd_vel_pub.publish(vel)

            # Write actions to file
            if self.interface.is_save_enabled():
                with open(self.interface.get_save_path(), "a") as f:
                    f.write(key + "\n")

            self.rate.sleep()