import warnings
import random
from nicegui import ui

# Configuración de advertencias Unicode
warnings.simplefilter('always', UnicodeWarning)

# Poema de Amor Romántico
POEMA_HTML = """
<div style="text-align: center; font-size: 1.1rem; line-height: 2;">
    <p style="margin-bottom: 1.5rem;">
        Entre destellos de luz y suave resplandor,<br>
        florece en el alma un secreto amor,<br>
        tus ojos son faros en mi oscuridad,<br>
        que guían mi vida a la eternidad.
    </p>
    
    <p style="margin-top: 1.5rem; margin-bottom: 2rem;">
        Como el girasol que persigue la estrella,<br>
        mi corazón busca la huella más bella,<br>
        y en cada latido de este dulce palpitar,<br>
        prometo en silencio siempre adorar.
    </p>
    
    <div style="font-size: 1.2rem; font-weight: bold; color: #fbbf24; margin-top: 1rem; border-top: 1px solid rgba(245, 158, 11, 0.3); padding-top: 0.8rem;">
        ✨ Tu Amor Ilumina Mi Mundo ✨
    </div>
</div>
"""

PALABRAS_CORTAS = [
    "Te Amo", "Mi Amor", "Eternidad", "Tu Sonrisa",
    "Juntos", "Deseo", "Pasión", "Mi Luz", "Siempre"
]

COLORES_NEON = [
    '#22d3ee', '#ff007f', '#00ff66', '#ffea00', '#a855f7', '#ff5722', '#3b82f6'
]

def notificar_unicodewarning():
    warnings.warn("Advertencia de codificación Unicode registrada.", UnicodeWarning)
    ui.notify('⚠️ Se ha registrado un UnicodeWarning', type='warning')

# Estilos globales
ui.query('body').style('''
    background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
    font-family: 'Inter', sans-serif;
    color: #ffffff;
    min-height: 100vh;
''')

# Reglas CSS
ui.add_head_html('''
<style>
    @keyframes girarPetalos {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    @keyframes caidaPalabra {
        0% { top: -60px; opacity: 0; }
        5% { opacity: 1; }
        90% { opacity: 1; }
        100% { top: 520px; opacity: 0; }
    }

    @keyframes parpadeoEstrella {
        0%, 100% { opacity: 0.2; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); }
    }

    .anim-girasol {
        animation: girarPetalos 20s linear infinite;
        transform-origin: 250px 250px;
    }

    .estrella-brillante {
        animation: parpadeoEstrella linear infinite alternate;
    }

    .palabra-cayendo {
        position: absolute;
        top: -60px;
        animation-name: caidaPalabra;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
        animation-fill-mode: backwards;
        white-space: nowrap;
        font-weight: bold;
        pointer-events: none;
        user-select: none;
        z-index: 10;
    }
</style>
''')

def generar_svg_estrellas(cantidad=60):
    estrellas_html = []
    for _ in range(cantidad):
        cx = random.randint(0, 500)
        cy = random.randint(0, 500)
        r = round(random.uniform(0.8, 2.2), 1)
        duracion = round(random.uniform(1.5, 4.0), 2)
        retraso = round(random.uniform(0.0, 3.0), 2)
        estrellas_html.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" class="estrella-brillante" '
            f'style="animation-duration: {duracion}s; animation-delay: {retraso}s;" />'
        )
    return "".join(estrellas_html)

with ui.column().classes('max-w-6xl mx-auto p-6 gap-6 items-center w-full'):
    
    ui.markdown('# 🎆 Girasol LED - Romance Neón').style('text-shadow: 0 0 10px #f59e0b, 0 0 20px #f59e0b;')
    
    # Integración oficial del reproductor de YouTube (Sax Amor)
    ui.html('''
        <div style="background: rgba(15, 23, 42, 0.9); padding: 12px 20px; border-radius: 12px; border: 1px solid rgba(236, 72, 153, 0.4); text-align: center; box-shadow: 0 0 15px rgba(236, 72, 153, 0.2);">
            <p style="margin-bottom: 8px; font-size: 0.95rem; color: #f472b6; font-weight: bold;">🎷 Saxo Romántico (Desde YouTube)</p>
            <iframe width="320" height="70" src="https://www.youtube.com/embed/GMXxZyKD1js?enablejsapi=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 8px;"></iframe>
        </div>
    ''')

    # Tarjeta del Poema de Amor
    with ui.card().classes('w-full p-8 bg-slate-900/80 border border-amber-500/40 rounded-xl backdrop-blur-md shadow-[0_0_15px_rgba(245,158,11,0.2)] flex flex-col items-center justify-center'):
        ui.html(POEMA_HTML).classes('text-amber-100 w-full')

    # CUADRO PRINCIPAL
    with ui.card().classes('w-full p-8 border-2 border-cyan-400/80 bg-slate-950/90 rounded-3xl flex flex-col items-center justify-center shadow-[0_0_35px_rgba(34,211,238,0.5)] relative overflow-hidden'):
        
        ui.label('✨ Lluvia Neón de Amor ✨').classes('text-cyan-300 font-bold text-lg mb-2')

        with ui.element('div').classes('relative w-[500px] h-[500px] rounded-2xl bg-[#050b14] overflow-hidden border border-slate-800 shadow-[0_0_25px_rgba(251,191,36,0.4)]'):
            
            svg_contenido = f'''
            <svg width="500" height="500" viewBox="0 0 500 500" style="position: absolute; top:0; left:0; z-index: 1;">
                <g>{generar_svg_estrellas(60)}</g>
                <line x1="250" y1="250" x2="250" y2="470" stroke="#00ff66" stroke-width="10" stroke-linecap="round" style="filter: drop-shadow(0 0 15px #00ff66);" />
                
                <g class="anim-girasol" id="girasol-petalos">
                    <ellipse cx="250" cy="175" rx="22" ry="60" fill="rgba(255, 215, 0, 0.85)" stroke="#ffea00" stroke-width="3" style="filter: drop-shadow(0 0 15px #ffea00);" />
                    <ellipse cx="250" cy="325" rx="22" ry="60" fill="rgba(255, 215, 0, 0.85)" stroke="#ffea00" stroke-width="3" style="filter: drop-shadow(0 0 15px #ffea00);" />
                    <ellipse cx="175" cy="250" rx="60" ry="22" fill="rgba(255, 215, 0, 0.85)" stroke="#ffea00" stroke-width="3" style="filter: drop-shadow(0 0 15px #ffea00);" />
                    <ellipse cx="325" cy="250" rx="60" ry="22" fill="rgba(255, 215, 0, 0.85)" stroke="#ffea00" stroke-width="3" style="filter: drop-shadow(0 0 15px #ffea00);" />
                    
                    <ellipse cx="197" cy="197" rx="22" ry="60" transform="rotate(-45 197 197)" fill="rgba(255, 215, 0, 0.85)" stroke="#ffea00" stroke-width="3" style="filter: drop-shadow(0 0 15px #ffea00);" />
                    <ellipse cx="303" cy="303" rx="22" ry="60" transform="rotate(-45 303 303)" fill="rgba(255, 215, 0, 0.85)" stroke="#ffea00" stroke-width="3" style="filter: drop-shadow(0 0 15px #ffea00);" />
                    <ellipse cx="303" cy="197" rx="22" ry="60" transform="rotate(45 303 197)" fill="rgba(255, 215, 0, 0.85)" stroke="#ffea00" stroke-width="3" style="filter: drop-shadow(0 0 15px #ffea00);" />
                    <ellipse cx="197" cy="303" rx="22" ry="60" transform="rotate(45 197 303)" fill="rgba(255, 215, 0, 0.85)" stroke="#ffea00" stroke-width="3" style="filter: drop-shadow(0 0 15px #ffea00);" />
                </g>
                <circle cx="250" cy="250" r="40" fill="#ff007f" stroke="#00ffff" stroke-width="4" style="filter: drop-shadow(0 0 20px #ff007f);" />
            </svg>
            '''
            ui.html(svg_contenido)

            capa_palabras = ui.element('div').classes('absolute inset-0 z-10 pointer-events-none')

            def generar_lluvia_palabras():
                capa_palabras.clear()
                columnas_x = [25, 75, 125, 175, 225, 275, 325, 375, 410]
                random.shuffle(columnas_x)

                with capa_palabras:
                    for idx, palabra in enumerate(PALABRAS_CORTAS):
                        pos_x = columnas_x[idx % len(columnas_x)]
                        duracion = round(random.uniform(4.5, 7.5), 2)
                        retraso = round(idx * 0.8 + random.uniform(0.1, 0.5), 2)
                        color = random.choice(COLORES_NEON)
                        es_destacada = random.choice([True, False])

                        tamanio = '19px' if es_destacada else '13px'
                        sombra = f'0 0 16px {color}' if es_destacada else f'0 0 8px {color}'

                        estilo_palabra = f'''
                            left: {pos_x}px;
                            color: {color};
                            font-size: {tamanio};
                            text-shadow: {sombra};
                            animation-duration: {duracion}s;
                            animation-delay: {retraso}s;
                        '''
                        ui.label(f'✨ {palabra}').classes('palabra-cayendo').style(estilo_palabra)

            generar_lluvia_palabras()

    # Panel Interactivo para agregar palabras de amor
    with ui.row().classes('w-full max-w-xl gap-2 items-center justify-center bg-slate-900/60 p-4 rounded-xl border border-slate-700'):
        nueva_palabra_input = ui.input(placeholder='Escribe una frase romántica...').classes('flex-1').props('dense dark bg-color=slate-800')
        
        def agregar_palabra_usuario():
            val = nueva_palabra_input.value.strip()
            if val:
                PALABRAS_CORTAS.append(val)
                nueva_palabra_input.value = ''
                generar_lluvia_palabras()
                ui.notify(f'✨ "{val}" añadida a la lluvia', type='positive')

        ui.button('Añadir Palabra', on_click=agregar_palabra_usuario).props('color=pink icon=favorite')

    # Controles de Efectos
    with ui.row().classes('gap-4 mt-2'):
        ui.button('Regenerar Lluvia', on_click=generar_lluvia_palabras).props('color=amber icon=refresh')
        ui.button('Lanzar UnicodeWarning', on_click=notificar_unicodewarning).props('color=warning outline icon=warning')

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        host="127.0.0.1",
        port=8080,
        title="Girasol LED - Romance Neón",
        favicon="💖",
        reload=False,
        show=True
    )