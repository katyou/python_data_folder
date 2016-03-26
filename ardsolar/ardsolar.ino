int v;
int i;
int myStrings[300];
int yourStrings[300];
int x;

void setup()
{
  pinMode(8,OUTPUT);
  
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
      digitalWrite(8,LOW);
      Measure();
    }
    
    a == Serial.read();
    if (a == 'y')
    {
      digitalWrite(8,HIGH);
    }
  }
}

void Measure()
{
  for(x = 0; x <= 150; x++)
  {
    myStrings[x] = analogRead(A3);
    yourStrings[x] = analogRead(A4);
    delayMicroseconds(100);
  }
  
  for (x = 0; x <= 150; x++)
  {
    data();
  }
}

void data()
{
  Serial.print(myStrings[x]);
  Serial.print(",");
  Serial.println(yourStrings[x]);
}

