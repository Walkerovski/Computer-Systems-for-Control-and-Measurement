from time import sleep, time
import math
import gpio4

def pwm(gpio, duty_cycle: float, frequency: float, duty_cycle_change: int) -> None:
    gpio = gpio4.SysfsGPIO(gpio)
    gpio.export = True
    gpio.direction = 'out'
    gpio.value = 0
    
    high_duration = duty_cycle / frequency
    low_duration = 1 / frequency - high_duration

    start = time()
    end = time()

    x = 0
    while end - start < 10:
        end = time()
        gpio.value = 1
        sleep(high_duration)
        gpio.value = 0
        sleep(low_duration)        
	
        duty_cycle = (math.sin(x)+1)/2   
        
        high_duration = duty_cycle / frequency
        low_duration = 1 / frequency - high_duration
        x += duty_cycle_change
        
    gpio.export = False

def main():
	pwm(24, 0, 60, 0.1)

if __name__ == '__main__':
    main()
