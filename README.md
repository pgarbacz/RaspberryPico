# RapsberryPico
## DIY projects with Raspberry Pi Pico

### List of projects:
- Thermostat controler
- Intruder detection
- Pico Nerd Game
- Blinking LED

---
 Thermostat controler

Project Goal:

To design and implement a cost-effective and versatile thermostat system using a Raspberry Pi Pico microcontroller. The system will accurately monitor temperature using a PT100 sensor, control a heater via a relay module, and provide user interaction through an LCD display and a joystick/buttons for setting desired temperature and hysteresis.

System Overview:

Temperature Sensing:

A PT100 temperature sensor will be connected to a MAX31865 amplifier.
The MAX31865 will provide accurate and amplified temperature readings to the Pico.
The Pico will read temperature data from the MAX31865 via SPI communication.1   
Heater Control: A Pico Dual Channel Relay HAT will be used to control the heater.
The Pico will control the relay to switch the heater on/off based on temperature readings and user-defined settings.
User Interface:

A 1.3" IPS LCD display will provide real-time temperature readings, desired temperature, hysteresis value, and system status.
A joystick and buttons will allow users to: 
Adjust the desired temperature.
Set the hysteresis (temperature difference between on/off thresholds).
View system settings and status.
Data Processing and Control Logic:
The Pico will implement the control logic:
Compare the current temperature to the desired temperature and hysteresis settings.
Activate the relay to turn the heater ON when the temperature falls below the lower threshold.
Deactivate the relay to turn the heater OFF when the temperature rises above the upper threshold.
Implement safety features such as over-temperature alarms.

 Parts list:

 - PT100 amplifiler MAX31865 EAN: 5904422375911
 - P100 Sensor EAN: 5904422306977
 - Pico Dual Channel Relay HAT  EAN: 5055652921284
 - Pico Dual Expander Waveshare 19343 EAN: 5904422371685
 - Display LCD IPS 1,3'' 240x240px - SPI - 65K RGB - Waveshare 19650 EAN: 5904422371883
---
Intruder Detection

 Simple application for detecting objects/intruders with use of PIR sensor.
 The code can be tested on WOKWI https://wokwi.com/projects/419243512269148161

 Connection Diagram: 
 ---
 ![schema](img/intruder_detect_schema.png)
 ---
Pico Nerd Game

 The code can be tested on WOKWI https://wokwi.com/projects/418430503854160897

 Connection Diagram: 
 ---
 ![schema](img/nerd_game_schema.png)
 ---
 Simple game for testing user knowledge regarding binary representation of numbers.
 In each turn a number (in range up to 255) is randomly selected and printed on the LCD screen. 
 The user task is to switch on LED's that corresponds to high bit values of the current number.

 Note: libraries for LCD controll source: https://www.circuitschools.com/interfacing-16x2-lcd-module-with-raspberry-pi-pico-with-and-without-i2c/ 

---
Blinkin LED
The code can be tested on WOKWI https://wokwi.com/projects/418355273497277441
