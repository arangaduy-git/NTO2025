void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i <= 5; i++){
    String myString = String(i) + "|" + String(5 - i) + "|" + String(5 - i);
    Serial.println(myString);
    delay(50);
  }
}
