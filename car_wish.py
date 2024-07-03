import time
import RPi.GPIO as GPIO

# Настройка GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Реле для включения пылесоса
GPIO.setup(23, GPIO.IN)   # Датчик присутствия автомобиля

# Настройка параметров
VACUUM_DURATION = 120  # Время работы пылесоса в секундах
DELAY_BEFORE_START = 10  # Задержка перед запуском пылесоса в секундах

def start_vacuum():
    print("Включение пылесоса...")
    GPIO.output(18, GPIO.HIGH)  # Включение реле
    time.sleep(VACUUM_DURATION)
    GPIO.output(18, GPIO.LOW)   # Выключение реле
    print("Пылесос выключен.")

def main():
    print("Система автоматизации пылесоса запущена.")
    while True:
        if GPIO.input(23) == GPIO.HIGH:
            print("Автомобиль обнаружен.")
            time.sleep(DELAY_BEFORE_START)
            start_vacuum()
        else:
            print("Ожидание автомобиля...")
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Программа завершена.")