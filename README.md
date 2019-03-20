# rosserial_encoder_motor


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

`cd ~/Arduino_Encoder_Motors`
`mv Encoder /home/user/Documents/arduino-1.8.7/libraries/`

Open sketch and upload. Open terminal and check out the encoder readings.

### Add ROS Serial 
Follow the installation steps : [http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup]

