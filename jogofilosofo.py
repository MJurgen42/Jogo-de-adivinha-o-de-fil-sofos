import tkinter as tk
from tkinter import messagebox
import random

frases = [
    {"frase": "Só sei que nada sei.", "autor": "Sócrates", "dica": "Filósofo grego do século V a.C."},
    {"frase": "O homem é a medida de todas as coisas.", "autor": "Protágoras", "dica": "Filósofo pré-socrático grego."},
    {"frase": "Penso, logo existo.", "autor": "Descartes", "dica": "Filósofo francês do século XVII."},
    {"frase": "A vida sem reflexão não vale a pena ser vivida.", "autor": "Sócrates", "dica": "Filósofo grego do século V a.C."},
    {"frase": "O homem nasce livre, mas por toda parte encontra-se acorrentado.", "autor": "Rousseau", "dica": "Filósofo suíço do século XVIII."},
    {"frase": "A felicidade é o bem supremo.", "autor": "Aristóteles", "dica": "Filósofo grego discípulo de Platão."},
    {"frase": "Deus está morto.", "autor": "Nietzsche", "dica": "Filósofo alemão do século XIX."},
    {"frase": "O inferno são os outros.", "autor": "Sartre", "dica": "Filósofo francês do século XX."}
]

class JogoFilosofosApp:
    def __init__(self, master):
        self.master = master
        master.title("Jogo das Frases Filosóficas")
        master.geometry("600x400")

        self.pontos = 0
        self.pergunta_atual = None
        self.tentativa = 0

        self.label_frase = tk.Label(master, text="", wraplength=550, font=("Arial", 14))
        self.label_frase.pack(pady=20)

        self.entry_resposta = tk.Entry(master, font=("Arial", 14))
        self.entry_resposta.pack()

        self.botao_enviar = tk.Button(master, text="Enviar", command=self.verificar_resposta)
        self.botao_enviar.pack(pady=10)

        self.label_dica = tk.Label(master, text="", fg="blue", font=("Arial", 12))
        self.label_dica.pack()

        self.label_pontos = tk.Label(master, text="Pontuação: 0", font=("Arial", 12))
        self.label_pontos.pack(pady=10)

        self.nova_pergunta()

    def nova_pergunta(self):
        self.tentativa = 0
        self.label_dica.config(text="")
        self.entry_resposta.delete(0, tk.END)
        self.pergunta_atual = random.choice(frases)
        self.label_frase.config(text=f"Quem disse:\n\"{self.pergunta_atual['frase']}\" ?")

    def verificar_resposta(self):
        resposta = self.entry_resposta.get().strip().lower()
        autor_correto = self.pergunta_atual["autor"].lower()

        if resposta == autor_correto:
            self.pontos += 1
            self.label_pontos.config(text=f"Pontuação: {self.pontos}")
            messagebox.showinfo("Resposta", "✅ Parabéns, você acertou!")
            self.nova_pergunta()
        else:
            self.tentativa += 1
            if self.tentativa == 1:
                self.label_dica.config(text=f"Dica: {self.pergunta_atual['dica']}")
                self.entry_resposta.delete(0, tk.END)
            else:
                messagebox.showinfo("Resposta", f"❌ Errado! A resposta correta é {self.pergunta_atual['autor']}.")
                self.nova_pergunta()

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoFilosofosApp(root)
    root.mainloop()
