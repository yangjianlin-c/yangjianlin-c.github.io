## Kalman滤波

### 库

[SimpleKalmanFilter](https://github.com/denyssene/SimpleKalmanFilter)

```arduino
SimpleKalmanFilter kf = SimpleKalmanFilter(e_mea, e_est, q);

 while (1) {
  float x = analogRead(A0);
  float estimated_x = kf.updateEstimate(x);
  
  // ...
 } 
```

### 实例

```arduino
#include <SimpleKalmanFilter.h>

//the ADC pin of esp32
#define ADC_PIN 34
// update Serial Ploter every 100ms
#define UPDATE_TIME  100

long current;
//init Kalman with params, you can modify params to make better result
SimpleKalmanFilter kalman(2, 2, 0.01);

void setup() {
  Serial.begin(115200);
  Serial.print(0);  // To freeze the lower limit
  Serial.print(" ");
  Serial.print(3.3);  // To freeze the upper limit
  Serial.print(" ");
}

void loop() {
  //to make demo interesting we add random noise to measurement
  float rand_noise = random(-100,100)/100.0;
  
  // Reading LDR value, ADC of esp32 0-4095 according to 0-3.3V
  float measured_value = analogRead(ADC_PIN)/4095.0 * 3.3 + rand_noise;
  //Kalman update estimate
  float estimated_value = kalman.updateEstimate(measured_value);

  //update plotter
  if (millis() > current) {
    Serial.print(measured_value);
    Serial.print(",");
    Serial.print(estimated_value);
    Serial.println();
    
    current = millis() + UPDATE_TIME;
  }
}
```
