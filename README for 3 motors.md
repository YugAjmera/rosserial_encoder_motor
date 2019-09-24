# rosserial_encoder_motor

Control three motors using rosserial with custom message.

### Things used :
* Arduino Mega
* motors with encoders x3
* L298N x2
* Power Source
* External computer ( with ROS Installed )

### Connections for individual motor :
1. M1 and M2 are Motor power wires. Connect them to 1st L298N output. 
* Motor 1 to OUT1 (red) , OUT2 (white).
* Motor 2 to OUT3 (red) , OUT4 (white).

Take another L293D :
* Motor 3 to OUT1 (red) , OUT2 (white).

2. L298N ENA to Pin 5 and ENB to Pin 10.
* IN1 to Pin 6
* IN2 to Pin 7
* IN3 to Pin 8
* IN4 to Pin 9

2nd L298N ENA to Pin 2.
* IN1 to Pin 3
* IN2 to Pin 4

Do not forget to make the ground common of Arduino and L298N.

### Running one motor
Copy Encoder Library to Arduino Libraries :
Open terminal :
```
cd ~/Arduino_Encoder_Motors
mv Encoder /home/user/Documents/arduino-1.8.7/libraries/
```

### Add ROS Serial 
In a new terminal :
```
git clone " add url here "
cd catkin_ws/
catkin_make
```

* Follow the installation steps : [here](http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup)
* If already installed then just type these :
```
rm -r ~/Arduino/libraries/ros_lib
rosrun rosserial_arduino make_libraries.py /home/yug/Arduino/libraries/
```
### Run the motors 
Upload the code "Run_3_motors" to Ardunio Mega.
```
roscore
rosrun rosserial_python serial_node.py /dev/ttyUSB0
python teleop_keyboard_omni3.py
```

