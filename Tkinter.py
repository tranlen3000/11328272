import tkinter as tk

# Hàm tính toán kết quả
def calculate():
    try:
        result = eval(entry.get())  # Sử dụng eval để tính toán biểu thức trong ô nhập
        entry.delete(0, tk.END)  # Xóa ô nhập
        entry.insert(tk.END, str(result))  # Hiển thị kết quả
    except:
        entry.delete(0, tk.END)  # Xóa ô nhập nếu có lỗi
        entry.insert(tk.END, "Lỗi")  # Hiển thị "Lỗi" khi có lỗi

# Hàm xử lý sự kiện khi nhấn các nút số hoặc phép toán
def button_click(char):
    entry.insert(tk.END, char)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng Dụng Tính Toán")

# Tạo ô nhập liệu (Entry) để hiển thị các phép toán và kết quả
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Các nút bấm số và phép toán
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Tạo các nút và gán hành động cho từng nút
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), command=calculate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Chạy ứng dụng
root.mainloop()