//Bord Name :- NodeMcu 1.0 (ESP-12E Module)
#include <ESP8266WiFi.h>

void setup() {
  
  Serial.begin(9600);
  WiFi.begin("Azad Sir Mess", "12345678");
  while(WiFi.status() != WL_CONNECTED){
    Serial.println("Connecting...!");
    delay(200);
  }// while End

  Serial.println();
  Serial.println("NodeMcu Connected!");
  Serial.print("Node Mcu IP Address : ");
  Serial.println(WiFi.localIP()); // Print Ip 
  
} // Void Setup End




void loop() {
  // put your main code here, to run repeatedly:

}
