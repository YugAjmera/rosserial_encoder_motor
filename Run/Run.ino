
#include <ros.h>
#include <rosserial_encoder_motor/motor.h>

ros::NodeHandle  nh;

void messageCb( const rosserial_encoder_motor::motor& msg){
  if(msg.name==1){          // run motor 1
    analogWrite(5,msg.speed);
    if(msg.direction =='F'){  // ASCII 70
      digitalWrite(6,LOW); 
      digitalWrite(7,HIGH); 
    }
    if(msg.direction =='B'){  // ASCII 66
      digitalWrite(6,HIGH); 
      digitalWrite(7,LOW); 
    }
  }

  if(msg.name==2){          // run motor 1
    analogWrite(10,msg.speed);
    if(msg.direction =='F'){  // ASCII 70
      digitalWrite(8,LOW); 
      digitalWrite(9,HIGH); 
    }
    if(msg.direction =='B'){  // ASCII 66
      digitalWrite(8,HIGH); 
      digitalWrite(9,LOW); 
    }
  }
}

ros::Subscriber<rosserial_encoder_motor::motor> sub("control_motor", &messageCb );

void setup()
{ 
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
