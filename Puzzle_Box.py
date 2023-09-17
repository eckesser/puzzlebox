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
        self.gui = ctk.CTk()  # Esta linha foi movida para o topo
        self.gui.title("Slider Solver")
        self.gui.geometry('250x250')
        self.gui.resizable(False, False)
        self.gui.eval('tk::PlaceWindow . center')
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

    def StartSolving(self, data):
        solverData = data
        array = self.sortingout(solverData["Instructions"])
        random.seed()
        rs2client_windows = [window for window in pygetwindow.getAllWindows() if "RuneScape" in window.title]
        if len(rs2client_windows) > 0:
            val = rs2client_windows[0]
            val.activate()
            for text in array:
                millisecondsTimeout = random.uniform(0.1, 0.3)
                if not GlobalVariables.isRunning:
                    return
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
        self.is_running = True
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
        self.is_running = False

    def clear_textbox(self):
        self.gui.entry.delete("1.0", ctk.END)

if __name__ == "__main__":
    app = GUI()
    app.gui.mainloop()
