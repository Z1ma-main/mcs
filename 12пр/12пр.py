import tkinter as tk
from tkinter import messagebox
import requests
import json

def get_repo_data(repo_name):
    repo_url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(repo_url)
    if response.status_code != 200:
        raise Exception(f"Ошибка: {response.status_code}")
    repo_info = response.json()
    
    owner_url = repo_info['owner']['url']
    owner_response = requests.get(owner_url)
    if owner_response.status_code != 200:
        raise Exception(f"Ошибка владельца: {owner_response.status_code}")
    owner_info = owner_response.json()
    
    result = {
        'company': owner_info.get('company'),
        'created_at': repo_info.get('created_at'),
        'email': owner_info.get('email'),
        'id': repo_info['owner']['id'],
        'name': repo_info['owner']['login'],
        'url': repo_info['owner']['url']
    }
    
    with open('github_info.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    return json.dumps(result, indent=2, ensure_ascii=False)

def get_info():
    repo_name = entry.get().strip()
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите имя репозитория")
        return
    try:
        result = get_repo_data(repo_name)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
        messagebox.showinfo("Успех", "Сохранено в github_info.json")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

root = tk.Tk()
root.title("GitHub Info")
root.geometry("500x400")

tk.Label(root, text="Имя репозитория (owner/repo):").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.insert(0, "dotnet/corefx")

tk.Button(root, text="Получить информацию", command=get_info).pack(pady=5)

tk.Label(root, text="Результат:").pack(pady=(10,0))
result_text = tk.Text(root, width=60, height=15)
result_text.pack(pady=5)

root.mainloop()
