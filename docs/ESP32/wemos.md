+++
description = "WeMos开发板的使用"
title = "WeMos开发板的使用"
+++


## WeMos D1 Drivers & Software Environment

Install the latest [Ch340G drivers](http://www.wemos.cc/wiki/doku.php?id=en:ch340g) if you’re on Windows or Mac. Both platform’s drivers are available on that link. If you’re running Linux, you’re in luck – no drivers required.

I’m going to presume you already have at least v 1.6.5 of the Arduino developer environment set up on your PC – if not, visit the [Arduino Software](https://www.arduino.cc/en/Main/Software) page, download, install, then come back here. Once you’re ready, start Arduino and:

1. Select **File**, then **Preferences**
2. In the **Additional Boards Manager URLs** text box, enter `http://arduino.esp8266.com/stable/package_esp8266com_index.json` and hit OK
3. Select **Tools**, mouse over your currently selected board, and choose **Boards Manager** from the popup menu

[![Board Manager](https://i1.wp.com/www.beerandchips.net/wp-content/uploads/2016/01/2016-01-23-board-manager-1.jpg?resize=656%2C656)](https://i1.wp.com/www.beerandchips.net/wp-content/uploads/2016/01/2016-01-23-board-manager-1.jpg)

4. In the Boards Manager window that appears, enter ESP in the *Filter your search…* box, click on the **esp8266 by ESP8266 Community** entry that appears, and then select **Install**

[![2ESP8266 Arduino plugin](https://i0.wp.com/www.beerandchips.net/wp-content/uploads/2016/01/2016-01-23-board-manager-2.jpg?resize=660%2C372)](https://i0.wp.com/www.beerandchips.net/wp-content/uploads/2016/01/2016-01-23-board-manager-2.jpg)

5. Wait for a while, while the Board Definitions and Tools are downloaded – and note, you can use this same download to support a whole heap of other boards, including the WeMos D1 mini, the Adafruit HUZZAH ESP8266, and the NodeMCU ESP-12E dev board that I’m so, so fond of.
6. Once complete, select **Tools** again, and choose the WeMos D1 from the **Boards** dropdown.

Voila, you’re all set! Well, you might like to get some sample code to play with of course. Here’s how you can do that:

1. Download the Samples zip file from [GitHub](https://github.com/wemos/D1_mini_Examples/archive/master.zip)

2. Open the zip file, and move the D1_mini_Examples-master to your default Sketch directory (if you’re not sure where that is, open **File / Preferences** and it’ll tell you there)

3. Rename the D1_mini_Examples-master folder to D1_mini_Examples

4. Restart the Arduino IDE

5. You’ll find all the example code under **File / Examples** under the Examples from Custom Libraries section

Try some of the <b>HelloServer</b> sketch example – load it, enter your SSID name and password in place of the dots here:

const char* ssid = "........";
const char* password = "........";

then verify and upload it. Open your serial monitor to see the IP address that your board has been assigned, and connect to it with your web browser.

## WeMos D1 Documentation

You’ll absolutely want to review the [ESP8266 Arduino Core](http://arduino.esp8266.com/versions/1.6.5-947-g39819f0/doc/reference.html) documentation, a great resource covering Digital and Analog IO, timing and delays, the Serial object, use of WiFi, some ESP8266 specific APIs, and much more. Thre are many differences here if you’re coming from a NodeMCU Lua-based background, somewhat more familiar ground if your coming at this with Arduino experience, but either way a must-read. Other libraries include servo support (up to 24 supported on any available output pin), DNS, SPI, SSDP, and I2C. Plenty to keep you busy.

There’s a useful section linking on to other APIs not included in the standard setup – some particularly interesting examples include [Blynk](http://arduino.esp8266.com/versions/1.6.5-947-g39819f0/doc/reference.html), the widget-based gui builder with Android support that let’s you control devices over the Internet, and Adafruit’s [NeoPixel](http://arduino.esp8266.com/versions/1.6.5-947-g39819f0/doc/reference.html) library.