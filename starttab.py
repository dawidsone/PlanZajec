import customtkinter as ctk
import datetime

def budowa(master):
    frame_start = ctk.CTkFrame(master, corner_radius=10)

    label_start = ctk.CTkLabel(frame_start, text="Witaj na stronie głównej!", font=("Arial", 24))
    label_start.pack(pady=(40, 10))

    label_data = ctk.CTkLabel(frame_start, text="data", font=("Arial", 18))
    label_data.pack(pady=5)

    label_czas = ctk.CTkLabel(frame_start, text="czas", font=("Arial", 48, "bold"), text_color="#1f6aa5")
    label_czas.pack(pady=10)
#Czas
    def zegar():
        teraz = datetime.datetime.now()
        data = teraz.strftime("%d.%m.%Y")
        czas = teraz.strftime("%H:%M:%S")
        
        label_data.configure(text=data)
        label_czas.configure(text=czas)
        label_czas.after(1000, zegar)
#Statystyki notatek i zadan
    def statystyki():
        stat = ctk.CTkFrame(frame_start, fg_color="transparent")
        stat.pack(pady=30)

        notatki=ctk.CTkFrame(stat, fg_color="blue", corner_radius=10)
        notatki.grid(row=0, column=0, padx=15, )

        ctk.CTkLabel(notatki, text="Notatki", font=("Arial",15)).pack()
        


    zegar()
    return frame_start
