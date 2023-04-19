from setuptools import setup

package_name = 'robot_taller2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='juan',
    maintainer_email='je.cardona@uniandes.edu.co',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_interface = robot_taller2.robot_interface:main',
            'raspy_serial = robot_taller2.Raspy_serial:main',
            'robot_teleop = robot_taller2.robot_teleop:main',
            'robot_player = robot_taller2.robot_player:main'


        ],
    },
)
