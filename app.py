import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Germane Media LLC — The Blackbox Incident",
    page_icon="🕵️",
    layout="wide",
)

HTML = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<style>
:root{
    --bg:#080808;
    --panel:#121212;
    --gold:#d1ad65;
    --red:#b74343;
    --white:#eee9df;
    --muted:#969188;
    --line:#2b2925;
}

*{
    box-sizing:border-box;
}

html,body{
    margin:0;
    padding:0;
    background:
        radial-gradient(
            circle at 70% 5%,
            #292015,
            #080808 42%
        );
    color:var(--white);
    font-family:Arial,sans-serif;
}

button,
input{
    font:inherit;
}

button{
    cursor:pointer;
}

button:disabled{
    cursor:not-allowed;
    opacity:.55;
}

.app{
    max-width:1400px;
    margin:auto;
    padding:22px;
}

.top{
    display:flex;
    justify-content:space-between;
    align-items:center;
    border-bottom:1px solid var(--line);
    padding:10px 0 16px;
    position:sticky;
    top:0;
    background:#090909ee;
    z-index:5;
}

.brand{
    font-size:11px;
    letter-spacing:3px;
    color:var(--gold);
    font-weight:800;
}

.timer{
    font:900 28px monospace;
    color:var(--gold);
    margin-left:10px;
}

.urgent{
    color:#e05a5a;
}

.hero{
    min-height:88vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
}

.hero h1{
    font:normal 82px/.88 Georgia,serif;
    letter-spacing:2px;
    margin:20px;
}

.hero h2{
    letter-spacing:6px;
    font-size:14px;
    color:#c8bfae;
}

.hero p{
    max-width:680px;
    color:var(--muted);
    line-height:1.7;
}

.cta{
    background:linear-gradient(
        135deg,
        #e3c27c,
        #a47e3b
    );
    border:0;
    padding:15px 25px;
    font-weight:900;
    letter-spacing:2px;
    margin-top:18px;
    color:#17130d;
}

.setup{
    width:min(520px,90%);
    border:1px solid var(--line);
    background:#101010;
    padding:25px;
    text-align:left;
}

.setup label{
    font-size:11px;
    letter-spacing:2px;
    color:#888;
    display:block;
    margin-bottom:8px;
}

.setup input{
    width:100%;
    padding:13px;
    background:#080808;
    color:white;
    border:1px solid #3a352d;
    outline:none;
}

.setup input:focus{
    border-color:var(--gold);
}

.grid{
    display:grid;
    grid-template-columns:210px 1fr 230px;
    gap:16px;
    margin-top:18px;
}

.side,
.right,
.panel{
    background:
        linear-gradient(
            150deg,
            #151515,
            #0d0d0d
        );
    border:1px solid var(--line);
}

.side,
.right{
    padding:16px;
}

.side{
    min-height:650px;
}

.panel{
    padding:24px;
    min-height:650px;
}

.section{
    font-size:10px;
    letter-spacing:2px;
    color:#777;
    font-weight:bold;
}

.levels{
    display:grid;
    gap:7px;
    margin-top:14px;
}

.lvl,
.tiny,
.ans{
    background:#101010;
    border:1px solid #302d28;
    color:#bbb;
    padding:11px;
    text-align:left;
}

.lvl{
    width:100%;
}

.lvl.active{
    border-color:var(--gold);
    color:var(--gold);
    background:#1d180f;
}

.lvl.done{
    color:#8fbc9a;
}

.score{
    border:1px solid var(--line);
    padding:14px;
    margin:18px 0;
    font:900 28px monospace;
    color:var(--gold);
}

.ev{
    background:#0a0a0a;
    border-left:2px solid #705b37;
    padding:9px;
    margin:6px 0;
    font-size:11px;
    color:#bdb6aa;
}

.head{
    display:flex;
    justify-content:space-between;
    border-bottom:1px solid var(--line);
    padding-bottom:16px;
    margin-bottom:18px;
}

.no{
    color:var(--gold);
    font-size:10px;
    letter-spacing:3px;
}

.title{
    font:38px Georgia,serif;
    margin-top:6px;
}

.brief{
    color:var(--muted);
    line-height:1.55;
}

.scene{
    height:400px;
    border:1px solid #413a30;
    background:
        radial-gradient(
            circle at 50% 35%,
            #454036,
            #171615 60%
        );
    position:relative;
    overflow:hidden;
}

.scene:before{
    content:"CONFERENCE ROOM // 04:17";
    position:absolute;
    top:14px;
    left:16px;
    color:#ad9158;
    font:11px monospace;
}

.desk{
    position:absolute;
    left:14%;
    bottom:70px;
    width:72%;
    height:80px;
    background:#30271d;
    border:2px solid #5b4c39;
}

.obj{
    position:absolute;
    background:#0d0d0ddd;
    border:1px solid #74603a;
    color:#ead6a5;
    padding:9px;
    font-size:10px;
}

.o1{left:44%;top:80px}
.o2{left:24%;bottom:95px}
.o3{left:45%;bottom:110px}
.o4{left:61%;bottom:110px}
.o5{left:71%;bottom:92px}

.q{
    margin-top:20px;
    border-top:1px solid var(--line);
    padding-top:18px;
}

.answers{
    display:flex;
    flex-wrap:wrap;
    gap:8px;
}

.ans.sel{
    border-color:var(--gold);
    background:#211a0d;
    color:#f0d18b;
}

.feedback{
    padding:12px;
    background:#17140f;
    border-left:3px solid var(--gold);
    margin-top:12px;
    line-height:1.5;
}

.riddle{
    padding:35px;
    text-align:center;
    font:23px/1.7 Georgia,serif;
    border:1px solid #373128;
    background:#090909;
}

.terminal{
    font:13px/1.8 monospace;
    background:#050505;
    border:1px solid #393a32;
    padding:20px;
    color:#a9c7a9;
}

.code{
    display:block;
    margin:20px auto;
    padding:12px;
    width:210px;
    text-align:center;
    font:28px monospace;
    letter-spacing:9px;
    background:#090909;
    border:1px solid #5d5039;
    color:white;
}

.pieces{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:7px;
}

.piece{
    padding:15px 8px;
    min-height:65px;
    background:#0b0b0b;
    border:1px dashed #534938;
    color:#c9c0b0;
}

.piece.sel{
    border-color:var(--gold);
    background:#211b10;
}

.assembled{
    margin-top:15px;
    min-height:100px;
    background:#eee6d3;
    color:#252119;
    padding:18px;
    font:17px/1.5 Georgia,serif;
}

.suspects{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:9px;
}

.sus{
    padding:13px;
    background:#0b0b0b;
    border:1px solid var(--line);
}

.ava{
    width:46px;
    height:46px;
    border-radius:50%;
    display:grid;
    place-items:center;
    border:1px solid #604f32;
    color:var(--gold);
    margin-bottom:8px;
    font-weight:bold;
}

.sus small{
    color:#777;
    display:block;
    margin-top:4px;
}

.timeline{
    display:grid;
    gap:6px;
    width:min(720px,100%);
}

.time{
    display:grid;
    grid-template-columns:80px 1fr;
    background:#0b0b0b;
    border-left:2px solid #614e30;
    padding:9px;
    text-align:left;
}

.time b{
    font:11px monospace;
    color:var(--gold);
}

.final{
    text-align:center;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
}

.stamp{
    border:2px solid var(--gold);
    padding:10px 20px;
    letter-spacing:6px;
    color:var(--gold);
    transform:rotate(-3deg);
}

.reveal{
    font:64px Georgia,serif;
    color:#f0d18b;
    margin:20px;
}

.modal{
    position:fixed;
    inset:0;
    background:#000c;
    display:grid;
    place-items:center;
    z-index:20;
}

.modalbox{
    width:min(760px,92%);
    max-height:80vh;
    overflow:auto;
    background:#111;
    border:1px solid #5b4b32;
    padding:22px;
}

.close{
    float:right;
    background:none;
    border:0;
    color:#aaa;
    font-size:22px;
}

.rule{
    border:1px solid #302d28;
    background:#0b0b0b;
    padding:14px;
    margin:12px 0;
    color:#aaa;
    font-size:12px;
    line-height:1.6;
}

@media(max-width:1050px){
    .grid{
        grid-template-columns:1fr;
    }

    .side,
    .right{
        min-height:auto;
    }
}

@media(max-width:650px){
    .hero h1{
        font-size:54px;
    }

    .suspects,
    .pieces{
        grid-template-columns:1fr 1fr;
    }

    .title{
        font-size:29px;
    }

    .top{
        flex-direction:column;
        gap:12px;
        align-items:flex-start;
    }

    .timer{
        margin-left:5px;
    }
}
</style>
</head>

<body>

<div class="app" id="app"></div>

<script>

/* =========================================================
   CASE DATA
========================================================= */

const C = [
    [
        "Alex Morgan",
        "Chief Operating Officer",
        "AM",
        "Private video meeting, scheduled 4:00–4:30 PM.",
        "Recording has a confirmed 4:13–4:19 PM gap.",
        "Could be protecting the company."
    ],

    [
        "Maya Kapoor",
        "Head of Marketing",
        "MK",
        "Preparing a campaign presentation from 4:00–4:30 PM.",
        "Laptop remained connected to the conference-room display.",
        "Could gain strategic advantage."
    ],

    [
        "Ryan Carter",
        "Technology Lead",
        "RC",
        "Fixing a server issue in the technical area.",
        "Access card was used near the security room at 4:14 PM.",
        "Understands security infrastructure."
    ],

    [
        "Sophie Bennett",
        "Finance Manager",
        "SB",
        "Reviewing invoices in the finance department.",
        "Recently discovered an unusual transaction.",
        "May want to investigate privately."
    ],

    [
        "Daniel Ross",
        "Sales Director",
        "DR",
        "On a client call from 3:55–4:15 PM.",
        "Call records confirm the call ended at 4:09 PM.",
        "A confidential strategy could help a deal."
    ],

    [
        "Olivia Reed",
        "People & Culture Manager",
        "OR",
        "Employee meeting scheduled from 4:00–4:30 PM.",
        "The attendee left at 4:11 PM; no second attendee was recorded.",
        "Wanted evidence protecting herself from Victor."
    ]
];

const E = [
    [
        "Clock stopped at 4:17 PM.",
        "Security card registered near the security room at 4:14 PM.",
        "Conference-room display connection logged before the incident.",
        "Coffee was still warm, indicating recent presence.",
        "Torn document mentions a hidden transfer."
    ],

    [
        "Security log: system disabled from 4:17 PM to 4:24 PM.",
        "Security outage lasted exactly 7 minutes.",
        "The security log records 4 suspicious access attempts."
    ],

    [
        "Security code decoded: 6747.",
        "Hidden CCTV frame: figure enters conference room at 4:18 PM."
    ],

    [
        "Transfer authorization names Victor Sterling and Olivia Reed.",
        "Meeting scheduled for 4:30 PM.",
        "Document is marked INTERNAL ONLY."
    ],

    [
        "Daniel's call ended at 4:09 PM.",
        "Alex's recording gap is 4:13–4:19 PM.",
        "Ryan's card was used at 4:14 PM, but his server log places him elsewhere.",
        "Olivia's employee meeting ended when the attendee left at 4:11 PM.",
        "No second attendee was recorded for Olivia's 4:00–4:30 meeting."
    ],

    [
        "Olivia sought evidence that would protect her from Victor's actions.",
        "Method: disable security → enter → take document → confrontation → leave.",
        "Olivia leaves the conference area at approximately 4:23 PM."
    ]
];

const names = [
    "THE CRIME SCENE",
    "THE RIDDLE FILE",
    "CRACK THE CODE",
    "ASSEMBLE THE EVIDENCE",
    "THE ALIBI GAME",
    "THE FINAL ACCUSATION"
];

const P = [
    "TRANSFER",
    "APPROVED",
    "Authorization",
    "required from",
    "Victor Sterling",
    "Project Blackbox",
    "Olivia Reed",
    "Meeting scheduled",
    "4:30 PM",
    "— INTERNAL ONLY"
];

/* =========================================================
   GAME STATE
========================================================= */

let S = {
    screen:"open",

    team:"",

    level:0,

    score:0,

    totalSeconds:1800,

    remain:1800,

    lastTick:0,

    activeElapsed:0,

    paused:false,

    hints:3,

    evidence:[],

    found:[],

    sel:"",

    wrong:0,

    q1:"",

    q2:"",

    q3:"",

    pieces:[],

    feedback:""
};

/* =========================================================
   UTILITIES
========================================================= */

function esc(x){

    return String(x).replace(/[&<>]/g,a=>({
        "&":"&amp;",
        "<":"&lt;",
        ">":"&gt;"
    }[a]));
}

function addEvidence(items){

    items.forEach(item=>{

        if(!S.evidence.includes(item)){
            S.evidence.push(item);
        }

    });
}

/* =========================================================
   OPEN SCREEN
========================================================= */

function open(){

    document.getElementById("app").innerHTML = `

    <div class="hero">

        <div class="brand">
            GERMANE MEDIA LLC PRESENTS
        </div>

        <h1>
            THE BLACKBOX<br>
            INCIDENT
        </h1>

        <h2>
            CORPORATE CRIME MYSTERY
        </h2>

        <p>
            Six suspects. One missing project file.
            Seven minutes of darkness. One person is lying.
        </p>

        <p>
            Investigate the evidence, challenge the alibis,
            reconstruct the document and identify the culprit.
        </p>

        <button
            class="cta"
            onclick="showSetup()"
        >
            START INVESTIGATION
        </button>

    </div>`;
}

/* =========================================================
   SETUP
========================================================= */

function showSetup(){

    document.getElementById("app").innerHTML = `

    <div class="hero">

        <div class="brand">
            CASE FILE // INITIALIZE
        </div>

        <h2 style="font-size:30px;letter-spacing:1px">
            ENTER YOUR TEAM
        </h2>

        <div class="setup">

            <label>
                TEAM NAME
            </label>

            <input
                id="team"
                placeholder="e.g. Team Sherlock"
                maxlength="28"
                autocomplete="off"
            >

            <p style="font-size:12px;color:#777">
                Designed for teams of 5.
                One person controls the shared screen.
            </p>

            <button
                class="cta"
                onclick="beginCase()"
            >
                BEGIN CASE
            </button>

        </div>

    </div>`;
}

/* =========================================================
   START GAME
========================================================= */

function beginCase(){

    try{

        const input =
            document.getElementById("team");

        if(
            input &&
            input.value &&
            input.value.trim()
        ){

            S.team =
                input.value.trim();

        }else{

            S.team =
                "Team Sherlock";
        }

        S.screen = "game";

        S.level = 0;

        S.score = 0;

        S.remain =
            S.totalSeconds;

        S.lastTick =
            Date.now();

        S.activeElapsed = 0;

        S.paused = false;

        S.hints = 3;

        S.evidence = [];

        S.found = [];

        S.sel = "";

        S.wrong = 0;

        S.q1 = "";

        S.q2 = "";

        S.q3 = "";

        S.pieces = [];

        S.feedback = "";

        render();

        clock();

    }catch(error){

        console.error(
            "GAME START ERROR:",
            error
        );

        document.getElementById("app").innerHTML = `

        <div class="hero">

            <h2 style="color:#e05a5a">
                GAME INITIALIZATION ERROR
            </h2>

            <p>
                Something went wrong while starting
                the investigation.
            </p>

            <div class="rule">
                ${esc(error.message)}
            </div>

            <button
                class="cta"
                onclick="showSetup()"
            >
                RETURN TO SETUP
            </button>

        </div>`;
    }
}

/* =========================================================
   TIMER
========================================================= */

function clock(){

    if(S.screen !== "game"){
        return;
    }

    const now =
        Date.now();

    if(!S.paused){

        const delta =
            Math.floor(
                (now - S.lastTick) / 1000
            );

        if(delta > 0){

            S.activeElapsed +=
                delta;

            S.lastTick =
                now;
        }

        S.remain =
            Math.max(
                0,
                S.totalSeconds -
                S.activeElapsed
            );

    }else{

        /*
          While paused, the current time is continually
          reset so paused duration is never counted.
        */

        S.lastTick =
            now;
    }

    if(S.remain <= 0){

        S.remain = 0;

        S.level = 5;

        S.feedback =
            "TIME'S UP — make your final accusation.";

        render();

        return;
    }

    updateTimer();

    setTimeout(
        clock,
        1000
    );
}

function togglePause(){

    if(S.paused){

        S.lastTick =
            Date.now();

        S.paused =
            false;

    }else{

        const now =
            Date.now();

        const delta =
            Math.floor(
                (now - S.lastTick) / 1000
            );

        if(delta > 0){

            S.activeElapsed +=
                delta;
        }

        S.remain =
            Math.max(
                0,
                S.totalSeconds -
                S.activeElapsed
            );

        S.lastTick =
            now;

        S.paused =
            true;
    }

    render();
}

function updateTimer(){

    const e =
        document.getElementById("timer");

    if(!e){
        return;
    }

    const m =
        Math.floor(
            S.remain / 60
        );

    const s =
        S.remain % 60;

    e.textContent =
        String(m).padStart(2,"0") +
        ":" +
        String(s).padStart(2,"0");

    e.className =
        "timer " +
        (
            S.remain < 600
            ? "urgent"
            : ""
        );
}

/* =========================================================
   MAIN SHELL
========================================================= */

function shell(){

    return `

    <div class="top">

        <div>

            <div class="brand">
                GERMANE MEDIA LLC PRESENTS
            </div>

            <div style="font-size:12px;color:#777">
                ${esc(S.team)}
                // INVESTIGATION
            </div>

        </div>

        <div>

            <button
                class="tiny"
                onclick="togglePause()"
            >
                ${S.paused ? "RESUME" : "PAUSE"}
            </button>

            <button
                class="tiny"
                onclick="showEvidence()"
            >
                EVIDENCE
            </button>

            <span
                id="timer"
                class="timer"
            >
                30:00
            </span>

        </div>

    </div>

    <div class="grid">

        <aside class="side">

            <div class="section">
                CASE PROGRESS
            </div>

            <div class="levels">

                ${
                    names.map(
                        (n,i)=>`

                        <button
                            class="
                                lvl
                                ${i===S.level ? "active" : ""}
                                ${i<S.level ? "done" : ""}
                            "
                            ${
                                i<S.level
                                ?
                                `onclick="
                                    S.level=${i};
                                    S.feedback='';
                                    S.sel='';
                                    render();
                                "`
                                :
                                "disabled"
                            }
                        >
                            ${String(i+1).padStart(2,"0")}
                            — ${n}
                        </button>
                    `
                    ).join("")
                }

            </div>

            <div class="score">

                <div class="section">
                    LIVE SCORE
                </div>

                ${S.score}

            </div>

            <button
                class="tiny"
                style="width:100%"
                onclick="showCharacters()"
            >
                CHARACTERS
            </button>

        </aside>

        <main>
            ${level()}
        </main>

        <aside class="right">

            <div class="section">
                EVIDENCE INVENTORY
            </div>

            ${
                S.evidence.length
                ?
                S.evidence.map(
                    x=>`
                        <div class="ev">
                            ${esc(x)}
                        </div>
                    `
                ).join("")
                :
                `
                <p
                    style="
                        color:#555;
                        font-size:11px
                    "
                >
                    No evidence collected yet.
                </p>
                `
            }

            <div
                class="section"
                style="margin-top:18px"
            >
                HINTS
            </div>

            <p
                style="
                    font-size:11px;
                    color:#888
                "
            >
                3 total • 50 points each
            </p>

            <button
                class="tiny"
                onclick="useHint()"
                ${S.hints===0 ? "disabled" : ""}
            >
                USE HINT (${S.hints})
            </button>

        </aside>

    </div>`;
}

/* =========================================================
   LEVEL HEADER
========================================================= */

function head(n,t,b){

    return `

    <div class="head">

        <div>

            <div class="no">
                CASE FILE ${String(n).padStart(2,"0")}
            </div>

            <div class="title">
                ${t}
            </div>

        </div>

        <div
            style="
                font-size:10px;
                color:#666
            "
        >
            30 MIN INVESTIGATION
        </div>

    </div>

    <div class="brief">
        ${b}
    </div>`;
}

/* =========================================================
   LEVEL ROUTER
========================================================= */

function level(){

    if(S.level === 0){
        return level1();
    }

    if(S.level === 1){
        return level2();
    }

    if(S.level === 2){
        return level3();
    }

    if(S.level === 3){
        return level4();
    }

    if(S.level === 4){
        return level5();
    }

    return level6();
}

/* =========================================================
   LEVEL 1
========================================================= */

function level1(){

    const objects = [

        [
            "DIGITAL CLOCK",
            "4:17 PM"
        ],

        [
            "ACCESS CARD",
            "Registered near security room at 4:14 PM."
        ],

        [
            "LAPTOP",
            "Display connection logged shortly before incident."
        ],

        [
            "COFFEE MUG",
            "Still warm."
        ],

        [
            "TORN DOCUMENT",
            "If they discover the transfer, everything is over."
        ]
    ];

    return `

    <div class="panel">

        ${head(
            1,
            "THE CRIME SCENE",
            "Inspect all five suspicious objects. Then determine the most likely incident time."
        )}

        <div class="scene">

            <div class="desk"></div>

            ${
                objects.map(
                    (x,i)=>`

                    <button
                        class="obj o${i+1}"
                        onclick="inspectObject(${i})"
                    >
                        ${x[0]}
                    </button>

                    `
                ).join("")
            }

        </div>

        <p>

            ${
                S.found.map(
                    i=>`

                    <span
                        class="ev"
                        style="
                            display:inline-block
                        "
                    >
                        ✓ ${objects[i][0]}
                    </span>

                    `
                ).join("")
            }

        </p>

        ${
            S.feedback
            ?
            `<div class="feedback">${S.feedback}</div>`
            :
            ""
        }

        <div class="q">

            <h3>
                When did the incident most likely occur?
            </h3>

            <div class="answers">

                ${
                    [
                        "4:09 PM",
                        "4:14 PM",
                        "4:17 PM",
                        "4:24 PM"
                    ].map(
                        x=>`

                        <button
                            class="
                                ans
                                ${S.sel===x ? "sel" : ""}
                            "
                            onclick="
                                S.sel='${x}';
                                render();
                            "
                        >
                            ${x}
                        </button>

                        `
                    ).join("")
                }

            </div>

            <button
                class="cta"
                onclick="
                    answerLevel(
                        0,
                        S.sel==='4:17 PM'
                    )
                "
            >
                SUBMIT DEDUCTION
            </button>

        </div>

    </div>`;
}

function inspectObject(i){

    if(!S.found.includes(i)){

        S.found.push(i);

        addEvidence([
            E[0][i]
        ]);
    }

    S.feedback = [
        "The clock stopped at 4:17 PM.",
        "The access card was registered near the security room at 4:14 PM.",
        "The display connection forms part of the digital trail.",
        "The warm coffee suggests someone was present shortly before the incident.",
        "The torn sentence points toward a hidden transfer."
    ][i];

    render();
}

/* =========================================================
   LEVEL 2
========================================================= */

function level2(){

    return `

    <div class="panel">

        ${head(
            2,
            "THE RIDDLE FILE",
            "Solve the riddle to unlock the security log."
        )}

        <div class="riddle">

            I leave a record without making a sound.<br>

            I show the path you took without following you.<br><br>

            Investigators find me on the ground
            after someone has passed by.<br><br>

            <b>What am I?</b>

        </div>

        <div class="q">

            <div class="answers">

                ${
                    [
                        "A shadow",
                        "A footprint",
                        "A calendar",
                        "A password"
                    ].map(
                        x=>`

                        <button
                            class="
                                ans
                                ${S.sel===x ? "sel" : ""}
                            "
                            onclick="
                                S.sel='${x}';
                                render();
                            "
                        >
                            ${x}
                        </button>

                        `
                    ).join("")
                }

            </div>

            <button
                class="cta"
                onclick="
                    answerLevel(
                        1,
                        S.sel==='A footprint'
                    )
                "
            >
                UNLOCK FILE
            </button>

        </div>

        ${
            S.feedback
            ?
            `<div class="feedback">${S.feedback}</div>`
            :
            ""
        }

    </div>`;
}

/* =========================================================
   LEVEL 3
========================================================= */

function level3(){

    return `

    <div class="panel">

        ${head(
            3,
            "CRACK THE CODE",
            "Use the security log to derive the four-digit security code."
        )}

        <div class="terminal">

            SECURITY KEYPAD<br><br>

            FIRST DIGIT
            = people inside the investigation area<br>

            SECOND DIGIT
            = minutes security was disabled<br>

            THIRD DIGIT
            = suspicious access attempts<br>

            FOURTH DIGIT
            = stopped clock minute display<br><br>

            SECURITY LOG<br>
            ----------------------------<br>

            People inside: 6<br>
            Security disabled: 7 minutes<br>
            Suspicious access attempts: 4<br>
            Clock stopped: 4:17 PM

        </div>

        <div class="rule">

            The four digits are:

            <b>6 → 7 → 4 → 7</b>

            Therefore the security code is
            <b>6747</b>.

        </div>

        <input
            id="securityCode"
            class="code"
            maxlength="4"
            inputmode="numeric"
            placeholder="____"
            autocomplete="off"
        >

        <button
            class="cta"
            style="
                display:block;
                margin:auto
            "
            onclick="
                const code =
                    document.getElementById(
                        'securityCode'
                    ).value;

                answerLevel(
                    2,
                    code === '6747'
                );
            "
        >
            VERIFY CODE
        </button>

        ${
            S.feedback
            ?
            `<div class="feedback">${S.feedback}</div>`
            :
            ""
        }

    </div>`;
}

/* =========================================================
   LEVEL 4
========================================================= */

function level4(){

    return `

    <div class="panel">

        ${head(
            4,
            "ASSEMBLE THE EVIDENCE",
            "Select the ten fragments in the correct order to reconstruct the torn document."
        )}

        <div class="rule">

            <b>Document clues:</b><br><br>

            1. Start with the subject.<br>
            2. The approval status follows the subject.<br>
            3. Then identify the authorization requirement.<br>
            4. Name the person whose authorization is required.<br>
            5. Identify the project.<br>
            6. Identify the recipient/person connected to it.<br>
            7. Finish with the meeting details and document classification.

        </div>

        <div class="pieces">

            ${
                P.map(
                    (x,i)=>`

                    <button
                        class="
                            piece
                            ${S.pieces.includes(i)
                                ? "sel"
                                : ""}
                        "
                        onclick="
                            selectPiece(${i})
                        "
                    >
                        ${i+1}. ${x}
                    </button>

                    `
                ).join("")
            }

        </div>

        <div class="assembled">

            ${
                S.pieces.length
                ?
                S.pieces
                    .map(i=>P[i])
                    .join(" ")
                :
                "Selected fragments will appear here in sequence."
            }

        </div>

        <button
            class="cta"
            onclick="
                answerLevel(
                    3,
                    JSON.stringify(S.pieces) ===
                    JSON.stringify(
                        [0,1,2,3,4,5,6,7,8,9]
                    )
                )
            "
        >
            ASSEMBLE DOCUMENT
        </button>

        ${
            S.feedback
            ?
            `<div class="feedback">${S.feedback}</div>`
            :
            ""
        }

    </div>`;
}

function selectPiece(i){

    const index =
        S.pieces.indexOf(i);

    if(index >= 0){

        S.pieces.splice(
            index,
            1
        );

    }else{

        S.pieces.push(i);
    }

    render();
}

/* =========================================================
   LEVEL 5
========================================================= */

function level5(){

    return `

    <div class="panel">

        ${head(
            5,
            "THE ALIBI GAME",
            "Compare the six suspect files and identify the two alibis that cannot be trusted."
        )}

        <div class="suspects">

            ${
                C.map(
                    c=>`

                    <div class="sus">

                        <div class="ava">
                            ${c[2]}
                        </div>

                        <b>
                            ${c[0]}
                        </b>

                        <small>
                            ${c[1]}
                        </small>

                        <p
                            style="
                                font-size:11px;
                                color:#aaa
                            "
                        >
                            <b>Alibi:</b>
                            ${c[3]}
                        </p>

                        <p
                            style="
                                font-size:11px;
                                color:#c8ae77
                            "
                        >
                            <b>Suspicious:</b>
                            ${c[4]}
                        </p>

                    </div>

                    `
                ).join("")
            }

        </div>

        <div class="rule">

            <b>Timeline cross-check:</b><br><br>

            • Alex's recording disappears from
              <b>4:13–4:19 PM</b>.<br>

            • Olivia's scheduled meeting attendee
              leaves at <b>4:11 PM</b>.<br>

            • No second attendee is recorded
              for Olivia's meeting.<br>

            • Daniel's call ended at
              <b>4:09 PM</b>.<br>

            • Ryan's card was used at 4:14 PM,
              but his server activity places him
              elsewhere.

        </div>

        <div class="q">

            <h3>
                Which TWO alibis are definitely unreliable?
            </h3>

            <div class="answers">

                ${
                    [
                        "Alex + Maya",
                        "Alex + Olivia",
                        "Ryan + Daniel",
                        "Sophie + Olivia"
                    ].map(
                        x=>`

                        <button
                            class="
                                ans
                                ${S.sel===x ? "sel" : ""}
                            "
                            onclick="
                                S.sel='${x}';
                                render();
                            "
                        >
                            ${x}
                        </button>

                        `
                    ).join("")
                }

            </div>

            <button
                class="cta"
                onclick="
                    answerLevel(
                        4,
                        S.sel==='Alex + Olivia'
                    )
                "
            >
                LOCK TIMELINE
            </button>

        </div>

        ${
            S.feedback
            ?
            `<div class="feedback">${S.feedback}</div>`
            :
            ""
        }

    </div>`;
}

/* =========================================================
   LEVEL 6
========================================================= */

function level6(){

    return `

    <div class="panel">

        ${head(
            6,
            "THE FINAL ACCUSATION",
            "Use everything you have learned. Answer all three questions."
        )}

        <div class="q">

            <h3>
                1. Who committed the crime?
            </h3>

            <div class="answers">

                ${
                    C.map(
                        c=>`

                        <button
                            class="
                                ans
                                ${S.q1===c[0] ? "sel" : ""}
                            "
                            onclick="
                                S.q1='${c[0]}';
                                render();
                            "
                        >
                            ${c[0]}
                        </button>

                        `
                    ).join("")
                }

            </div>

        </div>

        <div class="q">

            <h3>
                2. Why?
            </h3>

            <div class="answers">

                ${
                    [
                        [
                            "A",
                            "Revenge"
                        ],
                        [
                            "B",
                            "Steal money"
                        ],
                        [
                            "C",
                            "Obtain evidence to protect herself from being blamed for Victor's actions"
                        ],
                        [
                            "D",
                            "Destroy the company"
                        ]
                    ].map(
                        x=>`

                        <button
                            class="
                                ans
                                ${S.q2===x[0] ? "sel" : ""}
                            "
                            onclick="
                                S.q2='${x[0]}';
                                render();
                            "
                        >
                            ${x[0]}. ${x[1]}
                        </button>

                        `
                    ).join("")
                }

            </div>

        </div>

        <div class="q">

            <h3>
                3. How?
            </h3>

            <div class="answers">

                ${
                    [
                        [
                            "A",
                            "Disable security → enter → take document → confrontation → leave"
                        ],
                        [
                            "B",
                            "Steal card → hack server → destroy evidence → leave"
                        ],
                        [
                            "C",
                            "Confront Victor → steal money → disable CCTV → leave"
                        ]
                    ].map(
                        x=>`

                        <button
                            class="
                                ans
                                ${S.q3===x[0] ? "sel" : ""}
                            "
                            onclick="
                                S.q3='${x[0]}';
                                render();
                            "
                        >
                            ${x[0]}. ${x[1]}
                        </button>

                        `
                    ).join("")
                }

            </div>

        </div>

        <button
            class="cta"
            onclick="submitFinal()"
        >
            SUBMIT FINAL ACCUSATION
        </button>

        ${
            S.feedback
            ?
            `<div class="feedback">${S.feedback}</div>`
            :
            ""
        }

    </div>`;
}

/* =========================================================
   ANSWER PROCESSING
========================================================= */

function answerLevel(l,correct){

    const base =
        [100,150,200,200,250,300][l];

    if(correct){

        S.score +=
            base +
            (
                S.wrong === 0 && l < 5
                ? 25
                : 0
            );

        addEvidence(E[l]);

        S.feedback =
            "✓ CORRECT — evidence secured.";

        setTimeout(
            ()=>{
                S.level =
                    Math.min(
                        5,
                        l + 1
                    );

                S.sel = "";

                S.wrong = 0;

                S.feedback = "";

                render();
            },
            700
        );

    }else{

        S.wrong++;

        S.score =
            Math.max(
                0,
                S.score -
                (
                    S.wrong === 1
                    ? 25
                    : 50
                )
            );

        const messages = [

            "✕ Incorrect. Compare the stopped clock with the other timestamps.",

            "✕ Incorrect. The answer leaves a physical trail left on the ground.",

            "✕ Incorrect. Read the four security-log numbers in order.",

            "✕ Incorrect. Use the document clues to determine the sequence.",

            "✕ Incorrect. Compare the exact alibi windows against the timeline."

        ];

        S.feedback =
            messages[l] ||
            "✕ Incorrect. Review the evidence.";

        render();
    }
}

/* =========================================================
   FINAL ACCUSATION
========================================================= */

function submitFinal(){

    if(
        S.q1 === "Olivia Reed" &&
        S.q2 === "C" &&
        S.q3 === "A"
    ){

        S.score += 200;

        S.screen =
            "reveal";

        render();

    }else{

        S.score =
            Math.max(
                0,
                S.score - 50
            );

        S.feedback =
            "The accusation does not fit every clue. Revisit the evidence board.";

        render();
    }
}

/* =========================================================
   FINAL REVEAL
========================================================= */

function reveal(){

    let rank =
        S.score >= 1200
        ?
        "S-RANK — MASTER DETECTIVES"
        :
        S.score >= 950
        ?
        "A-RANK — ELITE INVESTIGATORS"
        :
        S.score >= 700
        ?
        "B-RANK — SOLID DETECTIVES"
        :
        S.score >= 450
        ?
        "C-RANK — ROOKIE DETECTIVES"
        :
        "D-RANK — THE SUSPECTS WERE RIGHT";

    return `

    <div class="panel final">

        <div class="stamp">
            CASE CLOSED
        </div>

        <div
            style="
                color:#999;
                letter-spacing:3px;
                margin-top:25px
            "
        >
            THE CULPRIT WAS...
        </div>

        <div class="reveal">
            OLIVIA REED
        </div>

        <p
            style="
                max-width:720px;
                color:#aaa;
                line-height:1.7
            "
        >
            Olivia discovered that Victor Sterling had
            secretly manipulated an internal project and
            planned to blame her department if it failed.

            She wanted the document proving what had happened.

            She used the security outage as a window to enter
            the conference room, took Project Blackbox and
            confronted Victor.

            Victor became unconscious during the confrontation.

            Olivia then left the conference area before
            security was restored.
        </p>

        <div class="timeline">

            ${
                [
                    [
                        "4:09 PM",
                        "Daniel's client call ends."
                    ],
                    [
                        "4:12 PM",
                        "Server access is recorded."
                    ],
                    [
                        "4:14 PM",
                        "Security room access is recorded."
                    ],
                    [
                        "4:17 PM",
                        "Security system is disabled."
                    ],
                    [
                        "4:18 PM",
                        "Olivia enters the conference room."
                    ],
                    [
                        "4:20 PM",
                        "Project Blackbox is removed."
                    ],
                    [
                        "4:22 PM",
                        "Victor confronts Olivia."
                    ],
                    [
                        "4:23 PM",
                        "Olivia leaves the conference area."
                    ],
                    [
                        "4:24 PM",
                        "Security system is restored."
                    ]
                ].map(
                    x=>`

                    <div class="time">

                        <b>
                            ${x[0]}
                        </b>

                        <span>
                            ${x[1]}
                        </span>

                    </div>

                    `
                ).join("")
            }

        </div>

        <h2>
            FINAL SCORE: ${S.score}
        </h2>

        <div
            style="letter-spacing:3px"
        >
            ${rank}
        </div>

        <button
            class="cta"
            onclick="location.reload()"
        >
            NEW GAME
        </button>

    </div>`;
}

/* =========================================================
   EVIDENCE MODAL
========================================================= */

function showEvidence(){

    document.body.insertAdjacentHTML(
        "beforeend",
        `

        <div
            class="modal"
            id="evidenceModal"
        >

            <div class="modalbox">

                <button
                    class="close"
                    onclick="
                        document
                        .getElementById(
                            'evidenceModal'
                        )
                        .remove()
                    "
                >
                    ×
                </button>

                <div class="section">
                    EVIDENCE BOARD
                </div>

                <h2>
                    CASE CONNECTIONS
                </h2>

                ${
                    S.evidence.length
                    ?
                    S.evidence.map(
                        (e,i)=>`

                        <div class="ev">

                            EVIDENCE
                            ${String(i+1).padStart(2,"0")}
                            — ${esc(e)}

                        </div>

                        `
                    ).join("")
                    :
                    "<p>No evidence yet.</p>"
                }

            </div>

        </div>
        `
    );
}

/* =========================================================
   CHARACTER MODAL
========================================================= */

function showCharacters(){

    document.body.insertAdjacentHTML(
        "beforeend",
        `

        <div
            class="modal"
            id="charactersModal"
        >

            <div class="modalbox">

                <button
                    class="close"
                    onclick="
                        document
                        .getElementById(
                            'charactersModal'
                        )
                        .remove()
                    "
                >
                    ×
                </button>

                <div class="section">
                    SUSPECT FILES
                </div>

                ${
                    C.map(
                        c=>`

                        <div
                            style="
                                padding:13px 0;
                                border-bottom:
                                1px solid #292621
                            "
                        >

                            <div class="ava">
                                ${c[2]}
                            </div>

                            <b>
                                ${c[0]}
                            </b>

                            <small
                                style="color:#777"
                            >
                                ${c[1]}
                            </small>

                            <p
                                style="
                                    font-size:11px;
                                    color:#aaa
                                "
                            >

                                <b>Alibi:</b>
                                ${c[3]}<br><br>

                                <b>Suspicious:</b>
                                ${c[4]}<br><br>

                                <b>Possible motive:</b>
                                ${c[5]}

                            </p>

                        </div>

                        `
                    ).join("")
                }

            </div>

        </div>
        `
    );
}

/* =========================================================
   HINT SYSTEM
========================================================= */

function useHint(){

    if(S.hints <= 0){
        return;
    }

    S.hints--;

    S.score =
        Math.max(
            0,
            S.score - 50
        );

    const hints = [

        "The strongest direct timestamp is the stopped clock. Inspect the digital clock.",

        "The riddle describes a physical trace left on the ground after someone passes.",

        "The security log gives 6, 7, 4 and the minute display 7. The code is 6747.",

        "The document starts with its subject and ends with meeting details. Follow the document clues.",

        "Alex has a 4:13–4:19 recording gap. Olivia's meeting attendee left at 4:11 and no replacement attendee was recorded.",

        "Olivia has the motive, opportunity, document connection and the timeline opportunity."
    ];

    S.feedback =
        hints[S.level] ||
        hints[0];

    render();
}

/* =========================================================
   RENDER
========================================================= */

function render(){

    const app =
        document.getElementById("app");

    if(!app){
        return;
    }

    if(S.screen === "open"){

        open();

        return;
    }

    if(S.screen === "setup"){

        showSetup();

        return;
    }

    if(S.screen === "reveal"){

        app.innerHTML =
            reveal();

        return;
    }

    app.innerHTML =
        shell();

    updateTimer();
}

/* =========================================================
   START
========================================================= */

open();

</script>

</body>
</html>
"""

components.html(
    HTML,
    height=2200,
    scrolling=False,
)
