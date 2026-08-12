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

const isFa=document.documentElement.lang==='fa';
const repoBase='/amir-ahmadi-research-papers';
function languagePath(targetLang){
  let path=location.pathname;
  const prefix=repoBase+'/';
  if(!path.startsWith(prefix)) return targetLang==='fa'?'/fa/':'/';
  let rest=path.slice(prefix.length);
  if(rest==='fa') rest='fa/';
  if(targetLang==='fa'){
    if(!rest.startsWith('fa/')) rest='fa/'+rest;
  }else{
    if(rest.startsWith('fa/')) rest=rest.slice(3);
  }
  return prefix+rest+location.search+location.hash;
}

// Quiet command field in the header. This is an interface convention, not a security boundary.
const nav=document.querySelector('.nav');
if(nav){
  const command=document.createElement('form');
  command.className='command-box';
  command.setAttribute('role','search');
  command.setAttribute('aria-label',isFa?'کادر فرمان':'Command field');
  command.innerHTML=`<span class="command-mark">⌘</span><input type="text" autocomplete="off" spellcheck="false" aria-label="${isFa?'فرمان':'Command'}" placeholder="${isFa?'فرمان…':'command…'}"><span class="command-hint">↵</span>`;
  const anchor=nav.querySelector('.menu-btn');
  nav.insertBefore(command,anchor||null);
  command.addEventListener('submit',e=>{
    e.preventDefault();
    const input=command.querySelector('input');
    const value=input.value.trim().toLowerCase();
    if(!isFa && value==='@@fa') location.href=languagePath('fa');
    else if(isFa && (value==='@@en'||value==='en')) location.href=languagePath('en');
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

const routesEn={
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
const routesFa={
  'حکمرانی زنده تصمیم':'papers/living-decision-governance/',
  'فراتر از هوشمندی — تکامل هوش مصنوعی':'papers/beyond-intelligence-ai-evolution/',
  'از شخصی‌سازی سبز تا هم‌تکاملی رابطه‌ای':'papers/relational-co-evolution/',
  'بازتاب‌ها و صاحبانشان':'papers/reflections-and-their-owners/',
  'از مُهر تا اتحاد: بازتعریف گواهی هوش مصنوعی':'papers/from-stamp-to-alliance/',
  'از پول تا پیمان':'papers/from-money-to-pledge/',
  'من، تو و ما':'papers/i-you-and-we/',
  'طراحی استراحت':'papers/designing-rest/',
  'پیش از فصل اول':'papers/before-the-first-chapter/',
  'از پیدایش تا شاهد':'papers/from-genesis-to-witness/',
  'فراتر از مدل‌ها: به‌سوی سامانه‌های پایدار همکاری انسان–هوش مصنوعی':'papers/beyond-models-hacs/'
};
const routes=isFa?routesFa:routesEn;
document.querySelectorAll('.paper-card').forEach(card=>{
  const h=card.querySelector('h3');
  if(!h)return;
  const route=routes[h.textContent.trim()];
  if(!route)return;
  card.classList.add('has-page');
  card.setAttribute('tabindex','0');
  card.setAttribute('role','link');
  card.setAttribute('aria-label',isFa?`باز کردن صفحه پژوهش ${h.textContent.trim()}`:`Open ${h.textContent.trim()} research page`);
  const actions=card.querySelector('.actions');
  if(actions){
    let a=actions.querySelector('[data-research-page]')||actions.querySelector('.btn.primary');
    if(!a){a=document.createElement('a');a.className='btn primary';actions.prepend(a)}
    a.href=route;a.dataset.researchPage='true';a.textContent=isFa?'مطالعه کامل مقاله →':'Read full paper →';
  }
  const open=()=>{location.href=route};
  card.addEventListener('click',e=>{if(!e.target.closest('a,button'))open()});
  card.addEventListener('keydown',e=>{if((e.key==='Enter'||e.key===' ')&&!e.target.closest('a,button')){e.preventDefault();open()}});
});

const progress=document.querySelector('.reading-progress span');
if(progress){
  const updateProgress=()=>{
    const root=document.documentElement;
    const max=Math.max(1,root.scrollHeight-root.clientHeight);
    const pct=Math.min(100,Math.max(0,(root.scrollTop/max)*100));
    progress.style.width=`${pct}%`;
  };
  updateProgress();
  addEventListener('scroll',updateProgress,{passive:true});
  addEventListener('resize',updateProgress,{passive:true});
}

document.querySelectorAll('.copy-citation').forEach(button=>{
  button.addEventListener('click',async()=>{
    const citation=button.dataset.citation||'';
    try{
      await navigator.clipboard.writeText(citation);
      const original=button.textContent;
      button.classList.add('copied');
      button.textContent=isFa?'کپی شد ✓':'Copied ✓';
      setTimeout(()=>{button.textContent=original;button.classList.remove('copied')},1600);
    }catch{
      const area=document.createElement('textarea');area.value=citation;document.body.append(area);area.select();document.execCommand('copy');area.remove();
    }
  });
});

// Curated network: intentionally limited to the five public surfaces that support the research narrative.
const footer=document.querySelector('.footer');
if(footer&&!footer.querySelector('.research-network')){
  const network=document.createElement('div');
  network.className='research-network shell';
  const items=[
    ['Amir Ahmadi','https://axamir.github.io/'],
    ['Shahnameh of Agents','https://axamir.github.io/shahnameh-of-agents/'],
    ['Persistent AI Lineage','https://axamir.github.io/persistent-ai-lineage/'],
    ['PDRP-88','https://axamir.github.io/PDRP-88/'],
    ['Evidence Archive','https://axamir.github.io/echoes-consented-record/']
  ];
  const title=isFa?'شبکه پژوهشی':'Research Network';
  const intro=isFa?'پنج مسیر منتخب و مرتبط با این آرشیو پژوهشی.':'A curated set of public systems connected to this research archive.';
  network.innerHTML=`<div class="research-network-head"><div><span class="research-network-kicker">${title}</span><p>${intro}</p></div></div><div class="research-network-links">${items.map(([label,url],i)=>`<a href="${url}" target="_blank" rel="noopener"><span class="network-index">0${i+1}</span><span>${label}</span><span aria-hidden="true">↗</span></a>`).join('')}</div>`;
  footer.prepend(network);

  const style=document.createElement('style');
  style.textContent=`
  .research-network{padding:8px 0 34px}.research-network-head{display:flex;justify-content:space-between;gap:24px;padding:0 0 18px}.research-network-kicker{font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;font-weight:800;color:#46535a}.research-network-head p{margin:7px 0 0;color:#70787d;font-size:.84rem;max-width:560px}.research-network-links{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.research-network-links a{min-height:86px;padding:16px 14px;display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:10px;text-decoration:none;border-right:1px solid var(--line);font-size:.82rem;font-weight:700;transition:background .18s ease,transform .18s ease}.research-network-links a:last-child{border-right:0}.research-network-links a:hover{background:rgba(255,255,255,.42)}.network-index{font:600 .66rem/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:#8b9295}.research-network-links a:focus-visible{outline:3px solid #6f8d9b;outline-offset:-3px}html[dir="rtl"] .research-network-kicker{letter-spacing:0;text-transform:none}html[dir="rtl"] .research-network-links a{border-right:0;border-left:1px solid var(--line)}html[dir="rtl"] .research-network-links a:last-child{border-left:0}@media(max-width:920px){.research-network-links{grid-template-columns:1fr 1fr}.research-network-links a:nth-child(2n){border-right:0}.research-network-links a{border-bottom:1px solid var(--line)}html[dir="rtl"] .research-network-links a:nth-child(2n){border-left:0}}@media(max-width:560px){.research-network{padding-bottom:26px}.research-network-links{grid-template-columns:1fr}.research-network-links a,.research-network-links a:nth-child(2n){border-right:0;border-left:0;min-height:62px}.research-network-links a:last-child{border-bottom:0}}
  `;
  document.head.append(style);
}

const year=document.querySelector('[data-year]');
if(year)year.textContent=new Date().getFullYear();
