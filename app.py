import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Germane Media LLC — The Blackbox Incident",
    page_icon="🕵️",
    layout="wide",
)

HTML = r'''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{--bg:#080808;--p:#121212;--g:#d5b267;--r:#c95757;--w:#eee9df;--m:#969188;--l:#302d28;--ok:#8fbd9a}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#080808;color:var(--w);font-family:Arial,sans-serif}
body{background:radial-gradient(circle at 75% 0%,#292016,#080808 40%)}
button,input,select{font:inherit}button{cursor:pointer}
.app{max-width:1480px;margin:auto;padding:18px}
.top{display:flex;justify-content:space-between;align-items:center;gap:15px;border-bottom:1px solid var(--l);padding:8px 0 14px;position:sticky;top:0;background:#090909f2;z-index:10}
.brand{font-size:11px;letter-spacing:3px;color:var(--g);font-weight:800}
.teamline{font-size:12px;color:#777;margin-top:5px}
.timer{font:900 27px monospace;color:var(--g)}
.timer.urgent{color:#e05a5a}
.tiny{background:#101010;border:1px solid #3b3730;color:#c6c0b5;padding:10px 13px;font-size:11px;letter-spacing:1px}
.hero{min-height:88vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.hero h1{font:normal 82px/.9 Georgia,serif;letter-spacing:2px;margin:18px 0}
.hero h2{letter-spacing:5px;font-size:14px;color:#c8bfae}
.hero p{max-width:720px;color:var(--m);line-height:1.7}
.cta{background:linear-gradient(135deg,#e3c27c,#a47e3b);border:0;color:#090909;padding:14px 23px;font-weight:900;letter-spacing:2px;margin-top:16px}
.setup{width:min(560px,92%);border:1px solid var(--l);background:#101010;padding:26px;text-align:left}
.setup label{font-size:11px;letter-spacing:2px;color:#888;display:block;margin-bottom:8px}
.setup input{width:100%;padding:13px;background:#080808;color:white;border:1px solid #3a352d}
.rules,.note{margin:16px 0;padding:13px;background:#0b0b0b;border-left:2px solid #705b37;color:#aaa;font-size:12px;line-height:1.6}
.grid{display:grid;grid-template-columns:215px minmax(0,1fr) 245px;gap:15px;margin-top:16px}
.side,.right,.panel{background:linear-gradient(150deg,#151515,#0d0d0d);border:1px solid var(--l)}
.side,.right{padding:15px}.side{min-height:700px}.panel{padding:25px;min-height:700px}
.section{font-size:10px;letter-spacing:2px;color:#777;font-weight:bold}
.levels{display:grid;gap:6px;margin-top:13px}
.lvl{background:#101010;border:1px solid #302d28;color:#888;padding:10px;text-align:left;font-size:11px}
.lvl.active{border-color:var(--g);color:var(--g);background:#1d180f}.lvl.done{color:var(--ok)}
.score{border:1px solid var(--l);padding:13px;margin:17px 0;font:900 28px monospace;color:var(--g)}
.ev{background:#0a0a0a;border-left:2px solid #705b37;padding:8px;margin:6px 0;font-size:11px;color:#c6c0b6}
.head{display:flex;justify-content:space-between;gap:20px;border-bottom:1px solid var(--l);padding-bottom:15px;margin-bottom:17px}
.no{color:var(--g);font-size:10px;letter-spacing:3px}.title{font:38px Georgia,serif;margin-top:6px}
.brief{color:var(--m);line-height:1.55}
.scene{height:390px;border:1px solid #413a30;background:radial-gradient(circle at 50% 35%,#474239,#171615 62%);position:relative;overflow:hidden}
.scene:before{content:"CONFERENCE ROOM // 04:17";position:absolute;top:13px;left:15px;color:#ad9158;font:11px monospace}
.scene:after{content:"";position:absolute;left:10%;bottom:48px;width:80%;height:22px;background:#241d16;border-top:2px solid #594b38}
.obj{position:absolute;background:#0c0c0de8;border:1px solid #74603a;color:#ead6a5;padding:9px;font-size:10px;z-index:2}
.obj.found{border-color:var(--ok);color:var(--ok)}
.o1{left:44%;top:68px}.o2{left:18%;bottom:76px}.o3{left:38%;bottom:90px}.o4{left:58%;bottom:92px}.o5{left:72%;bottom:72px}.o6{left:76%;top:115px}
.answers{display:flex;flex-wrap:wrap;gap:8px}
.ans{background:#101010;border:1px solid #35312b;color:#c1bbb1;padding:11px 13px;text-align:left}
.ans:hover{border-color:#716044}.ans.sel{border-color:var(--g);background:#211a0d;color:#f0d18b}
.q{margin-top:19px;border-top:1px solid var(--l);padding-top:17px}
.feedback{padding:12px;background:#17140f;border-left:3px solid var(--g);margin-top:12px;line-height:1.5}
.feedback.good{border-left-color:var(--ok)}.feedback.bad{border-left-color:var(--r)}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.card{padding:14px;background:#0b0b0b;border:1px solid var(--l);min-height:105px;color:var(--w);text-align:left}
.card b{display:block;margin-bottom:7px}.card small{color:#999;line-height:1.45}
.order-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}
.order{padding:13px;background:#0b0b0b;border:1px dashed #534938;color:#c9c0b0;min-height:60px;text-align:left}
.order.selected{border-color:var(--g);background:#211b10;color:#f0d18b}
.sequence{min-height:72px;margin-top:12px;padding:12px;background:#eee6d3;color:#252119;font:16px/1.5 Georgia,serif}
.terminal{font:13px/1.8 monospace;background:#050505;border:1px solid #393a32;padding:19px;color:#a9c7a9;white-space:pre-line}
.code{display:block;margin:18px auto;padding:12px;width:220px;text-align:center;font:28px monospace;letter-spacing:9px;background:#090909;border:1px solid #5d5039;color:#fff}
.match{display:grid;grid-template-columns:1fr 1fr;gap:15px}.matchcol{border:1px solid var(--l);padding:12px;background:#0a0a0a}
.matchrow{display:flex;justify-content:space-between;gap:8px;align-items:center;border-bottom:1px solid #27241f;padding:10px 0}.matchrow:last-child{border-bottom:0}
.logic{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px}.logicbox{padding:13px;background:#0b0b0b;border:1px solid var(--l);min-height:92px}
.logicbox b{color:var(--g);display:block;margin-bottom:7px}
.final{text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center}
.stamp{border:2px solid var(--g);padding:10px 20px;letter-spacing:6px;color:var(--g);transform:rotate(-3deg)}
.reveal{font:62px Georgia,serif;color:#f0d18b;margin:18px}.rank{letter-spacing:3px;color:#d7b56a}
.timeline{display:grid;gap:6px;width:min(760px,100%)}.time{display:grid;grid-template-columns:82px 1fr;background:#0b0b0b;border-left:2px solid #614e30;padding:9px;text-align:left}.time b{font:11px monospace;color:var(--g)}
.modal{position:fixed;inset:0;background:#000d;display:grid;place-items:center;z-index:50}.modalbox{width:min(820px,92%);max-height:82vh;overflow:auto;background:#111;border:1px solid #5b4b32;padding:22px}.close{float:right;background:none;border:0;color:#aaa;font-size:24px}
@media(max-width:1050px){.grid{grid-template-columns:1fr}.side,.right{min-height:auto}.cards{grid-template-columns:repeat(2,1fr)}}
@media(max-width:650px){.hero h1{font-size:54px}.title{font-size:29px}.cards,.order-grid,.logic,.match{grid-template-columns:1fr}.top{align-items:flex-start}.timer{font-size:22px}}
</style>
</head>
<body><div class="app" id="app"></div>
<script>
"use strict";

const SUSPECTS=[
{name:"Alex Morgan",role:"COO",init:"AM",alibi:"Private video meeting, 4:00–4:30.",detail:"Recording gap from 4:13–4:19.",motive:"Feared the file would expose a bad executive decision."},
{name:"Maya Kapoor",role:"Head of Marketing",init:"MK",alibi:"Preparing a campaign deck.",detail:"Laptop stayed connected to the studio display.",motive:"Wanted the project for a competing campaign."},
{name:"Ryan Carter",role:"Technology Lead",init:"RC",alibi:"Fixing a server issue.",detail:"His card pinged the security room at 4:14.",motive:"Had the knowledge to disable security."},
{name:"Sophie Bennett",role:"Finance Manager",init:"SB",alibi:"Reviewing invoices.",detail:"Found an unusual transfer earlier that day.",motive:"Wanted to stop an unauthorized payment."},
{name:"Daniel Ross",role:"Sales Director",init:"DR",alibi:"On a client call.",detail:"Call records show it ended at 4:09.",motive:"Wanted confidential project details."},
{name:"Olivia Reed",role:"People & Culture",init:"OR",alibi:"Employee meeting in Room 2.",detail:"No independent timestamp from 4:16–4:23.",motive:"Found evidence Victor planned to blame her department."}
];

const LEVEL_NAMES=[
"SCENE SWEEP","WITNESS CONTRADICTIONS","TIMELINE LOCK","CIPHER ROOM",
"ACCESS LOGS","EVIDENCE MATCH","LOGIC TEST","INTERROGATION","VAULT CODE","FINAL ACCUSATION"
];

let S={
screen:"open",team:"",level:0,score:0,remain:1800,start:0,paused:false,hints:3,
evidence:[],found:[],sel:"",wrong:0,temp:{},feedback:"",
final:{who:"",why:"",how:"",proof:""}
};

function esc(x){return String(x).replace(/[&<>"]/g,a=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[a]));}
function addEvidence(items){items.forEach(x=>{if(!S.evidence.includes(x))S.evidence.push(x)});}
function scoreFor(l){return [100,125,150,150,175,175,200,225,250,400][l];}

function start(){
 const el=document.getElementById("team");
 S.team=(el&&el.value.trim())||"Team Sherlock";
 S.start=Date.now();S.screen="game";S.level=0;S.remain=1800;
 render();clock();
}
function clock(){
 if(S.screen!=="game")return;
 if(!S.paused)S.remain=Math.max(0,1800-Math.floor((Date.now()-S.start)/1000));
 updateTimer();
 if(S.remain===0){S.level=9;S.feedback="TIME'S UP — you still have one final accusation.";render();return;}
 setTimeout(clock,1000);
}
function updateTimer(){
 const e=document.getElementById("timer");if(!e)return;
 const m=Math.floor(S.remain/60),s=S.remain%60;
 e.textContent=String(m).padStart(2,"0")+":"+String(s).padStart(2,"0");
 e.className="timer "+(S.remain<600?"urgent":"");
}
function togglePause(){
 S.paused=!S.paused;
 if(!S.paused)S.start=Date.now()-(1800-S.remain)*1000;
 render();
}
function success(level){
 const bonus=S.wrong===0?25:0;
 S.score+=scoreFor(level)+bonus;
 S.feedback="✓ CASE FILE SOLVED — new evidence unlocked.";
 setTimeout(()=>{S.level=Math.min(9,level+1);S.sel="";S.wrong=0;S.temp={};S.feedback="";render();},650);
}
function fail(msg){
 S.wrong++;S.score=Math.max(0,S.score-(S.wrong===1?15:25));
 S.feedback="✕ "+msg;render();
}
function check(level,ok,msg){if(ok)success(level);else fail(msg);}

function open(){
 document.getElementById("app").innerHTML=`
 <div class="hero">
  <div class="brand">GERMANE MEDIA LLC PRESENTS</div>
  <h1>THE BLACKBOX<br>INCIDENT</h1>
  <h2>10-LEVEL TEAM MYSTERY</h2>
  <p>Six suspects. One missing project file. A seven-minute blackout. Ten challenges stand between your team and the truth.<br><br><b>FUN FRIDAY MODE:</b> Share your screen, debate every clue, and solve it as one team.</p>
  <p><b>Nothing is revealed automatically.</b> Inspect, compare, decode, reconstruct and prove your accusation.<br><span style="color:#8fbd9a">Tip: talk it out — the game is designed to be solved together.</span></p>
  <button class="cta" onclick="setup()">START INVESTIGATION</button>
 </div>`;
}
function setup(){
 document.getElementById("app").innerHTML=`
 <div class="hero">
  <div class="brand">CASE FILE // INITIALIZE</div>
  <h2 style="font-size:30px;letter-spacing:1px">ENTER YOUR TEAM</h2>
  <div class="setup">
   <label>TEAM NAME</label>
   <input id="team" placeholder="e.g. Team Sherlock" maxlength="28">
   <div class="rules"><b>10 LEVELS • 30 MINUTES • 3 HINTS</b><br>
   Wrong answers cost points, but keep moving — you can recover. Each solved level unlocks evidence. Several levels require a precise sequence or combination. <b>Best played with one person sharing their screen while the whole team discusses.</b></div>
   <button class="cta" onclick="start()">BEGIN CASE</button>
  </div>
 </div>`;
 setTimeout(()=>document.getElementById("team")?.focus(),50);
}
function head(n,t,b){
 return `<div class="head"><div><div class="no">CASE FILE ${String(n).padStart(2,"0")}</div><div class="title">${t}</div></div><div style="font-size:10px;color:#666">30 MIN INVESTIGATION</div></div><div class="brief">${b}</div>`;
}
function shell(){
 return `<div class="top">
 <div><div class="brand">GERMANE MEDIA LLC PRESENTS</div><div class="teamline">${esc(S.team)} // INVESTIGATION</div></div>
 <div><button class="tiny" onclick="togglePause()">${S.paused?"RESUME":"PAUSE"}</button>
 <button class="tiny" onclick="evidence()">EVIDENCE</button> <span id="timer" class="timer">30:00</span></div></div>
 <div class="grid">
 <aside class="side"><div class="section">CASE PROGRESS</div><div class="levels">
 ${LEVEL_NAMES.map((n,i)=>`<button class="lvl ${i===S.level?"active":""} ${i<S.level?"done":""}" ${i<S.level?`onclick="S.level=${i};S.feedback='';S.sel='';S.temp={};render()"`:"disabled"}>${String(i+1).padStart(2,"0")} — ${n}</button>`).join("")}
 </div><div class="score"><div class="section">LIVE SCORE</div>${S.score}</div><div class="teamline" style="margin-top:10px;color:#8fbd9a">🤝 TEAM MODE • Talk it out</div>
 <button class="tiny" style="width:100%" onclick="chars()">SUSPECT FILES</button></aside>
 <main>${level()}</main>
 <aside class="right"><div class="section">EVIDENCE INVENTORY</div>
 ${S.evidence.length?S.evidence.map(x=>`<div class="ev">${esc(x)}</div>`).join(""):"<p style='color:#555;font-size:11px'>No evidence collected yet.</p>"}
 <div class="section" style="margin-top:18px">HINTS</div><p style="font-size:11px;color:#888">3 total • 50 points each • Use them when the team is genuinely stuck</p>
 <button class="tiny" onclick="hint()">USE HINT (${S.hints})</button></aside></div>`;
}
function level(){return [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10][S.level]();}

/* 1 — Search */
function l1(){
 const o=[
 ["DIGITAL CLOCK","Clock stopped at 4:17 PM."],
 ["ACCESS CARD","Security card pinged the security room at 4:14 PM."],
 ["COFFEE MUG","Coffee was still warm."],
 ["TORN NOTE","Note mentions a hidden transfer."]
 ];
 return `<div class="panel">${head(1,"SCENE SWEEP","Inspect the four objects together. Discuss what each clue tells you, then choose the clearest incident time.")}<div class="scene">${o.map((x,i)=>`<button class="obj o${i+1}" onclick="inspectScene(${i})">${x[0]}</button>`).join("")}</div>
 <p>${S.found.map(i=>`<span class="ev" style="display:inline-block">✓ ${o[i][0]}</span>`).join("")}</p>
 ${S.feedback?`<div class="feedback ${S.feedback.startsWith("✓")?"good":"bad"}">${S.feedback}</div>`:""}
 <div class="q"><h3>What time did the incident happen?</h3><div class="answers">${["4:09 PM","4:14 PM","4:17 PM","4:24 PM"].map(x=>`<button class="ans ${S.sel===x?"sel":""}" onclick="S.sel='${x}';render()">${x}</button>`).join("")}</div>
 <button class="cta" onclick="check(0,S.found.length===4&&S.sel==='4:17 PM','The clock is your anchor. Make sure your team has inspected all four objects before locking the scene.')">LOCK SCENE</button></div></div>`;
}
function inspectScene(i){
 const d=[
 "Clock stopped at 4:17 PM.","Security card pinged the security room at 4:14 PM.",
 "Conference display disconnected shortly before the incident.","Coffee was still warm at the scene.",
 "Torn note mentions a hidden transfer.","Four suspicious access attempts were logged."
 ];
 if(!S.found.includes(i))S.found.push(i);addEvidence([d[i]]);
 S.feedback="✓ "+d[i];render();
}

/* 2 — Contradictions */
function l2(){
 return `<div class="panel">${head(2,"THE SUSPECT BOARD","One suspect's alibi has a gap during the most important part of the timeline. Find that suspect.")}<div class="cards">
 ${SUSPECTS.map((s,i)=>`<button class="card ${S.sel===s.name?"ans sel":""}" onclick="S.sel='${s.name}';render()"><b>${s.name}</b><small>${s.role}<br>${s.alibi}<br>${s.detail}</small></button>`).join("")}</div>
 <div class="note">CASE WINDOW: <b>4:13 PM–4:19 PM</b>. Which suspect cannot fully account for their whereabouts during this window?</div>
 ${S.feedback?`<div class="feedback ${S.feedback.startsWith("✓")?"good":"bad"}">${S.feedback}</div>`:""}
 <button class="cta" onclick="check(1,S.sel==='Alex Morgan','Read every alibi carefully. Ask: who has a gap inside 4:13–4:19?')">IDENTIFY SUSPECT</button></div>`;
}
function togglePick(i){
 S.temp.picked=S.temp.picked||[];const p=S.temp.picked.indexOf(i);
 if(p>=0)S.temp.picked.splice(p,1);else if(S.temp.picked.length<2)S.temp.picked.push(i);
 render();
}

/* 3 — Timeline */
function l3(){
 const e=[["A","Daniel's call ends","4:09"],["B","Security card ping","4:14"],["C","Security is disabled","4:17"],["D","Figure enters room","4:18"]];
 const q=S.temp.seq||[];
 return `<div class="panel">${head(3,"EASY TIMELINE","Put the four events in time order. The times are shown on each card.")}<div class="order-grid">${e.map((x,i)=>`<button class="order ${q.includes(i)?"selected":""}" onclick="pickOrder(${i})"><b>${x[0]}</b> — ${x[1]}<br><span style="color:#777;font:11px monospace">${x[2]}</span></button>`).join("")}</div>
 <div class="sequence">${q.length?q.map(i=>`${e[i][0]} — ${e[i][1]}`).join(" → "):"Click the events from earliest to latest."}</div>
 ${S.feedback?`<div class="feedback ${S.feedback.startsWith("✓")?"good":"bad"}">${S.feedback}</div>`:""}
 <button class="cta" onclick="check(2,JSON.stringify(S.temp.seq||[])===JSON.stringify([0,1,2,3]),'Start with the earliest timestamp, then work forward one event at a time.')">LOCK TIMELINE</button></div>`;
}
function pickOrder(i){S.temp.seq=S.temp.seq||[];if(!S.temp.seq.includes(i)&&S.temp.seq.length<8)S.temp.seq.push(i);render();}

/* 4 — Cipher */
function l4(){
 return `<div class="panel">${head(4,"SECRET MESSAGE","Decode the short message. Every letter has been moved forward by 1. Move each letter back by 1.")}<div class="terminal">ENCRYPTED MESSAGE

TFDSFU

CLUE: Move every letter back by ONE.

What is the secret word?</div>
 <input id="cipher" style="width:min(620px,100%);margin-top:18px;padding:14px;background:#080808;color:#fff;border:1px solid #403a31;text-transform:uppercase" placeholder="ENTER SECRET WORD">
 ${S.feedback?`<div class="feedback ${S.feedback.startsWith("✓")?"good":"bad"}">${S.feedback}</div>`:""}
 <button class="cta" onclick="checkCipher()">DECODE MESSAGE</button></div>`;
}
function checkCipher(){
 const v=(document.getElementById("cipher")?.value||"").trim().toUpperCase().replace(/\s+/g," ");
 check(3,v==="SECRET","Each encrypted letter is one step ahead. Move every letter back by one.");
}

/* 5 — Access logs */
function l5(){
 const logs=[
 "4:14   RC-204   Security room        CARD ACCEPTED",
 "4:17   SYS      Security control     DISABLE",
 "4:18   OR-119   Conference room      DOOR OPEN",
 "4:20   OR-119   Conference room      FILE ACCESS"
 ].join("\n");
 const register=[
 ["AM-101","Alex Morgan"],["MK-107","Maya Kapoor"],["RC-204","Ryan Carter"],
 ["SB-113","Sophie Bennett"],["DR-116","Daniel Ross"],["OR-119","Olivia Reed"]
 ];
 return `<div class="panel">${head(5,"ACCESS LOG","The file was accessed at 4:20 PM. Use the badge register to identify the person behind the badge code.")}<div class="terminal">${logs}</div>
 <div class="note"><b>BADGE REGISTER</b><br>${register.map(x=>`${x[0]}  —  ${x[1]}`).join("<br>")}</div>
 <div class="q"><h3>Who used the badge that accessed the file?</h3><div class="answers">${SUSPECTS.map(s=>`<button class="ans ${S.sel===s.name?"sel":""}" onclick="S.sel='${s.name}';render()">${s.name}</button>`).join("")}</div>
 ${S.feedback?`<div class="feedback ${S.feedback.startsWith("✓")?"good":"bad"}">${S.feedback}</div>`:""}
 <button class="cta" onclick="check(4,S.sel==='Olivia Reed','Start at the 4:20 FILE ACCESS row, then trace that badge to its owner.')">MATCH ACCESS</button></div></div>`;
}
/* 6 — Evidence matching */
function l6(){
 const rows=["Person who entered conference room","Person named in transfer document","Person whose card opened security room"];
 const options=["Olivia Reed","Victor Sterling","Ryan Carter"];
 const m=S.temp.map||{};
 return `<div class="panel">${head(6,"MATCH THE EVIDENCE","Three clues point to three different people. Match each clue to the person it describes.")}<div class="match">
 <div class="matchcol"><div class="section">CLUES</div>
 ${rows.map((r,i)=>`<div class="matchrow"><span>${r}</span><span style="color:#d7b56a;font-size:11px">${m[i]!==undefined?options[m[i]]:"UNMATCHED"}</span></div>`).join("")}</div>
 <div class="matchcol"><div class="section">YOUR MATCHES</div>
 ${rows.map((r,i)=>`<div class="matchrow"><span style="color:#777">Clue ${i+1}</span><select onchange="setMatch(${i},this.value)" style="background:#080808;color:#ddd;border:1px solid #3b3730;padding:7px"><option value="-1">Choose…</option>${options.map((x,j)=>`<option value="${j}" ${m[i]==j?"selected":""}>${x}</option>`).join("")}</select></div>`).join("")}
 </div></div>
 <div class="note">Evidence: the conference-room badge register, the transfer authorization, and the security-room card log.</div>
 ${S.feedback?`<div class="feedback ${S.feedback.startsWith("✓")?"good":"bad"}">${S.feedback}</div>`:""}
 <button class="cta" onclick="checkMatches()">VERIFY MATCHES</button></div>`;
}
function setMatch(i,v){S.temp.map=S.temp.map||{};if(v==="-1")delete S.temp.map[i];else S.temp.map[i]=Number(v);}
function checkMatches(){
 const m=S.temp.map||{},ok=m[0]===0&&m[1]===1&&m[2]===2;
 check(5,ok,"Slow down and match each clue to the person directly connected to that event.");
}

/* 7 — Logic */
function l7(){
 const w=S.temp.who||"";
 return `<div class="panel">${head(7,"SPOT THE LIE","Use the badge register and the known access log. Only one statement contradicts the evidence.")}<div class="logic">
 <div class="logicbox"><b>ALEX</b> “My badge is AM-101, and I was never in the conference room.”</div>
 <div class="logicbox"><b>RYAN</b> “My badge is RC-204, and it was used at the security room.”</div>
 <div class="logicbox"><b>OLIVIA</b> “My badge is OR-119, and it was never used at the conference room.”</div></div>
 <div class="logic" style="grid-template-columns:1fr"><div class="logicbox"><b>KNOWN FACT</b> The access log shows <b>OR-119</b> opening the conference-room door at 4:18 PM.</div></div>
 <div class="q"><h3>Who is lying?</h3><div class="answers">${["Alex","Ryan","Olivia"].map(x=>`<button class="ans ${w===x?"sel":""}" onclick="S.temp.who='${x}';render()">${x}</button>`).join("")}</div>
 ${S.feedback?`<div class="feedback ${S.feedback.startsWith("✓")?"good":"bad"}">${S.feedback}</div>`:""}
 <button class="cta" onclick="check(6,S.temp.who==='Olivia','Focus on OR-119. Which person claims that badge, and what does the 4:18 entry prove?')">CALL THE LIAR</button></div></div>`;
}
/* 8 — Interrogation */
function l8(){
 const q=S.temp.questions||[];
 const qs=[
 "Where were you at 4:18?",
 "Why does OR-119 appear in the file-access log?",
 "What is your favorite movie?"
 ];
 return `<div class="panel">${head(8,"ASK THE RIGHT QUESTIONS","Choose the two questions that help solve the case. One is clearly unrelated.")}<div class="cards">${qs.map((x,i)=>`<button class="card ${q.includes(i)?"ans sel":""}" onclick="toggleQuestion(${i})"><b>QUESTION ${i+1}</b><small>${x}</small></button>`).join("")}</div>
 <div class="q"><h3>Selected: ${q.length}/2</h3>
 ${S.feedback?`<div class="feedback ${S.feedback.startsWith("✓")?"good":"bad"}">${S.feedback}</div>`:""}
 <button class="cta" onclick="check(7,JSON.stringify((S.temp.questions||[]).sort())===JSON.stringify([0,1]),'Pick the questions that could actually expose the suspect. Ignore the small talk.')">START INTERROGATION</button></div></div>`;
}
function toggleQuestion(i){
 S.temp.questions=S.temp.questions||[];const p=S.temp.questions.indexOf(i);
 if(p>=0)S.temp.questions.splice(p,1);else if(S.temp.questions.length<2)S.temp.questions.push(i);
 render();
}

/* 9 — Vault */
function l9(){
 return `<div class="panel">${head(9,"VAULT CODE","The vault uses four simple case facts. Calculate each digit from the four facts below, then enter the four digits in order.")}<div class="terminal">VAULT INSTRUCTIONS

DIGIT 1 = number of suspects
DIGIT 2 = length of the security blackout in minutes
DIGIT 3 = hour shown on the stopped clock
DIGIT 4 = number of suspicious access attempts

Use the case evidence — not guesswork.</div>
 <div class="note">You have already seen all four facts in earlier levels. Check the Evidence Board if you need to review them.</div>
 <input id="vault" class="code" maxlength="4" inputmode="numeric" placeholder="____">
 ${S.feedback?`<div class="feedback ${S.feedback.startsWith("✓")?"good":"bad"}">${S.feedback}</div>`:""}
 <button class="cta" onclick="checkVault()">OPEN VAULT</button></div>`;
}
function checkVault(){
 const v=(document.getElementById("vault")?.value||"").trim();
 check(8,v==="6744","Calculate each digit: suspects • blackout minutes • clock hour • suspicious attempts.");
}

/* 10 — Final accusation */
function l10(){
 const F=S.final;
 return `<div class="panel">${head(10,"FINAL ACCUSATION","You have all the important clues. Make the final call.")}<div class="q"><h3>1. Who took the file?</h3><div class="answers">${SUSPECTS.map(s=>`<button class="ans ${F.who===s.name?"sel":""}" onclick="S.final.who='${s.name}';render()">${s.name}</button>`).join("")}</div></div>
 <div class="q"><h3>2. Why?</h3><div class="answers">${[["A","To steal money"],["B","To get evidence before Victor blamed her department"],["C","To ruin the company"]].map(x=>`<button class="ans ${F.why===x[0]?"sel":""}" onclick="S.final.why='${x[0]}';render()">${x[0]}. ${x[1]}</button>`).join("")}</div></div>
 <div class="q"><h3>3. What is the strongest proof?</h3><div class="answers">${[["A","Warm coffee"],["B","OR-119 accessed the conference room at 4:18"],["C","Daniel's call ended at 4:09"]].map(x=>`<button class="ans ${F.proof===x[0]?"sel":""}" onclick="S.final.proof='${x[0]}';render()">${x[0]}. ${x[1]}</button>`).join("")}</div></div>
 ${S.feedback?`<div class="feedback ${S.feedback.startsWith("✓")?"good":"bad"}">${S.feedback}</div>`:""}
 <button class="cta" onclick="finalSubmit()">CLOSE CASE</button></div>`;
}
function finalSubmit(){
 if(S.final.who==="Olivia Reed"&&S.final.why==="B"&&S.final.proof==="B"){
  S.score+=250;S.screen="reveal";render();
 }else{
  S.score=Math.max(0,S.score-25);
  S.feedback="The evidence does not support all three answers. Check the OR-119 clue.";
  render();
 }
}

function evidence(){
 document.body.insertAdjacentHTML("beforeend",`<div class="modal" id="modal"><div class="modalbox">
 <button class="close" onclick="document.getElementById('modal')?.remove()">×</button>
 <div class="section">EVIDENCE BOARD</div><h2>CASE CONNECTIONS</h2>
 ${S.evidence.map((e,i)=>`<div class="ev">EVIDENCE ${String(i+1).padStart(2,"0")} — ${esc(e)}</div>`).join("")||"<p>No evidence yet.</p>"}
 </div></div>`);
}
function chars(){
 document.body.insertAdjacentHTML("beforeend",`<div class="modal" id="modal"><div class="modalbox">
 <button class="close" onclick="document.getElementById('modal')?.remove()">×</button>
 <div class="section">SUSPECT FILES</div>
 ${SUSPECTS.map(s=>`<div style="padding:13px 0;border-bottom:1px solid #292621"><b>${s.name}</b> <small style="color:#777">${s.role}</small>
 <p style="font-size:11px;color:#aaa">Alibi: ${s.alibi}<br>Detail: ${s.detail}<br>Possible motive: ${s.motive}</p></div>`).join("")}
 </div></div>`);
}
function hint(){
 if(!S.hints)return;
 S.hints--;S.score=Math.max(0,S.score-50);
 const h=[
 "Inspect all four objects before locking the scene.",
 "Compare each suspect’s alibi with the critical window.",
 "Start with the printed timestamps and move left to right in time.",
 "The Caesar shift is the 3-minute difference between 4:14 and 4:17.",
 "Trace the badge from the file-access row back to the badge register.",
 "Ask whether the clue points to an actor, document owner or system.",
 "Compare the badge claimed by each suspect with the access log.",
 "Choose questions connecting time + access + motive.",
 "Count suspects, blackout minutes, clock hour and suspicious attempts."
 ];
 S.feedback="HINT — "+h[S.level];render();
}
function reveal(){
 const rank=S.score>=2200?"S-RANK — MASTER DETECTIVES":S.score>=1800?"A-RANK — ELITE INVESTIGATORS":S.score>=1400?"B-RANK — SOLID DETECTIVES":S.score>=1000?"C-RANK — ROOKIE DETECTIVES":"D-RANK — CASE STILL COLD";
 return `<div class="panel final"><div class="stamp">CASE CLOSED</div>
 <div style="color:#999;letter-spacing:3px;margin-top:25px">THE CULPRIT WAS...</div><div class="reveal">OLIVIA REED</div>
 <p style="max-width:760px;color:#aaa;line-height:1.7">Olivia discovered that Victor Sterling had prepared a transfer authorization and planned to shift responsibility to her department. She used the security blackout to enter the conference room, retrieve Project Blackbox and confront Victor before the scheduled 4:30 meeting. The access logs, timeline and transfer authorization connect the actions.</p>
 <div class="timeline">${[
 ["4:09","Daniel's client call ends."],["4:12","Server access appears."],["4:14","Ryan's card pings security."],["4:17","Security is disabled."],
 ["4:18","Olivia's identity opens the conference room."],["4:20","Project Blackbox is accessed."],["4:22","Victor confronts Olivia."],["4:24","Security is restored."]
 ].map(x=>`<div class="time"><b>${x[0]}</b><span>${x[1]}</span></div>`).join("")}</div>
 <h2>FINAL SCORE: ${S.score}</h2><div class="rank">${rank}</div>
 <button class="cta" onclick="location.reload()">NEW INVESTIGATION</button></div>`;
}
function render(){
 if(S.screen==="open"){open();return}
 if(S.screen==="setup"){setup();return}
 if(S.screen==="reveal"){document.getElementById("app").innerHTML=reveal();return}
 document.getElementById("app").innerHTML=shell();updateTimer();
}
open();
</script>
</body>
</html>
'''

components.html(HTML, height=2500, scrolling=True)
