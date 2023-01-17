import smbus
from time import sleep

# I2C bus address of the accelerometer
address = 0x1d

# Initialize I2C bus
bus = smbus.SMBus(1)

# Set the range of the accelerometer to +/- 2g
bus.write_byte_data(address, 0x2b, 0x00)


def Acc():
    while True:
        # Read raw data from the accelerometer
        data = bus.read_i2c_block_data(address, 0x00, 6)

        # Convert raw data to g values
        x = data[0] * 256 + data[1]
        if x > 32767:
            x -= 65536

        y = data[2] * 256 + data[3]
        if y > 32767:
            y -= 65536

        z = data[4] * 256 + data[5]
        if z > 32767:
            z -= 65536

        x = x / 16384.0
        y = y / 16384.0
        z = z / 16384.0

        # Print the acceleration values
        print("X: " + str(x) + " g")
        print("Y: " + str(y) + " g")
        print("Z: " + str(z) + " g")

        # Wait for a moment before reading the next data
        sleep(0.5)

Acc()