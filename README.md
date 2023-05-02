**Raspberry-Pi-Pico:**
Aggregate of Raspberry Pi Pico related codes, firmware, libraries, etc.

**Getting started with Micropython**

**Setting the firmware**
1) Download the MicroPython firmware from the Firmware directory in the Micropython folder or from official Raspberry Pi's site.
2) Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer. Release the BOOTSEL button after your Pico is detected.
3) It will mount as a Mass Storage Device called RPI-RP2.
4) Place the MicroPython UF2 file onto the RPI-RP2 volume. The Raspberry Pi Pico should reboot and be ready for programming using Micropython.


**Programming the Pico**
1) You can use any Micropython based IDE for programming the Pico. However, the recommended IDE is the Thonny.
2) Raspberry Pi boards come with Thonny preinstalled. If you are using other systems, you can download and install Thonny.
3) To program the Pico, after opening the Thonny IDE, click on Run menu and click on the Select interpreter option. And from the Drop-down, select Raspberry Pi Pico.

**Mosquitto**
Mosquitto is an open source implementation of a server for version 5.0, 3.1.1, and 3.1 of the MQTT protocol, and the mosquitto_pub and mosquitto_sub utilities for publishing and subscribing messages.

**Quick start**
If you have installed a binary package the broker should have been started automatically. If not, it can be started with a basic configuration:
mosquitto

Then use mosquitto_sub to subscribe to a topic:
mosquitto_sub -t 'test' -v

And to publish a message:
mosquitto_pub -t 'test' -m 'hello world'

**Node Red**
Low-code programming for event-driven applications. which will be used here to subscribe the topic and load it in mysql database.



