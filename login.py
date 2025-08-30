import tkinter as tk
#import psycopg2

root = tk.Tk()
root.title("Login")
#root.geometry("300x260")

tk.Label(root, text="Codigo").pack(pady=10)
email = tk.Entry(root)
email.pack(pady=15)

tk.Label(root, text="NIP").pack(pady=20)
pwd = tk.Entry(root)
pwd.pack(pady= 25)


tk.Button(root, text="Login", command = None).pack(pady=30)
tk.Button(root, text="Cancel", command = root.destroy).pack(pady=30)

root.mainloop()
