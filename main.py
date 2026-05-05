import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class WeatherDiary:
 def __init__(self, root):
 self.Root = root
 self.Root.Title("Weather Diary")
 self.Records = []
 self.Load_data()

 # Поля ввода
 tk.Label(root, text="Дата (ДД.ММ.ГГГГ):").Grid(row=0, column=0)
 self.Date_entry = tk.Entry(root)
 self.Date_entry.Grid(row=0, column=1)

 tk.Label(root, text="Температура (°C):").Grid(row=1, column=0)
 self.Temp_entry = tk.Entry(root)
 self.Temp_entry.Grid(row=1, column=1)

 tk.Label(root, text="Описание:").Grid(row=2, column=0)
 self.Desc_entry = tk.Entry(root)
 self.Desc_entry.Grid(row=2, column=1)

 tk.Label(root, text="Осадки (да/нет):").Grid(row=3, column=0)
 self.Rain_var = tk.StringVar(value="нет")
 tk.Radiobutton(root, text="да", variable=self.Rain_var, value="да").Grid(row=3, column=1)
 tk.Radiobutton(root, text="нет", variable=self.Rain_var, value="нет").Grid(row=3, column=2)

 # Кнопка добавления
 tk.Button(root, text="Добавить запись", command=self.Add_record).Grid(row=4, column=0, columnspan=3)

 # Таблица для отображения записей
 self.Table = tk.Listbox(root, width=80, height=15)
 self.Table.Grid(row=5, column=0, columnspan=3)

 # Фильтры
 tk.Button(root, text="Фильтр по дате", command=self.Filter_by_date).Grid(row=6, column=0)
 tk.Button(root, text="Фильтр по температуре (>10°C)", command=self.Filter_by_temp).Grid(row=6, column=1)

 tk.Button(root, text="Сохранить в JSON", command=self.Save_to_json).Grid(row=7, column=0)
 tk.Button(root, text="Загрузить из JSON", command=self.Load_from_json).Grid(row=7, column=1)

 def add_record(self):
 # Проверка ввода
 if not self.Validate_input():
 return

 record = {
 "date": self.Date_entry.Get(),
 "temp": float(self.Temp_entry.Get()),
 "desc": self.Desc_entry.Get(),
 "rain": self.Rain_var.Get()
}
 self.Records.Append(record)
 self.Update_table()
 self.Save_data()

 def validate_input(self):
 try:
 date_str = self.Date_entry.Get()
 datetime.Strptime(date_str, "%d.%m.%Y")

 temp = float(self.Temp_entry.Get())

 desc = self.Desc_entry.Get().Strip()
 if not desc:
 messagebox.
