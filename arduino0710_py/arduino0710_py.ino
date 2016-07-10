void setup()
{
  pinMode(2, OUTPUT);
  Serial.begin(9600);
}


void loop()
{
  char a;
  if (Serial.available() > 0)
  {
    a = Serial.read();
    if (a == 'z')
    {
      delay(10);
      digitalWrite(2,LOW);
      Measure();
    }

    if (a == 'y')
    {
      digitalWrite(2,HIGH);

    }
  }
}

void Measure()
{
  float Vi;
  float Im;
  float v[50];
  float i[50];
  delay(10);
  int x;
  for(x = 1; x <= 50; x++)
  {
    Vi = analogRead(A3);
    v[x] = Vi;
    Im = analogRead(A4);
    i[x] = Im;
    delayMicroseconds(1000);

  }
  delay(5000);
  for(x = 1; x <= 50; x++)
  {
    Serial.print(v[x]);
    Serial.print(',');
    Serial.println(i[x]);
  }
}

