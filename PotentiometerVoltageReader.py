import smbus
import time
address = 0x48 #default address of PCF8591
bus=smbus.SMBus(1)
cmd=0x40
def analogRead(chn):# read ADC value，chn:0,1,2,3
    value = bus.read_byte_data(address,cmd+chn)
    return value
def analogWrite(value):#write DAC value
    bus.write_byte_data(address,cmd,value)
def loop():
 while True:
     value = analogRead(0)
     analogWrite(value)
     voltage = value / 255.0 * 3.3
     print ("ADC Value : %d, Voltage : %.2f" % (value,voltage))
     time.sleep(0.01)
def destroy():
    bus.close()
if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
