# ESP32 AD输入

- 0~3.3V
- 12bit



https://randomnerdtutorials.com/esp32-adc-analog-read-arduino-ide/

```c
// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6) 
const int potPin = 34;

// variable for storing the potentiometer value
int potValue = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);
}

void loop() {
  // Reading potentiometer value
  potValue = analogRead(potPin);
  Serial.println(potValue);
  delay(500);
}
```





### Fast sampling from analog input

The first part of the [OScope project](http://yaab-arduino.blogspot.com/p/oscope.html) is to implement the Arduino sketch to read the input values from an analog pin. In this article will describe how to achieve a reliable sampling of analog signals up to 615 KHz using some advanced techniques.

Arduino provides an convenient way to read analog input this using the *analogRead()* function. Without going into much details the *analogRead()* function takes 100 microseconds leading to a theoretical sampling rate of 9600 Hz. You can read more about this topic [here](http://forum.arduino.cc/index.php/topic,6549.0.html).

The following piece of code takes 1000 samples using the *analogRead()* calculates some statistics.



```c
void setup()
{
  Serial.begin(115200);
  pinMode(A0, INPUT);
}

void loop()
{
  long t0, t;

  t0 = micros();
  for(int i=0; i<1000; i++) {
    analogRead(A0);
  }
  t = micros()-t0;  // calculate elapsed time

  Serial.print("Time per sample: ");
  Serial.println((float)t/1000);
  Serial.print("Frequency: ");
  Serial.println((float)1000*1000000/t);
  Serial.println();
  delay(2000);
}
```




This code gives 112us per sample for a **8928 Hz sampling rate**.

So how can we increase sampling rate?



### Speedup the analogRead() function


We now need a little more details. The ADC clock is 16 MHz divided by a 'prescale factor'. The **prescale is set by default to 128** which leads to 16MHz/128 = 125 KHz ADC clock. Since a conversion takes 13 ADC clocks, the **default sample rate is about 9600 Hz** (125KHz/13).
Adding few lines of code in the setup() function we can **set an ADC prescale to 16** to have a clock of 1 MHz and a **sample rate of 76.8KHz**.



```
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))

void setup()
{
  sbi(ADCSRA, ADPS2);
  cbi(ADCSRA, ADPS1);
  cbi(ADCSRA, ADPS0);
  ...
```




The real frequency measured with the test program is 17us per sample for a **58.6 KHz sampling rate**.

The following table shows prescale values with registers values and theoretical sample rates. Note that prescale values below 16 are not recommended because the ADC clock is rated.



| **Prescale** | **ADPS2 ADPS1 ADPS0** | **Clock freq (MHz)** | **Sampling rate (KHz)** |
| ------------ | --------------------- | -------------------- | ----------------------- |
| 2            | 0 0 1                 | 8                    | 615                     |
| 4            | 0 1 0                 | 4                    | 307                     |
| 8            | 0 1 1                 | 2                    | 153                     |
| 16           | 1 0 0                 | 1                    | 76.8                    |
| 32           | 1 0 1                 | 0.5                  | 38.4                    |
| 64           | 1 1 0                 | 0.25                 | 19.2                    |
| 128          | 1 1 1                 | 0.125                | 9.6                     |





### Interrupts


A better strategy is to avoid calling the *analogRead()* function and use the 'ADC Free Running mode'. This is a mode in which the ADC continuously converts the input and throws an interrupt at the end of each conversion. This approach has two major advantages:

1. Do not waste time waiting for the next sample allowing to execute additional logic in the loop function.
2. Improve accuracy of sampling reducing jitter.

In this new test program I set the prescale to 16 as the example above getting a **76.8 KHz sampling rate**.



```
int numSamples=0;
long t, t0;

void setup()
{
  Serial.begin(115200);

  ADCSRA = 0;             // clear ADCSRA register
  ADCSRB = 0;             // clear ADCSRB register
  ADMUX |= (0 & 0x07);    // set A0 analog input pin
  ADMUX |= (1 << REFS0);  // set reference voltage
  ADMUX |= (1 << ADLAR);  // left align ADC value to 8 bits from ADCH register

  // sampling rate is [ADC clock] / [prescaler] / [conversion clock cycles]
  // for Arduino Uno ADC clock is 16 MHz and a conversion takes 13 clock cycles
  //ADCSRA |= (1 << ADPS2) | (1 << ADPS0);    // 32 prescaler for 38.5 KHz
  ADCSRA |= (1 << ADPS2);                     // 16 prescaler for 76.9 KHz
  //ADCSRA |= (1 << ADPS1) | (1 << ADPS0);    // 8 prescaler for 153.8 KHz

  ADCSRA |= (1 << ADATE); // enable auto trigger
  ADCSRA |= (1 << ADIE);  // enable interrupts when measurement complete
  ADCSRA |= (1 << ADEN);  // enable ADC
  ADCSRA |= (1 << ADSC);  // start ADC measurements
}

ISR(ADC_vect)
{
  byte x = ADCH;  // read 8 bit value from ADC
  numSamples++;
}
  
void loop()
{
  if (numSamples>=1000)
  {
    t = micros()-t0;  // calculate elapsed time

    Serial.print("Sampling frequency: ");
    Serial.print((float)1000000/t);
    Serial.println(" KHz");
    delay(2000);
    
    // restart
    t0 = micros();
    numSamples=0;
  }
}
```





If you want to learn more on ADC Free Running mode and tweaking ADC register you can look at the following pages.

[‎AVR Guide - Analog Inputs](https://sites.google.com/site/qeewiki/books/avr-guide/analog-input)
[Instructables - Girino - Fast Arduino Oscilloscope](http://www.instructables.com/id/Girino-Fast-Arduino-Oscilloscope/?ALLSTEPS)
[Instructables - Arduino Audio Input](http://www.instructables.com/id/Arduino-Audio-Input/?ALLSTEPS)
[Arduino Forum - Faster Analog Read](http://forum.arduino.cc/index.php/topic,6549.0.html)