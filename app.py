import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def add_number():
    try:
        number = int(entry.get())
        if number == 0:
            # При вводе 0, отображаем результат и завершаем ввод
            show_result()
        else:
            digit_sum = sum_of_digits(number)
            numbers.append((number, digit_sum))
            entry.delete(0, tk.END)  # Очищаем поле ввода
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число.")

def show_result():
    if numbers:
        max_num = max(numbers, key=lambda x: x[1])[0]
        messagebox.showinfo("Результат", f"Число с максимальной суммой цифр: {max_num}")
    else:
        messagebox.showinfo("Результат", "Не было введено ни одного числа.")
    root.destroy()  # Закрываем окно

# Создание основного окна
root = tk.Tk()
root.title("Сумма цифр")
root.geometry('520x300')

numbers = []

# Настраиваем шрифты
font_helv26 = tkFont.Font(family='Helvetica', size=26, weight=tkFont.BOLD)
font_helv20 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)

# Фрейм по центру
frame = tk.Frame()
frame.place(anchor="c", relx=.5, rely=.5)

# Поле ввода
entry = tk.Entry(frame, font=font_helv26)
entry.pack(pady=10)

# Кнопка для добавления числа
submit_button = tk.Button(frame, text="Добавить число", font=font_helv20, command=add_number)
submit_button.pack(pady=5)

# Запуск основного цикла
root.mainloop()