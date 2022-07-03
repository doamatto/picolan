# PicoLAN
This is a simple MicroPython program to allow the [Pico W(H)](https://www.raspberrypi.com/news/raspberry-pi-pico-w-your-6-iot-platform/) to broadcast its own WiFi network. This is useful for applications that only need LAN access and not access to the greater Internet (for me, it's my stupid scanner and its inability to stay connected to my actual WiFi network because of wall materials).

## Usage
You should open `sensor.py` and change lines 8 and 12 (`ssid= 'PicoLAN'` and `key= 'tarmac nappy manual reoccupy'`, respectively) to your own SSID and network key for security reasons. Flash using MicroPython REPL to a Pico W(H).

## Acknowledgements
This codebase is licensed under the 3-clause BSD License. It is included in the root of this repository in the `LICENSE` file and accessible online [here](https://github.com/doamatto/picolan/blob/main/LICENSE).
