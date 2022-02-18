int led = 13;
int IR = A0;
int IrState = 0;


void setup() {
  pinMode(led, OUTPUT);
  pinMode(IR, INPUT);
  Serial.begin(9600);

}

void loop() {
  IrState = analogRead(IR);
  Serial.println(IrState);

  if(IrState < 200)
    digitalWrite(led, HIGH);
  
  
  else
    digitalWrite(led, LOW);
  

}
