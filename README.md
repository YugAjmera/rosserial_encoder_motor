# rosserial_encoder_motor

Control two motors using rosserial with custom message.

### Things used :
* Arduino Uno
* motors with encoders
* L298N 
* Power Source
* External computer ( with ROS Installed )

### Connections for individual motor :
1. M1 and M2 are Motor power wires. Connect them to L298N output. 
* Motor 1 to OUT1 (red) , OUT2 (white).
* Motor 2 to OUT4 (red) , OUT3 (white).

2. GND and 3.3V wires are to power the encoder. Connect them to the Arduino.

3. C1 and C2 are channel wires for encoder outputs. 

* Motor 1 : C1 - Pin 2 , C2 - Pin 3
* Motor 2 : C1 - Pin 4, C2 - Pin 5

4. L298N ENA to Pin 5 and ENB to Pin 10.
* IN1 to Pin 6
* IN2 to Pin 7
* IN3 to Pin 8
* IN4 to Pin 9

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
Upload the code "Run" to Ardunio Uno.
```
roscore
rosrun rosserial_python serial_node.py /dev/ttyUSB0
rostopic pub /control_motor rosserial_encoder_motor/motor "direction: 70 speed: 250 name: 1" 
```

* Direction : 
 	* Forward : 70 
 	* Backward : 66
* Speed : 0 to 255
* Name : 1 or 2
