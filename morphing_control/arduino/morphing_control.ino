#include <Servo.h>
#define NUM_ACTUATORS 4
Servo actuators[NUM_ACTUATORS];
int actuatorPins[NUM_ACTUATORS] = {3, 5, 6, 9};

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < NUM_ACTUATORS; i++) {
    actuators[i].attach(actuatorPins[i]);
    actuators[i].write(90); // Neutral position
  }
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if (cmd.startsWith("MORPH:")) {
      int values[NUM_ACTUATORS];
      int idx = 0;
      int last = 6;
      for (int i = 0; i < NUM_ACTUATORS; i++) {
        int next = cmd.indexOf(',', last+1);
        if (next == -1) next = cmd.length();
        values[i] = cmd.substring(last+1, next).toInt();
        last = next;
      }
      for (int i = 0; i < NUM_ACTUATORS; i++) {
        actuators[i].write(constrain(values[i], 0, 180));
      }
      digitalWrite(LED_BUILTIN, HIGH);
      delay(100);
      digitalWrite(LED_BUILTIN, LOW);
    } else if (cmd == "RESET") {
      for (int i = 0; i < NUM_ACTUATORS; i++) actuators[i].write(90);
    }
  }
  delay(10);
} 