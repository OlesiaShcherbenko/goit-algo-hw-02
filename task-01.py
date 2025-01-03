import queue
import random
import time

# Створення черги для заявок
queue_requests = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    # Генеруємо унікальний номер заявки
    request_id = random.randint(1000, 9999)
    request = f"Заявка №{request_id}"
    
    # Додавання заявки до черги
    queue_requests.put(request)
    print(f"Нова заявка надійшла: {request}")

# Функція для обробки заявки
def process_request():
    if not queue_requests.empty():
        # Видалення заявки з черги
        request = queue_requests.get()
        print(f"Обробка заявки: {request}")
    else:
        print("Черга пуста, немає заявок для обробки.")

# Головний цикл програми
def main():
    while True:
        print("\n1. Створити нову заявку")
        print("2. Обробити заявку")
        print("3. Вийти з програми")
        choice = input("Оберіть дію (1/2/3): ")
        
        if choice == '1':
            generate_request()
        elif choice == '2':
            process_request()
        elif choice == '3':
            print("Завершення роботи програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")
        
        time.sleep(1)  # Трошки затримки для кращого сприйняття

# Запуск програми
if __name__ == "__main__":
    main()