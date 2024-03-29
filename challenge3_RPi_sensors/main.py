import RPi.GPIO as GPIO
import time
import threading
from configuration import Configuration
from morse import encrypt_morse

config = Configuration()


def read_sensors():
    # initialize variables
    cond_latency = False
    cond_pir = False

    while True:

        # begin trigger pulse
        GPIO.output(config.GPIO_TRIG, GPIO.HIGH)
        time.sleep(0.0001)
        # end trigger pulse
        GPIO.output(config.GPIO_TRIG, GPIO.LOW)

        # wait until pulse is received back
        while GPIO.input(config.GPIO_ECHO) == 0:
            start_time = time.time()
        # pulse has arrived
        while GPIO.input(config.GPIO_ECHO) == 1:
            back_time = time.time()

        # do evaluations
        latency = round(back_time - start_time, 5)
        cond_latency = True if latency >= 0.00117 and latency <= 0.002 else False
        print(f"Latency: {latency}, {cond_latency}")

        # check PIR state
        cond_pir = True if GPIO.input(config.GPIO_PIR) else False
        print(f"Trigger: {cond_pir}")

        if cond_latency and cond_pir:
            t2 = threading.Thread(target=get_output, args=())
            t2.start()
            time.sleep(0.5)
            t2.join()
        time.sleep(3)


def get_output():
    with open("passphrase.txt", "r") as data_file:
        morse_code = encrypt_morse(data_file.read())

    words = morse_code.split("  ")
    print(words)
    for word in words:
        # use blue led to output morse symbol
        for char in word:
            if char == "-":
                GPIO.output(config.GPIO_BLUE, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(config.GPIO_BLUE, GPIO.LOW)
                time.sleep(0.1)
            elif char == ".":
                GPIO.output(config.GPIO_BLUE, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(config.GPIO_BLUE, GPIO.LOW)
                time.sleep(0.1)
            else:
                time.sleep(0.3)

        # use green led to output blank space (word separation)
        GPIO.output(config.GPIO_GREEN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(config.GPIO_GREEN, GPIO.LOW)


if __name__ == "__main__":
    # condition variable to sync threads
    cond1 = threading.Condition()

    t1 = threading.Thread(target=read_sensors, args=())

    t1.start()
