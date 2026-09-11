import streamlit as st

# Configure Streamlit page layout and metadata
st.set_page_config(
    page_title="The Great Indian Office Chaos | Germane Media LLC",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide default Streamlit padding and header elements for a seamless game show UI
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Full Interactive Browser Game Engine (HTML5, CSS3, JavaScript Web Audio API)
HTML_GAME = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Great Indian Office Chaos</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
            font-family: 'Poppins', sans-serif;
        }

        body {
            background: #0f0c20;
            color: #ffffff;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            overflow-x: hidden;
            padding: 10px;
        }

        /* GAME SHOW CONTAINER */
        #game-container {
            width: 100%;
            max-width: 1000px;
            background: #181335;
            border: 4px solid #ffd700;
            border-radius: 20px;
            box-shadow: 0 0 30px rgba(255, 215, 0, 0.3), inset 0 0 15px rgba(0, 0, 0, 0.8);
            padding: 20px;
            position: relative;
            min-height: 820px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* HEADER HUD */
        .hud-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0, 0, 0, 0.5);
            padding: 12px 20px;
            border-radius: 12px;
            border: 2px solid #ff007f;
            margin-bottom: 15px;
            flex-wrap: wrap;
            gap: 10px;
        }

        .hud-title {
            font-size: 14px;
            font-weight: 900;
            color: #ff9900;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .hud-badges {
            display: flex;
            gap: 15px;
            align-items: center;
        }

        .badge {
            background: #281e51;
            padding: 6px 14px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 14px;
            border: 1px solid #00f2fe;
            box-shadow: 0 0 8px rgba(0, 242, 254, 0.4);
        }

        .badge-timer { color: #ff3366; border-color: #ff3366; }
        .badge-score { color: #00ff88; border-color: #00ff88; }
        .badge-level { color: #ffd700; border-color: #ffd700; }

        /* CHAOS METER */
        .chaos-container {
            width: 100%;
            background: #000;
            height: 16px;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #ff3366;
            margin-bottom: 15px;
            position: relative;
        }

        .chaos-bar {
            height: 100%;
            width: 10%;
            background: linear-gradient(90deg, #00ff88, #ffd700, #ff007f);
            transition: width 0.5s ease;
        }

        .chaos-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 10px;
            font-weight: 900;
            color: #fff;
            text-shadow: 1px 1px 2px #000;
        }

        /* SOUND & HINT CONTROL BUTTONS */
        .top-controls {
            display: flex;
            gap: 10px;
        }

        .btn-ctrl {
            background: #ff007f;
            border: none;
            color: white;
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            transition: transform 0.1s, background 0.2s;
        }

        .btn-ctrl:hover { transform: scale(1.05); background: #e0006c; }

        /* LEVEL STAGE CANVAS / CONTENT AREA */
        .stage-area {
            flex-grow: 1;
            background: #211a45;
            border-radius: 15px;
            padding: 20px;
            border: 2px dashed #00f2fe;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            text-align: center;
            overflow: hidden;
        }

        /* TYPOGRAPHY & BUTTONS */
        h1 { font-size: 28px; color: #ffd700; text-shadow: 2px 2px 0 #ff007f; margin-bottom: 10px; }
        h2 { font-size: 20px; color: #00f2fe; margin-bottom: 15px; }
        p { font-size: 14px; color: #e0e0e0; margin-bottom: 15px; line-height: 1.5; }

        .btn-main {
            background: linear-gradient(135deg, #ff7b00, #ff0055);
            color: white;
            font-size: 18px;
            font-weight: 900;
            padding: 14px 28px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 6px 0 #990033, 0 10px 20px rgba(255, 0, 85, 0.4);
            transition: all 0.15s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 15px;
        }

        .btn-main:active {
            transform: translateY(4px);
            box-shadow: 0 2px 0 #990033, 0 4px 10px rgba(255, 0, 85, 0.4);
        }

        .option-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            width: 100%;
            max-width: 700px;
            margin-top: 15px;
        }

        .btn-option {
            background: #2d245c;
            border: 2px solid #00f2fe;
            color: white;
            padding: 14px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: left;
        }

        .btn-option:hover {
            background: #00f2fe;
            color: #000;
            transform: translateY(-2px);
        }

        /* TRAFFIC SIMULATOR CANVAS (LEVEL 1) */
        .traffic-box {
            position: relative;
            width: 100%;
            max-width: 750px;
            height: 380px;
            background: linear-gradient(180deg, #3a2e6e 0%, #1a1533 100%);
            border-radius: 12px;
            border: 3px solid #ffd700;
            overflow: hidden;
            margin-bottom: 15px;
        }

        .traffic-target {
            position: absolute;
            cursor: pointer;
            font-size: 32px;
            transition: transform 0.2s;
            padding: 8px;
            background: rgba(0,0,0,0.4);
            border-radius: 50%;
            border: 2px solid #ffd700;
        }

        .traffic-target:hover { transform: scale(1.3) rotate(5deg); }
        .traffic-target.found { opacity: 0.3; pointer-events: none; border-color: #00ff88; }

        /* PUZZLE GRID (LEVEL 2) */
        .puzzle-grid {
            display: grid;
            grid-template-columns: repeat(3, 90px);
            grid-template-rows: repeat(3, 90px);
            gap: 6px;
            margin: 15px auto;
        }

        .puzzle-tile {
            background: #3b2d75;
            border: 2px solid #ffd700;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            font-weight: 900;
            cursor: pointer;
            color: #fff;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
            transition: transform 0.2s, background 0.2s;
        }

        .puzzle-tile.selected {
            background: #ff007f;
            transform: scale(1.1);
            border-color: #00ff88;
        }

        /* KEYPAD (LEVEL 4) */
        .upi-keypad {
            display: grid;
            grid-template-columns: repeat(3, 60px);
            gap: 10px;
            margin: 15px auto;
        }

        .key-btn {
            background: #2e235e;
            border: 2px solid #00f2fe;
            color: white;
            font-size: 20px;
            font-weight: 900;
            height: 55px;
            border-radius: 10px;
            cursor: pointer;
        }

        .key-btn:hover { background: #00f2fe; color: #000; }

        /* RECURRING CHARACTER POPUP MODAL */
        .char-modal {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(15, 12, 32, 0.95);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 30px;
            z-index: 100;
            animation: popIn 0.3s ease;
        }

        @keyframes popIn {
            from { transform: scale(0.8); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }

        .char-avatar {
            font-size: 70px;
            margin-bottom: 10px;
            filter: drop-shadow(0 0 10px #ffd700);
        }

        .char-name {
            font-size: 22px;
            font-weight: 900;
            color: #ff007f;
            margin-bottom: 5px;
        }

        .char-quote {
            font-style: italic;
            font-size: 16px;
            color: #ffd700;
            max-width: 500px;
            margin-bottom: 20px;
            background: rgba(255,255,255,0.05);
            padding: 12px;
            border-radius: 10px;
            border-left: 4px solid #ff007f;
        }

        /* LEVEL TRACKER FOOTER */
        .level-tracker {
            display: flex;
            justify-content: center;
            gap: 6px;
            margin-top: 15px;
            flex-wrap: wrap;
        }

        .dot {
            width: 28px;
            height: 28px;
            border-radius: 6px;
            background: #281e51;
            border: 1px solid #55418a;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-weight: 700;
            color: #888;
        }

        .dot.active { background: #ff007f; color: #fff; border-color: #ffd700; box-shadow: 0 0 8px #ff007f; }
        .dot.done { background: #00ff88; color: #000; border-color: #00ff88; }

        /* WARNING OVERLAY */
        .alert-banner {
            background: #ff0033;
            color: white;
            font-weight: 900;
            padding: 6px;
            font-size: 12px;
            border-radius: 6px;
            margin-bottom: 10px;
            animation: pulse 1s infinite;
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }

        /* CONFETTI ANIMATION */
        .confetti-particle {
            position: absolute;
            width: 10px;
            height: 10px;
            background: #ffd700;
            top: -10px;
            animation: fall 2.5s infinite linear;
        }

        @keyframes fall {
            to { transform: translateY(800px) rotate(360deg); }
        }
    </style>
</head>
<body>

<div id="game-container">
    <!-- TOP HUD -->
    <div class="hud-header">
        <div>
            <div class="hud-title">🇮🇳 GERMANE MEDIA LLC PRESENTS</div>
            <div style="font-size:12px; font-weight:700; color:#fff;" id="display-team">TEAM: READY TO SURVIVE</div>
        </div>
        <div class="hud-badges">
            <div class="badge badge-timer" id="timer-display">⏱️ 30:00</div>
            <div class="badge badge-score" id="score-display">SCORE: 0000</div>
            <div class="badge badge-level" id="level-display">LEVEL: 0 / 10</div>
        </div>
        <div class="top-controls">
            <button class="btn-ctrl" onclick="toggleSound()" id="sound-btn">🔊 SOUND ON</button>
            <button class="btn-ctrl" onclick="useHint()" id="hint-btn">💡 HINT (3)</button>
        </div>
    </div>

    <!-- CHAOS METER -->
    <div class="chaos-container">
        <div class="chaos-bar" id="chaos-bar"></div>
        <div class="chaos-text" id="chaos-text">🔥 CHAOS METER: 10%</div>
    </div>

    <div id="alert-zone"></div>

    <!-- MAIN STAGE -->
    <div class="stage-area" id="stage">
        <!-- Dynamic content rendered by JS -->
    </div>

    <!-- LEVEL TRACKER -->
    <div class="level-tracker" id="level-tracker">
        <!-- Rendered by JS -->
    </div>
</div>

<script>
    // GAME STATE VARIABLES
    let score = 0;
    let currentLevel = 0;
    let timerSeconds = 1800; // 30 mins
    let timerInterval = null;
    let soundEnabled = true;
    let hintsLeft = 3;
    let teamName = "THE JUGAADUS";
    let chaosLevel = 10;
    let tarangWrongAttempts = 0;
    let waCorrect = 0;
    let level5Correct = 0;
    let wfhCorrect = 0;
    let bollyCorrect = 0;
    let jugaadCorrect = 0;

    // WEB AUDIO SYNTHESIZER
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    let audioCtx = null;

    function initAudio() {
        if (!audioCtx) audioCtx = new AudioContext();
    }

    function playSound(type) {
        if (!soundEnabled) return;
        initAudio();
        const now = audioCtx.currentTime;

        if (type === 'ting') {
            let osc = audioCtx.createOscillator();
            let gain = audioCtx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(880, now);
            osc.frequency.exponentialRampToValueAtTime(1760, now + 0.2);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
            osc.connect(gain); gain.connect(audioCtx.destination);
            osc.start(now); osc.stop(now + 0.2);
        } else if (type === 'beep') {
            let osc = audioCtx.createOscillator();
            let gain = audioCtx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(150, now);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
            osc.connect(gain); gain.connect(audioCtx.destination);
            osc.start(now); osc.stop(now + 0.3);
        } else if (type === 'pop') {
            let osc = audioCtx.createOscillator();
            let gain = audioCtx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(300, now);
            osc.frequency.exponentialRampToValueAtTime(900, now + 0.1);
            gain.gain.setValueAtTime(0.4, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
            osc.connect(gain); gain.connect(audioCtx.destination);
            osc.start(now); osc.stop(now + 0.1);
        } else if (type === 'cheer') {
            [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {
                let osc = audioCtx.createOscillator();
                let gain = audioCtx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(freq, now + idx * 0.08);
                gain.gain.setValueAtTime(0.3, now + idx * 0.08);
                gain.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.08 + 0.4);
                osc.connect(gain); gain.connect(audioCtx.destination);
                osc.start(now + idx * 0.08); osc.stop(now + idx * 0.08 + 0.4);
            });
        } else if (type === 'scratch') {
            let osc = audioCtx.createOscillator();
            let gain = audioCtx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(600, now);
            osc.frequency.linearRampToValueAtTime(80, now + 0.25);
            gain.gain.setValueAtTime(0.4, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
            osc.connect(gain); gain.connect(audioCtx.destination);
            osc.start(now); osc.stop(now + 0.25);
        }
    }

    function toggleSound() {
        soundEnabled = !soundEnabled;
        document.getElementById('sound-btn').innerText = soundEnabled ? "🔊 SOUND ON" : "🔇 SOUND OFF";
    }

    function updateHUD() {
        document.getElementById('score-display').innerText = `SCORE: ${String(score).padStart(4, '0')}`;
        document.getElementById('level-display').innerText = `LEVEL: ${currentLevel} / 10`;
        
        // Update Chaos Meter
        chaosLevel = Math.min(100, Math.max(10, currentLevel * 10));
        document.getElementById('chaos-bar').style.width = `${chaosLevel}%`;
        document.getElementById('chaos-text').innerText = `🔥 CHAOS METER: ${chaosLevel}%`;

        // Update dots
        const tracker = document.getElementById('level-tracker');
        tracker.innerHTML = '';
        for (let i = 1; i <= 10; i++) {
            let dot = document.createElement('div');
            dot.className = `dot ${i === currentLevel ? 'active' : ''} ${i < currentLevel ? 'done' : ''}`;
            dot.innerText = i < currentLevel ? '✓' : i;
            tracker.appendChild(dot);
        }
    }

    function startTimer() {
        if (timerInterval) clearInterval(timerInterval);
        timerInterval = setInterval(() => {
            if (timerSeconds > 0) {
                timerSeconds--;
                let mins = Math.floor(timerSeconds / 60);
                let secs = timerSeconds % 60;
                document.getElementById('timer-display').innerText = `⏱️ ${String(mins).padStart(2,'0')}:${String(secs).padStart(2,'0')}`;

                let alertZone = document.getElementById('alert-zone');
                if (timerSeconds === 300) {
                    alertZone.innerHTML = '<div class="alert-banner">⚠️ CHAOS LEVEL: HIGH! 5 MINUTES REMAINING!</div>';
                    playSound('beep');
                } else if (timerSeconds === 60) {
                    alertZone.innerHTML = '<div class="alert-banner">🚨 LAST MINUTE! FINISH THE CHAOS!</div>';
                    playSound('beep');
                } else if (timerSeconds === 0) {
                    alertZone.innerHTML = '<div class="alert-banner">⏰ TIME\'S UP! Complete your final answer!</div>';
                    clearInterval(timerInterval);
                    timerInterval = null;
                }
            }
        }, 1000);
    }

    function useHint() {
        if (hintsLeft <= 0) {
            alert("No hints remaining!");
            return;
        }
        hintsLeft--;
        score = Math.max(0, score - 50);
        document.getElementById('hint-btn').innerText = `💡 HINT (${hintsLeft})`;
        updateHUD();

        const hints = [
            "Start Screen: Click Start to kick off Friday!",
            "Level 1: Look at the road! Indian roads always have cows, chai stalls, and auto-rickshaws!",
            "Level 2: Swap the tiles until the tea cup and samosa form a clean office picture!",
            "Level 3: Think like an Indian WhatsApp group admin!",
            "Level 4: CHAI=4 letters, INDIA=5 letters, Square=4 sides, Auto=3 wheels -> 4543!",
            "Level 5: It's the most famous tea-time biscuit and noodle in India!",
            "Level 6: Choose the option that keeps your manager and family happy!",
            "Level 7: Mogambo is ALWAYS khush!",
            "Level 8: Free food always disappears first in any Indian office!",
            "Level 9: The true Jugaadu way is always the most creative local trick!",
            "Level 10: Is there REALLY any option other than TARANG SRIVASTAVA? Choose wisely!"
        ];
        alert(`💡 HINT (-50 Points): ${hints[currentLevel] || "Think like an Indian!"}`);
    }

    // SHOW RECURRING CHARACTER MODAL
    function showCharacterPopup(avatar, name, quote, nextCallback) {
        playSound('cheer');
        let stage = document.getElementById('stage');
        let modal = document.createElement('div');
        modal.className = 'char-modal';
        modal.innerHTML = `
            <div class="char-avatar">${avatar}</div>
            <div class="char-name">${name}</div>
            <div class="char-quote">"${quote}"</div>
            <button class="btn-main" id="char-btn">CONTINUE 🚀</button>
        `;
        stage.appendChild(modal);
        document.getElementById('char-btn').onclick = () => {
            modal.remove();
            nextCallback();
        };
    }

    // RENDER START SCREEN
    function renderStartScreen() {
        if (timerInterval) {
            clearInterval(timerInterval);
            timerInterval = null;
        }

        score = 0;
        currentLevel = 0;
        timerSeconds = 1800;
        hintsLeft = 3;
        tarangWrongAttempts = 0;
        teamName = "THE JUGAADUS";
        waCorrect = 0;
        level5Correct = 0;
        wfhCorrect = 0;
        bollyCorrect = 0;
        jugaadCorrect = 0;

        document.getElementById('timer-display').innerText = "⏱️ 30:00";
        document.getElementById('display-team').innerText = "TEAM: READY TO SURVIVE";
        document.getElementById('hint-btn').innerText = "💡 HINT (3)";
        document.getElementById('alert-zone').innerHTML = '';
        updateHUD();
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h1>🇮🇳 GERMANE MEDIA LLC PRESENTS</h1>
            <h2 style="font-size:32px; color:#ffd700;">THE GREAT INDIAN OFFICE CHAOS</h2>
            <p style="font-size:16px; font-weight:700; color:#ff007f;">"Can you survive a normal Friday in India?"</p>
            <div style="background:rgba(0,0,0,0.4); padding:15px; border-radius:12px; margin:15px 0; max-width:500px;">
                <p>⏱️ <strong>30 MINUTES</strong> | 🧩 <strong>10 LEVELS</strong> | 👥 <strong>5 PLAYERS</strong></p>
                <p style="font-size:12px; color:#aaa;">🚨 ALERT! It's Friday. Workday traffic, WhatsApp forwards, UPI PINs, WFH drama, and Bollywood chaos await!</p>
            </div>
            <div style="margin-bottom:15px;">
                <label style="font-size:12px; font-weight:700;">ENTER TEAM NAME:</label><br>
                <input type="text" id="team-input" value="THE JUGAADUS" style="padding:10px; border-radius:8px; border:2px solid #ffd700; background:#110d29; color:#fff; font-weight:700; text-align:center; font-size:16px;">
            </div>
            <button class="btn-main" onclick="startGame()">START THE CHAOS 🚀</button>
        `;
    }

    function startGame() {
        let input = document.getElementById('team-input').value;
        if (input.trim()) teamName = input.trim().toUpperCase();
        document.getElementById('display-team').innerText = `TEAM: ${teamName}`;
        startTimer();
        playSound('cheer');
        showCharacterPopup('👨‍💼', 'TARANG (The HR Boss)', 'Welcome to Friday! 30 minutes on the clock. Survive all 10 challenges and don\'t embarrass HR!', loadLevel1);
    }

    // LEVEL 1: TRAFFIC SIMULATOR
    let level1Targets = { cow: false, auto: false, chai: false, rider: false, scooter: false };
    function loadLevel1() {
        currentLevel = 1;
        updateHUD();
        level1Targets = { cow: false, auto: false, chai: false, rider: false, scooter: false };
        
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h2>🚗 LEVEL 1: INDIAN TRAFFIC SIMULATOR</h2>
            <p>Click and find all 5 iconic traffic items on the road!</p>
            <div class="traffic-box" id="traffic-canvas">
                <div class="traffic-target" style="top:220px; left:280px;" onclick="findTraffic('cow', this)">🐄</div>
                <div class="traffic-target" style="top:120px; left:100px;" onclick="findTraffic('auto', this)">🛺</div>
                <div class="traffic-target" style="top:40px; left:550px;" onclick="findTraffic('chai', this)">☕</div>
                <div class="traffic-target" style="top:260px; left:620px;" onclick="findTraffic('rider', this)">🏍️</div>
                <div class="traffic-target" style="top:180px; left:440px;" onclick="findTraffic('scooter', this)">🛵</div>
            </div>
            <div style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center;" id="traffic-checklist">
                <span class="badge" id="chk-cow">🐄 Cow</span>
                <span class="badge" id="chk-auto">🛺 Auto</span>
                <span class="badge" id="chk-chai">☕ Chai Stall</span>
                <span class="badge" id="chk-rider">🏍️ Helmetless Rider</span>
                <span class="badge" id="chk-scooter">🛵 Red Scooter</span>
            </div>
        `;
    }

    function findTraffic(key, el) {
        if (!level1Targets[key]) {
            level1Targets[key] = true;
            playSound('pop');
            el.classList.add('found');
            document.getElementById(`chk-${key}`).style.background = '#00ff88';
            document.getElementById(`chk-${key}`).style.color = '#000';

            if (Object.values(level1Targets).every(v => v)) {
                score += 125;
                playSound('ting');
                showCharacterPopup('👴', 'SHARMA JI', 'Beta! Even in peak Silk Board traffic, you found everything! +125 Points!', loadLevel2);
            }
        }
    }

    // LEVEL 2: CHAI BREAK CRISIS (PUZZLE)
    let puzzleState = [3, 7, 1, 9, 2, 5, 8, 4, 6];
    let selectedTileIndex = null;
    const tileIcons = ["☕", "🥐", "💻", "📱", "🍪", "📒", "🖊️", "🥪", "⏰"];

    function loadLevel2() {
        currentLevel = 2;
        updateHUD();
        puzzleState = [3, 7, 1, 9, 2, 5, 8, 4, 6];
        selectedTileIndex = null;
        renderPuzzle();
    }

    function renderPuzzle() {
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h2>☕ LEVEL 2: CHAI BREAK CRISIS</h2>
            <p>Click two tiles to swap them and assemble the office chai table (1 to 9)!</p>
            <div class="puzzle-grid" id="puzzle-grid"></div>
        `;
        let grid = document.getElementById('puzzle-grid');
        puzzleState.forEach((val, idx) => {
            let tile = document.createElement('div');
            tile.className = `puzzle-tile ${selectedTileIndex === idx ? 'selected' : ''}`;
            tile.innerHTML = `<div>${tileIcons[val-1]}<div style="font-size:10px;">${val}</div></div>`;
            tile.onclick = () => onTileClick(idx);
            grid.appendChild(tile);
        });
    }

    function onTileClick(idx) {
        playSound('pop');
        if (selectedTileIndex === null) {
            selectedTileIndex = idx;
        } else {
            let temp = puzzleState[selectedTileIndex];
            puzzleState[selectedTileIndex] = puzzleState[idx];
            puzzleState[idx] = temp;
            selectedTileIndex = null;

            if (puzzleState.every((val, i) => val === i + 1)) {
                score += 150;
                playSound('cheer');
                showCharacterPopup('☕', 'RAJU (Chai Wala)', 'Chai is ready. Productivity can wait! +150 Points!', loadLevel3);
                return;
            }
        }
        renderPuzzle();
    }

    // LEVEL 3: WHATSAPP UNIVERSITY
    let waIndex = 0;
    const waQuestions = [
        { q: 'What does a text saying "Hmm." REALLY mean?', opts: ["A. Okay", "B. I am neutral", "C. We need to talk / Danger!", "D. Nothing"], ans: 2 },
        { q: 'What does a text saying "K." mean?', opts: ["A. Passive aggressive anger", "B. Okay cool", "C. Keyboard broken", "D. Okay bro"], ans: 0 },
        { q: 'A message is "Seen at 10:42 PM". Should you reply?', opts: ["A. Reply immediately", "B. DO NOT reply unless you want trouble", "C. Send GIF", "D. Call them"], ans: 1 },
        { q: 'Uncle sends a "Good Morning Lotus GIF" in family group. What to do?', opts: ["A. Ignore it", "B. Reply with folded hands 🙏", "C. Leave group", "D. Report spam"], ans: 1 },
        { q: 'Forward: "Drinking chai cures 100% of software bugs". Reaction?', opts: ["A. Scientifically true", "B. Share with manager", "C. Acknowledge the wisdom", "D. All of the above!"], ans: 3 }
    ];

    function loadLevel3() {
        currentLevel = 3;
        updateHUD();
        waIndex = 0;
        waCorrect = 0;
        renderWA();
    }

    function renderWA() {
        let qData = waQuestions[waIndex];
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h2>📱 LEVEL 3: WHATSAPP UNIVERSITY (${waIndex+1}/5)</h2>
            <div style="background:#075e54; padding:12px; border-radius:10px; max-width:500px; width:100%; margin-bottom:15px; text-align:left;">
                <span style="color:#25d366; font-size:12px; font-weight:700;">💬 INCOMING WHATSAPP MESSAGE</span>
                <div style="background:#dcf8c6; color:#000; padding:10px; border-radius:8px; margin-top:5px; font-weight:700;">
                    ${qData.q}
                </div>
            </div>
            <div class="option-grid">
                ${qData.opts.map((opt, i) => `<button class="btn-option" onclick="answerWA(${i})">${opt}</button>`).join('')}
            </div>
        `;
    }

    function answerWA(idx) {
        if (idx === waQuestions[waIndex].ans) {
            waCorrect++;
            score += 30;
            playSound('ting');
        } else {
            playSound('beep');
        }
        updateHUD();
        waIndex++;
        if (waIndex < waQuestions.length) {
            renderWA();
        } else {
            showCharacterPopup('👨‍💻', 'ROHIT (Employee)', `WhatsApp University result: ${waCorrect}/5 correct! +${waCorrect * 30} Points!`, loadLevel4);
        }
    }

    // LEVEL 4: CRACK THE UPI CODE
    let enteredCode = "";
    function loadLevel4() {
        currentLevel = 4;
        updateHUD();
        enteredCode = "";
        renderUPI();
    }

    function renderUPI() {
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h2>🔐 LEVEL 4: CRACK THE UPI CODE</h2>
            <p>Solve the 4 clues to enter the UPI PIN:</p>
            <div style="background:rgba(0,0,0,0.3); padding:10px; border-radius:10px; max-width:500px; text-align:left; font-size:12px; margin-bottom:10px;">
                1️⃣ Number of letters in CHAI = ?<br>
                2️⃣ Number of letters in INDIA = ?<br>
                3️⃣ How many sides does a square have? = ?<br>
                4️⃣ How many wheels does an auto have? = ?
            </div>
            <div style="font-size:28px; font-weight:900; letter-spacing:10px; color:#00f2fe; margin-bottom:10px;">
                ${(enteredCode + "••••").slice(0,4)}
            </div>
            <div class="upi-keypad">
                ${[1,2,3,4,5,6,7,8,9].map(num => `<button class="key-btn" onclick="pressUPI('${num}')">${num}</button>`).join('')}
                <button class="key-btn" style="background:#ff0033;" onclick="pressUPI('C')">C</button>
                <button class="key-btn" onclick="pressUPI('0')">0</button>
                <button class="key-btn" style="background:#00ff88; color:#000;" onclick="submitUPI()">✓</button>
            </div>
        `;
    }

    function pressUPI(val) {
        playSound('pop');
        if (val === 'C') {
            enteredCode = "";
        } else if (enteredCode.length < 4) {
            enteredCode += val;
        }
        renderUPI();
    }

    function submitUPI() {
        if (enteredCode === "4543") {
            score += 150;
            playSound('cheer');
            let stage = document.getElementById('stage');
            stage.innerHTML = `
                <h2>🔓 PAYMENT SUCCESSFUL ₹0.00</h2>
                <p style="font-size:20px; color:#00ff88;">"Congratulations. You still have money." 😂</p>
            `;
            setTimeout(() => {
                showCharacterPopup('📱', 'UPI SERVER', 'Transaction completed in 0.2 seconds! +150 Points!', loadLevel5);
            }, 1500);
        } else {
            playSound('beep');
            alert("WRONG PIN! Try again! (Hint: Check the clues!)");
            enteredCode = "";
            renderUPI();
        }
    }

    // LEVEL 5: WHAT'S IN THE OFFICE?
    let level5Index = 0;
    const level5Items = [
        { name: "PARLE-G", hint: "Iconic yellow biscuit packet with a famous baby!", opts: ["PARLE-G", "BOURBON", "GOOD DAY", "HIDE & SEEK"], ans: 0 },
        { name: "SAMOSA", hint: "Triangular golden crispy snack filled with spicy potato!", opts: ["KACHORI", "SAMOSA", "BREAD PAKORA", "SPRING ROLL"], ans: 1 },
        { name: "MAGGI", hint: "2-minute yellow noodles cooked in office pantry!", opts: ["CHOWMEIN", "PASTA", "MAGGI", "RAMEN"], ans: 2 },
        { name: "DELHI METRO CARD", hint: "Smart card swiped every morning at the turnstile!", opts: ["CREDIT CARD", "DELHI METRO CARD", "GYM PASS", "PAN CARD"], ans: 1 },
        { name: "PRESSURE COOKER", hint: "Whistling kitchen hero heard during WFH calls!", opts: ["PRESSURE COOKER", "THERMOS", "KETTLE", "WATER BOTTLE"], ans: 0 }
    ];

    function loadLevel5() {
        currentLevel = 5;
        updateHUD();
        level5Index = 0;
        level5Correct = 0;
        renderLevel5();
    }

    function renderLevel5() {
        let item = level5Items[level5Index];
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h2>🍕 LEVEL 5: WHAT'S IN THE OFFICE? (${level5Index+1}/5)</h2>
            <div style="font-size:60px; margin:15px; filter:blur(2px); transition:filter 0.5s;" id="blur-obj">
                ${['🍪', '🥟', '🍜', '💳', '🍲'][level5Index]}
            </div>
            <p><strong>CLUE:</strong> "${item.hint}"</p>
            <div class="option-grid">
                ${item.opts.map((opt, i) => `<button class="btn-option" onclick="answerLevel5(${i})">${opt}</button>`).join('')}
            </div>
        `;
    }

    function answerLevel5(idx) {
        if (idx === level5Items[level5Index].ans) {
            level5Correct++;
            score += 30;
            playSound('ting');
        } else {
            playSound('beep');
        }
        updateHUD();
        level5Index++;
        if (level5Index < level5Items.length) {
            renderLevel5();
        } else {
            showCharacterPopup('👨‍🍳', 'PANTRY GUY', `Office pantry score: ${level5Correct}/5 correct! +${level5Correct * 30} Points!`, loadLevel6);
        }
    }

    // LEVEL 6: THE WFH SURVIVAL TEST
    let wfhIndex = 0;
    const wfhScenarios = [
        { q: "On a serious Google Meet. Mom asks: 'Beta, chai bana du?'", opts: ["A. Pretend internet froze", "B. Say 'One minute' and mute", "C. Start making chai", "D. Introduce Mom to VP"], ans: 1 },
        { q: "Your dog barks loudly during manager's presentation.", opts: ["A. 'Sir, that's neighbour's dog!'", "B. Bark back", "C. Leave meeting", "D. Put dog on camera"], ans: 0 },
        { q: "Manager asks: 'Share screen' (37 Chrome tabs open).", opts: ["A. Share full desktop", "B. Cry", "C. Panic close tabs & share window only", "D. Disconnect call"], ans: 2 },
        { q: "Wi-Fi dies 2 minutes before Friday deadline.", opts: ["A. Stand near window for 5G hotspot", "B. Send telegram", "C. Restart laptop 10x", "D. Blame solar flare"], ans: 0 },
        { q: "Delivery boy rings bell repeatedly during townhall.", opts: ["A. Ignore pizza", "B. Thumbs up emoji & sprint to door", "C. Scream 'AAYA!'", "D. Cancel order"], ans: 1 }
    ];

    function loadLevel6() {
        currentLevel = 6;
        updateHUD();
        wfhIndex = 0;
        wfhCorrect = 0;
        renderWFH();
    }

    function renderWFH() {
        let sc = wfhScenarios[wfhIndex];
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h2>🧑‍💻 LEVEL 6: WFH SURVIVAL TEST (${wfhIndex+1}/5)</h2>
            <p style="font-size:16px; font-weight:700; color:#ffd700;">SITUATION: "${sc.q}"</p>
            <div class="option-grid">
                ${sc.opts.map((opt, i) => `<button class="btn-option" onclick="answerWFH(${i})">${opt}</button>`).join('')}
            </div>
        `;
    }

    function answerWFH(idx) {
        if (idx === wfhScenarios[wfhIndex].ans) {
            wfhCorrect++;
            score += 40;
            playSound('ting');
        } else {
            playSound('beep');
        }
        updateHUD();
        wfhIndex++;
        if (wfhIndex < wfhScenarios.length) {
            renderWFH();
        } else {
            showCharacterPopup('🎧', 'MONU (WFH Legend)', `WFH survival score: ${wfhCorrect}/5 correct! +${wfhCorrect * 40} Points!`, loadLevel7);
        }
    }

    // LEVEL 7: GUESS THE BOLLYWOOD MOMENT
    let bollyIndex = 0;
    const bollyQuestions = [
        { q: "🚢 ❤️ 💔", opts: ["Titanic", "Dil Dhadakne Do", "Housefull", "Lagaan"], ans: 0 },
        { q: "👑 🦁", opts: ["The Lion King", "Bahubali", "RRR", "Dangal"], ans: 0 },
        { q: "🎸 ❤️ 🎤", opts: ["Aashiqui 2", "Rockstar", "Rock On", "Dil Chahta Hai"], ans: 0 },
        { q: "Dialogue: 'Mogambo ______ hua!'", opts: ["khush", "dukh", "pagal", "gussa"], ans: 0 },
        { q: "Dialogue: 'Picture abhi ______ hai mere dost!'", opts: ["baaki", "khatam", "delayed", "hit"], ans: 0 }
    ];

    function loadLevel7() {
        currentLevel = 7;
        updateHUD();
        bollyIndex = 0;
        bollyCorrect = 0;
        renderBolly();
    }

    function renderBolly() {
        let bq = bollyQuestions[bollyIndex];
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h2>🎬 LEVEL 7: BOLLYWOOD MOMENT (${bollyIndex+1}/5)</h2>
            <div style="font-size:36px; margin:15px;">${bq.q}</div>
            <div class="option-grid">
                ${bq.opts.map((opt, i) => `<button class="btn-option" onclick="answerBolly(${i})">${opt}</button>`).join('')}
            </div>
        `;
    }

    function answerBolly(idx) {
        if (idx === bollyQuestions[bollyIndex].ans) {
            bollyCorrect++;
            score += 40;
            playSound('ting');
        } else {
            playSound('beep');
        }
        updateHUD();
        bollyIndex++;
        if (bollyIndex < bollyQuestions.length) {
            renderBolly();
        } else {
            showCharacterPopup('💃', 'BOLLYWOOD DIRECTOR', `Bollywood score: ${bollyCorrect}/5 correct! +${bollyCorrect * 40} Points!`, loadLevel8);
        }
    }

    // LEVEL 8: THE GREAT INDIAN FOOD WAR
    let foodIndex = 0;
    const foodWars = [
        { q: "ROUND 1: Samosa 🆚 Kachori", opts: ["Samosa", "Kachori"] },
        { q: "ROUND 2: Chai 🆚 Coffee", opts: ["Chai", "Coffee"] },
        { q: "ROUND 3: Pizza 🆚 Biryani", opts: ["Pizza", "Biryani"] },
        { q: "ROUND 4: Momos 🆚 Golgappa", opts: ["Momos", "Golgappa"] },
        { q: "BONUS: Which food disappears FIRST in office pantry?", opts: ["Free Samosas!", "Anything complimentary!"] }
    ];

    function loadLevel8() {
        currentLevel = 8;
        updateHUD();
        foodIndex = 0;
        renderFood();
    }

    function renderFood() {
        let fw = foodWars[foodIndex];
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h2>🍛 LEVEL 8: THE GREAT INDIAN FOOD WAR (${foodIndex+1}/5)</h2>
            <p style="font-size:18px; font-weight:700;">${fw.q}</p>
            <div style="display:flex; gap:20px; margin-top:20px; justify-content:center; width:100%; max-width:500px;">
                ${fw.opts.map((opt) => `<button class="btn-main" style="flex:1;" onclick="answerFood()">${opt}</button>`).join('')}
            </div>
        `;
    }

    function answerFood() {
        playSound('pop');
        foodIndex++;
        if (foodIndex < foodWars.length) {
            renderFood();
        } else {
            score += 150;
            showCharacterPopup('🍕', 'PANTRY HERO', 'Food debate settled without regional wars! +150 Points!', loadLevel9);
        }
    }

    // LEVEL 9: JUGAAD MASTER
    let jugaadIndex = 0;
    const jugaadProbs = [
        { q: "PROBLEM: Phone at 2%, no charger available.", opts: ["A. Plug USB into colleague's laptop while they get chai", "B. Put phone in fridge", "C. Cry", "D. Use solar power"], ans: 0 },
        { q: "PROBLEM: Online meeting in 2 mins, internet gone.", opts: ["A. Run to balcony for phone 5G hotspot", "B. Send letter", "C. Blame ISP", "D. Restart router 10x"], ans: 0 },
        { q: "PROBLEM: Delivery guy calls: 'Sir exact location?'", opts: ["A. 'Bhaiya, red water tank ke paas banyan tree ke peeche!'", "B. Send GPS again", "C. Cancel order", "D. Sing song"], ans: 0 }
    ];

    function loadLevel9() {
        currentLevel = 9;
        updateHUD();
        jugaadIndex = 0;
        jugaadCorrect = 0;
        renderJugaad();
    }

    function renderJugaad() {
        let jp = jugaadProbs[jugaadIndex];
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h2>🧩 LEVEL 9: JUGAAD MASTER (${jugaadIndex+1}/3)</h2>
            <p style="font-size:16px; font-weight:700; color:#ffd700;">${jp.q}</p>
            <div class="option-grid">
                ${jp.opts.map((opt, i) => `<button class="btn-option" onclick="answerJugaad(${i})">${opt}</button>`).join('')}
            </div>
        `;
    }

    function answerJugaad(idx) {
        if (idx === jugaadProbs[jugaadIndex].ans) {
            jugaadCorrect++;
            score += 67;
            playSound('ting');
        } else {
            playSound('beep');
        }
        updateHUD();
        jugaadIndex++;
        if (jugaadIndex < jugaadProbs.length) {
            renderJugaad();
        } else {
            showCharacterPopup('💡', 'JUGAAD KING', `Jugaad score: ${jugaadCorrect}/3 correct! +${jugaadCorrect * 67} Points!`, triggerLevel10Intro);
        }
    }

    // LEVEL 10 INTRO & FINALE (TARANG SRIVASTAVA)
    function triggerLevel10Intro() {
        currentLevel = 10;
        updateHUD();
        playSound('scratch');
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <div style="animation: pulse 0.5s infinite;">
                <h1 style="font-size:40px; color:#ff007f;">🚨 FINAL BOSS LEVEL 🚨</h1>
                <h2 style="font-size:24px; color:#ffd700;">THE ULTIMATE QUESTION</h2>
            </div>
            <p>One final decision remains to survive Friday...</p>
            <button class="btn-main" onclick="loadLevel10()">FACE THE FINAL QUESTION 👑</button>
        `;
    }

    function loadLevel10() {
        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h2>👑 LEVEL 10: THE FINAL QUESTION</h2>
            <h1 style="font-size:32px; color:#ffd700; margin:20px 0;">WHO DO YOU THINK IS THE BEST HR?</h1>
            <div class="option-grid">
                <button class="btn-option" style="border-color:#ffd700; font-size:16px;" onclick="answerTarang('A')">OPTION A: Tarang Srivastava</button>
                <button class="btn-option" onclick="answerTarang('B')">OPTION B: The HR Robot 🤖</button>
                <button class="btn-option" onclick="answerTarang('C')">OPTION C: Google HR</button>
                <button class="btn-option" onclick="answerTarang('D')">OPTION D: That HR Guy From LinkedIn</button>
            </div>
            <div id="tarang-feedback" style="margin-top:15px; font-size:18px; font-weight:900;"></div>
        `;
    }

    function answerTarang(option) {
        let fb = document.getElementById('tarang-feedback');
        if (option === 'A') {
            score += 500;
            playSound('cheer');
            
            // Confetti
            for(let i=0; i<30; i++) {
                let p = document.createElement('div');
                p.className = 'confetti-particle';
                p.style.left = Math.random()*100 + '%';
                p.style.background = ['#ffd700', '#ff007f', '#00ff88'][Math.floor(Math.random()*3)];
                document.body.appendChild(p);
            }

            stage.innerHTML = `
                <h1 style="font-size:45px; color:#00ff88;">🎉 CORRECT! 🎉</h1>
                <h2 style="color:#ffd700;">"Obviously. Did you really think there was another answer?" ❤️</h2>
                <p style="font-size:18px; color:#fff;">+500 BONUS POINTS AWARDED!</p>
                <button class="btn-main" onclick="showGameOver()">VIEW FINAL SCORECARD 🏆</button>
            `;
        } else {
            tarangWrongAttempts++;
            playSound('scratch');
            if (tarangWrongAttempts === 1) {
                fb.innerHTML = `<span style="color:#ff0033;">❌ WRONG ANSWER 😡 Seriously? Try again!</span>`;
            } else if (tarangWrongAttempts === 2) {
                fb.innerHTML = `<span style="color:#ff0033;">😡 DO YOU REALLY THINK I AM NOT GOOD? Think carefully!</span>`;
            } else {
                fb.innerHTML = `<span style="color:#ffd700;">"Okay... now you're just doing this on purpose." 😂</span>`;
            }
        }
    }

    // GAME OVER / FINAL SCORECARD
    function showGameOver() {
        if (timerInterval) clearInterval(timerInterval);
        playSound('cheer');

        let totalScore = score;
        let rank = "";
        let rankDesc = "";

        if (totalScore >= 1800) {
            rank = "🏆 INDIAN OFFICE LEGENDS";
            rankDesc = "Promotions for everyone! Sharma Ji is proud of your team!";
        } else if (totalScore >= 1400) {
            rank = "🔥 PROFESSIONAL JUGAADU";
            rankDesc = "You can fix any office crisis with tape and a hot cup of chai.";
        } else if (totalScore >= 1100) {
            rank = "😎 FRIDAY SURVIVORS";
            rankDesc = "You survived Friday without getting sent to HR!";
        } else if (totalScore >= 800) {
            rank = "☕ CHAI BREAK SPECIALISTS";
            rankDesc = "More chai, less work. Still a respectable Friday effort.";
        } else {
            rank = "😭 PLEASE TAKE ANOTHER HR FRIDAY";
            rankDesc = "Tarang will see your team in his office on Monday morning.";
        }

        let stage = document.getElementById('stage');
        stage.innerHTML = `
            <h1>🎉 GAME OVER - CHAOS SURVIVED!</h1>
            <h2 style="color:#ffd700;">TEAM: ${teamName}</h2>
            <div style="background:rgba(0,0,0,0.5); padding:20px; border-radius:15px; border:2px solid #00ff88; margin:15px 0; max-width:600px; width:100%;">
                <div style="font-size:36px; font-weight:900; color:#00ff88;">TOTAL SCORE: ${totalScore}</div>
                <div style="font-size:20px; font-weight:700; color:#ffd700; margin-top:10px;">${rank}</div>
                <p style="font-size:14px; color:#ddd; margin-top:5px;">"${rankDesc}"</p>
            </div>

            <div style="display:flex; gap:15px; flex-wrap:wrap;">
                <button class="btn-main" onclick="renderStartScreen()">PLAY AGAIN 🔄</button>
            </div>
        `;
    }

    // INITIALIZE ON LOAD
    renderStartScreen();
</script>
</body>
</html>
"""

def main():
    # Render the interactive single page application component inside Streamlit
    st.components.v1.html(HTML_GAME, height=920, scrolling=True)

if __name__ == "__main__":
    main()
