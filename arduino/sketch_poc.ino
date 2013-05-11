#define pirPin 7

int photoresValue;
int pirValue;
char separator[] = ";";

void setup() {
  Serial.begin(9600);
  pinMode(pirPin, INPUT);
  delay(3000);
}

void loop() {
  photoresValue = analogRead(A0);
  pirValue = digitalRead(pirPin);
  Serial.print(photoresValue);
  Serial.print(separator);
  Serial.println(pirValue);
  delay(200);
}
