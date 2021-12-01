This article will introduce how to develop ESP-CAM board with Platform IO.

Create a new project, choose board **Al Thinker esp32cam**.

![](C:\Project\Website\docs\docs\esp32\images\2021-06-09-09-46-24-image.png)

## esp32cam introduction

esp32cam is developed by AI thinker, while ESP-EYE is developed by Espressif itself.

| **Microcontroller** | esp32cam |
| ------------------- | -------- |
| **Frequency**       | 240MHz   |
| **Flash**           | 4MB      |
| **RAM**             | 320KB    |

ESP32-CAM board is without a UART to serial converter, you need to buy one, and there is a coverter board. So suggest you to by this one.

![Picture 3 of 10](https://i.ebayimg.com/images/g/pwIAAOSwiItft8-q/s-l640.jpg)

## Streaming Video from ESP32-CAM

Get the code from https://github.com/espressif/arduino-esp32/tree/master/libraries/ESP32/examples/Camera/CameraWebServer

Copy CameraWebServer.ino content to main.c file, and create and copy other files containt to \src folder.

- Uncomment line #define CAMERA_MODEL_AI_THINKER // Has PSRAM

- Delete #if 0 in file main.c and app_httpd.cpp.

- Modify wifi name and password

build and upload project to ESP-CAM.

Run the code and open the serial monitor in your PlatformIO. Notice to press the Reset button to start the application

![ESP32-CAM running on PlatformIO. WebServerCam URL to stream video](https://www.survivingwithandroid.com/wp-content/uploads/2020/05/esp32-cam-running.png)

Now you can start streaming video from the ESP32-CAM. Open your browswer and copy the URL shown in the previous image:

![ESP32-CAM video streaming settings](https://www.survivingwithandroid.com/wp-content/uploads/2020/05/esp32-cam-ov2640-video-streaming-min-1024x536.png)

## image classification

- Initializing the ESP32-CAM

- Acquiring picture

- send picture to cloud machine learning platform

- get the feedback

```arduino
#include <base64.h>

void classifyImage() {
  
  // Capture picture
   camera_fb_t * fb = NULL;
   fb = esp_camera_fb_get(); //captures image
   
   if(!fb) {
    Serial.println("Camera capture failed");
    return;
   }

  size_t size = fb->len;
  String buffer = base64::encode((uint8_t *) fb->buf, fb->len); //encode in base64 the image
  
String payload = "{\"inputs\": [{ \"data\": {\"image\": {\"base64\": \"" + buffer + "\"}}}]}";

  buffer = "";
  // Uncomment this if you want to show the payload
  // Serial.println(payload);

  esp_camera_fb_return(fb);
  
  // Generic model
  String model_id = "aaa03c23b3724a16a56b629203edc62c";

  HTTPClient http;
  http.begin("https://api.clarifai.com/v2/models/" + model_id + "/outputs");
  http.addHeader("Content-Type", "application/json");     
  http.addHeader("Authorization", "Key your_key"); 
  int response_code = http.POST(payload);
}
```

### use tensorflow.js

https://www.survivingwithandroid.com/esp32-cam-tensorflow-js/
