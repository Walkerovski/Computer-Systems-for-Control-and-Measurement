UP = 1
DOWN = 0


def pwm_frequency(frequency_list: list, duty_cycle: float) -> list:
    value_time_list = []
    for freq in frequency_list:
        period = 1.0 / freq
        value_time_list.append((period * duty_cycle, UP))
        value_time_list.append((period * (1 - duty_cycle), DOWN))
    return value_time_list


def pwm_duty_cycle(duty_cycles: list, frequency: float) -> list:
    value_time_list = []
    period = 1.0 / frequency
    for duty in duty_cycles:
        value_time_list.append((period * duty, UP))
        value_time_list.append((period * (1 - duty), DOWN))
    return value_time_list
