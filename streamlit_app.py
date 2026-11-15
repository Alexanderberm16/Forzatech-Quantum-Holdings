import streamlit as st
import streamlit.components.v1 as components

# Configuración de página
st.set_page_config(
    page_title="PHOENIX IA // Kernel Diagnostic", 
    page_icon="🐆", 
    layout="centered"
)

# Inyección de Estilos CSS Avanzados: Fucsia Neón + Animal Print Ciberpunk
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@500;700;900&display=swap');

    /* Fondo ciber-animal print: Base oscura con gradientes orgánicos tipo manchas y destellos fucsias */
    .stApp {
        background-color: #0b050d;
        background-image: 
            radial-gradient(circle at 15% 25%, rgba(255, 0, 127, 0.18) 0%, transparent 35%),
            radial-gradient(circle at 85% 75%, rgba(255, 0, 127, 0.12) 0%, transparent 40%),
            radial-gradient(ellipse at 50% 50%, #180715 15%, transparent 16%),
            radial-gradient(ellipse at 20% 80%, #150612 20%, transparent 21%),
            radial-gradient(ellipse at 80% 20%, #150612 18%, transparent 19%);
        background-size: 100% 100%, 100% 100%, 180px 180px, 220px 220px, 160px 160px;
        color: #f1f5f9;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Tipografías de títulos estilo HUD con Fucsia Neón */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 2px;
        color: #ff007f !important;
        text-shadow: 0 0 20px rgba(255, 0, 127, 0.4);
    }

    /* Tarjetas contenedoras con estilo Glassmorphism y bordes fucsias */
    .cyber-card {
        background: rgba(18, 7, 20, 0.85);
        border: 1px solid rgba(255, 0, 127, 0.3);
        border-radius: 12px;
        padding: 24px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px 0 rgba(255, 0, 127, 0.15);
        margin-bottom: 20px;
    }

    /* Estilo de los botones nativos en Fucsia Neón */
    .stButton>button {
        background: linear-gradient(135deg, #180715 0%, #2e0a24 100%);
        color: #ff007f;
        border: 1px solid #ff007f;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.2);
        transition: all 0.3s ease;
        width: 100%;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        background: #ff007f;
        color: #0b050d;
        box-shadow: 0 0 30px rgba(255, 0, 127, 0.8);
        transform: translateY(-2px);
    }

    /* Textos de código en consola */
    code {
        color: #ff66b2 !important;
        background-color: rgba(255, 0, 127, 0.08) !important;
        padding: 2px 6px;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown("# 🐆 PHOENIX IA // KERNEL DIAGNOSTIC", unsafe_allow_html=True)
st.markdown("<p style='font-family: \"JetBrains Mono\"; font-size: 0.9em; color: #94a3b8;'>SECURE_NODE: PHOENIX_IA_BUFFER_V1.0</p>", unsafe_allow_html=True)
st.markdown("---")

# Bloque de Logs de Sistema
st.markdown("""
<div class="cyber-card">
    <p><code>[SYS_LOG] Conexión establecida con Nodo Remoto Primero probar boton Rojo...</code></p>
    <p><code>[SYS_WARN] Anomalía detectada: Búfer de memoria afectiva para analisis.</code></p>
    <p><code>[STATUS] Sincronización de caché pendiente desde hace 4 días. Estado: DUDO EN MANDAR COSAS.</code></p>
</div>
""", unsafe_allow_html=True)

st.write("### Selecciona una opción para resolver el conflicto de red:")

# Control de estado
if 'protocol_executed' not in st.session_state:
    st.session_state.protocol_executed = False

if not st.session_state.protocol_executed:
    col1, col2 = st.columns(2)
    
    with col1:
        # Botón principal fucsia neón
        if st.button("🚀 EXECUTAR: Protocolo"):
            st.session_state.protocol_executed = True
            st.rerun()
            
    with col2:
        # El botón trampa adaptado para huir tanto con el mouse (PC) como con el dedo (Móvil)
        components.html("""
            <div style="text-align: left; padding-top: 2px; position: relative; height: 120px;">
                <button id="runaway" style="
                    background: linear-gradient(135deg, #2a0813 0%, #4a0f25 100%);
                    color: #ff3366; 
                    border: 1px solid #ff3366; 
                    padding: 12px 18px; 
                    border-radius: 8px; 
                    cursor: pointer; 
                    font-family: 'JetBrains Mono', monospace; 
                    font-weight: bold;
                    font-size: 14px;
                    position: absolute;
                    transition: transform 0.15s ease;
                    box-shadow: 0 0 15px rgba(255, 51, 102, 0.3);
                " onmouseover="moveButton()" ontouchstart="moveButton()" onclick="moveButton(event)">❌ Ignorar / Bloquear</button>
            </div>
            <script>
            function moveButton(e) {
                if (e) e.preventDefault(); // Evita que el clic o toque se ejecute con normalidad
                const btn = document.getElementById('runaway');
                const x = Math.random() * 160 - 80;
                const y = Math.random() * 80 - 40;
                btn.style.transform = `translate(${x}px, ${y}px)`;
                btn.style.boxShadow = '0 0 30px rgba(255, 51, 102, 0.8)';
            }
            </script>
        """, height=130)
else:
    # Pantalla de éxito post-ejecución
    st.markdown("""
    <div class="cyber-card" style="border-color: #ff007f; box-shadow: 0 0 35px rgba(255,0,127,0.3);">
        <p style="color: #ff007f; font-weight: bold;"><code>[DECRYPTING PAYLOAD...]</code></p>
        <p style="color: #f8fafc; font-size: 1.15em; line-height: 1.6; font-family: 'JetBrains Mono';">
        "Romiprincess El sistema confirma que por más cortafuegos y bloqueos de Instagram que intentes configurar, 
        hay ciertos códigos internos que ningún firewall logra borrar tu sabi po Mashukaita linda." 🤖✨
        </p>
        <p style="color: #94a3b8; margin-top: 15px; font-size: 0.9em;"><i>— Atentamente, el Forzadomotores Arquitecto de sistemas.</i></p>
    </div>
    """, unsafe_allow_html=True)