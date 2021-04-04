import time
import threading
import config


def calculate_time_drink(drink):
    max_t = 0
    for liquid in drink.quantities:
        mls = drink.quantities[liquid] * config.bic_size
        t_int = mls/(config.pump_rate * len(liquid.position))
        if (t_int > max_t):
            max_t = t_int
    return max_t


def calculate_time_shot(liquid):
    return config.shot_size/config.pump_rate


def open_pump(pump_no, t):
    print("Started pump no " + str(pump_no))
    time.sleep(t)
    print("Stopped pump no " + str(pump_no))


def dispense_shot(liquid):
    open_pump(liquid.position[0], config.shot_size/config.pump_rate)


def dispense_drink(drink):
    threads = []
    for liquid in drink.quantities:
        mls = drink.quantities[liquid] * config.bic_size
        # time interval
        t_int = mls/(config.pump_rate * len(liquid.position))
        for pump in liquid.position:
            t = threading.Thread(target=open_pump, args=(pump, t_int))
            threads.append(t)
            t.start()
    for t in threads:
        t.join()
