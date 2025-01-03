from collections import deque

def is_palindrome(input_string):
    # Підготовка рядка: видалення пробілів та перетворення до нижнього регістру
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Додавання символів до deque
    char_deque = deque(cleaned_string)
    
    # Перевірка паліндрому
    while len(char_deque) > 1:
        # Порівнюємо символи з обох кінців
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Тестування функції
test_strings = [
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw",
    "No lemon, no melon",
    "Hello, World!",
    "Madam",
    "12321",
    "Not a palindrome"
]

for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' -> {'паліндром' if result else 'не паліндром'}")