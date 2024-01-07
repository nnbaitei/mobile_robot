#define LED PC13
#define Tx PA2
#define Rx PA3
#define ModePin PA15  

void setup()
{
  Serial.begin(9600);
  Serial2.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(ModePin, INPUT);
}

void loop()
{

  int mode = digitalRead(ModePin);

  // read
   if (mode == 0 && Serial2.available() > 0)
  {
    String incomingString = Serial2.readStringUntil(';');
    Serial.println("Received: " + incomingString);
  } 

  // send
  else if (mode == 1)
  {
    Serial.println("send mode");
    Serial2.println("Hello from STM32");
    digitalWrite(LED, HIGH);
    delay(1000);
    digitalWrite(LED, LOW);
  }

  else if (mode==9)
  {
    exit(0);
  }
}