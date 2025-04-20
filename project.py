
import RPi.GPIO as GPIO
import time
from time import sleep 
import numpy as np
import serial
import cv2
import sys
import datetime

import imutils
import picamera

import ssar_tsd

camera = picamera.PiCamera() 
camera.resolution = (1028, 720)

predictions = []

current_frame = None

time.sleep(1)

detector = ssar_tsd.TrafficSignDetector()

# Define GPIO to LCD mapping
LCD_RS = 11
LCD_E  = 9
LCD_D4 = 10
#LCD_D5 = 24
#LCD_D6 = 23
#LCD_D7 = 18
LCD_D5 = 22
LCD_D6 = 27
LCD_D7 = 17

buz = 21


print("Init DONE...")

GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7

GPIO.setup(buz, GPIO.OUT) # DB7


def main():
    # Main program block

    # Initialise display

    global ch
    global i
    global key
    lcd_init()

    lcd_string("  Raspberry Pi",LCD_LINE_1)
    lcd_string("Traffic Sign Dete",LCD_LINE_2)
    time.sleep(1) # 700 milli second delay

    GPIO.output(buz, True) # LED
    time.sleep(0.7) # 700 milli second delay
    GPIO.output(buz, False) # LED
    time.sleep(0.7) # 700 milli second delay  
    GPIO.output(buz, True) # LED
    time.sleep(0.7) # 700 milli second delay
    GPIO.output(buz, False) # LED

    while True:
    
        lcd_string("Monitoring",LCD_LINE_1)
        
        camera.capture('image.jpg')
        time.sleep(0.1)
        img=cv2.imread("image.jpg") #Read img from user (captured from raspberry)
        cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        predictions = detector.predict(cur_frame)
        print(predictions)
          
        lcd_byte(0x01, LCD_CMD)   
        GPIO.output(buz, False) # LED
        for i in predictions:
            if i == 5:                
                print("Traffic Sign 80 ")  
                lcd_byte(0x01, LCD_CMD)              
                lcd_string("S Limit:80KM/H",LCD_LINE_2)
                GPIO.output(buz, True) # LED
            if i == 6 or i == 7:                
                print("Traffic Sign 100 ")    
                lcd_byte(0x01, LCD_CMD)                 
                lcd_string("S Limit:100KM/H",LCD_LINE_2)
                GPIO.output(buz, True) # LED
            if i == 3:                
                print("Traffic Sign 60 ")    
                lcd_byte(0x01, LCD_CMD)                 
                lcd_string("S Limit:60KM/H",LCD_LINE_2)
                GPIO.output(buz, True) # LED
            if i == 2:                
                print("Traffic Sign 50 ")     
                lcd_byte(0x01, LCD_CMD)                
                lcd_string("S Limit:50KM/H",LCD_LINE_2)
                GPIO.output(buz, True) # LED
        
 
if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Please Restart...",LCD_LINE_1)
    GPIO.cleanup()
      
      
        