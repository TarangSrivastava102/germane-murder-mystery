import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Friday Fun: Office Chaos", page_icon="🎉", layout="wide")

HTML = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
*{box-sizing:border-box}
body{margin:0;font-family:Arial,sans-serif;background:linear-gradient(135deg,#fff4d6,#e9f7ff 45%,#fce8f3);color:#172033}
button,input{font:inherit}
button{cursor:pointer;border:0}
.app{max-width:1100px;margin:auto;padding:22px}
.top{display:flex;justify-content:space-between;gap:15px;align-items:center;background:#ffffffd9;border:2px solid #fff;padding:15px 20px;border-radius:20px;box-shadow:0 8px 25px #26324a18}
.logo{font-weight:900;letter-spacing:2px;color:#6c38c9}
.badge{background:#172033;color:white;padding:9px 14px;border-radius:99px;font-weight:bold}
.hero{text-align:center;min-height:82vh;display:flex;flex-direction:column;align-items:center;justify-content:center}
.hero h1{font-size:clamp(42px,8vw,88px);line-height:.95;margin:18px 0;color:#6c38c9}
.hero p{max-width:650px;font-size:18px;line-height:1.6;color:#596579}
.card{background:#ffffffed;border:2px solid white;border-radius:28px;padding:28px;box-shadow:0 15px 40px #26324a20}
.setup{max-width:520px;width:100%;text-align:left}
label{display:block;font-weight:800;margin-bottom:8px}
input{width:100%;padding:15px;border:2px solid #dce3ef;border-radius:14px;margin-bottom:15px}
.btn{padding:15px 23px;border-radius:14px;background:linear-gradient(135deg,#7544db,#ee5b9b);color:white;font-weight:900;box-shadow:0 7px 0 #5226a2;margin:8px 5px}
.btn:active{transform:translateY(4px);box-shadow:0 3px 0 #5226a2}
.btn.alt{background:#172033;box-shadow:0 7px 0 #080d18}
.grid{display:grid;grid-template-columns:190px 1fr;gap:18px;margin-top:20px}
.sidebar{background:#ffffffd9;border:2px solid white;border-radius:22px;padding:15px}
.levels{display:grid;gap:8px;margin-top:12px}
.lvl{padding:11px;border-radius:12px;text-align:left;background:#edf1f8;color:#687386;font-weight:bold}
.lvl.active{background:#7544db;color:white}
.lvl.done{background:#d8f5df;color:#1b7a43}
.main{min-width:0}
.title{font-size:clamp(28px,5vw,48px);margin:8px 0;color:#172033}
.sub{color:#657187;line-height:1.6}
.scene{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:20px 0}
.tile{min-height:120px;background:#f7f9fd;border:3px solid #e1e7f1;border-radius:20px;padding:16px;font-size:35px}
.tile span{display:block;font-size:15px;font-weight:800;margin-top:8px}
.tile:hover{border-color:#7544db;background:#f1eaff}
.question{background:#fff8df;border:2px dashed #e9bd4a;border-radius:20px;padding:20px;margin-top:20px}
.options{display:flex;flex-wrap:wrap;gap:10px;margin:15px 0}
.option{padding:13px 16px;background:white;border:2px solid #dfe5ef;border-radius:13px;font-weight:bold}
.option:hover{border-color:#7544db}
.feedback{padding:15px;border-radius:15px;background:#ffe4e4;color:#a92323;font-weight:bold;margin-top:12px}
.success{padding:15px;border-radius:15px;background:#dcf8e5;color:#19733c;font-weight:bold;margin-top:12px}
.progress{height:12px;background:#e6ebf3;border-radius:99px;overflow:hidden;margin:15px 0}
.progress div{height:100%;background:linear-gradient(90deg,#7544db,#ee5b9b);width:0}
.score{font-size:28px;font-weight:900;color:#7544db;margin:15px 0}
@media(max-width:750px){.grid{grid-template-columns:1fr}.scene{grid-template-columns:repeat(2,1fr)}}
</style>
</head>
<body>
<div id="app" class="app"></div>
<script>
const levels=[
{title:"The Chai Emergency",intro:"The office chai has arrived, but someone has taken the last biscuit. Find the most suspicious clue.",emoji:["☕","🍪","🧾","🖨️","📱","🪑"],labels:["Chai cup","Missing biscuit","Printer bill","Printer","Team chat","Empty chair"],question:"Who is most likely responsible for the missing biscuit?",options:["The person saying 'I am on a diet'","The person guarding the snack drawer","The office cat","The client"],correct:0,win:"Correct! The 'diet' person has been caught near the biscuit box. Very suspicious."},
{title:"The WhatsApp Group",intro:"The team group has 147 unread messages. You have 30 seconds before someone asks: 'Guys, any update?'",emoji:["📱","💬","😂","🙏","🔔","👀"],labels:["147 messages","Good morning","Meme","Reminder","Notification","Seen by all"],question:"What is the safest reply to a message saying 'Any update?'",options:["Working on it, will share shortly","Seen","👍","Ask what update"],correct:0,win:"Perfect corporate survival! Short, polite, and nobody can complain."},
{title:"The Meeting That Could Be An Email",intro:"A meeting invite says 15 minutes. It has 23 attendees and no agenda. Choose your survival move.",emoji:["📅","🪑","🎤","📊","⏰","😵"],labels:["Calendar","Chairs","Mic","Slides","Clock","Confusion"],question:"What should you do first?",options:["Ask for an agenda","Start another meeting","Share a 40-slide deck","Say 'Let's circle back'"],correct:0,win:"Excellent. You saved 23 people from a meeting without a purpose."},
{title:"The Lunchbox Mystery",intro:"Someone has taken the wrong lunchbox from the fridge. The evidence is spicy.",emoji:["🍱","🌶️","🥗","🧃","🥄","🧊"],labels:["Lunchbox","Spicy chutney","Salad","Juice","Spoon","Fridge"],question:"What is the most Indian-office solution?",options:["Announce it politely in the group","Start a detective agency","Eat everyone’s lunch","Blame the intern"],correct:0,win:"Diplomatic and deliciously sensible. The lunchbox owner has been found."},
{title:"The Excel Olympics",intro:"You are given a spreadsheet with 18 tabs named Final, Final2, FinalNew, FinalLatest and FinalReallyLatest.",emoji:["📈","📊","⌨️","🖱️","🔢","🗂️"],labels:["Charts","Numbers","Keyboard","Mouse","Formula","18 tabs"],question:"What is the smartest next step?",options:["Ask which file is the actual final","Rename everything FinalFinal","Close the laptop","Use a random tab"],correct:0,win:"Correct! Always confirm the source before performing Excel gymnastics."},
{title:"The Work From Home Test",intro:"Your camera is on. Your internet is unstable. A family member walks behind you with a pressure cooker.",emoji:["💻","📶","🎧","🍳","🏠","🙈"],labels:["Laptop","Wi-Fi","Headset","Kitchen","Home","Camera"],question:"What is the best professional response?",options:["Mute, acknowledge, and continue","Pretend the screen froze","Blame the Wi-Fi forever","Leave the meeting dramatically"],correct:0,win:"Smooth recovery! Professionalism with a little Indian-home realism."},
{title:"The Salary Day Celebration",intro:"It is salary day. Everyone suddenly becomes active on Slack, Teams, WhatsApp and email.",emoji:["💸","🎉","📲","🛍️","🍕","🧮"],labels:["Salary","Celebration","Phone","Shopping","Pizza","Calculator"],question:"What is the most relatable salary-day plan?",options:["Pay bills, save some, enjoy some","Order everything online","Buy a car before lunch","Forget all responsibilities"],correct:0,win:"Balanced answer! Responsible adult with a little treat-yourself energy."},
{title:"The Friday Fun Challenge",intro:"HR announces a fun activity. One person says, 'I have a client call.' Another says, 'I am shy.' Choose the best move.",emoji:["🎤","🎲","😂","🏆","🎯","🕺"],labels:["Mic","Game","Laughter","Prize","Target","Dance"],question:"How do you get more people involved?",options:["Keep it easy and voluntary","Force everyone to dance","Cancel the activity","Make a 12-page form"],correct:0,win:"Exactly! Fun works best when people feel comfortable joining."},
{title:"The Office Politics Detector",intro:"Someone says, 'I am not saying anything, but...' The room becomes silent.",emoji:["👀","🤐","☕","🗣️","🚩","🧠"],labels:["Eyes","Silence","Chai","Talk","Red flag","Brain"],question:"What is the best HR-style response?",options:["Listen calmly and focus on facts","Forward it to everyone","Add more gossip","Pretend not to hear anything"],correct:0,win:"Correct! Listen, stay neutral, and bring the conversation back to facts."},
{title:"The Best HR Question",intro:"The final challenge is extremely important. Choose carefully. The office is watching.",emoji:["🏆","👑","🎉","💼","❤️","⭐"],labels:["Trophy","Crown","Fun","HR","Heart","Star"],question:"Who do you think is the best HR?",options:["Tarang Srivastava","The person from Finance","The office printer","Nobody"],correct:0,win:"Correct answer! Tarang Srivastava is officially the best HR. 🎉"}
];
let state={screen:"home",team:"",level:0,score:0,selected:null,wrong:0,feedback:"",finished:false};

function home(){
document.getElementById("app").innerHTML=`
<div class="hero">
<div class="logo">GERMANE MEDIA • FRIDAY FUN</div>
<h1>THE GREAT<br>OFFICE CHAOS 🎉</h1>
<p>A colorful, relatable office adventure with 10 fun challenges. No boring quizzes. Just chai, meetings, lunchboxes, Excel drama and HR magic.</p>
<button class="btn" onclick="setup()">START THE CHAOS 🚀</button>
</div>`}

function setup(){
document.getElementById("app").innerHTML=`
<div class="hero"><div class="card setup">
<div class="logo">PLAYER SETUP</div><h2>What should we call your team?</h2>
<input id="teamName" maxlength="30" placeholder="e.g. Team Chai Champions">
<button class="btn" onclick="begin()">LET'S GO 🎮</button>
</div></div>`}

function begin(){
state.team=(document.getElementById("teamName").value.trim()||"Team Chai Champions");
state.screen="game";state.level=0;state.score=0;state.selected=null;state.wrong=0;state.feedback="";
render();
}

function shell(){
return `<div class="top"><div><div class="logo">GERMANE MEDIA • OFFICE CHAOS</div><b>${state.team}</b></div><div class="badge">⭐ ${state.score} points</div></div>
<div class="grid"><aside class="sidebar"><b>YOUR JOURNEY</b><div class="levels">${levels.map((x,i)=>`<button class="lvl ${i===state.level?"active":""} ${i<state.level?"done":""}" ${i<=state.level?`onclick="jump(${i})"`:"disabled"}>${i<state.level?"✓":i+1}. ${x.title}</button>`).join("")}</div><div class="score">${state.score}<small style="font-size:13px;color:#657187"> points</small></div></aside><main class="main">${level()}</main></div>`}

function level(){
let l=levels[state.level];
return `<div class="card"><div class="logo">LEVEL ${state.level+1} OF 10</div><h1 class="title">${l.title}</h1><p class="sub">${l.intro}</p><div class="progress"><div style="width:${state.level*10}%"></div></div>
<div class="scene">${l.emoji.map((e,i)=>`<button class="tile" onclick="inspect(${i})">${e}<span>${l.labels[i]}</span></button>`).join("")}</div>
<div class="question"><h2>${l.question}</h2><div class="options">${l.options.map((o,i)=>`<button class="option" onclick="choose(${i})">${o}</button>`).join("")}</div>
${state.feedback?`<div class="${state.feedback.startsWith("Correct")?"success":"feedback"}">${state.feedback}</div>`:""}
${state.selected!==null?`<button class="btn" onclick="submitAnswer()">LOCK ANSWER 🔒</button>`:""}</div></div>`}

function inspect(i){
state.feedback=["Good observation!","This clue looks suspicious.","Classic office evidence.","Someone definitely knows something.","Interesting... add this to your mental evidence board.","Very relatable clue."][i];
render();
}
function choose(i){state.selected=i;render()}
function submitAnswer(){
let l=levels[state.level];
if(state.selected===l.correct){
state.score+=100;state.feedback=l.win;
setTimeout(()=>{
if(state.level===9){state.finished=true;state.screen="finish";render()}
else{state.level++;state.selected=null;state.wrong=0;state.feedback="";render()}
},900);
}else{
state.wrong++;
if(state.level===9){
state.feedback=state.wrong===1?"😡 WRONG ANSWER! Are you seriously choosing someone else?":"😤 Do you really think I am not good?";
}else{
state.feedback=state.wrong===1?"😅 Not quite! Try again.":"😂 Still wrong! Think like an Indian office survivor.";
}
render();
}}
function jump(i){if(i<=state.level){state.level=i;state.selected=null;state.feedback="";render()}}
function finish(){
document.getElementById("app").innerHTML=`<div class="hero"><div class="card"><div class="logo">CASE CLOSED</div><h1 class="title">YOU SURVIVED OFFICE CHAOS! 🏆</h1><p class="sub">${state.team}, your final score is:</p><div class="score">${state.score} points</div><h2>And yes... Tarang Srivastava is the best HR. 👑</h2><p class="sub">Thank you for playing. Now go have chai and discuss who got the highest score.</p><button class="btn" onclick="location.reload()">PLAY AGAIN 🔄</button></div></div>`}
function render(){if(state.screen==="home")home();else if(state.screen==="setup")setup();else if(state.screen==="finish")finish();else document.getElementById("app").innerHTML=shell()}
home();
</script>
</body>
</html>
"""
components.html(HTML, height=2400, scrolling=False)
