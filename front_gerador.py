import streamlit as st
import gerador
import html
import base64

# ======= CONFIGURAÇÕES =======
st.set_page_config(page_title="Gerador de Senhas", layout="centered")

# ======= ESTILOS =======
st.markdown("""
<style>
    body, .stApp { 
        background-color: #1c2431; 
    }

    .titulo-principal {
        color: white;
        text-align: center; 
        font-weight: 700;
        font-size: 2.2rem;
        margin-top: 1.5rem;
    }
    .subtexto {
        color: #d0d0d0;
        text-align: center;
        font-size: 0.9rem;
        margin-bottom: 2rem;
    }
    .senha-box {
        background-color: #2b3444;
        padding: 12px;
        border-radius: 8px;
        color: white; 
        font-family: monospace;
        display: flex; 
        justify-content: space-between; 
        align-items: center;
    }
    .senha-texto { 
        word-break: break-all; 
        }
            
    .stButton>button {
        background-color: #3a9fff; 
        color: white; 
        border-radius: 8px;
        border: none; 
        font-weight: 600; 
        transition: 0.2s;
    }
    .stButton>button:hover { 
        background-color: #1f6fd1; 
        }
            
    .success-msg {
        background-color: #1f512b; 
        color: #b5ffb8;
        padding: 10px; 
        border-radius: 8px;
        margin-top: 10px;
        font-weight: 500; 
        text-align: left; 
        margin-bottom: 14px;
    }
            
    .espacamento { 
        margin-top: 25px;
        }
            
    .copy-button {
        background: none; 
        border: none; 
        cursor: pointer; 
        padding: 6px;
        display: inline-flex; 
        align-items: center; 
        justify-content: center;
    }
            
</style>
""", unsafe_allow_html=True)

# ======= CONTEÚDO =======
st.markdown("<h1 class='titulo-principal'>Gerador de Senhas em Python 🔒</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtexto'>Crie senhas aleatórias e seguras com facilidade</p>", unsafe_allow_html=True)

tamanho = st.number_input(
    "Quantos caracteres você quer em sua senha ?",
    min_value=4, max_value=128, value=12, step=1
)

if st.button("Gerar senha"):
    try:
        senha = gerador.gerador_senhas(tamanho)
        senha_segura = html.escape(senha)
        senha_b64 = base64.urlsafe_b64encode(senha.encode("utf-8")).decode("ascii")

        st.markdown("<div class='success-msg'>✅ Senha gerada com sucesso !</div>", unsafe_allow_html=True)

        svg_copy = """
        <svg xmlns='http://www.w3.org/2000/svg' width='20' height='20'
        viewBox='0 0 24 24' fill='none' stroke='#3a9fff' stroke-width='2'
        stroke-linecap='round' stroke-linejoin='round'>
            <rect x='9' y='9' width='13' height='13' rx='2'/>
            <rect x='3' y='3' width='13' height='13' rx='2'/>
        </svg>
        """

        senha_html = f"""
        <div class="senha-box espacamento">
            <span class="senha-texto">{senha_segura}</span>
            <button class="copy-button" data-pw="{senha_b64}">{svg_copy}</button>
        </div>

        <script>
        (function() {{
            document.querySelectorAll('.copy-button').forEach(btn => {{
                if (btn.dataset._listener) return;
                btn.dataset._listener = '1';
                btn.addEventListener('click', () => {{
                    alert('Função de copiar simulada!');
                }});
            }});
        }})();
        </script>
        """
        st.markdown(senha_html, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Ocorreu um erro ao gerar a senha: {e}")

else:
    st.markdown(
        "<div class='senha-box'><span class='senha-texto'>A senha aparecerá aqui...</span></div>",
        unsafe_allow_html=True
    )