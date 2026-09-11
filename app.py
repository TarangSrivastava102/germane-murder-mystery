import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='The Great Indian Office Chaos', page_icon='🇮🇳', layout='wide')
st.markdown('''<style>header,footer,#MainMenu{visibility:hidden}.block-container{padding:0!important;max-width:100%!important}</style>''', unsafe_allow_html=True)

GAME = r'''<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>
*{box-sizing:border-box}body{margin:0;background:#0d0a1d;color:white;font-family:Arial,sans-serif;min-height:100vh;padding:18px}.app{max-width:1000px;min-height:850px;margin:auto;padding:28px;border:4px solid #ffd400;border-radius:22px;background:#211b49;box-shadow:0 0 35px #ffd40055;display:flex;flex-direction:column}.top{text-align:center}.small{color:#ff4d9d;font-weight:bold}.title{font-size:clamp(28px,5vw,54px);color:#ffd400;font-weight:900;margin:18px 0}.sub{color:#ff4d9d;font-size:20px;font-weight:bold}.card{background:#100b29;border-radius:18px;padding:25px;text-align:center;margin:25px auto;width:min(100%,720px)}input{width:100%;padding:16px;border:2px solid #ffd400;border-radius:10px;background:#0d0a1d;color:white;font-size:18px;text-align:center}.btn{border:0;border-radius:35px;padding:17px 30px;margin:12px 5px;background:linear-gradient(90deg,#ff7a00,#ff005c);color:#fff;font-weight:900;font-size:18px;cursor:pointer;box-shadow:0 7px 0 #b90048}.btn:active{transform:translateY(4px);box-shadow:0 3px 0 #b90048}.option{display:block;width:100%;margin:12px 0;padding:18px;border:2px solid #00eaff;border-radius:12px;background:#281e51;color:#fff;font-size:17px;font-weight:bold;cursor:pointer}.option:hover{background:#3b2d70}.hud{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;border:2px solid #ff4d9d;padding:15px;border-radius:12px}.feedback{min-height:30px;font-size:18px;font-weight:bold;margin-top:18px}.good{color:#00ff88}.bad{color:#ff476f}.hidden{display:none}</style></head><body><div class="app"><div id="root"></div></div>
<script>
'use strict';
const levels=[
['WhatsApp Office Emergency','Your manager sends “URGENT” at 5:59 PM. What do you do?',['Reply “Sure, will do” and disappear','Reply professionally and clarify priority','Forward it to the entire company','Switch off Wi‑Fi'],1],
['The Chai Crisis','The office chai is finished. Your next move?',['Start a peaceful chai committee','Blame the intern','Cry in the pantry','Order 47 cups'],0],
['UPI PIN Drama','A colleague asks for your UPI PIN. You should…',['Share it privately','Post it in the group','Never share your PIN','Ask for their OTP too'],2],
['Friday Traffic','You are late because of traffic. Best response?',['Inform your manager early','Say the dog ate your bike','Ignore every call','Blame Mercury retrograde'],0],
['WFH Camera','You are on a video call. What is safest?',['Check camera and background','Join while sleeping','Use a fake moustache','Keep microphone always on'],0],
['Meeting That Could Be Email','A meeting has no agenda. You…',['Ask for an agenda and objective','Invite 20 more people','Start a dance party','Leave without a word'],0],
['Salary Spreadsheet','You notice an error in payroll data. You…',['Hide it','Verify and report it immediately','Change everyone’s salary','Send it to a random group'],1],
['Office Politics','Two coworkers are arguing. You…',['Take sides immediately','Listen neutrally and involve the right person','Record it for memes','Add more drama'],1],
['Deadline Attack','A deadline is impossible. You…',['Communicate risks and renegotiate scope','Promise everything silently','Blame the printer','Delete the project'],0],
['HR Final Boss','What makes a great workplace?',['Fear','Trust, clarity and respect','Unlimited meetings','No holidays'],1]
];
let team='',score=0,index=0,seconds=1800,clock=null,answered=false;
const root=document.getElementById('root');
function esc(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function start(){team=(document.getElementById('team').value||'TEAM').trim().toUpperCase();if(!team)team='TEAM';score=0;index=0;seconds=1800;clearInterval(clock);clock=setInterval(tick,1000);renderLevel();}
function tick(){seconds--;const el=document.getElementById('time');if(el)el.textContent=format(seconds);if(seconds<=0){clearInterval(clock);gameOver(true);}}
function format(s){return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0');}
function renderStart(){root.innerHTML=`<div class="top"><div class="small">IN GERMANE MEDIA LLC PRESENTS</div><div class="title">THE GREAT INDIAN OFFICE CHAOS</div><div class="sub">Can you survive a normal Friday in India?</div></div><div class="card"><h2>⏱ 30 MINUTES | 🧩 10 LEVELS | 👥 5 PLAYERS</h2><p>Workday traffic, WhatsApp forwards, UPI PINs, WFH drama and Bollywood chaos await!</p><h3>ENTER TEAM NAME</h3><input id="team" maxlength="30" value="TARANG" placeholder="Enter team name"><br><button class="btn" id="start">START THE CHAOS 🚀</button></div>`;document.getElementById('start').addEventListener('click',start);document.getElementById('team').addEventListener('keydown',e=>{if(e.key==='Enter')start();});}
function renderLevel(){const l=levels[index];root.innerHTML=`<div class="hud"><b>TEAM: ${esc(team)}</b><b>LEVEL: ${index+1}/10</b><b>SCORE: ${score}</b><b>TIME: <span id="time">${format(seconds)}</span></b></div><div class="card"><h1>${esc(l[0])}</h1><p>${esc(l[0]==='HR Final Boss'?'Choose wisely, HR legend!':'Choose the best office response.')}</p><div id="opts">${l[2].map((x,i)=>`<button class="option" data-i="${i}">${String.fromCharCode(65+i)}. ${esc(x)}</button>`).join('')}</div><div id="feedback" class="feedback"></div></div>`;document.querySelectorAll('.option').forEach(b=>b.addEventListener('click',()=>answer(Number(b.dataset.i))));}
function answer(choice){if(answered)return;answered=true;const l=levels[index],fb=document.getElementById('feedback');if(choice===l[3]){score+=100;fb.className='feedback good';fb.textContent='✅ Correct! +100 points';}else{fb.className='feedback bad';fb.textContent='❌ Not quite! The correct answer was '+String.fromCharCode(65+l[3])+'.';}document.querySelectorAll('.option').forEach(b=>b.disabled=true);setTimeout(()=>{answered=false;index++;if(index>=levels.length)gameOver(false);else renderLevel();},1000);}
function gameOver(timeout){clearInterval(clock);root.innerHTML=`<div class="top"><div class="title">${timeout?'⏰ TIME UP!':'🎉 CHAOS SURVIVED!'}</div><div class="sub">TEAM: ${esc(team)}</div></div><div class="card"><h1 class="good">FINAL SCORE: ${score}</h1><h2>${score>=800?'🏆 OFFICE LEGEND':'☕ FRIDAY SURVIVOR'}</h2><p>Thanks for surviving The Great Indian Office Chaos.</p><button class="btn" id="again">PLAY AGAIN 🔄</button></div>`;document.getElementById('again').addEventListener('click',renderStart);}
renderStart();
</script></body></html>'''

components.html(GAME, height=950, scrolling=True)
