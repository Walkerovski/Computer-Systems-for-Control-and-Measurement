from time import sleep, time
import math
import gpio4

def pwm(gpio, duty_cycle: float, frequency: float) -> None:
    gpio = gpio4.SysfsGPIO(gpio)
    gpio.export = True
    gpio.direction = 'out'


    high_duration = duty_cycle / frequency
    low_duration = 1 / frequency - high_duration

    for _ in range(200):
        gpio.value = 1
        sleep(high_duration)
        gpio.value = 0
        sleep(low_duration)        
            
    gpio.export = False

def main():
    frequencies = [
    261.63,  # C4
    293.66,  # D4
    329.63,  # E4
    349.23,  # F4
    392.00,  # G4
    440.00,  # A4
    493.88,  # B4
    523.25,  # C5
    587.33,  # D5
    659.25,  # E5
    698.46,  # F5
    783.99,  # G5
    880.00,  # A5
    987.77,  # B5
    1046.50,  # C6
]

    for f in frequencies:
    	pwm(18, 0.5, f)

if __name__ == '__main__':
    main()
