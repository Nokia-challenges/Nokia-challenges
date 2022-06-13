import RPi.GPIO as GPIO
import time
import threading
from configuration import Configuration
from morse import encrypt_morse

config = Configuration()

def read_sensors(cond1):
    # initialize variables
    cond_latency = False
    cond_pir = False
    
    while True:
        cond1.acquire()
        
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
            cond1.notifyAll()
            cond1.release()
            cond1.wait()
        time.sleep(3)
    
def get_output(cond1): 
    while True:
        cond1.acquire()
        cond1.wait()
        with open("passphrase.txt", "r") as data_file:
            morse_code = encrypt_morse(data_file.read())

        words = morse_code.split('  ')
        print(words)
        for word in words:
            # use blue led to output morse symbol
            for char in word:
                if char == '-':
                    GPIO.output(config.GPIO_BLUE, GPIO.HIGH)
                    time.sleep(1.5)
                    GPIO.output(config.GPIO_BLUE, GPIO.LOW)
                    time.sleep(0.5)
                elif char == '.':
                    GPIO.output(config.GPIO_BLUE, GPIO.HIGH)
                    time.sleep(0.7)
                    GPIO.output(config.GPIO_BLUE, GPIO.LOW)
                    time.sleep(0.5)
                else:
                    time.sleep(1.5)
                
            # use green led to output blank space (word separation)
            GPIO.output(config.GPIO_GREEN, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(config.GPIO_GREEN, GPIO.LOW)
            
            cond1.notifyAll()
            cond1.release()

if __name__ == "__main__":
    # condition variable to sync threads
    cond1 = threading.Condition()
    
    t1 = threading.Thread(target=read_sensors, args=(cond1,))
    t2 = threading.Thread(target=get_output, args=(cond1,))
    
    t2.start()
    t1.start()
