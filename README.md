
# Desafio de Projeto – Keylogger (BootCamp Santander - Cibersegurança 2025)

Este projeto apresenta um **Keylogger em Python** construído utilizando a biblioteca `pynput`, com um **menu avançado**, funções administrativas, modo stealth, tratamento completo de teclas especiais e suporte a teclado numérico.

Este documento descreve o funcionamento do sistema, sua arquitetura e seus principais componentes, servindo como documentação oficial para apresentação ou hospedagem no GitHub.

---

## 📌 Objetivo do Projeto
Desenvolver um Keylogger funcional em um ambiente **controlado** para fins educacionais, demonstrando:

- Captura de entradas do teclado usando `pynput`.
- Tratamento correto de caracteres, inclusive **teclado numérico (VK codes)**.
- Estrutura modular e segura.
- Execução do keylogger em segundo plano (thread).
- Menu de controle para iniciar, parar, limpar logs, alterar configurações e modo stealth.
- Registro opcional de teclas especiais.

> **⚠️ Uso exclusivamente acadêmico. Este projeto deve ser executado somente em ambientes controlados e autorizados.**

---

## 📁 Estrutura do Projeto
```
Projeto_Keylogger/
│
├── main.py               # Menu principal e controlador do keylogger
├── keylogger.py          # Lógica de captura das teclas
└── log.txt               # Arquivo de registro gerado automaticamente
```

---

## 🚀 Funcionalidades Implementadas
### ✔ Captura de teclas em tempo real
Utiliza a biblioteca `pynput.keyboard.Listener` para registrar pressionamentos.

### ✔ Registro de números mesmo quando `.char` é `None`
Implementado tratamento especial para teclados numéricos utilizando códigos **VK (Virtual-Key)**.

### ✔ Threading (roda em background)
O keylogger pode ser iniciado e parado pelo menu sem encerrar o programa.

### ✔ Menu administrativo completo
- Iniciar keylogger
- Parar keylogger
- Mostrar logs
- Limpar logs
- Alterar arquivo de log
- Ativar/desativar teclas especiais
- Modo stealth
- Sair

### ✔ Modo Stealth
Limpa a tela e mantém o programa rodando silenciosamente.

### ✔ Registro opcional de teclas especiais
Permite habilitar ou desabilitar registro de teclas como:
- Shift
- Ctrl
- Alt
- Setas
- Backspace
- F1…F12

### ✔ Log com codificação UTF-8
Evita erros com acentos e caracteres especiais.

---

## 🧠 Como funciona o tratamento de teclas
Em teclas normais:
```python
tipo.char → "a", "1", "%"...
```

Para teclas sem `.char` (como números do keypad):
```python
key.vk → retorna códigos entre 96–105
```
Exemplo:
- VK **97** = número **1**
- VK **98** = número **2**

O código converte automaticamente esses valores.

---

## 📄 Estrutura do `main.py`
O arquivo `main.py` funciona como o painel de controle do keylogger. Ele apresenta um menu interativo no terminal, contendo todas as opções administrativas.

Funções principais:
- `iniciar_keylogger()`
- `parar_keylogger()`
- `mostrar_logs()`
- `limpar_logs()`
- `alterar_nome_log()`
- `alternar_teclas_especiais()`
- `modo_stealth()`
- `menu()`

O menu permanece ativo até o usuário escolher **0 - Sair**.

---

## 📄 Estrutura do `keylogger.py`
O módulo realiza a captura das teclas.

Principais componentes:
- Listener `pynput.keyboard.Listener`
- Tratamento de teclas especiais
- Captura de números do keypad via `vk`
- Escrita no arquivo de log com tratamento seguro
- Ignora teclas irrelevantes (Shift, Ctrl, etc.)

---

## 🗂 Arquivo de Log
Todas as teclas capturadas são salvas em:
```
log.txt
```

O formato é contínuo, sem timestamps explícitos (opcional caso queira adicionar).

---

## ▶ Como executar o projeto
### 1️⃣ Instale a biblioteca necessária:
```bash
pip install pynput
```

### 2️⃣ Execute o menu principal:
```bash
python main.py
```

### 3️⃣ Escolha a função desejada no menu.

---

## 🔒 Considerações Éticas e de Segurança
Este projeto:
- Deve ser usado **somente** em ambientes controlados.
- Não deve ser instalado em máquinas de terceiros.
- É apenas para demonstração educacional.

O uso indevido de keyloggers é **crime** de acordo com legislações de diversos países.

---

## 📌 Pontos de Destaque
- Projeto completo e funcional.
- Menu interativo avançado.
- Total compatibilidade com números do teclado numérico.
- Execução em background.
- Modo stealth.
- Documentação profissional para GitHub.

---

## 📜 Licença
Este projeto é distribuído apenas para fins acadêmicos. Uso indevido é responsabilidade exclusiva do usuário.

---

## 👤 Autor
Projeto desenvolvido para estudo acadêmico de manipulação de entrada de teclado, organização modular de software e interação com threads em Python.

---

Se quiser, posso adicionar também:
- **Badges do GitHub (shields.io)**
- **GIF de demonstração**
- **Seções extras como Screenshots, Instalação rápida, CLI docs**, etc.


