void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(0, OUTPUT);
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
}

uint8_t sine_table[32][4] = {
  {1, 0, 0, 1}, {1, 0, 1, 0}, {1, 0, 1, 1}, {1, 1, 0, 0}, {1, 1, 0, 1}, {1, 1, 1, 0}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 0}, {1, 1, 0, 1}, {1, 1, 0, 0}, {1, 0, 1, 1}, 
  {1, 0, 0, 1}, {1, 0, 0, 0}, {0, 1, 1, 0}, {0, 1, 0, 1}, {0, 0, 1, 1}, {0, 0, 1, 0}, {0, 0, 0, 1}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 1}, {0, 0, 1, 0}, 
  {0, 0, 1, 1}, {0, 1, 0, 0}, {0, 1, 1, 0}, {1, 0, 0, 0}
};


void loop() {
  for (int i = 0; i < 32; i++){
    for (int j = 0; j < 4; j++){
      if (sine_table[i][j] == 1) {
        PORTB |= (1 << PB0);
      }
      else {
        PORTB &= ~(1 << PB0);
      }
      PORTB |= (1 << PB1);
      PORTB &= ~(1 << PB1);
    }
    PORTB |= (1 << PB2);
    PORTB &= ~(1 << PB2);
    delayMicroseconds(7.8125);
  }
}
