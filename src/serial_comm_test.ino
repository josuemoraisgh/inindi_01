<<<<<<< HEAD
#include <Arduino.h>

void setup()
{
  Serial.begin(115200);
  // Print log
  Serial.println("setup");
}

float i = 0;
void loop()
{
  i += 0.1;

  // Print log
  Serial.print("casa");
  Serial.println(i);

  // Plot a sinus
  Serial.print(">sin:");
  Serial.println(sin(i));

  // Plot a cosinus
  Serial.print(">Sum:");
  Serial.println(0.8*sin(i)+0.2*cos(i));

  delay(50);
}
=======
#include <Arduino.h>

void setup()
{
  Serial.begin(115200);
  // Print log
  Serial.println("setup");
}

float i = 0;
void loop()
{
  i += 0.1;

  // Print log
  Serial.print("casa");
  Serial.println(i);

  // Plot a sinus
  Serial.print(">sin:");
  Serial.println(sin(i));

  // Plot a cosinus
  Serial.print(">Sum:");
  Serial.println(sin(i)+cos(i));

  delay(50);
}
>>>>>>> 0d43539a8abd1a10aaa09c064baf6a1a280091bd
