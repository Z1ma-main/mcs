import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

win = tk.Tk()
win.title("Асеев Евгений Юрьевич")
win.geometry("600x400")

tabs = ttk.Notebook(win)
tabs.pack(fill='both', expand=True, padx=10, pady=10)

tab1 = tk.Frame(tabs)
tabs.add(tab1, text="Калькулятор")

tk.Label(tab1, text="Первое число:").grid(row=0, column=0, padx=10, pady=10)
e1 = tk.Entry(tab1)
e1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(tab1, text="Второе число:").grid(row=1, column=0, padx=10, pady=10)
e2 = tk.Entry(tab1)
e2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(tab1, text="Операция:").grid(row=2, column=0, padx=10, pady=10)
op = ttk.Combobox(tab1, values=["+", "-", "*", "/"])
op.set("+")
op.grid(row=2, column=1, padx=10, pady=10)

def calc():
    try:
        a = float(e1.get())
        b = float(e2.get())
        oper = op.get()
        
        if oper == "+": 
            r = a + b
        elif oper == "-": 
            r = a - b
        elif oper == "*": 
            r = a * b
        elif oper == "/": 
            if b == 0: 
                messagebox.showerror("Ошибка", "Нельзя делить на ноль!")
                return
            r = a / b
        else:
            messagebox.showerror("Ошибка", "Выберите операцию!")
            return
            
        res.config(text=f"Результат: {r}")
    except:
        messagebox.showerror("Ошибка", "Введите числа правильно!")

tk.Button(tab1, text="Вычислить", command=calc).grid(row=3, column=0, columnspan=2, pady=20)
res = tk.Label(tab1, text="Результат: ")
res.grid(row=4, column=0, columnspan=2)

tab2 = tk.Frame(tabs)
tabs.add(tab2, text="Чекбоксы")

c1 = tk.BooleanVar()
c2 = tk.BooleanVar()
c3 = tk.BooleanVar()

tk.Checkbutton(tab2, text="Первый", variable=c1).grid(row=0, column=0, padx=20, pady=20, sticky='w')
tk.Checkbutton(tab2, text="Второй", variable=c2).grid(row=1, column=0, padx=20, pady=20, sticky='w')
tk.Checkbutton(tab2, text="Третий", variable=c3).grid(row=2, column=0, padx=20, pady=20, sticky='w')

def show():
    ch = []
    if c1.get(): 
        ch.append("первый")
    if c2.get(): 
        ch.append("второй")
    if c3.get(): 
        ch.append("третий")
    
    msg = f"Вы выбрали: {', '.join(ch)}" if ch else "Вы ничего не выбрали"
    messagebox.showinfo("Ваш выбор", msg)

tk.Button(tab2, text="Показать выбор", command=show).grid(row=3, column=0, pady=30)

tab3 = tk.Frame(tabs)
tabs.add(tab3, text="Текст")

def load():
    path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if path:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                text.delete(1.0, tk.END)
                text.insert(1.0, f.read())
            messagebox.showinfo("Успех", "Текст загружен!")
        except:
            messagebox.showerror("Ошибка", "Не удалось загрузить файл")

m = tk.Menu(win)
fm = tk.Menu(m, tearoff=0)
fm.add_command(label="Загрузить текст", command=load)
fm.add_separator()
fm.add_command(label="Выход", command=win.quit)
m.add_cascade(label="Файл", menu=fm)
win.config(menu=m)

text = tk.Text(tab3, wrap='word')
text.pack(padx=10, pady=10, fill='both', expand=True)

win.mainloop()
