void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(A0, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensor_value = analogRead(A0);
  float voltage = sensor_value * (5.0 / 1023.0);
  Serial.println(String(voltage) + "|20|20");
  delay(2);
}
