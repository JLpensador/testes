int valorPot = 0;

void setup()
{
  pinMode(0, INPUT);
  pinMode(1, INPUT);
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(8, INPUT);
}

void loop()
{
  valorPot = analogRead(A0);
  analogWrite(0, valorPot);
  analogWrite(1, valorPot / 3);
  analogWrite(2, valorPot / 6);

  if (digitalRead(8) == 1)
  {
    for (int led = 0; led < 4; led++)
    {
      digitalWrite(3, HIGH);
      delay(500);
      digitalWrite(3, LOW);
      delay(500);
      digitalWrite(5, HIGH);
      delay(500);
      digitalWrite(5, LOW);
      delay(500);
      for (int i = 0; i < 3; i++)
      {
        digitalWrite(4, HIGH);
        delay(500);
        digitalWrite(4, LOW);
        delay(500);
      }
      if (4 == LOW)
      {
        digitalWrite(3, HIGH);
        delay(500);
        digitalWrite(3, LOW);
        delay(500);
        digitalWrite(5, HIGH);
        delay(500);
        digitalWrite(5, LOW);
        delay(500);
        for (int i = 0; i < 3; i++)
        {
          digitalWrite(4, HIGH);
          delay(500);
          digitalWrite(4, LOW);
          delay(500);
        }
      }
    }
  }
}
