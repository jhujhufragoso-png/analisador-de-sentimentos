import nltk
import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Garante o download do léxico do VADER (necessário para a análise)
nltk.download("vader_lexicon")


def analisar_sentimento(texto):
    sia = SentimentIntensityAnalyzer()
    # O VADER retorna um dicionário com notas: pos, neg, neu e compound
    scores = sia.polarity_scores(texto)
    compound = scores["compound"]

    # Classificação simples baseada no score compound
    if compound >= 0.05:
        return "😊 Positivo"
    elif compound <= -0.05:
        return "😢 Negativo"
    else:
        return "😐 Neutro"


# --- Interface do Streamlit ---
st.title("Análise de Sentimento com NLTK")
st.write(
    "Digite uma frase (de preferência em inglês para melhor precisão do VADER) e veja o sentimento."
)

# Prompt de entrada do usuário
user_input = st.text_input("Sua frase:", placeholder="Type something here...")

# Botão para executar
if st.button("Analisar"):
    if user_input.strip() != "":
        resultado = analisar_sentimento(user_input)
        # Exibe o resultado
        st.write(f"O sentimento detectado foi: **{resultado}**")
    else:
        st.write("Por favor, digite algo antes de clicar em analisar.")