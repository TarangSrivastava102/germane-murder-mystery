from pathlib import Path
import re

src = Path("/mnt/data/Pasted text(20260911-073306).txt")
out = Path("/mnt/data/great_indian_office_chaos_fixed.py")
code = src.read_text(encoding="utf-8")

# Replace the start button with a direct inline handler as the primary path.
code = code.replace(
    '<button class="btn-main" id="start-game-btn" type="button">START THE CHAOS 🚀</button>',
    '<button class="btn-main" id="start-game-btn" type="button" onclick="window.startGame && window.startGame(); return false;">START THE CHAOS 🚀</button>'
)

# Replace the old start-button binding block with a simpler, robust binding.
old = '''        // Bind the Start button directly. Also keep a document-level fallback so
        // Streamlit/iframe event handling cannot prevent the game from starting.
        const startBtn = document.getElementById('start-game-btn');
        if (startBtn) {
            // Use BOTH click and pointerup. This is deliberately redundant for
            // Streamlit's iframe/browser event handling.
            startBtn.addEventListener('click', function(event) {
                event.preventDefault();
                event.stopPropagation();
                window.startGame();
            }, false);
            startBtn.addEventListener('pointerup', function(event) {
                if (event.button !== 0) return;
                event.preventDefault();
                event.stopPropagation();
                window.startGame();
            }, false);
        }'''
new = '''        // The button also has an inline onclick handler. This listener is a
        // secondary fallback for browsers/iframes where event listeners behave oddly.
        const startBtn = document.getElementById('start-game-btn');
        if (startBtn) {
            startBtn.onclick = function(event) {
                if (event) event.preventDefault();
                window.startGame();
                return false;
            };
        }'''
if old not in code:
    raise RuntimeError("Expected start-button binding block was not found.")
code = code.replace(old, new)

# Replace the document-level capture fallback; capture + inline onclick can otherwise
# result in the handler firing twice in some embedded environments.
old2 = '''    // Extra-safe click fallback for Streamlit iframe environments.
    document.addEventListener('click', function(event) {
        const btn = event.target.closest ? event.target.closest('#start-game-btn') : null;
        if (btn) {
            event.preventDefault();
            window.startGame();
        }
    }, true);'''
new2 = '''    // Final fallback: if a browser/iframe prevents the button's normal handler,
    // catch the click without using capture mode (avoids double execution).
    document.addEventListener('click', function(event) {
        const btn = event.target && event.target.closest
            ? event.target.closest('#start-game-btn')
            : null;
        if (btn && typeof window.startGame === 'function') {
            event.preventDefault();
            window.startGame();
        }
    }, false);'''
if old2 not in code:
    raise RuntimeError("Expected document fallback block was not found.")
code = code.replace(old2, new2)

# Make the start function globally available before any initial rendering.
# This avoids any timing edge case with inline onclick.
needle = '''    // LEVEL 1: TRAFFIC SIMULATOR
    let level1Targets'''
replacement = '''    // Make the function available immediately to inline button handlers.
    window.startGame = startGame;

    // LEVEL 1: TRAFFIC SIMULATOR
    let level1Targets'''
if needle not in code:
    raise RuntimeError("Expected level 1 marker was not found.")
code = code.replace(needle, replacement, 1)

# Remove the duplicate assignment later.
code = code.replace(
    '''    // Make it explicitly available to inline/fallback handlers.
    window.startGame = startGame;

''',
    '',
    1
)

# Add a visible JS error box inside the component so future failures are obvious.
marker = '''    // INITIALIZE ON LOAD
    if (document.readyState === 'loading') {'''
error_hook = '''    // Surface JavaScript errors inside the game instead of failing silently.
    window.addEventListener('error', function(event) {
        console.error('Game error:', event.error || event.message);
        const zone = document.getElementById('alert-zone');
        if (zone) {
            zone.innerHTML = '<div class="alert-banner">⚠️ GAME ERROR — Please refresh the game.</div>';
        }
    });

    // INITIALIZE ON LOAD
    if (document.readyState === 'loading') {'''
if marker not in code:
    raise RuntimeError("Initialization marker was not found.")
code = code.replace(marker, error_hook, 1)

out.write_text(code, encoding="utf-8")
print(f"Fixed file created: {out}")
print("Main fix: Start button now has a direct inline handler, with simpler fallback handling and visible JS-error reporting.")
