import tkinter as tk
from tkinter import filedialog
import random as rd
from golanglexer import lexanalysis
from golangsintax import analizar_sintac


def message(output, description):
    output_codigo.config(state=tk.NORMAL)
    output_codigo.delete('1.0', tk.END)
    if output[1] != '':
        output_codigo.insert(1.0, "\n".join(output[0]) + "\nErrores\n" + output[1])
    else:
        output_codigo.insert(1.0, "\n" + output[0] + f"Sin errores {description}")
    output_codigo.config(state=tk.DISABLED)


def lex_analysis_e():
    text = input_codigo.get("1.0", "end-1c")
    output = lexanalysis(text)
    message(output, "lexico")


def analizar_sint_event():
    text = input_codigo.get("1.0", "end-1c")
    estado_output = analizar_sintac(text)
    err_sint = [estado_output.syntax_text, estado_output.syntax_error]
    text = input_codigo.get("1.0", "end-1c")
    message(err_sint, "sintáctico")


def load_data(entrada, salida, file):
    content = ''.join(file.readlines())
    entrada.delete('1.0', tk.END)
    entrada.insert(1.0, content)
    salida.config(state=tk.NORMAL)
    salida.delete('1.0', tk.END)
    salida.insert(1.0, "Aquí verá el resultado de su análisis.")
    salida.config(state=tk.DISABLED)
    file.close()


def random_example(entrada, salida):
    indice = rd.randint(1, 6)
    f = open(f'./pruebas/prueba{indice}.txt', encoding='utf-8')
    load_data(entrada, salida, f)


def open_example(entrada, salida):
    text_file = filedialog.askopenfilename(initialdir="C:/", title="Open File .txt or .csv",
                                           filetypes=(("Text File", "*.txt"), ("CSV File", "*.csv")))
    text_file = open(text_file, "r")
    load_data(entrada, salida, text_file)


root = tk.Tk()
root.title("GOLANG")
img = tk.PhotoImage(file='./images/icono.png')
root.tk.call('wm', 'iconphoto', root._w, img)

root.geometry("1200x650")
root.resizable(False, True)
root.config(bg="#323233")

canvas = tk.Canvas(root, bg="#74CEDD", width=1200, height=30, bd=0, highlightthickness=0, relief='ridge')
canvas.pack()

# TITlE
logo = tk.PhotoImage(file="./images/logo.png")
titulo = tk.Label(
    root, text='GOLANG ', font="Arial 40", bg="#323233", fg='#2CB7F6', image=logo, compound=tk.RIGHT)
titulo.place(x=450, y=60)

# EDITOR
input_codigo = tk.Text(root, height=24, width=57, bg="#EAEAEC", fg="#0C0D83", bd=0, highlightthickness=0,
                       relief='ridge', wrap="word")
input_codigo.insert(1.0, '//...')
# canvas_input_img.place(x=500, y=140)
input_codigo.place(x=75, y=160)

# OUT
output_codigo = tk.Text(root, height=24, width=57,
                        bg="#EAEAEC", fg="#0C0D83", bd=0, highlightthickness=0, relief='ridge', wrap="word")
output_codigo.insert(1.0, "Aquí verá el resultado de su análisis.")
output_codigo.config(state="disabled")
output_codigo.place(x=615, y=160)

# BUTTON SECTION
play = tk.PhotoImage(file="./images/run.png")
upload = tk.PhotoImage(file="./images/upload.png")
boton_random = tk.Button(
    root, text="Random ", image=play, bg='#6A6A6A', compound=tk.LEFT, fg='white', padx=5, borderwidth=0,
    pady=5, command=lambda: random_example(input_codigo, output_codigo))
boton_file = tk.Button(
    root, text="Open File ", image=upload, bg='#6A6A6A', compound=tk.LEFT, fg='white', padx=5, borderwidth=0,
    pady=5, command=lambda: open_example(input_codigo, output_codigo))
boton_lexico = tk.Button(
    root, text="Analizador léxico", image=play, bg='#6A6A6A', fg='white', compound=tk.LEFT, padx=5, borderwidth=0,
    pady=5, command=lambda: lex_analysis_e())
boton_sintactico = tk.Button(
    root, text="Analizador sintactico/semantico", image=play, bg='#6A6A6A', fg='white', compound=tk.LEFT, padx=5,
    borderwidth=0,
    pady=5, command=lambda: analizar_sint_event())

# boton_semantico = tk.Button(root, text="Analizador semantico", image=play, bg='#6A6A6A', fg='white', compound=tk.LEFT, padx=5, borderwidth=0,pady=5,)

boton_random.place(x=200, y=565)
boton_file.place(x=300, y=565)
boton_lexico.place(x=630, y=600)
boton_sintactico.place(x=760, y=600)
# boton_semantico.place(x=910, y=600)

root.mainloop()
