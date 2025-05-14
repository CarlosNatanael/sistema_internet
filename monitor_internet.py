import tkinter as tk
from tkinter import ttk
import speedtest
import threading
from time import sleep

class InternetSpeedMonitor:
    def __init__(self, root):
        self.root = root
        self.st = speedtest.Speedtest()
        self.root.title("Monitor de Velocidade da Internet")
        self.root.geometry("400x450")
        self.root.iconbitmap('icone.ico')
        
        # Configurar tema escuro
        self.style = ttk.Style()
        self.style.theme_use('alt')  # Tema mais escuro
        self.configure_dark_theme()
        
        # Variáveis para armazenar os valores
        self.download_speed = tk.StringVar(value="0.00 Mbps")
        self.upload_speed = tk.StringVar(value="0.00 Mbps")
        self.ping = tk.StringVar(value="0 ms")
        self.quality = tk.StringVar(value="Qualidade: -")
        self.is_monitoring = False
        self.quality_label = None  # Será criado no setup_ui
        
        # Configuração da interface
        self.setup_ui()
        
    def configure_dark_theme(self):
        """Configura as cores para o modo escuro"""
        self.root.configure(bg='#333333')
        self.style.configure('TFrame', background='#333333')
        self.style.configure('TLabel', background='#333333', foreground='white')
        self.style.configure('TButton', background='#555555', foreground='white')
        self.style.configure('TProgressbar', background='#0078d7')
        self.style.map('TButton',
                      background=[('active', '#666666')],
                      foreground=[('active', 'white')])
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="Monitor de Velocidade", 
            font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=10)
        
        # Labels de velocidade
        ttk.Label(main_frame, text="Download:").pack()
        download_label = ttk.Label(
            main_frame, 
            textvariable=self.download_speed, 
            font=("Helvetica", 14)
        )
        download_label.pack(pady=5)
        
        ttk.Label(main_frame, text="Upload:").pack()
        upload_label = ttk.Label(
            main_frame, 
            textvariable=self.upload_speed, 
            font=("Helvetica", 14)
        )
        upload_label.pack(pady=5)
        
        ttk.Label(main_frame, text="Ping:").pack()
        ping_label = ttk.Label(
            main_frame, 
            textvariable=self.ping, 
            font=("Helvetica", 14)
        )
        ping_label.pack(pady=5)
        
        # Label de qualidade da conexão (agora como atributo da classe)
        self.quality_label = ttk.Label(
            main_frame, 
            textvariable=self.quality,
            font=("Helvetica", 12, "bold")
        )
        self.quality_label.pack(pady=10)
        
        # Botões
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        self.start_button = ttk.Button(
            button_frame, 
            text="Iniciar Monitoramento", 
            command=self.toggle_monitoring
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        # Barra de progresso
        self.progress = ttk.Progressbar(
            main_frame, 
            orient=tk.HORIZONTAL, 
            mode='indeterminate'
        )
        self.progress.pack(fill=tk.X, pady=10)
        
    def toggle_monitoring(self):
        if self.is_monitoring:
            self.is_monitoring = False
            self.start_button.config(text="Iniciar Monitoramento")
            self.progress.stop()
        else:
            self.is_monitoring = True
            self.start_button.config(text="Parar Monitoramento")
            self.progress.start(10)
            threading.Thread(target=self.monitor_speed, daemon=True).start()
    
    def monitor_speed(self):
        while self.is_monitoring:
            self.run_speed_test()
            sleep(30)
    
    def evaluate_connection(self, download, upload, ping):
        """Avalia a qualidade da conexão com base nos parâmetros"""
        if download < 5 or upload < 1 or ping > 150:
            return ("Fraca", "red")
        elif download < 25 or upload < 5 or ping > 100:
            return ("Média", "orange")
        elif download < 100 or upload < 20 or ping > 50:
            return ("Boa", "#4CAF50")  # Verde mais suave
        else:
            return ("Ótima", "#00FF00")  # Verde brilhante
    
    def run_speed_test(self):
        try:
            st = speedtest.Speedtest()
            st.get_servers()
            st.get_best_server()

            # Teste de ping
            ping = st.results.ping
            self.ping.set(f"{ping:.2f} ms")

            # Teste de download
            self.download_speed.set("Testando...")
            download_speed = st.download() / 1_000_000
            self.download_speed.set(f"{download_speed:.2f} Mbps")

            # Teste de upload
            self.upload_speed.set("Testando...")
            upload_speed = st.upload() / 1_000_000
            self.upload_speed.set(f"{upload_speed:.2f} Mbps")

            # Avalia e atualiza a qualidade
            quality, color = self.evaluate_connection(download_speed, upload_speed, ping)
            self.quality.set(f"Qualidade: {quality}")
            self.quality_label.configure(foreground=color)  # Atualiza a cor diretamente

        except speedtest.ConfigRetrievalError:
            self.handle_error("Erro na conexão")
        except speedtest.NoMatchedServers:
            self.handle_error("Servidores indisponíveis")
        except Exception as e:
            self.handle_error(f"Erro: {str(e)}")

    def handle_error(self, message):
        self.download_speed.set(message)
        self.upload_speed.set(message)
        self.ping.set("--")
        self.quality.set("Qualidade: Erro")
        self.quality_label.configure(foreground="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = InternetSpeedMonitor(root)
    root.mainloop()