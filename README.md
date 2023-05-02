Raspberry-Pi-Pico:
Aggregate of Raspberry Pi Pico related codes, firmware, libraries, etc.

Getting started with Micropython

Setting the firmware
Download the MicroPython firmware from the Firmware directory in the Micropython folder or from official Raspberry Pi's site by clicking here.
Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer. Release the BOOTSEL button after your Pico is detected.
It will mount as a Mass Storage Device called RPI-RP2.
Place the MicroPython UF2 file onto the RPI-RP2 volume. The Raspberry Pi Pico should reboot and be ready for programming using Micropython.


Programming the Pico
You can use any Micropython based IDE for programming the Pico. However, the recommended IDE is the Thonny.
Raspberry Pi boards come with Thonny preinstalled. If you are using other systems, you can download and install Thonny from here.
To program the Pico, after opening the Thonny IDE, click on Run menu and click on the Select interpreter option. And from the Drop-down, select Raspberry Pi Pico.
