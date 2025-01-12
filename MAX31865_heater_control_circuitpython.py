import time
import board
import busio
import digitalio
import adafruit_max31865


# Configure SPI for sensor
spi = busio.SPI(clock=board.GP18, MOSI=board.GP19, MISO=board.GP16)
cs = digitalio.DigitalInOut(board.GP17)

# Create sensor object
sensor = adafruit_max31865.MAX31865(spi, cs)

# **Define thermostat parameters**
target_temperature = 80.0  # Target temperature in degrees Celsius
hysteresis = 2          # Temperature hysteresis in degrees Celsius

# **Define output pins**
heater_pin = digitalio.DigitalInOut(board.GP6) 
heater_pin.direction = digitalio.Direction.OUTPUT
led_pin = digitalio.DigitalInOut(board.LED)  # Use the onboard LED pin
led_pin.direction = digitalio.Direction.OUTPUT

def control_heater(temperature):
    """
    Controls the heater and onboard LED based on temperature and hysteresis.

    Args:
        temperature: Current temperature reading.
    """
    global heater_pin, led_pin

    if temperature < target_temperature - hysteresis:
        heater_pin.value = True  # Turn on heater
        led_pin.value = True     # Turn on LED
    elif temperature > target_temperature + hysteresis:
        heater_pin.value = False  # Turn off heater
        led_pin.value = False     # Turn off LED

while True:
    try:
        temp = sensor.temperature
        print(f"Temperature: {temp:.2f} °C") 

        # Call the control_heater function
        control_heater(temp)

    except RuntimeError as error:
        # Handle potential errors (e.g., short-to-ground fault)
        print(f"Error: {error}") 

    time.sleep(1)