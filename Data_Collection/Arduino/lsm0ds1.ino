/*
  Arduino LSM9DS1 - Simple Accelerometer
  This example reads the acceleration values from the LSM9DS1
  sensor and continuously prints them to the Serial Monitor
  or Serial Plotter.
  The circuit:
  - Arduino Nano 33 BLE Sense
  created 10 Jul 2019
  by Riccardo Rizzo
  This example code is in the public domain.
*/
#include <Arduino_LSM9DS1.h>

void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  Serial.println();
  Serial.println("Acceleration in g's");
  Serial.println("X\tY\tZ");
}

void loop() {
  float x, y, z;
  // float gx, gy, gz;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);
    // IMU.readMagneticField(gx, gy, gz);
    // IMU.readGyroscope(gx, gy, gz);
    // if (isnan(x) || isnan(y) || isnan(z)){
    //   Serial.print(0);
    //   Serial.print("/");
    //   Serial.print(0);
    //   Serial.print("/");
    //   Serial.print(0);
    //   // Serial.print("/");
    //   // Serial.print(0);
    //   // Serial.print("/");
    //   // Serial.print(0);
    //   // Serial.print("/");
    //   // Serial.print(0);
    //   Serial.println("");
    // }
    // else{
    Serial.print(x);
    Serial.print("/");
    Serial.print(y);
    Serial.print("/");
    Serial.print(z);
    // Serial.print("/");
    // Serial.print(gx);
    // Serial.print("/");
    // Serial.print(gy);
    // Serial.print("/");
    // Serial.print(gz);
    Serial.println("");
    // }
    
  }


  delay(10);
}