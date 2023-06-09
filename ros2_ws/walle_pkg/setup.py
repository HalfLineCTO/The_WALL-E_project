from setuptools import setup

package_name = 'walle_pkg'

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
            'turtle_bot_teleop = walle_pkg.turtle_bot_teleop:main'
            'connectionSerial = walle_pkg.connection_serial:main'
            'turtle_bot_interface = walle_pkg.walle_interface:main'
            
        ],
    },
)
