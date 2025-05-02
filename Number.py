import random

def log_write(file, text):
    file.write(text + "\n")

def guess_number():
    target = random.randint(1, 100)
    attempts = 0

    log = open("game_log.txt", "a", encoding="utf-8")
    log_write(log, "\nНовая Игра")
    print("Угадайте число от 1 до 100!")

    try:
        while True:
            try:
                guess = int(input(f"Попытка {attempts + 1}: "))
            except ValueError:
                print("Ошибка! Введите число")
                log_write(log, f"Неправильный ввод {attempts + 1}")
                continue

            attempts += 1
            log_write(log, f"Попытка {attempts}: {guess}")

            if guess == target:
                print(f"Вы угадали за {attempts} попыток!")
                log_write(log, f"УСПЕХ! Число: {target}, Попыток: {attempts}")
                log_write(log, "=" * 40)
                break

            hint = "Меньше" if guess > target else "Больше"
            print(hint)
            log_write(log, hint)
    finally:
        log.close()

guess_number()