import pyautogui
import time 
import csv
import webbrowser


def automation():

    print("Automação Iniciada!")

    # Pausa o cursor por alguns segundos 
    pyautogui.PAUSE = 1.5

    # Abre o link
    webbrowser.open("http://127.0.0.1:5000")

    # Pausa o código por alguns segundos
    time.sleep(3.5)

    # Pressiona o enter
    pyautogui.press("enter")

    # Abre o arquivo de registros
    with open("data/logs.csv", mode="r", encoding="utf-8") as file: 
        # Armaneza e lê o arquivo de registros
        reader = csv.DictReader(file)

        # Itera as linhas e executa os comandos para o preenchimento automático
        for row in reader:

            pyautogui.click(
                x=937, 
                y=519
            )

            pyautogui.typewrite(
                row["user"], 
                interval=0.1
            )
            pyautogui.press("tab")

            pyautogui.typewrite(
                row["password"], 
                interval=0.1
            )

            pyautogui.press("tab")    

            pyautogui.press("enter")

            pyautogui.press("enter")

            time.sleep(2)

    print("Automação finalizada!")

if __name__ == "__main__": 
    automation()