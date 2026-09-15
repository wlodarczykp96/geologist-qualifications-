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

# Inicjalizacja stanu aplikacji (pamięć sesji na telefonie)
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = []
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []
if "answered" not in st.session_state:
    st.session_state.answered = False


def start_quiz(mode):
    if mode == "cz1":
        questions = list(PYTANIA_CZ1)
    elif mode == "cz2":
        questions = list(PYTANIA_CZ2)
    else:
        questions = list(PYTANIA_CZ1) + list(PYTANIA_CZ2)

    random.shuffle(questions)
    st.session_state.quiz_data = questions
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.answered = False
    st.session_state.page = "quiz"


# --- EKRAN 1: MENU GŁÓWNE ---
if st.session_state.page == "menu":
    st.title("📝 Test Kwalifikacyjny")
    st.write("Wybierz zakres pytań, aby rozpocząć:")

    if st.button("Rozpocznij: Część 1", use_container_width=True):
        start_quiz("cz1")
        st.rerun()

    if st.button("Rozpocznij: Część 2", use_container_width=True):
        start_quiz("cz2")
        st.rerun()

    if st.button("Rozpocznij: Wszystkie pytania", use_container_width=True):
        start_quiz("all")
        st.rerun()

# --- EKRAN 2: TEST ---
elif st.session_state.page == "quiz":
    q_list = st.session_state.quiz_data
    idx = st.session_state.current_idx
    q = q_list[idx]

    st.caption(f"Pytanie {idx + 1} z {len(q_list)}")
    st.progress((idx + 1) / len(q_list))

    st.subheader(q["pytanie"])

    # Przygotowanie opcji do wyboru
    options = [f"{k}: {v}" for k, v in q["odpowiedzi"].items()]

    # Wybór odpowiedzi (pole wyboru wielokrotnego)
    selected = st.multiselect(
        "Wybierz odpowiedź/odpowiedzi:",
        options,
        disabled=st.session_state.answered,
    )

    if not st.session_state.answered:
        if st.button("Zatwierdź odpowiedź", use_container_width=True):
            user_keys = sorted([opt.split(":")[0] for opt in selected])
            correct_keys = sorted(q["poprawne"])

            st.session_state.user_answers = user_keys
            st.session_state.answered = True

            if user_keys == correct_keys:
                st.session_state.score += 1
            st.rerun()
    else:
        user_keys = st.session_state.user_answers
        correct_keys = sorted(q["poprawne"])

        if user_keys == correct_keys:
            st.success("✅ Poprawna odpowiedź!")
        else:
            st.error(
                f"❌ Błąd! Poprawna odpowiedź to: {', '.join(correct_keys)}"
            )

        if "podstawa_prawna" in q and q["podstawa_prawna"]:
            st.info(f"📜 Podstawa prawna: {q['podstawa_prawna']}")

        if idx + 1 < len(q_list):
            if st.button("Następne pytanie ➡️", use_container_width=True):
                st.session_state.current_idx += 1
                st.session_state.answered = False
                st.rerun()
        else:
            if st.button("Zobacz wyniki 🏆", use_container_width=True):
                st.session_state.page = "result"
                st.rerun()

# --- EKRAN 3: WYNIKI ---
elif st.session_state.page == "result":
    st.title("🏆 Koniec testu!")

    total = len(st.session_state.quiz_data)
    score = st.session_state.score
    percentage = (score / total * 100) if total > 0 else 0

    st.metric(
        label="Twój wynik", value=f"{score} / {total}", delta=f"{percentage:.1f}%"
    )

    if percentage >= 80:
        st.balloons()

    if st.button("Powrót do menu głównego", use_container_width=True):
        st.session_state.page = "menu"
        st.rerun()