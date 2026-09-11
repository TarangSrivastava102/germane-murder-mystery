import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="The Great Office Chaos",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

GAME_HTML = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Great Office Chaos</title>
<style>
:root{
  --bg:#080b12;
  --panel:#111722;
  --panel2:#171f2d;
  --yellow:#ffd43b;
  --orange:#ff8a3d;
  --red:#ff4d5a;
  --blue:#4da3ff;
  --green:#4ee19b;
  --white:#f7f9fc;
  --muted:#aeb8c8;
  --border:#2a3445;
}
*{box-sizing:border-box}
body{
  margin:0;background:
  radial-gradient(circle at 10% 0%,rgba(255,212,59,.12),transparent 30%),
  radial-gradient(circle at 90% 20%,rgba(77,163,255,.10),transparent 28%),
  var(--bg);
  color:var(--white);
  font-family:Arial,Helvetica,sans-serif;
}
button{font:inherit}
#app{max-width:1150px;margin:auto;padding:22px}
.topbar{
  display:flex;justify-content:space-between;align-items:center;gap:15px;
  padding:12px 16px;border:1px solid var(--border);background:rgba(17,23,34,.92);
  border-radius:18px;position:sticky;top:8px;z-index:20;backdrop-filter:blur(10px)
}
.brand{font-weight:900;letter-spacing:.5px}
.brand span{color:var(--yellow)}
.stats{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.pill{border:1px solid var(--border);background:#0d131d;border-radius:999px;padding:8px 13px;font-size:14px}
#timer{font-weight:900;color:var(--yellow);min-width:90px;text-align:center}
#soundBtn{cursor:pointer}
.hero{text-align:center;padding:45px 15px 28px}
.kicker{color:var(--yellow);font-weight:900;letter-spacing:3px;font-size:13px}
h1{font-size:clamp(40px,7vw,78px);line-height:.95;margin:13px 0}
.hero h1 span{color:var(--orange)}
.subtitle{max-width:720px;margin:0 auto;color:var(--muted);font-size:18px;line-height:1.5}
.cta{
  margin-top:28px;background:var(--yellow);color:#111;border:0;border-radius:14px;
  padding:15px 25px;font-weight:900;cursor:pointer;box-shadow:0 8px 25px rgba(255,212,59,.16)
}
.cta:hover{transform:translateY(-1px)}
.card{
  background:linear-gradient(145deg,var(--panel),#0e141e);
  border:1px solid var(--border);border-radius:22px;padding:25px;
  box-shadow:0 20px 60px rgba(0,0,0,.18)
}
.level-head{display:flex;justify-content:space-between;gap:15px;align-items:flex-start}
.level-number{color:var(--yellow);font-weight:900;letter-spacing:1px}
h2{font-size:34px;margin:7px 0 8px}
.instruction{color:var(--muted);font-size:16px;line-height:1.5}
.progress{height:9px;background:#202938;border-radius:99px;overflow:hidden;margin:18px 0 25px}
.progress div{height:100%;background:linear-gradient(90deg,var(--yellow),var(--orange));width:10%;transition:width .4s}
.question{font-size:21px;font-weight:800;margin:22px 0}
.options{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:13px}
.option{
  min-height:64px;background:var(--panel2);color:var(--white);border:1px solid var(--border);
  border-radius:15px;padding:14px 16px;text-align:left;cursor:pointer;transition:.15s;
}
.option:hover{border-color:var(--yellow);transform:translateY(-2px)}
.option.correct{border-color:var(--green);background:rgba(78,225,155,.12)}
.option.wrong{border-color:var(--red);background:rgba(255,77,90,.12);animation:shake .25s}
@keyframes shake{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.feedback{
  margin-top:17px;padding:15px 17px;border-radius:14px;background:#0c121c;border:1px solid var(--border);
  min-height:52px;font-weight:700
}
.feedback.good{border-color:rgba(78,225,155,.5);color:var(--green)}
.feedback.bad{border-color:rgba(255,77,90,.5);color:#ff8f98}
.next{
  margin-top:18px;background:var(--blue);color:white;border:0;border-radius:13px;padding:13px 20px;
  font-weight:900;cursor:pointer;display:none
}
.visual{
  border:1px solid var(--border);border-radius:18px;background:#0b1018;
  padding:25px;margin:15px 0 20px;min-height:220px;display:flex;align-items:center;justify-content:center
}
.desk{display:grid;grid-template-columns:repeat(5,1fr);gap:15px;width:min(800px,100%)}
.obj{
  background:#171f2d;border:2px solid #2b3648;border-radius:17px;padding:20px 10px;
  text-align:center;font-size:46px;cursor:pointer;transition:.15s
}
.obj span{display:block;font-size:13px;color:var(--muted);margin-top:8px}
.obj:hover{border-color:var(--yellow);transform:scale(1.03)}
.soundbox{text-align:center}
.sound-icon{font-size:80px;margin:5px}
.sound-btn{
  background:#202a3a;border:1px solid #354157;color:white;border-radius:50%;
  width:90px;height:90px;font-size:35px;cursor:pointer
}
.codebox{display:flex;gap:9px;justify-content:center;margin:20px 0}
.codebox input{
  width:60px;height:70px;text-align:center;font-size:30px;font-weight:900;
  color:white;background:#0a1018;border:2px solid #344055;border-radius:12px
}
.code-hint{text-align:center;color:var(--muted)}
.puzzle{
  display:grid;grid-template-columns:repeat(3,92px);grid-template-rows:repeat(3,92px);
  gap:6px;justify-content:center;margin:12px auto 22px
}
.tile{
  background:#1d2736;border:2px solid #44516a;border-radius:10px;display:flex;align-items:center;
  justify-content:center;font-size:42px;cursor:pointer;user-select:none;position:relative
}
.tile.selected{border-color:var(--yellow);box-shadow:0 0 0 3px rgba(255,212,59,.16)}
.tile small{position:absolute;top:4px;left:6px;font-size:10px;color:#728098}
.target{
  text-align:center;color:var(--muted);font-size:13px;margin-bottom:10px
}
.diff-grid{display:grid;grid-template-columns:1fr 1fr;gap:15px}
.scene{
  background:linear-gradient(145deg,#182233,#101721);border:1px solid var(--border);
  border-radius:16px;padding:18px;min-height:260px
}
.scene h3{margin-top:0;color:var(--yellow)}
.scene-items{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.scene-item{background:#0b111b;border:1px solid #2d394c;border-radius:12px;padding:14px;text-align:center;font-size:30px}
.whatsapp{max-width:650px;margin:auto;background:#101923;border-radius:18px;overflow:hidden;border:1px solid var(--border)}
.wa-head{background:#172433;padding:15px;font-weight:900}
.msg{padding:11px 14px;margin:9px 12px;border-radius:13px;max-width:80%;line-height:1.4}
.msg.left{background:#202b38}
.msg.right{background:#264d42;margin-left:auto}
.emoji-big{text-align:center;font-size:70px;padding:20px}
.final{
  text-align:center;padding:25px 10px
}
.final h2{font-size:45px}
.final-options{max-width:700px;margin:25px auto;display:grid;grid-template-columns:1fr 1fr;gap:13px}
.final .option{text-align:center;min-height:70px;font-size:17px}
.overlay{
  position:fixed;inset:0;background:rgba(0,0,0,.78);display:none;align-items:center;justify-content:center;
  z-index:100;padding:20px
}
.popup{
  width:min(620px,100%);background:#111722;border:2px solid var(--yellow);border-radius:24px;
  padding:30px;text-align:center;box-shadow:0 30px 100px rgba(0,0,0,.5)
}
.popup .big{font-size:68px}
.popup h3{font-size:30px;margin:8px 0}
.popup p{color:var(--muted);line-height:1.5}
.confetti{position:fixed;inset:0;pointer-events:none;z-index:110;display:none}
.confetti i{position:absolute;width:9px;height:18px;animation:fall 2.2s linear forwards}
@keyframes fall{to{transform:translateY(110vh) rotate(720deg);opacity:.9}}
@media(max-width:700px){
  #app{padding:10px}.topbar{position:relative}.options,.final-options,.diff-grid{grid-template-columns:1fr}
  .desk{grid-template-columns:repeat(2,1fr)}.puzzle{grid-template-columns:repeat(3,76px);grid-template-rows:repeat(3,76px)}
  .tile{font-size:34px}.hero{padding-top:28px}.hero h1{font-size:48px}.level-head{display:block}
}
</style>
</head>
<body>
<div id="app">
  <div class="topbar">
    <div class="brand">GERMANE MEDIA <span>• OFFICE CHAOS</span></div>
    <div class="stats">
      <div class="pill">Level <b id="levelStat">0/10</b></div>
      <div class="pill">Score <b id="score">0</b></div>
      <div class="pill" id="timer">25:00</div>
      <button class="pill" id="soundBtn" onclick="toggleSound()">🔊 Sound ON</button>
    </div>
  </div>

  <section id="home" class="hero">
    <div class="kicker">GERMANE MEDIA LLC PRESENTS</div>
    <h1>THE GREAT<br><span>OFFICE CHAOS</span></h1>
    <p class="subtitle">
      Someone has created complete chaos in the office. Your team has 10 easy challenges
      to solve it. Chai, WhatsApp, puzzles, codes, objects and a little bit of madness.
    </p>
    <button class="cta" onclick="startGame()">🚨 START THE CHAOS</button>
  </section>

  <section id="game" style="display:none">
    <div class="card">
      <div class="level-head">
        <div>
          <div class="level-number" id="levelKicker">LEVEL 1</div>
          <h2 id="title"></h2>
          <div class="instruction" id="instruction"></div>
        </div>
      </div>
      <div class="progress"><div id="progressBar"></div></div>
      <div id="content"></div>
      <div id="feedback" class="feedback"></div>
      <button id="nextBtn" class="next" onclick="nextLevel()">NEXT CHALLENGE →</button>
    </div>
  </section>
</div>

<div class="overlay" id="popupOverlay">
  <div class="popup">
    <div class="big" id="popupEmoji">🎉</div>
    <h3 id="popupTitle">Correct!</h3>
    <p id="popupText"></p>
    <button class="cta" onclick="closePopup()">Continue</button>
  </div>
</div>

<div class="confetti" id="confetti"></div>

<script>
let level=0, score=0, timeLeft=25*60, timerId=null, soundOn=true;
let answered=false, selectedTile=null, puzzleState=[], finalMistakes=0;

const levels = [
  {
    title:"Find What Is Missing",
    instruction:"Look at the very normal Indian office desk. One important thing is missing. Click the missing object.",
    points:100
  },
  {
    title:"Guess That Sound",
    instruction:"Press PLAY, listen carefully, and choose the sound. It is something you hear in normal Indian life.",
    points:100
  },
  {
    title:"Crack the Chai Code",
    instruction:"Each emoji has a number. Add them from left to right and enter the 4-digit code.",
    points:125
  },
  {
    title:"Assemble the Chai Break",
    instruction:"Click two tiles to swap them. Put the 9 pieces in the correct order. No need to rush.",
    points:150
  },
  {
    title:"Who Is Avoiding The Meeting?",
    instruction:"Read the WhatsApp chat. Choose the person who is obviously trying to escape the meeting.",
    points:100
  },
  {
    title:"Spot The Difference",
    instruction:"Compare the two office scenes. Click the ONE item that is different.",
    points:125
  },
  {
    title:"What Is This?",
    instruction:"The picture is zoomed in. Identify the everyday Indian object.",
    points:100
  },
  {
    title:"Decode The Emojis",
    instruction:"What very familiar office situation do these emojis describe?",
    points:100
  },
  {
    title:"The Indian Office Code",
    instruction:"Count the letters in each word. CHAI, CUP, TEA, PHONE. Put the four numbers together.",
    points:150
  },
  {
    title:"The Most Important Question",
    instruction:"This is the final question. Choose wisely. HR is watching. 👀",
    points:200
  }
];

function startGame(){
  document.getElementById("home").style.display="none";
  document.getElementById("game").style.display="block";
  level=0;score=0;timeLeft=25*60;finalMistakes=0;
  document.getElementById("score").textContent=score;
  if(timerId) clearInterval(timerId);
  timerId=setInterval(tick,1000);
  renderLevel();
  beep("start");
}

function tick(){
  if(timeLeft<=0){
    clearInterval(timerId);
    timeLeft=0;
    updateTimer();
    showPopup("⏰","TIME'S UP!","The clock has stopped, but you can still finish the final question.");
    return;
  }
  timeLeft--;
  updateTimer();
}
function updateTimer(){
  let m=Math.floor(timeLeft/60),s=timeLeft%60;
  document.getElementById("timer").textContent=String(m).padStart(2,"0")+":"+String(s).padStart(2,"0");
  if(timeLeft<=300) document.getElementById("timer").style.color="#ff8f98";
  else document.getElementById("timer").style.color="var(--yellow)";
}

function renderLevel(){
  answered=false;selectedTile=null;
  const L=levels[level];
  document.getElementById("levelKicker").textContent="LEVEL "+(level+1);
  document.getElementById("levelStat").textContent=(level+1)+"/10";
  document.getElementById("title").textContent=L.title;
  document.getElementById("instruction").textContent=L.instruction;
  document.getElementById("progressBar").style.width=((level+1)*10)+"%";
  document.getElementById("feedback").className="feedback";
  document.getElementById("feedback").textContent="";
  document.getElementById("nextBtn").style.display="none";

  const c=document.getElementById("content");
  if(level===0) renderMissing(c);
  if(level===1) renderSound(c);
  if(level===2) renderChaiCode(c);
  if(level===3) renderPuzzle(c);
  if(level===4) renderWhatsapp(c);
  if(level===5) renderDifference(c);
  if(level===6) renderObject(c);
  if(level===7) renderEmoji(c);
  if(level===8) renderOfficeCode(c);
  if(level===9) renderFinal(c);
}

function correct(message){
  if(answered) return;
  answered=true;
  score += levels[level].points;
  document.getElementById("score").textContent=score;
  const f=document.getElementById("feedback");
  f.className="feedback good";
  f.textContent="✅ Correct! "+message+"  +"+levels[level].points+" points";
  document.getElementById("nextBtn").style.display="inline-block";
  beep("correct");
}
function wrong(message="Not this one. Try again!"){
  const f=document.getElementById("feedback");
  f.className="feedback bad";
  f.textContent="❌ "+message;
  beep("wrong");
}

function renderMissing(c){
  c.innerHTML=`
    <div class="visual">
      <div class="desk">
        <div class="obj" onclick="correct('The chai is always important.')">💻<span>Laptop</span></div>
        <div class="obj" onclick="correct('The chai is always important.')">🖱️<span>Mouse</span></div>
        <div class="obj" onclick="correct('The chai is always important.')">📒<span>Notebook</span></div>
        <div class="obj" onclick="correct('The chai is always important.')">🔌<span>Charger</span></div>
        <div class="obj" onclick="wrong('Nope. Look again. What keeps Indian offices alive?')">🍪<span>Biscuit</span></div>
      </div>
    </div>
    <div class="question">Which important office item is missing?</div>
    <div class="options">
      <button class="option" onclick="correct('The chai is always important.')">☕ Chai</button>
      <button class="option" onclick="wrong()">🔋 Power bank</button>
      <button class="option" onclick="wrong()">🎧 Headphones</button>
      <button class="option" onclick="wrong()">🧴 Sanitizer</button>
    </div>`;
}

function renderSound(c){
  c.innerHTML=`
    <div class="visual soundbox">
      <div class="sound-icon">🔊</div>
      <button class="sound-btn" onclick="playIndianSound()">▶️</button>
      <div style="margin-top:12px;color:var(--muted)">Press play. You can listen more than once.</div>
    </div>
    <div class="question">What sound did you hear?</div>
    <div class="options">
      <button class="option" onclick="correct('Exactly. Chai time has a sound.')">☕ Pressure cooker whistle</button>
      <button class="option" onclick="wrong()">🖨️ Office printer</button>
      <button class="option" onclick="wrong()">🚗 Car horn</button>
      <button class="option" onclick="wrong()">📞 Phone ringing</button>
    </div>`;
}

function playIndianSound(){
  if(!soundOn) return;
  const ctx=new (window.AudioContext||window.webkitAudioContext)();
  let o=ctx.createOscillator(),g=ctx.createGain();
  o.type="sine";o.frequency.setValueAtTime(700,ctx.currentTime);
  o.frequency.exponentialRampToValueAtTime(2100,ctx.currentTime+.9);
  g.gain.setValueAtTime(.001,ctx.currentTime);
  g.gain.exponentialRampToValueAtTime(.22,ctx.currentTime+.08);
  g.gain.exponentialRampToValueAtTime(.001,ctx.currentTime+1.05);
  o.connect(g);g.connect(ctx.destination);o.start();o.stop(ctx.currentTime+1.1);
}

function renderChaiCode(c){
  c.innerHTML=`
    <div class="visual" style="display:block;text-align:center">
      <div style="font-size:55px;letter-spacing:12px">☕ 🍪 🥛 🍩</div>
      <div style="font-size:20px;margin-top:18px">2 &nbsp;&nbsp; 4 &nbsp;&nbsp; 1 &nbsp;&nbsp; 7</div>
      <div class="code-hint">Enter the numbers from left to right.</div>
      <div class="codebox">
        <input maxlength="1" inputmode="numeric" id="c1">
        <input maxlength="1" inputmode="numeric" id="c2">
        <input maxlength="1" inputmode="numeric" id="c3">
        <input maxlength="1" inputmode="numeric" id="c4">
      </div>
      <button class="cta" onclick="checkCode()">🔓 UNLOCK</button>
    </div>
    <div class="question">What is the 4-digit code?</div>`;
}
function checkCode(){
  const code=["c1","c2","c3","c4"].map(id=>document.getElementById(id).value).join("");
  if(code==="2417") correct("The chai locker is open!");
  else wrong("Wrong code. Read the numbers from left to right.");
}

const solvedPuzzle=["☕","🫖","🍪","🥛","🍩","📱","💻","📝","🔑"];
function renderPuzzle(c){
  puzzleState=[...solvedPuzzle].sort(()=>Math.random()-.5);
  if(puzzleState.join("")===solvedPuzzle.join("")) [puzzleState[0],puzzleState[1]]=[puzzleState[1],puzzleState[0]];
  c.innerHTML=`
    <div class="target">🧩 Click one tile, then another tile to swap them. Assemble the chai-break picture.</div>
    <div class="puzzle" id="puzzle"></div>
    <div style="text-align:center;color:var(--muted);font-size:13px">Correct order: chai → kettle → biscuit → milk → donut → phone → laptop → note → key</div>`;
  drawPuzzle();
}
function drawPuzzle(){
  const p=document.getElementById("puzzle");p.innerHTML="";
  puzzleState.forEach((x,i)=>{
    const d=document.createElement("div");d.className="tile"+(selectedTile===i?" selected":"");
    d.innerHTML=x+"<small>"+(i+1)+"</small>";
    d.onclick=()=>tileClick(i);p.appendChild(d);
  });
}
function tileClick(i){
  if(answered) return;
  if(selectedTile===null){selectedTile=i;drawPuzzle();return}
  [puzzleState[selectedTile],puzzleState[i]]=[puzzleState[i],puzzleState[selectedTile]];
  selectedTile=null;drawPuzzle();
  if(puzzleState.join("")===solvedPuzzle.join("")) correct("Perfect! Chai break assembled.");
}

function renderWhatsapp(c){
  c.innerHTML=`
    <div class="visual">
      <div class="whatsapp">
        <div class="wa-head">💬 Office Group — 4:55 PM</div>
        <div class="msg left"><b>Manager:</b><br>Guys, quick call at 5?</div>
        <div class="msg right">Sure 👍</div>
        <div class="msg left">Yes, joining.</div>
        <div class="msg right">Can we do tomorrow? 😅</div>
        <div class="msg left"><b>Manager:</b><br>It will only take 5 minutes.</div>
        <div class="msg right">I am just stepping out for chai...</div>
      </div>
    </div>
    <div class="question">Who is most likely avoiding the meeting?</div>
    <div class="options">
      <button class="option" onclick="correct('You caught the chai escape plan.')">😅 The person going for chai</button>
      <button class="option" onclick="wrong()">👨‍💼 The manager</button>
      <button class="option" onclick="wrong()">🙋 The person who said yes</button>
      <button class="option" onclick="wrong()">📱 The group admin</button>
    </div>`;
}

function renderDifference(c){
  c.innerHTML=`
    <div class="diff-grid">
      <div class="scene"><h3>LEFT DESK</h3><div class="scene-items">
        <div class="scene-item">☕</div><div class="scene-item">💻</div><div class="scene-item">🌱</div>
        <div class="scene-item">🖱️</div><div class="scene-item">📒</div><div class="scene-item">🖊️</div>
      </div></div>
      <div class="scene"><h3>RIGHT DESK</h3><div class="scene-items">
        <div class="scene-item">☕</div><div class="scene-item">💻</div><div class="scene-item">🌱</div>
        <div class="scene-item">🖱️</div><div class="scene-item">📕</div><div class="scene-item">🖊️</div>
      </div></div>
    </div>
    <div class="question">What is different?</div>
    <div class="options">
      <button class="option" onclick="wrong()">☕ The cup</button>
      <button class="option" onclick="wrong()">💻 The laptop</button>
      <button class="option" onclick="correct('Yes! The notebook changed from blue to red.')">📒 The notebook</button>
      <button class="option" onclick="wrong()">🌱 The plant</button>
    </div>`;
}

function renderObject(c){
  c.innerHTML=`
    <div class="visual">
      <div style="text-align:center">
        <div style="font-size:150px;filter:drop-shadow(0 10px 20px rgba(0,0,0,.3))">🥫</div>
        <div style="font-size:13px;color:var(--muted)">ZOOMED-IN VIEW</div>
      </div>
    </div>
    <div class="question">What everyday Indian thing is this?</div>
    <div class="options">
      <button class="option" onclick="correct('Parle-G has entered the chat.')">🍪 Biscuit packet</button>
      <button class="option" onclick="wrong()">🧴 Shampoo bottle</button>
      <button class="option" onclick="wrong()">🥤 Cold drink</button>
      <button class="option" onclick="wrong()">🖨️ Printer cartridge</button>
    </div>`;
}

function renderEmoji(c){
  c.innerHTML=`
    <div class="visual"><div class="emoji-big">💻 + 📅 + 😐 + ☕</div></div>
    <div class="question">What does this describe?</div>
    <div class="options">
      <button class="option" onclick="correct('Monday meeting. Everyone knows this feeling.')">😐 Monday morning meeting</button>
      <button class="option" onclick="wrong()">🎂 Birthday party</button>
      <button class="option" onclick="wrong()">🏖️ Holiday</button>
      <button class="option" onclick="wrong()">🏏 Cricket match</button>
    </div>`;
}

function renderOfficeCode(c){
  c.innerHTML=`
    <div class="visual" style="display:block;text-align:center">
      <div style="font-size:30px;font-weight:900;line-height:1.9">
        ☕ CHAI = ?<br>
        🥤 CUP = ?<br>
        🍵 TEA = ?<br>
        📱 PHONE = ?
      </div>
      <div class="code-hint">Count the letters. Put the four numbers together.</div>
      <div class="codebox">
        <input maxlength="1" inputmode="numeric" id="o1">
        <input maxlength="1" inputmode="numeric" id="o2">
        <input maxlength="1" inputmode="numeric" id="o3">
        <input maxlength="1" inputmode="numeric" id="o4">
        <input maxlength="1" inputmode="numeric" id="o5">
      </div>
      <button class="cta" onclick="checkOfficeCode()">🔐 CHECK CODE</button>
    </div>`;
}
function checkOfficeCode(){
  const code=["o1","o2","o3","o4","o5"].map(id=>document.getElementById(id).value).join("");
  if(code==="43335") correct("Correct. 4, 3, 3, 5 = 4335. The extra 5 is your bonus confidence point. 😄");
  else if(code==="4335") correct("Correct! CHAI=4, CUP=3, TEA=3, PHONE=5.");
  else wrong("Count the letters: CHAI=4, CUP=3, TEA=3, PHONE=5.");
}

function renderFinal(c){
  c.innerHTML=`
    <div class="final">
      <div style="font-size:65px">🏆</div>
      <h2>THE MOST IMPORTANT QUESTION</h2>
      <p class="subtitle">After all this hard work, there is only one thing left to decide.</p>
      <div class="final-options">
        <button class="option" onclick="finalWrong()">👨‍💼 Alex</button>
        <button class="option" onclick="finalWrong()">👩‍💼 Priya</button>
        <button class="option" onclick="finalWrong()">🧑‍💻 Rahul</button>
        <button class="option" onclick="finalCorrect()">👑 Tarang Srivastava</button>
      </div>
      <div id="finalMessage" class="feedback"></div>
    </div>`;
}
function finalWrong(){
  finalMistakes++;
  const f=document.getElementById("finalMessage");
  f.className="feedback bad";
  if(finalMistakes===1){
    f.textContent="❌ 😡 WRONG ANSWER! Are you serious?";
  }else if(finalMistakes===2){
    f.textContent="😡 Do you really think I am not good?";
  }else{
    f.textContent="BRO... after everything HR has done for you? 😂";
  }
  beep("wrong");
}
function finalCorrect(){
  if(answered) return;
  answered=true;
  score += levels[9].points;
  document.getElementById("score").textContent=score;
  document.getElementById("finalMessage").className="feedback good";
  document.getElementById("finalMessage").textContent="🏆 CORRECT! Obviously. Tarang Srivastava is the BEST HR. +"+levels[9].points+" points";
  document.getElementById("nextBtn").style.display="inline-block";
  beep("win");confetti();
}

function nextLevel(){
  if(level<9){level++;renderLevel();window.scrollTo({top:0,behavior:"smooth"});beep("next");}
  else finishGame();
}
function finishGame(){
  if(timerId) clearInterval(timerId);
  document.getElementById("game").innerHTML=`
    <div class="card" style="text-align:center;padding:55px 25px">
      <div style="font-size:80px">🎉🏆🎉</div>
      <div class="kicker">CASE CLOSED</div>
      <h2>THE CHAOS HAS BEEN SOLVED!</h2>
      <p class="subtitle">Final score: <b style="color:var(--yellow);font-size:30px">${score}</b></p>
      <p class="subtitle">And yes... the best HR is still Tarang Srivastava. 😎</p>
      <button class="cta" onclick="location.reload()">🔄 PLAY AGAIN</button>
    </div>`;
  confetti();
  beep("win");
}

function showPopup(e,t,p){
  document.getElementById("popupEmoji").textContent=e;
  document.getElementById("popupTitle").textContent=t;
  document.getElementById("popupText").textContent=p;
  document.getElementById("popupOverlay").style.display="flex";
}
function closePopup(){document.getElementById("popupOverlay").style.display="none"}

function toggleSound(){
  soundOn=!soundOn;
  document.getElementById("soundBtn").textContent=soundOn?"🔊 Sound ON":"🔇 Sound OFF";
  if(soundOn) beep("correct");
}

function beep(type){
  if(!soundOn) return;
  try{
    const ctx=new (window.AudioContext||window.webkitAudioContext)();
    const notes=type==="correct"?[660,880]:type==="wrong"?[180,120]:type==="win"?[523,659,784,1047]:[440];
    notes.forEach((freq,i)=>{
      let o=ctx.createOscillator(),g=ctx.createGain();
      o.type=type==="wrong"?"sawtooth":"sine";o.frequency.value=freq;
      g.gain.setValueAtTime(.001,ctx.currentTime+i*.09);
      g.gain.exponentialRampToValueAtTime(.12,ctx.currentTime+i*.09+.02);
      g.gain.exponentialRampToValueAtTime(.001,ctx.currentTime+i*.09+.16);
      o.connect(g);g.connect(ctx.destination);o.start(ctx.currentTime+i*.09);o.stop(ctx.currentTime+i*.09+.18);
    });
  }catch(e){}
}

function confetti(){
  const box=document.getElementById("confetti");box.innerHTML="";box.style.display="block";
  const symbols=["🟨","🟧","🟥","🟦","🟩","⭐"];
  for(let i=0;i<80;i++){
    const x=document.createElement("i");
    x.textContent=symbols[Math.floor(Math.random()*symbols.length)];
    x.style.left=Math.random()*100+"%";x.style.top=(-10-Math.random()*30)+"px";
    x.style.animationDelay=Math.random()*1.2+"s";
    x.style.fontSize=(10+Math.random()*12)+"px";
    box.appendChild(x);
  }
  setTimeout(()=>box.style.display="none",3500);
}
</script>
</body>
</html>
"""

components.html(GAME_HTML, height=1250, scrolling=True)
