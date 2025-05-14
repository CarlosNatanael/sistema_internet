# 🖥️ Monitor de Velocidade da Internet

Aplicativo desktop simples e moderno para **monitorar a velocidade da internet em tempo real**, exibindo informações de **download**, **upload** e **ping**, além de **classificar automaticamente a qualidade da conexão**.

## ✨ Funcionalidades
- 🖤 **Modo Escuro elegante** (Dark Mode)
- 📶 Exibição das velocidades de **Download**, **Upload** e **Ping**
- 🟢 **Classificação automática da qualidade da conexão** (Fraca, Média, Boa, Ótima)
- 🔄 **Monitoramento contínuo a cada 30 segundos**
- 📊 Interface moderna com **barra de progresso animada**
- ⚙️ Desenvolvido em **Python + Tkinter**

## 📷 Captura de Tela
![screenshot exemplo](exemplo.png) <!-- coloque uma imagem do app aqui -->

## 🚀 Como usar
1. Instale as dependências:
    ```bash
    pip install speedtest-cli
    ```

2. Rode o script:
    ```bash
    python monitor_velocidade.py
    ```

3. Clique em **"Iniciar Monitoramento"** para começar a medir a velocidade.

## 🛠️ Estrutura do Projeto
sistema_internet/
├── icone.ico # Ícone do app (opcional)
├── internet_speed_monitor.py # Código principal
└── README.md # Documentação

## 🧰 Tecnologias Utilizadas
- Python 3.x
- Tkinter (Interface Gráfica)
- speedtest-cli (Medição de velocidade)
- threading (Execução em background)

## 📈 Avaliação da Conexão
| Download | Upload | Ping  | Qualidade |
|----------|--------|-------|-----------|
| < 5 Mbps | < 1 Mbps | > 150ms | Fraca    |
| < 25 Mbps| < 5 Mbps | > 100ms | Média    |
| < 100 Mbps| < 20 Mbps | > 50ms | Boa     |
| >= 100 Mbps | >= 20 Mbps | <= 50ms | Ótima |

## 🐞 Possíveis Erros
- **Erro na conexão**: Falha ao obter configuração da internet.
- **Servidores indisponíveis**: Nenhum servidor encontrado.
- **Erro geral**: Problemas inesperados tratados com mensagens amigáveis.

## To-Do (Melhorias futuras)
- [ ] Exportar histórico de medições
- [ ] Notificações de variações bruscas na conexão
- [ ] Configuração de intervalos de teste personalizados
- [ ] Gráfico de desempenho em tempo real

## Licença
Este projeto está licenciado sob a **MIT License**.

---

> Desenvolvido por **Carlos Natanael** — com muito café ☕ e paciência com a internet 🐢