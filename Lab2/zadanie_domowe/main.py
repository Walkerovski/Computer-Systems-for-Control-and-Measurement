import matplotlib.pyplot as plt
from pwm import pwm_frequency, pwm_duty_cycle


FREQUENCY_LIST = [2, 4, 6, 8, 6, 4, 2]
FREQUENCY = 2.0

DUTY_CYCLES = [0.5, 0.3, 0.1, 0.1, 0.3, 0.5]
DUTY_CYCLE = 0.5


def plotter(result: list) -> None:
    times = [value[0] for value in result]
    plotter_times = [0.0, 0.0]
    values = [value[1] for value in result]
    plotter_values = [0.0, 1.0]
    for i in range(len(times)):
        plotter_times.append(plotter_times[-1] + times[i])
        plotter_times.append(plotter_times[-1])
        plotter_values.append(values[i])
        if values[i] == 1.0:
            plotter_values.append(0.0)
        else:
            plotter_values.append(1.0)
    plt.yticks([0, 1])
    plt.xlabel("time")
    plt.ylabel("value")
    plt.plot(plotter_times, plotter_values)
    plt.savefig('pwm.pdf')
    plt.show()


def plot_pwm_duty_cycle(duty_cycles: list, freq: float) -> None:
    result = pwm_duty_cycle(duty_cycles, freq)
    plotter(result)


def plot_pwm_frequency(frequency_list: list, duty_cycle: float) -> None:
    result = pwm_frequency(frequency_list, duty_cycle)
    plotter(result)


def main() -> None:
    plot_pwm_frequency(FREQUENCY_LIST, DUTY_CYCLE)
    # plot_pwm_duty_cycle(DUTY_CYCLES, FREQUENCY)


if __name__ == '__main__':
    main()
