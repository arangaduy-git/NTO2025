void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensor_value = analogRead(A0);
  int sensor_value1 = analogRead(A1);
  int sensor_value2 = analogRead(A2);
  float voltage = sensor_value * (5.0 / 1023.0);
  float voltage1 = sensor_value1 * (5.0 / 1023.0);
  float voltage2 = sensor_value2 * (5.0 / 1023.0);
  Serial.println(String(voltage) + "|" + String(voltage1) + "|" + String(voltage2));
  delay(2);
}
