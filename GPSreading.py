import serial


########################################################################################
# serial port setting information 
SERIAL_PORT = '/dev/ttyUSB0'  #I use Linux this is the basic port usually
BAUD_RATE = 9600  

########################################################################################

#function 
def main():

    try:
        # Open the serial port  and connect 

        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print("Open serial port and read data from it")

        while True:
            # read data from serial port
            gps_data = ser.readline().decode().strip()
            #print data 
            print("Data GPS:", gps_data)

    except KeyboardInterrupt:
        # ctrl+c key interrupt
        print("\nProgram stopped")
    except Exception as e:
        # Other Exception Gestisce altre eccezioni
        print("error", str(e))
    finally:
        # Close connection 
        if ser.is_open:
            ser.close()
            print("Serial port closed")

if __name__ == "__main__":
    main()


