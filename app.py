import random
import streamlit as st

# Podstawowa konfiguracja widoku na telefonie
st.set_page_config(
    page_title="Test Kwalifikacyjny", page_icon="📝", layout="centered"
)

# ==========================================
# TUTAJ BAZY PYTAŃ
# ==========================================
PYTANIA_CZ1 = [
    {
        "pytanie": "Przykładowe pytanie z części 1?",
        "odpowiedzi": {"A": "Opcja A", "B": "Opcja B", "C": "Opcja C"},
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 1 Ust. 1",
    }
]

PYTANIA_CZ2 = []

# ==============================================================================
# INICJALIZACJA ZMIENNYCH STANU (Session State)
# ==============================================================================
if "krok" not in st.session_state:
    st.session_state.krok = "WYBOR_CZESCI"
if "baza_zrodlowa" not in st.session_state:
    st.session_state.baza_zrodlowa = []
if "pula_pytan" not in st.session_state:
    st.session_state.pula_pytan = []
if "indeks" not in st.session_state:
    st.session_state.indeks = 0
if "tryb_nauki" not in st.session_state:
    st.session_state.tryb_nauki = True
if "odpowiedzial" not in st.session_state:
    st.session_state.odpowiedzial = False
if "wynik_poprawne" not in st.session_state:
    st.session_state.wynik_poprawne = 0
if "wynik_bledne" not in st.session_state:
    st.session_state.wynik_bledne = 0
if "bledne_pytania" not in st.session_state:
    st.session_state.bledne_pytania = []

# ==============================================================================
# GŁÓWNA KLASA APLIKACJI INTERFEJSU
# ==============================================================================
class AplikacjaQuizu:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikacja Testowa - Quiz")
        self.root.geometry("900x700")
        self.root.minsize(700, 500)

        # Style TTK
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.skonfiguruj_style()

        # Zmienne stanu testu
        self.baza_pytan_zrodlowa = []
        self.pula_pytan = []
        self.indeks_pytania = 0
        self.tryb_nauki = False

        # Statystyki
        self.liczba_poprawnych = 0
        self.liczba_blednych = 0
        self.bledne_pytania = []

        # Kontener główny dla ekranów
        self.glowne_nowe_okno = ttk.Frame(self.root, padding=15)
        self.glowne_nowe_okno.pack(fill=tk.BOTH, expand=True)

        # Stopka z autorem na samym dole aplikacji
        self.zbuduj_stopke()

        # Uruchomienie ekranu początkowego
        self.ekran_wyboru_czesci()

    def skonfiguruj_style(self):
        """Konfiguracja styli wizualnych aplikacji."""
        self.style.configure("TFrame", background="#f5f5f5")
        self.style.configure("TLabel", background="#f5f5f5", font=("Segoe UI", 10))
        self.style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground="#2c3e50")
        self.style.configure("SubHeader.TLabel", font=("Segoe UI", 11, "italic"), foreground="#7f8c8d")
        self.style.configure("Footer.TLabel", font=("Segoe UI", 8, "italic"), foreground="#95a5a6", background="#f5f5f5")
        
        # Przyciski
        self.style.configure("Menu.TButton", font=("Segoe UI", 11, "bold"), padding=10)
        self.style.configure("Nav.TButton", font=("Segoe UI", 10, "bold"), padding=6)
        self.style.configure("Action.TButton", font=("Segoe UI", 10, "bold"), padding=8)

        # Checkbuttony
        self.style.configure("Odp.TCheckbutton", font=("Segoe UI", 11), background="#ffffff", padding=8)
        self.style.map("Odp.TCheckbutton", background=[("active", "#e8f4f8")])

    def zbuduj_stopke(self):
        """Tworzy stałą stopkę na dole okna z informacją o autorze."""
        frame_stopka = ttk.Frame(self.root)
        frame_stopka.pack(side=tk.BOTTOM, fill=tk.X, pady=(0, 5))
        
        lbl_autor = ttk.Label(
            frame_stopka, 
            text=f"Autor programu: {AUTOR}", 
            style="Footer.TLabel", 
            anchor="center"
        )
        lbl_autor.pack()

    def czysc_okno(self):
        """Usuwa wszystkie widgety z głównego kontenera."""
        for child in self.glowne_nowe_okno.winfo_children():
            child.destroy()

    # --------------------------------------------------------------------------
    # EKRAN 1: WYBÓR CZĘŚCI BAZY
    # --------------------------------------------------------------------------
    def ekran_wyboru_czesci(self):
        self.czysc_okno()

        frame_naglowek = ttk.Frame(self.glowne_nowe_okno)
        frame_naglowek.pack(pady=(20, 30))

        lbl_tytul = ttk.Label(frame_naglowek, text="System Testowy", style="Header.TLabel")
        lbl_tytul.pack()

        lbl_sub = ttk.Label(frame_naglowek, text="Wybierz część bazy pytań, aby rozpocząć naukę lub egzamin", style="SubHeader.TLabel")
        lbl_sub.pack(pady=5)

        frame_przyciski = ttk.Frame(self.glowne_nowe_okno)
        frame_przyciski.pack(pady=10)

        btn_cz1 = ttk.Button(
            frame_przyciski, 
            text=f"Część 1 ({len(PYTANIA_CZ1)} pytań)", 
            style="Menu.TButton",
            command=lambda: self.wybierz_czesc(PYTANIA_CZ1)
        )
        btn_cz1.pack(fill=tk.X, pady=10, ipadx=20)

        btn_cz2 = ttk.Button(
            frame_przyciski, 
            text=f"Część 2 ({len(PYTANIA_CZ2)} pytań)", 
            style="Menu.TButton",
            command=lambda: self.wybierz_czesc(PYTANIA_CZ2)
        )
        btn_cz2.pack(fill=tk.X, pady=10, ipadx=20)

        btn_obu = ttk.Button(
            frame_przyciski, 
            text=f"Połączone Części ({len(PYTANIA_CZ1) + len(PYTANIA_CZ2)} pytań)", 
            style="Menu.TButton",
            command=lambda: self.wybierz_czesc(PYTANIA_CZ1 + PYTANIA_CZ2)
        )
        btn_obu.pack(fill=tk.X, pady=10, ipadx=20)

    def wybierz_czesc(self, baza):
        if not baza:
            messagebox.showwarning("Brak pytań", "Wybrana baza jest pusta! Wklej pytania w kodzie źródłowym.")
            return
        self.baza_pytan_zrodlowa = baza
        self.ekran_wyboru_trybu()

    # --------------------------------------------------------------------------
    # EKRAN 2: WYBÓR TRYBU ROZWIAZYWANIA
    # --------------------------------------------------------------------------
    def ekran_wyboru_trybu(self):
        self.czysc_okno()

        frame_naglowek = ttk.Frame(self.glowne_nowe_okno)
        frame_naglowek.pack(pady=(20, 20))

        lbl_tytul = ttk.Label(frame_naglowek, text="Wybierz Tryb Rozwiązywania", style="Header.TLabel")
        lbl_tytul.pack()

        frame_opcje = ttk.Frame(self.glowne_nowe_okno)
        frame_opcje.pack(pady=10)

        btn_nauka = ttk.Button(
            frame_opcje, 
            text="Tryb Nauki (Kolejno + Podpowiedzi/Wyjaśnienia)", 
            style="Menu.TButton",
            command=lambda: self.start_quizu(losowo=False, tryb_nauki=True)
        )
        btn_nauka.pack(fill=tk.X, pady=8, ipadx=10)

        btn_nauka_los = ttk.Button(
            frame_opcje, 
            text="Tryb Nauki (Losowa kolejność + Podpowiedzi)", 
            style="Menu.TButton",
            command=lambda: self.start_quizu(losowo=True, tryb_nauki=True)
        )
        btn_nauka_los.pack(fill=tk.X, pady=8, ipadx=10)

        btn_egzamin = ttk.Button(
            frame_opcje, 
            text="Tryb Egzaminu (Losowo, Wynik na końcu)", 
            style="Menu.TButton",
            command=lambda: self.start_quizu(losowo=True, tryb_nauki=False)
        )
        btn_egzamin.pack(fill=tk.X, pady=8, ipadx=10)

        btn_powrot = ttk.Button(
            self.glowne_nowe_okno, 
            text="← Powrót do wyboru części", 
            style="Nav.TButton",
            command=self.ekran_wyboru_czesci
        )
        btn_powrot.pack(pady=(30, 0))

    # --------------------------------------------------------------------------
    # LOGIKA STARTOWA QUIZU
    # --------------------------------------------------------------------------
    def start_quizu(self, losowo=False, tryb_nauki=True):
        self.pula_pytan = list(self.baza_pytan_zrodlowa)
        if losowo:
            random.shuffle(self.pula_pytan)

        self.indeks_pytania = 0
        self.tryb_nauki = tryb_nauki
        self.liczba_poprawnych = 0
        self.liczba_blednych = 0
        self.bledne_pytania = []

        self.zbuduj_interfejs_pytania()
        self.wyswietl_pytanie()

    # --------------------------------------------------------------------------
    # EKRAN 3: INTERFEJS PYTANIA
    # --------------------------------------------------------------------------
    def zbuduj_interfejs_pytania(self):
        self.czysc_okno()

        # Górny panel (Postęp i powrót)
        frame_top = ttk.Frame(self.glowne_nowe_okno)
        frame_top.pack(fill=tk.X, pady=(0, 10))

        self.lbl_postep = ttk.Label(frame_top, text="", style="SubHeader.TLabel")
        self.lbl_postep.pack(side=tk.LEFT)

        btn_przerwij = ttk.Button(frame_top, text="Menu Główne", style="Nav.TButton", command=self.ekran_wyboru_czesci)
        btn_przerwij.pack(side=tk.RIGHT)

        # Panel Treści Pytania
        frame_pytanie = ttk.LabelFrame(self.glowne_nowe_okno, text=" Pytanie ", padding=15)
        frame_pytanie.pack(fill=tk.BOTH, expand=False, pady=5)

        self.lbl_tresc_pytania = tk.Text(
            frame_pytanie, 
            wrap=tk.WORD, 
            font=("Segoe UI", 11, "bold"), 
            height=4, 
            bg="#f9f9f9", 
            bd=0, 
            highlightthickness=0
        )
        self.lbl_tresc_pytania.pack(fill=tk.BOTH, expand=True)

        # Panel Odpowiedzi
        self.frame_odpowiedzi = ttk.Frame(self.glowne_nowe_okno, padding=5)
        self.frame_odpowiedzi.pack(fill=tk.BOTH, expand=True, pady=10)

        # Panel Informacji Zwrotnej
        self.frame_feedback = ttk.Frame(self.glowne_nowe_okno)
        self.frame_feedback.pack(fill=tk.BOTH, expand=True, pady=5)

        self.txt_feedback = tk.Text(
            self.frame_feedback, 
            wrap=tk.WORD, 
            font=("Segoe UI", 9), 
            height=6, 
            bg="#ffffff", 
            relief=tk.SOLID, 
            bd=1
        )

        # Dolny panel przycisków
        frame_bottom = ttk.Frame(self.glowne_nowe_okno)
        frame_bottom.pack(fill=tk.X, pady=(10, 0))

        self.btn_sprawdz = ttk.Button(frame_bottom, text="Sprawdź / Zatwierdź", style="Action.TButton", command=self.sprawdz_odpowiedz)
        self.btn_sprawdz.pack(side=tk.RIGHT, padx=5)

        self.btn_nastepne = ttk.Button(frame_bottom, text="Następne pytanie →", style="Action.TButton", command=self.nastepne_pytanie)
        self.btn_nastepne.pack(side=tk.RIGHT, padx=5)

    def wyswietl_pytanie(self):
        self.txt_feedback.pack_forget()
        self.btn_nastepne.pack_forget()
        self.btn_sprawdz.pack(side=tk.RIGHT, padx=5)
        self.btn_sprawdz.config(state=tk.NORMAL)

        pytanie = self.pula_pytan[self.indeks_pytania]

        self.lbl_postep.config(text=f"Pytanie {self.indeks_pytania + 1} z {len(self.pula_pytan)} (ID: {pytanie.get('id', '-')})")

        self.lbl_tresc_pytania.config(state=tk.NORMAL)
        self.lbl_tresc_pytania.delete("1.0", tk.END)
        self.lbl_tresc_pytania.insert(tk.END, pytanie["pytanie"])
        self.lbl_tresc_pytania.config(state=tk.DISABLED)

        for child in self.frame_odpowiedzi.winfo_children():
            child.destroy()

        self.zmienne_odpowiedzi = {}
        for klucz, tresc in pytanie["odpowiedzi"].items():
            var = tk.BooleanVar(value=False)
            self.zmienne_odpowiedzi[klucz] = var

            frame_chk = ttk.Frame(self.frame_odpowiedzi, padding=2)
            frame_chk.pack(fill=tk.X, pady=4, anchor="w")

            chk = ttk.Checkbutton(
                frame_chk, 
                text=f"{klucz}. {tresc}", 
                variable=var, 
                style="Odp.TCheckbutton"
            )
            chk.pack(fill=tk.X, side=tk.LEFT, anchor="w")

    def sprawdz_odpowiedz(self):
        pytanie = self.pula_pytan[self.indeks_pytania]
        wybrane = [k for k, v in self.zmienne_odpowiedzi.items() if v.get()]

        if not wybrane:
            messagebox.showwarning("Brak odpowiedzi", "Proszę zaznaczyć przynajmniej jedną odpowiedź!")
            return

        poprawne = pytanie["poprawne"]
        czy_poprawne = set(wybrane) == set(poprawne)

        if czy_poprawne:
            self.liczba_poprawnych += 1
        else:
            self.liczba_blednych += 1
            self.bledne_pytania.append((pytanie, wybrane))

        if self.tryb_nauki:
            self.txt_feedback.pack(fill=tk.BOTH, expand=True)
            self.txt_feedback.config(state=tk.NORMAL)
            self.txt_feedback.delete("1.0", tk.END)

            if czy_poprawne:
                self.txt_feedback.insert(tk.END, "DOKŁADNIE TAK! Odpowiedź poprawna.\n\n", "OK")
                self.txt_feedback.tag_config("OK", foreground="green", font=("Segoe UI", 10, "bold"))
            else:
                self.txt_feedback.insert(tk.END, f"BŁĄD!\nTwoje odpowiedzi: {', '.join(wybrane)}\nPoprawne odpowiedzi: {', '.join(poprawne)}\n\n", "ERR")
                self.txt_feedback.tag_config("ERR", foreground="red", font=("Segoe UI", 10, "bold"))

            if "podstawa_prawna" in pytanie or "tresc_artykulu" in pytanie:
                podstawa = pytanie.get("podstawa_prawna", "")
                tresc = pytanie.get("tresc_artykulu", "")
                self.txt_feedback.insert(tk.END, f"Podstawa prawna: {podstawa}\n{tresc}")

            self.txt_feedback.config(state=tk.DISABLED)

            self.btn_sprawdz.config(state=tk.DISABLED)
            self.btn_nastepne.pack(side=tk.RIGHT, padx=5)
        else:
            self.nastepne_pytanie()

    def nastepne_pytanie(self):
        self.indeks_pytania += 1
        if self.indeks_pytania < len(self.pula_pytan):
            self.wyswietl_pytanie()
        else:
            self.ekran_wynikow()

    # --------------------------------------------------------------------------
    # EKRAN 4: PODSUMOWANIE I WYNIKI
    # --------------------------------------------------------------------------
    def ekran_wynikow(self):
        self.czysc_okno()

        razem = len(self.pula_pytan)
        procent = (self.liczba_poprawnych / razem) * 100 if razem > 0 else 0

        frame_wynik = ttk.Frame(self.glowne_nowe_okno, padding=20)
        frame_wynik.pack(fill=tk.BOTH, expand=True)

        lbl_koniec = ttk.Label(frame_wynik, text="Koniec Testu!", style="Header.TLabel")
        lbl_koniec.pack(pady=10)

        lbl_stats = ttk.Label(
            frame_wynik, 
            text=f"Wynik: {self.liczba_poprawnych} / {razem} ({procent:.1f}%)\n"
                 f"Poprawne: {self.liczba_poprawnych} | Błędne: {self.liczba_blednych}",
            font=("Segoe UI", 12)
        )
        lbl_stats.pack(pady=10)

        if self.bledne_pytania:
            lbl_bledne_hdr = ttk.Label(frame_wynik, text="Podsumowanie błędnych odpowiedzi:", font=("Segoe UI", 10, "bold"))
            lbl_bledne_hdr.pack(anchor="w", pady=(10, 5))

            txt_bledne = tk.Text(frame_wynik, wrap=tk.WORD, font=("Segoe UI", 9), height=12)
            txt_bledne.pack(fill=tk.BOTH, expand=True)

            for py, wybrane in self.bledne_pytania:
                txt_bledne.insert(tk.END, f"• [ID: {py.get('id','-')}] {py['pytanie']}\n")
                txt_bledne.insert(tk.END, f"   Twoja odp: {', '.join(wybrane)} | Poprawna odp: {', '.join(py['poprawne'])}\n\n")

            txt_bledne.config(state=tk.DISABLED)

        btn_reset = ttk.Button(frame_wynik, text="Powrót do Menu", style="Menu.TButton", command=self.ekran_wyboru_czesci)
        btn_reset.pack(pady=15)
 
