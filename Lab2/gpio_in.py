from periphery import GPIO

gpio_in = GPIO("/dev/gpiochip0", "GPIO18", "in", edge="falling")
gpio_out = GPIO("/dev/gpiochip0", "GPIO27", "out")

while True:
    pressed = gpio_in.read()
    gpio_out.write(not pressed)

gpio_in.close()
gpio_out.close()


