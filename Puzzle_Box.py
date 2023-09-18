import threading
import customtkinter as ctk
import random
import re
import time
import pygetwindow
import keyboard

class GlobalVariables:
    isRunning = True

class GUI:
    def __init__(self):
        self.gui = ctk.CTk()
        self.gui.title("Puzzle Box v1.0")
        self.gui.geometry('250x250')
        self.gui.resizable(False, False)
        self.gui.eval('tk::PlaceWindow . center')

        # Define o ícone para a janela do programa
        self.gui.iconbitmap(r'C:\Users\Eck\Desktop\Projetos\puzzlebox\icone_small.ico')

        self.gui.clue_label = ctk.CTkLabel(self.gui, text="Digite as Instruções", font=("Lato-Regular", 13, 'bold'), text_color="#FFFFFF")
        self.gui.clue_label.place(x=52, y=15)
        self.gui.entry = ctk.CTkTextbox(self.gui, width=200, height=50)
        self.gui.entry.place(x=23, y=50)
        self.gui.start_button = ctk.CTkButton(self.gui, text="Iniciar (F9)", command=self.start_process, width=120, font=("Lato-Regular", 12, 'bold'), text_color="#FFFFFF")
        self.gui.start_button.place(x=63, y=120)
        self.gui.stop_button = ctk.CTkButton(self.gui, text="Parar (F10)", command=self.stop_process, width=120, font=("Lato-Regular", 12, 'bold'), text_color="#FFFFFF")
        self.gui.stop_button.place(x=63, y=160)
        self.gui.clear_button = ctk.CTkButton(self.gui, text="Limpar (F11)", command=self.clear_textbox, width=120, font=("Lato-Regular", 12, 'bold'), text_color="#FFFFFF")
        self.gui.clear_button.place(x=63, y=200)

        # Iniciar o monitoramento da área de transferência
        self.last_clipboard = self.gui.clipboard_get()  # Pegar o atual conteúdo da área de transferência
        self.gui.after(1000, self.check_clipboard)  # Verificar a área de transferência a cada 1 segundo

    def check_clipboard(self):
        try:
            clipboard_content = self.gui.clipboard_get()  # Tentar pegar o conteúdo atual da área de transferência
            if clipboard_content != self.last_clipboard:  # Se o conteúdo mudar
                if self.is_valid_instruction(clipboard_content):  # Se for uma instrução válida
                    self.gui.entry.delete("1.0", ctk.END)  # Limpar a caixa de entrada
                    self.gui.entry.insert(ctk.END, clipboard_content)  # Inserir a nova instrução
                    self.start_process()  # Iniciar o processo
                self.last_clipboard = clipboard_content  # Atualizar o último conteúdo da área de transferência
        except:
            pass
        finally:
            self.gui.after(1000, self.check_clipboard)  # Continuar verificando a área de transferência

    def is_valid_instruction(self, text):
        return bool(re.match(r"^[0-9]+\.", text))
    
    def StartSolving(self, data):
        solverData = data
        array = self.sortingout(solverData["Instructions"])
        random.seed()
        rs2client_windows = [window for window in pygetwindow.getAllWindows() if "RuneScape" in window.title]
        if len(rs2client_windows) > 0:
            val = rs2client_windows[0]
            val.activate()
            for text in array:
                if keyboard.is_pressed('F10') or not GlobalVariables.isRunning:
                    return
                millisecondsTimeout = random.uniform(0.150, 0.300)
                if "up" in text:
                    keyboard.press("down")
                    keyboard.release("down")
                    time.sleep(millisecondsTimeout)
                elif "left" in text:
                    keyboard.press("right")
                    keyboard.release("right")
                    time.sleep(millisecondsTimeout)
                elif "right" in text:
                    keyboard.press("left")
                    keyboard.release("left")
                    time.sleep(millisecondsTimeout)
                elif "down" in text:
                    keyboard.press("up")
                    keyboard.release("up")
                    time.sleep(millisecondsTimeout)

    def sortingout(self, instructions):
        text = re.sub(r"[0-9]+\.", "", instructions)
        text = text.replace("up", "up ")
        text = text.replace("down", "down ")
        text = text.replace("left", "left ")
        text = text.replace("right", "right ")
        return text.split()

    def start_process(self):
        GlobalVariables.isRunning = True
        parameter = self.gui.entry.get("1.0", ctk.END)
        instructions = parameter
        parameter = " ".join(self.sortingout(instructions))
        print(parameter)
        threading.Thread(target=self.start_solving, args=(parameter,)).start()
        self.gui.entry.delete("1.0", ctk.END)

    def start_solving(self, parameter):
        solverData = {"Instructions": parameter}
        self.StartSolving(solverData)

    def stop_process(self):
        GlobalVariables.isRunning = False

    def clear_textbox(self):
        self.gui.entry.delete("1.0", ctk.END)

if __name__ == "__main__":
    app = GUI()
    app.gui.mainloop()
