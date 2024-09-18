import tkinter as tk
import random

def on_no_enter(event):
    # Muda a posição do botão 'Não'
    x = random.randint(0, window_width - button_width)
    y = random.randint(0, window_height - button_height)
    button_no.place(x=x, y=y)  

def on_yes_click():
    # Ação quando o botão 'Sim' é clicado
    print("Você clicou em Sim!")

def on_no_click():
    # Ação quando o botão 'Não' é clicado
    print("Você clicou em Não!")

# Cria a janela principal
window = tk.Tk()
window.title("Pergunta Aleatória")
window_width = 400
window_height = 300
window.geometry(f"{window_width}x{window_height}")

# Cria a pergunta aleatória
question_label = tk.Label(window, text="Cuzinho hoje??")
question_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Cria o botão 'Sim'
button_yes = tk.Button(window, text="Sim", command=on_yes_click)
button_yes.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

# Cria o botão 'Não'
button_no = tk.Button(window, text="Não", command=on_no_click)
button_no.place(relx=0.7, rely=0.6, anchor=tk.CENTER)
button_no.bind("<Enter>", on_no_enter)  # Define a função para quando o mouse entra no botão 'Não'

# Obtém as dimensões dos botões
button_width = button_yes.winfo_reqwidth()
button_height = button_yes.winfo_reqheight()

# Inicia o loop principal da janela
window.mainloop()
