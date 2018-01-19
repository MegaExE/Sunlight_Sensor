# Sunlight_Sensor Build Instruction


## Table of Contents
1. [Introduction](#introduction)
2. [System Diagram](#system-diagram)
3. [Bill of Materials/Budget](#bill-of-materialsbudget)
4. [Time Commitment](#time-commitment)
5. [Mechanical Assembly](#mechanical-assembly)
6. [Power up](#power-up)
7. [Unit Testing](#unit-testing)
8. [Production Testing](#production-testing)
9. [Reproducible?](#reproducible?)


### Introduction

For my Hardware Project I decided to build with the sunlight sensor. The sunlight sensor will measures sunlight and break the sunlight down into three components (Ultraviolet light, visible light (in Lumens) and infrared light (in Lumens). This will allow to monitor the sunlight intensity, IR intensity and UV intensity.


The sunlight sensor uses SI1145 which will measure the total visible light (in Lumens), infrared light (in Lumens) and UV light (UV index). This can be useful because with this sensor you can detect how much visible light and infrared light is emitted by the sunlight. With the value from uv light you can use the data to find out the UV index and know how much UV light is emitting from the sunlight.

### System Diagram

![Image of System Diagram](https://raw.githubusercontent.com/RaphaelNajera/Sunlight_Sensor/master/documentation/Sunlight%20project%20system%20diagram.png)


### Bill of Materials/Budget
The materials needed to build the sunlight sensor project is Raspberry Pi 3, Grove I2C Sunlight Sensor / UV / IR and Pi2Grover - Grove Connector Interface for the Raspberry Pi. The parts can be bought from amazon or switchdoc labs. I bought my parts from amazon.

1) Raspberry Pi 3 (CanaKit Starter Kit):

* [Amazon](https://www.amazon.ca/CanaKit-Raspberry-Complete-Starter-Kit/dp/B01CCF6V3A/) CAD $99.99

2) Grove I2C Sunlight Sensor / UV / IR:
 
* [Amazon](https://www.amazon.ca/gp/product/B01MG08DPI/) CAD $21.64 
* [SwitchDoc Labs](https://shop.switchdoc.com/products/grove-sunlight-ir-uv-i2c-sensor) US $13.95

3) Pi2Grover - Grove Connector Interface for the Raspberry Pi:

* [Amazon](https://www.amazon.ca/Pi2Grover-Grove-Connector-Interface-Raspberry/dp/B01FPU4JTM/) CAD $31.17
* [SwitchDoc Labs](https://shop.switchdoc.com/products/pi2grover-raspberry-pi-to-grove-connector-interface-board) US $19.95

At the time when I bought the materials, the raspberry pie was $112.99, Sunlight sensor was $36.64 and Connector interface for the raspberry pi was $36.17, plus the shipping $15.41. The total cost for buying the materials was $201.21.

### Time Commitment
This project can be completed in a couple of days if you followed the mechanical assembly and the diagram. From my experience it took me 1 to 2 weeks to complete the build. I first had to order the materials which will take around a week to arrive. Once you receive the materials, I set up the raspberry pi which took around 3 hours. Connection the parts to the raspberry pi took around 30-60 minutes. And then setting up the code on the raspberry pi and testing the code took around a 1 hour.

Overall, I think the needed time to complete this build should be around 3 hours daily for 2-3 days.

### Mechanical Assembly

1) First, power of the Raspberry Pi
2) Next, will be connecting the connector interface to the Raspberry pi 3. While holding the connector interface, align the pins on the Raspberry Pi 3 GPIO header and carefully push down the connector interface board on to the Raspberry Pi 3 board.
3) Then, plug in a Grove Cable that comes with the Grove Sunlight sensor to the sunlight sensor and plug the other end of the cable to any of the I2C plugs on the connector interface. 
4) Once everything is connected, you can power up the Raspberry Pi. If you see a blue LED on the connector interface it shows that the connector interface is connected.


Below is the outcome after you connect the parts to the raspberry pi.

![Sunlight finish build](https://raw.githubusercontent.com/RaphaelNajera/Sunlight_Sensor/master/documentation/Sunlight%20finish%20build.jpg)

### Soldering


### Power Up
Before power up the Raspberry pi, check the micro SD card has the contents of NOOBS operation system installer which contains Raspbian. If not, you can download, unzip and copy the folder contents of [NOOBS](https://downloads.raspberrypi.org/NOOBS_latest) into the root directory of the micro SD card.
On the first boot you will be prompted to install the operating system and configure the wifi setting. Once the raspberry pi done installing the operating system. The first thing is to enable I2C because by default it is not enable. I2C bus allows the devices like the sunlight sensor to be connected and detected on to the Raspberry Pi.
To enable I2C: from the Start Menu -> Preferences -> Raspberry Pi configuration -> Interface set I2C to Enabled. 

Next on the terminal type the following command to check that you have i2c-tools utility installed.
```
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools
```







