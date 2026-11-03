const MESES = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"];
const mesLabel = data => MESES[data.getMonth()] + " de " + data.getFullYear();
const chaveData = data => data.getFullYear() + "-" + String(data.getMonth()+1).padStart(2,"0") + "-" + String(data.getDate()).padStart(2,"0");

export function initializeCalendar({ getTasks, onFocusTask }) {
  const mini = document.querySelector(".calendar-widget");
  const full = document.querySelector(".full-calendar");
  if (!mini || !full) return () => {};
  const agora = new Date();
  let month = new Date(agora.getFullYear(),agora.getMonth(),1);
  let popover = document.getElementById("calendar-focus-popover");
  if (!popover) {
    popover = document.createElement("dialog"); popover.id = "calendar-focus-popover"; popover.className = "calendar-focus-popover";
    popover.setAttribute("aria-labelledby","calendar-focus-title");
    const header = document.createElement("header"), title = document.createElement("h2"), close = document.createElement("button"), list = document.createElement("ul");
    title.id = "calendar-focus-title"; title.textContent = "Tarefas do dia"; close.type = "button"; close.textContent = "×"; close.setAttribute("aria-label","Fechar"); close.dataset.calendarClose = "";
    close.addEventListener("click",()=>popover.close()); header.append(title,close); popover.append(header,list); document.body.append(popover);
  }
  function mapTasks() {
    const map = new Map();
    for (const task of getTasks()) if (task.data_limite) { if (!map.has(task.data_limite)) map.set(task.data_limite,[]); map.get(task.data_limite).push(task); }
    return map;
  }
  function focusDay(date,map) {
    const tasks = [...(map.get(date) || [])].sort((a, b) =>
      String(a.titulo ?? "").localeCompare(
        String(b.titulo ?? ""),
        "pt-BR",
        { sensitivity: "base" }
      )
    );
    const title = popover.querySelector("h2");
    title.textContent = new Intl.DateTimeFormat("pt-BR",{dateStyle:"full",timeZone:"UTC"}).format(new Date(date+"T12:00:00Z"));
    const list = popover.querySelector("ul"); list.replaceChildren();
    if (!tasks.length) { const li=document.createElement("li"); li.textContent="Nenhuma tarefa com prazo nesta data."; list.append(li); }
    for (const task of tasks) {
      const li=document.createElement("li"), button=document.createElement("button"); button.type="button";
      button.textContent=task.titulo+(task.estado==="concluida"?" (concluída)":"");
      button.addEventListener("click",()=>{popover.close();onFocusTask(task.id);}); li.append(button); list.append(li);
    }
    if (!popover.open) popover.showModal();
  }
  function makeGrid(compact,map) {
    const grid=document.createElement("div"); grid.className=compact?"calendar-grid calendar-days":"full-calendar-grid full-calendar-days";
    const first=new Date(month.getFullYear(),month.getMonth(),1), start=new Date(first); start.setDate(1-first.getDay());
    const today=chaveData(new Date());
    for(let i=0;i<42;i++){
      const day=new Date(start); day.setDate(start.getDate()+i); const key=chaveData(day), tasks=map.get(key)||[];
      const button=document.createElement("button"); button.type="button"; button.className=compact?"calendar-day":"full-day";
      if(day.getMonth()!==month.getMonth()) button.classList.add("muted-day","outside-month");
      if(key===today) button.classList.add("today-day");
      if(tasks.length) button.classList.add("has-task");
      if(tasks.some(task => task.estado === "concluida")) button.classList.add("has-completed-task");
      button.setAttribute("aria-label",new Intl.DateTimeFormat("pt-BR",{dateStyle:"full"}).format(day)+": "+tasks.length+" tarefa(s)");
      button.textContent=String(day.getDate());
      if(tasks.length){const marker=document.createElement("i");marker.setAttribute("aria-hidden","true");button.append(marker);}
      button.addEventListener("click",()=>focusDay(key,map)); grid.append(button);
    }
    return grid;
  }
  function render() {
    const map=mapTasks(), label=mesLabel(month);
    mini.replaceChildren();
    const header=document.createElement("div");header.className="calendar-month";
    const prev=document.createElement("button"),next=document.createElement("button"),caption=document.createElement("span");
    prev.type=next.type="button";prev.className=next.className="month-arrow";prev.textContent="‹";next.textContent="›";prev.setAttribute("aria-label","Mês anterior");next.setAttribute("aria-label","Próximo mês");caption.textContent=label;
    prev.addEventListener("click",()=>{month.setMonth(month.getMonth()-1);render();});next.addEventListener("click",()=>{month.setMonth(month.getMonth()+1);render();});
    header.append(prev,caption,next);
    const weekdays=document.createElement("div");weekdays.className="calendar-grid calendar-weekdays";
    for(const day of ["D","S","T","Q","Q","S","S"]){const span=document.createElement("span");span.textContent=day;weekdays.append(span);}
    const legend=document.createElement("p");legend.className="calendar-legend";const dot=document.createElement("span");dot.setAttribute("aria-hidden","true");legend.append(dot,document.createTextNode("Dias com tarefas"));
    mini.append(header,weekdays,makeGrid(true,map),legend);
    const fullHeader=full.querySelector(".full-calendar-head");
    if(fullHeader){fullHeader.querySelector("h2").textContent=label;fullHeader.querySelectorAll("button").forEach((button,index)=>{button.disabled=false;button.onclick=()=>{month.setMonth(month.getMonth()+(index===0?-1:1));render();};});}
    full.querySelector(".full-calendar-days")?.replaceWith(makeGrid(false,map));
    full.querySelector(".mock-disclaimer")?.remove();
  }
  render();
  return Object.freeze({render,close:()=>{if(popover.open)popover.close();}});
}
