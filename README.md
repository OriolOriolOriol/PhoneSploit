# Phonesploit


**This project is under construction.** 

```
So when you connected by USB follow these commands:

stay connect via USB

connect to your WIFI network (computer and mobile device both)

ping DeviceIP (must be have ping to your device)

adb kill-server

adb usb

adb tcpip 5555

unplug usb cable (as per @captain_majid 's comment)
adb connect yourDeviceIP

adb devices (must be see two device names , one of them is by deviceIP)

unplug USB cable
```

## How to run?


```
python phonesploit.py
```