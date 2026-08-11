const menu=document.querySelector('.menu-btn');
const links=document.querySelector('.navlinks');
if(menu&&links){
  menu.addEventListener('click',()=>{
    links.classList.toggle('open');
    menu.setAttribute('aria-expanded',String(links.classList.contains('open')));
  });
  links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
    links.classList.remove('open');
    menu.setAttribute('aria-expanded','false');
  }));
}

// Quiet command field in the header. This is an interface convention, not a security boundary.
const nav=document.querySelector('.nav');
if(nav){
  const isFa=document.documentElement.lang==='fa';
  const command=document.createElement('form');
  command.className='command-box';
  command.setAttribute('role','search');
  command.setAttribute('aria-label',isFa?'کادر فرمان':'Command field');
  command.innerHTML=`<span class="command-mark">⌘</span><input type="text" autocomplete="off" spellcheck="false" aria-label="${isFa?'فرمان':'Command'}" placeholder="${isFa?'فرمان…':'command…'}"><span class="command-hint">↵</span>`;
  const anchor=nav.querySelector('.menu-btn');
  nav.insertBefore(command,anchor);
  command.addEventListener('submit',e=>{
    e.preventDefault();
    const input=command.querySelector('input');
    const value=input.value.trim().toLowerCase();
    if(!isFa && value==='@@fa') location.href='fa/';
    else if(isFa && (value==='@@en'||value==='en')) location.href='../';
    else {
      command.classList.remove('command-error');
      void command.offsetWidth;
      command.classList.add('command-error');
      input.select();
    }
  });
}

const chips=[...document.querySelectorAll('.chip')];
const entries=[...document.querySelectorAll('.entry')];
chips.forEach(chip=>chip.addEventListener('click',()=>{
  chips.forEach(c=>c.classList.remove('active'));
  chip.classList.add('active');
  const f=chip.dataset.filter;
  entries.forEach(e=>{e.style.display=(f==='all'||e.dataset.topic?.includes(f))?'grid':'none'});
}));

const routes={
  'Living Decision Governance':'papers/living-decision-governance/',
  'Beyond Intelligence — AI Evolution':'papers/beyond-intelligence-ai-evolution/',
  'From Green Personalisation to Relational Co‑Evolution':'papers/relational-co-evolution/',
  'Reflections and Their Owners':'papers/reflections-and-their-owners/',
  'From Stamp to Alliance: Redefining AI Certification':'papers/from-stamp-to-alliance/',
  'From Money to Pledge':'papers/from-money-to-pledge/',
  'I, You, and We':'papers/i-you-and-we/',
  'Designing Rest':'papers/designing-rest/',
  'Before the First Chapter':'papers/before-the-first-chapter/',
  'From Genesis to Witness':'papers/from-genesis-to-witness/',
  'Beyond Models: Toward Enduring Human–AI Collaborative Systems':'papers/beyond-models-hacs/'
};

if(document.documentElement.lang!=='fa'){
  document.querySelectorAll('.paper-card').forEach(card=>{
    const h=card.querySelector('h3');
    if(!h)return;
    const route=routes[h.textContent.trim()];
    if(!route)return;
    card.classList.add('has-page');
    card.setAttribute('tabindex','0');
    card.setAttribute('role','link');
    card.setAttribute('aria-label',`Open ${h.textContent.trim()} research page`);
    const actions=card.querySelector('.actions');
    if(actions&&!actions.querySelector('[data-research-page]')){
      const a=document.createElement('a');
      a.href=route;
      a.className='btn primary';
      a.dataset.researchPage='true';
      a.textContent='Explore research →';
      actions.prepend(a);
    }
    const open=()=>{location.href=route};
    card.addEventListener('click',e=>{if(!e.target.closest('a,button'))open()});
    card.addEventListener('keydown',e=>{
      if((e.key==='Enter'||e.key===' ')&&!e.target.closest('a,button')){
        e.preventDefault();open();
      }
    });
  });
}

const year=document.querySelector('[data-year]');
if(year)year.textContent=new Date().getFullYear();
