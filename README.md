# # Desafio de Projeto - Simula um keylogger no VScode simulando a captura de teclas digitadas pelo usuário em ambiente controlado e as enviando posteriormente ao E-mail de destino descrito no codigo (BootCamp Santander - Cibersegurança 2025)

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
- Envia o arquivo log.txt para o E-mail descrito no codigo todas as teclas digitadas pelo alvo.

> **⚠️ Uso exclusivamente acadêmico. Este projeto deve ser executado somente em ambientes controlados e autorizados.**

---

## 📁 Estrutura do Projeto
```
Projeto_Keylogger/
│
├── main.py               # Menu principal e controlador do keylogger
├── keylogger.pyw         # Lógica de captura das teclas executado em segundo plano
└── keylogger_email.py    # Envia o arquivo log.txt para o E-mail de Destino
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

## 📄 Estrutura do `keylogger.pyw`
O módulo realiza a captura das teclas.

Principais componentes:
- Listener `pynput.keyboard.Listener`
- Tratamento de teclas especiais
- Captura de números do keypad via `vk`
- Escrita no arquivo de log com tratamento seguro
- Ignora teclas irrelevantes (Shift, Ctrl, etc.)

## 📄 Estrutura do `keylogger_email.py`
O módulo envia o arquivo log.txt ao email de destino

- O código captura teclas pressionadas usando pynput e armazena tudo na variável log.
- A cada 60 segundos, a função enviar_email() é chamada para enviar o conteúdo registrado para um e-mail via SMTP do Gmail.
- Ele trata teclas especiais (espaço, enter, tab, backspace, esc) e ignora teclas de modificação.
- O keyboard.Listener fica rodando continuamente, registrando as teclas e disparando o envio automático.
- O e-mail é enviado usando autenticação TLS no servidor do Gmail.

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

pip install smtplib
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
- Envia E-mail via protocolo SMTP



---

## 🚨 Medidas de Mitigação 

- Uso de Software de Segurança

- Antivírus e Anti-malware: Instale e mantenha um software de antivírus ou anti-malware robusto e sempre atualizado. Esses programas são a maneira mais confiável de detectar e remover keyloggers, que muitas vezes se disfarçam de programas legítimos.

- Firewalls: Utilize firewalls para monitorar e bloquear tráfego malicioso, o que pode impedir que keyloggers enviem os dados coletados para os atacantes.

- Software Anti-keylogger dedicado: Considere o uso de software anti-keylogger especializado, que pode oferecer uma camada extra de proteção ao detectar padrões específicos de registro de teclas.
  
- Sistema de Prevenção de Intrusão (IPS): Em ambientes corporativos ou de infraestrutura crítica, um IPS pode ajudar a detectar e bloquear tráfego suspeito associado à atividade de keyloggers. 

- Práticas de Navegação e Uso Seguras

- Evite fontes desconhecidas: Bloqueie a instalação de aplicativos de fontes não confiáveis para reduzir significativamente o risco de infecção por malware e keyloggers.

- Tenha cautela com e-mails e downloads: Evite clicar em links ou baixar anexos de e-mails suspeitos ou de remetentes desconhecidos, pois essa é uma forma comum de disseminação de keyloggers.

- Mantenha sistemas atualizados: Use apenas sistemas operacionais e programas originais e mantenha-os sempre atualizados, pois as atualizações frequentemente corrigem vulnerabilidades de segurança exploradas por malwares.

- Use um teclado virtual: Ao inserir informações confidenciais, como senhas, em sites bancários ou de comércio eletrônico, use o teclado virtual (on-screen keyboard) fornecido pelo site ou pelo sistema operacional, se disponível. Isso impede o registro das teclas físicas pressionadas.

- Autenticação de dois fatores (2FA): Sempre que possível, ative a autenticação de dois fatores para adicionar uma camada extra de segurança, mesmo que a senha seja comprometida. 

- Vigilância Física

- Inspecione o hardware: Verifique fisicamente seus dispositivos (como computadores e caixas eletrônicos) em busca de quaisquer dispositivos de hardware keylogger não autorizados conectados entre o teclado e o computador. 

## 📜 Licença
Este projeto é distribuído apenas para fins acadêmicos. Uso indevido é responsabilidade exclusiva do usuário.

---

## 👤 Autor
Projeto desenvolvido para estudo acadêmico de manipulação de entrada de teclado, organização modular de software e interação com threads em Python.

Meu Linkedin:[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carlos-henrique-80365897/)
---

