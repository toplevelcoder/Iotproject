# Iotproject
#define NUMBER_OF_ALERTS 3   //the number of alerts available to user
#define EEPROM_START_ADDR 0  //The address for eeprom
#define HOUR 0               //used for currentSelector to cycle between hh:mm:AM/PM
#define MINUTES 1            //used for currentSelector to cycle between hh:mm:AM/PM
#define MERIDEM 2            //used for currentSelector to cycle between hh:mm:AM/PM
#define PM 0                 //used for meridem
#define AM 1                 //used for meridem
#define HOUR_MAX 12          //if hh is increased beyond this value it will, hh will be reset to 0
#define BUTTON_PRESS_DELAY 100 //Adds a delay after certain button press. Required.

#include <Wire.h>

             

#include <RTClib.h>
#include <LiquidCrystal_I2C.h>
#include <EEPROM.h>

const uint8_t SETTINGS_BUTTON_PIN = A0;  //Cycle between settings/main menu
const uint8_t INC_BUTTON_PIN = 3;
const uint8_t DEC_BUTTON_PIN = 4;
const uint8_t SAVE_BUTTON_PIN = 5;    //save
const uint8_t CYCLE1_BUTTON_PIN = 6;  //Cycle button HH and MM
const uint8_t CYCLE2_BUTTON_PIN = 7;  //Cycle between timers;
const uint8_t ENABLE_BUTTON_PIN = 10; //ENABLE BUTTONS FOR ALARM ON AND OFF

const uint8_t BUZZER_PIN = 13;
const uint8_t LED_PIN[] = {2,8,9};
bool enablealarm = true;
unsigned long reset;                                                                                                                                                                                                        
int resetperiod = 60000;


 
LiquidCrystal_I2C lcd(0x27, 16, 2);  // set the LCD address to 0x20 for a 16 chars and 2 line display
RTC_DS1307 rtc;


struct _timerAlert {
  byte mm = 0;       //Mintues
  byte hh = 0;       //Hours
  byte meridem = 0;  //AM OR PM
  byte ledPin = 0;   //LED Pin address to turn on
};
_timerAlert timerAlerts[NUMBER_OF_ALERTS];

//Button states
//Store the digitalRead of the respective buttons
byte s_settingsButton;
byte s_incButton;
byte s_decButton;
byte s_saveButton;
byte s_cycle1Button;
byte s_cycle2Button;
byte s_enableButton;

//states
bool inSettingsMenu = false;  //used to toggle between settings/main menu
uint8_t selector = 0;         //Used for selection of current alertTimer in the settings
uint8_t hh, mm;               //temporarily stores the hour, and minute. These values are saved when the save button is pressed
uint8_t meridem = 0;          //0 for PM, 1 for AM;
uint8_t currentSelection;     //HH(0) or MM(1) or AM/PM(2);
DateTime currentTime;         //For storing the current time

//LCD
//To store the last string printed to the lcd
//new string passed to writeToLcd are compared to these values
//lcd is updated or cleared only when there is a difference
String _m1, _m2;
unsigned long timeSinceLastBlink;
int blinkPeriod = 500;

//M1 is written in first row, m2 in second
void writeToLcd(String m1, String m2) {

  if (_m1 != m1 && _m2 != m2) {
    lcd.clear();
  }

  if (_m1 != m1) {
    lcd.setCursor(0, 0);  //Select first row
    lcd.print(m1);
    _m1 = m1;
  }

  if (_m2 != m2) {
    lcd.setCursor(0, 1);  //Select second row
    lcd.print(m2);
    _m2 = m2;
  }
}

//Load data from eeprom
void loadTimerDataFromEEPROM() {
  int address = EEPROM_START_ADDR;
  for (int i = 0; i < NUMBER_OF_ALERTS; i++) {
    EEPROM.get(address, timerAlerts[i]);
    address += sizeof(_timerAlert);
    Serial.print("Timer loaded:");
    Serial.print(timerAlerts[i].hh);
    Serial.print(":");
    Serial.print(timerAlerts[i].mm);
    Serial.print(":");
    Serial.println(timerAlerts[i].meridem);
  }
}

//Load data from EEPROM
void saveTimerDataToEEPROM(int timerAlertNumber = -1) {
  //Default, all timer are save one by one
  if (timerAlertNumber == -1) {
    int address = EEPROM_START_ADDR;
    for (int i = 0; i < NUMBER_OF_ALERTS; i++) {
      EEPROM.put(address, timerAlerts[i]);
      address += sizeof(_timerAlert);
    }
  } else if (timerAlertNumber >= 0) {
    //Specific timer alert is saved
    EEPROM.put(EEPROM_START_ADDR + (sizeof(_timerAlert) * timerAlertNumber), timerAlerts[timerAlertNumber]);
  } else {
    Serial.println("Invalid timerAlertNumber while saving");
  }
}

//for setting up the pins
void setupPins() {
  //initalize the buttons
  pinMode(SETTINGS_BUTTON_PIN, INPUT_PULLUP);
  pinMode(INC_BUTTON_PIN, INPUT_PULLUP);
  pinMode(DEC_BUTTON_PIN, INPUT_PULLUP);
  pinMode(CYCLE1_BUTTON_PIN, INPUT_PULLUP);
  pinMode(CYCLE2_BUTTON_PIN, INPUT_PULLUP);
  pinMode(SAVE_BUTTON_PIN, INPUT_PULLUP);
  pinMode(ENABLE_BUTTON_PIN, INPUT_PULLUP);
  pinMode(BUZZER_PIN, OUTPUT);
  

  int length = sizeof(LED_PIN)/sizeof(uint8_t);
  for(int i = 0; i < length; i++)
  {
    pinMode(LED_PIN[i], OUTPUT);
  }
 
}

void setup() {
  Serial.begin(9600);
  Serial.println("START");

  //Initialize LCD
  lcd.init();
  lcd.backlight();
  writeToLcd("Stay Health", "Medicine Box");  //display the welcome message

  //initialize RTC
  if (!rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1) {
      //wait
    }
  }
  if (!rtc.isrunning()) {
    Serial.println("RTC is NOT running!");
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }
  
  //Adjust rtc time to current pc time
  rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));

  //Adjust rtc time manually;
  //rtc.adjust(DateTime(2023,10, 12, 13, 18,55));

  //load data from eeprom
  loadTimerDataFromEEPROM();

  setupPins();
}

//function which stores the input from all the button
//pass "true" to print all button status in the serial monitor
void detectButtonInputs(bool printToMonitor) {

  s_settingsButton = digitalRead(SETTINGS_BUTTON_PIN);
  s_cycle1Button = digitalRead(CYCLE1_BUTTON_PIN);
  s_cycle2Button = digitalRead(CYCLE2_BUTTON_PIN);
  s_decButton = digitalRead(DEC_BUTTON_PIN);
  s_incButton = digitalRead(INC_BUTTON_PIN);
  s_saveButton = digitalRead(SAVE_BUTTON_PIN);
  s_enableButton = digitalRead(ENABLE_BUTTON_PIN);

  if (printToMonitor) {
    String output = "";  //SettingsButton, Cycle1, Cycle2, DEC, INC, SAVE
    output = s_settingsButton;
    output += ":Settings},{";
    output += s_cycle1Button;
    output += ":CYC1},{";
    output += s_cycle2Button;
    output += ":CYC2},{";
    output += s_decButton;
    output += ":DEC},{";
    output += s_incButton;
    output += ":INC},{SAVE:";
    output += s_saveButton;
    Serial.println(output);
    delay(100);
  }
}

//returns the hour in 24 hour format
//Used for comparison with the rtc.now() time
int getHour(byte hour, byte meridem) {
  if (meridem == PM) {
    //Serial.print("Hour:");
    //Serial.println(12 + hour);
      return (12 + hour);
  }
  //Serial.print("Hour:");
  //Serial.println(hour);
  return hour;
}

void onAlert(uint8_t led_pin) {
  //Do anything when the medicine alert is required
  //This function will run for a whole minute
  if (s_enableButton == 0 && enablealarm){
    digitalWrite(BUZZER_PIN, LOW);
    digitalWrite(led_pin, LOW);
    enablealarm = false;
    reset = millis();
    
  }
  
  if (!enablealarm) {
    return;
  }
  digitalWrite(BUZZER_PIN, HIGH);
  digitalWrite(led_pin, HIGH);
  Serial.println(led_pin);
  Serial.println("Alert");
  delay(100);
}

void checkAlert() {
  currentTime = rtc.now();
  for (int i = 0; i < NUMBER_OF_ALERTS; i++) {
    //compare current hour with timer alert hour(24 hr format)
    if (int(currentTime.hour()) == getHour(timerAlerts[i].hh, timerAlerts[i].meridem)) {
      if (int(currentTime.minute() == timerAlerts[i].mm)) {
        //Buzz alert;
        onAlert(LED_PIN[i]);
      }
    }
  }
}

void loop() {

  detectButtonInputs(false);

  //Check if its medicine time!!!!!
  checkAlert();
  if (millis()- reset > resetperiod){
    enablealarm = true;
  }

  if (s_settingsButton == 0) {
    inSettingsMenu = !inSettingsMenu;
    //Update hh,mm, meridem according to the current alertTimer stored in eeprom
    //Cancels the current alert settings if the settings button is pressed instead
    hh = timerAlerts[selector].hh;
    mm = timerAlerts[selector].mm;
    meridem = timerAlerts[selector].meridem;
    delay(BUTTON_PRESS_DELAY);
  }

  if (inSettingsMenu) {

    //Cycle between timerAlerts
    if (s_cycle1Button == 0) {
      

      if (selector == NUMBER_OF_ALERTS - 1) {
        selector = 0;
      } else {
        selector++;
      }

      delay(BUTTON_PRESS_DELAY);

      //Update hh,mm, meridem according to the current alertTimer stored in eeprom
      hh = timerAlerts[selector].hh;
      mm = timerAlerts[selector].mm;
      meridem = timerAlerts[selector].meridem;
    }

    //Cycle between hh:mm:AM/PM for current alertTimer
    if (s_cycle2Button == 0) {
      delay(BUTTON_PRESS_DELAY);
      if (currentSelection == 2) {
        currentSelection = 0;
      } else {
        currentSelection++;
      }
    }

    //INCREMENT
    if (s_incButton == 0) {
      if (currentSelection == HOUR) {
        //increment hours
        if (hh == HOUR_MAX) {
          hh = 0;
        } else {
          hh++;
        }
      } else if (currentSelection == MINUTES) {
        //increment minutes
        if (mm == 60) {
          mm = 0;
        } else {
          mm++;
        }
      } else if (currentSelection == MERIDEM) {
        //toggle between AM/PM
        meridem = !meridem;
      }
      delay(BUTTON_PRESS_DELAY);

    } else if (s_decButton == 0) {
      //DECREMENT
      if (currentSelection == HOUR) {
        //decrement hours
        if (hh == 0) {
          hh = HOUR_MAX;
        } else {
          hh--;
        }
      } else if (currentSelection == MINUTES) {
        //decrement minutes
        if (mm == 0) {
          mm = 60;
        } else {
          mm--;
        }
      } else if (currentSelection == MERIDEM) {
        //toggle between AM/PM
        meridem = !meridem;
      }
      delay(BUTTON_PRESS_DELAY);
    }

    if (s_saveButton == 0) {
      writeToLcd("Saved!!!", "");
      timerAlerts[selector].hh = hh;
      timerAlerts[selector].mm = mm;
      timerAlerts[selector].meridem = meridem;
      saveTimerDataToEEPROM(selector);
      delay(1000);
    }

    String alertNumberDisplay = "Alert";
    alertNumberDisplay += (selector + 1);
    alertNumberDisplay += ":";

    //Check if hh settings is selected, if yes then blink continuosly
    if (inSettingsMenu && currentSelection == HOUR) {
      //SELECTED
      if ((millis() - timeSinceLastBlink) > blinkPeriod) {
        if (String(hh).length() == 1) {
          alertNumberDisplay += "0";
        }
        alertNumberDisplay += hh;
        timeSinceLastBlink = millis();
      } else {
        alertNumberDisplay += "  ";
      }
    } else {
      //NOT SELECTED
      if (String(hh).length() == 1) {
        alertNumberDisplay += "0";
      }
      alertNumberDisplay += hh;
    }

    alertNumberDisplay += ":";

    //Check if mm settings is selected, if yes then blink continuosly
    if (inSettingsMenu && currentSelection == MINUTES) {
      //SELECT, BLINK
      if ((millis() - timeSinceLastBlink) > blinkPeriod) {
        if (String(mm).length() == 1) {
          alertNumberDisplay += "0";
        }
        alertNumberDisplay += mm;
        timeSinceLastBlink = millis();
      } else {
        alertNumberDisplay += "  ";
      }
    } else {
      //NOT SELECTED
      if (String(mm).length() == 1) {
        alertNumberDisplay += "0";
      }
      alertNumberDisplay += mm;
    }

    //Check if Meridem settings is selected, if yes then blink continuosly
    if (inSettingsMenu && currentSelection == MERIDEM) {
      if ((millis() - timeSinceLastBlink) > blinkPeriod) {
        //SELECTED, BLINK
        if (meridem == PM) {
          alertNumberDisplay += ":";
          alertNumberDisplay += "PM";
        } else if (meridem == AM) {
          alertNumberDisplay += ":";
          alertNumberDisplay += "AM";
        }
        timeSinceLastBlink = millis();
      } else {
        alertNumberDisplay += ":";
        alertNumberDisplay += "  ";
      }
    } else {
      //NOT SELECTED
      if (meridem == PM) {
        alertNumberDisplay += ":";
        alertNumberDisplay += "PM";
      } else if (meridem == AM) {
        alertNumberDisplay += ":";
        alertNumberDisplay += "AM";
      }
    }

    writeToLcd("Settings", alertNumberDisplay);

  } else {
    //Text to display on main screen
    String time = "";
    String m = "AM";
    uint8_t hour = int(currentTime.hour());
    if (hour > 12) {
      hour -= 12;
      m = "PM";
    }else if(hour == 12)
    {
      m = "PM";
    }
    if(hour > 24)
    {
      return;
    }
    time += hour;
    time += ":";
    time += int(currentTime.minute());
    time += ":";
    time += int(currentTime.second());
    time += " ";
    time += m;
    writeToLcd("Stay Healthy!", time);
    delay(100);
  }
  delay(100);
}
