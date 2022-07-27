
const int ADPin = 34;
void setup() {
  Serial.begin(115200);
}

void loop() {
  long t0;
  t0 = micros();
  int sensorValue = analogRead(ADPin);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  //float voltage = sensorValue * (3.3 / 4096.0);
  Serial.print(t0);
  Serial.print(";");
  Serial.println(sensorValue);
  
}
