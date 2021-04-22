String incomming_byte ;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available()){
    incomming_byte = Serial.readStringUntil('\n') ;
    if (incomming_byte =="on"){
        digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
        Serial.write("Led On") ;
      }
    else if  (incomming_byte =="off"){
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  Serial.write("Led off") ;

      } 
    }
                      
}
