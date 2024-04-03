# GPSreading
allows reading data from serial port from a GPS


## Installation
### 1 Install Python 
Download python from the official website
https://www.python.org/
### 2 Open cmd o terminal
### 3 Check your python installation
```bash
pip --version

```
### 4 Install the library
with the command **pip instal**
```bash
pip install pyserial

```
### 5 Check your installation
with the command **pip show**
```bash
pip show pyserial

```

## Find where your desired serial port is located
### macOS e Linux: 
use the terminal with command 
```bash
ls /dev/tty.*

```
will return a  lists of all serial ports

or use the terminal with command 
```bash
dmesg | grep tty

```
will return a list of available serial ports and their identifiers
### Windows
open the cmd and use this command 
```bash
mode 
```
or 
open the "Device Manager" by pressing Windows key + X and selecting "Device Manager".
    Expand the "Ports (COM and LPT)" section to view a list of available serial ports on your system.
## Note 
Don't forget to give permissions to your code




