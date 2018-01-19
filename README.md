# Sunlight_Sensor Build Instruction


## Table of Contents
1. [Introduction](#introduction)
2. [System Diagram](#system-diagram)
3. [Bill of Materials/Budget](#bill-of-materials/budget)
4. [Time Commitment](#time-commitment)
5. [Power up](#power-up)
6. [Unit Testing](#unit-testing)
7. [Production Testing](#production-testing)
8. [Reproducible?](#reproducible?)


### Introduction

For my Hardware Project I decided to build with the sunlight sensor. The sunlight sensor will measures sunlight and break the sunlight down into three components (Ultraviolet light, visible light (in Lumens) and infrared light (in Lumens). This will allow to monitor the sunlight intensity, IR intensity and UV intensity.


The sunlight sensor uses SI1145 which will measure the total visible light (in Lumens), infrared light (in Lumens) and UV light (UV index). This can be useful because with this sensor you can detect how much visible light and infrared light is emitted by the sunlight. With the value from uv light you can use the data to find out the UV index and know how much UV light is emitting from the sunlight.

### System Diagram

![Image of System Diagram](https://raw.githubusercontent.com/RaphaelNajera/Sunlight_Sensor/master/documentation/Sunlight%20project%20system%20diagram.png)


### Bill of Materials/Budget
The materials needed to build the sunlight sensor project is Raspberry Pi 3, Grove I2C Sunlight Sensor / UV / IR and Pi2Grover - Grove Connector Interface for the Raspberry Pi. The parts can be bought from amazon or from switchdoc labs. I bought my parts from amazon.

1) Raspberry Pi 3 (CanaKit Starter Kit):

* [Amazon](https://www.amazon.ca/CanaKit-Raspberry-Complete-Starter-Kit/dp/B01CCF6V3A/) CAD $99.99

2) Grove I2C Sunlight Sensor / UV / IR:
 
* [Amazon](https://www.amazon.ca/gp/product/B01MG08DPI/) CAD $21.64 
* [SwitchDoc Labs](https://shop.switchdoc.com/products/grove-sunlight-ir-uv-i2c-sensor) US $13.95

3) Pi2Grover - Grove Connector Interface for the Raspberry Pi:

* [Amazon](https://www.amazon.ca/Pi2Grover-Grove-Connector-Interface-Raspberry/dp/B01FPU4JTM/) CAD $31.17
* [SwitchDoc Labs](https://shop.switchdoc.com/products/pi2grover-raspberry-pi-to-grove-connector-interface-board) US $19.95

At the time when I bought the materials, the raspberry pie was $112.99, Sunlight sensor was $36.64 and Connector interface for the raspberry pi was $36.17, plus the shipping $15.41. The total cost for buying the materials was $201.21 



