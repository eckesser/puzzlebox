import tkinter as tk
from tkinter import messagebox
import os
import cv2
import numpy as np
import pyautogui
import keyboard

# Variável global para determinar se o programa está rodando ou não
running = False

# 1. Interface Gráfica
def on_start():
    global running
    running = True
    while running:
        detected, location = detect_puzzle_box()
        if detected:
            answer = messagebox.askyesno("Puzzle Box Detected", "Deseja iniciar o programa?")
            if answer:
                click_puzzle_box(location)
            # Parar após resolver um puzzle
            running = False
        # Esperar um pouco antes de verificar novamente
        pyautogui.sleep(1.0)

def on_stop():
    global running
    running = False

root = tk.Tk()
root.title("Puzzle Box Solver")

start_button = tk.Button(root, text="Start", command=on_start)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=on_stop)
stop_button.pack(pady=20)

# 2. Detecção do Puzzle Box
def detect_puzzle_box():
    # Capturar a tela
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot) 
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    for image_path in os.listdir("imagens_box"):
        template = cv2.imread(os.path.join("imagens_box", image_path), 0)
        result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        
        if max_val > 0.95:  # Threshold ajustável
            return True, max_loc
    return False, None

# 3. Simulação de Cliques
def click_puzzle_box(location):
    pyautogui.click(location[0], location[1])
    pyautogui.sleep(np.random.uniform(0.7, 1.0))  # Espera entre 700ms e 1s

# 4. Atalhos de Teclado
def check_keyboard_input():
    if keyboard.is_pressed('F11'):
        on_start()
    if keyboard.is_pressed('F12'):
        on_stop()

root.after(100, check_keyboard_input)  # Verifica a entrada do teclado a cada 100ms
root.mainloop()
