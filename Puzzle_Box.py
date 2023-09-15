import tkinter as tk
from tkinter import messagebox
import cv2
import numpy as np
import os
import pyautogui
import keyboard
import time

# 1. Funções de Interface Gráfica
def on_start():
    detected, location = detect_puzzle_box()
    if detected:
        answer = messagebox.askyesno("Puzzle Box Detected", "Deseja iniciar o programa?")
        if answer:
            solve_puzzle_box(location)

def on_stop():
    global running
    running = False

# 2. Detecção do Puzzle Box
def detect_puzzle_box():
    # Aqui, você precisa implementar a captura de tela usando outra biblioteca, como pyscreenshot ou pygetwindow.
    screenshot = ...  # Capturar a tela e converter para escala de cinza

    for image_path in os.listdir("imagens_box"):
        template = cv2.imread(os.path.join("imagens_box", image_path), 0)
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        
        if max_val > 0.95:  # Threshold ajustável
            return True, max_loc
    return False, None

# 3. Simulação de Cliques
def click_puzzle_box(location):
    pyautogui.click(location[0], location[1])
    time.sleep(np.random.uniform(0.7, 1.0))  # Espera entre 700ms e 1s

# 4. Solução do Puzzle Box
def solve_puzzle_box(initial_location):
    global running
    running = True
    while running:
        # Aqui, você pode adicionar a lógica para solucionar o puzzle box.
        # No exemplo, estamos apenas clicando no local detectado.
        click_puzzle_box(initial_location)
        # Adicione uma condição para parar quando o puzzle box for resolvido.

# 5. Monitoramento de Atalhos de Teclado
def monitor_keyboard():
    while True:
        if keyboard.is_pressed('F11'):
            on_start()
        elif keyboard.is_pressed('F12'):
            on_stop()
        time.sleep(0.1)

# Interface Gráfica
root = tk.Tk()
root.title("Puzzle Box Solver")

start_button = tk.Button(root, text="Start", command=on_start)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=on_stop)
stop_button.pack(pady=20)

# Iniciar monitoramento de teclado em uma thread separada
import threading
threading.Thread(target=monitor_keyboard, daemon=True).start()

root.mainloop()
