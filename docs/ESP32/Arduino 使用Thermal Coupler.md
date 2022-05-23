
## MX6675 模块

[MX6675规格书](http://datasheets.maximintegrated.com/en/ds/MAX6675.pdf)

**Features**



- Direct Digital Conversion of Type -K Thermocouple Output
- Cold-Junction Compensation
- Simple SPI-Compatible Serial Interface
- 12-Bit, 0.25°C Resolution
- Open Thermocouple Detection

[download the MAX6675 Arduino library code](http://github.com/adafruit/MAX6675-library) by going to the github page and clicking Download Source. Then uncompress the folder and rename it **MAX6675** and [install it into the library folder according to our handy tutorial](http://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries).

Restart the Arduino IDE and open up the **File** **->** **Examples->MAX6675/Adafruit_MAX31855 ** **->** **serialthermocouple** sketch and upload it to your Arduino. Once uploaded, open up the serial port monitor to display the current temperatures in both Celsius and Fahrenheit