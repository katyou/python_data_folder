void setup()
{
  pinMode(8, OUTPUT);
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
      delay(50);
      digitalWrite(8,LOW);
      Measure();
    }
    if (a == 'y')
    {
      digitalWrite(8,HIGH);
    }
  }
}

void Measure()
{
  float Vi;
  float Im;
  float v[50];
  float i[50];
  int x;
  for(x = 1; x <= 50; x++)
  {
    Vi = analogRead(A3);
    v[x] = Vi;
    Im = analogRead(A5);
    i[x] = Im;
    
    delay(400);
  }
  delay(5000);
  for(x = 1; x <= 50; x++)
  {
    Serial.print(v[x]);
    Serial.print(',');
    Serial.println(i[x]);
  }
}

