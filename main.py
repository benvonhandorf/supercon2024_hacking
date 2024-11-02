from letters import set_letter
import time


if __name__ == '__main__':

    while True:
        set_letter(i2c1, 'B')
        time.sleep(0.5)
        set_letter(i2c1, 'E')
        time.sleep(0.5)
        set_letter(i2c1, 'N')
        time.sleep(0.5)