const THRESHOLD = 8;
export function initializeDragDrop({ onMove, notify = () => {} }) {
  const board = document.getElementById("colunas-kanban");
  if (!board) return () => {};
  let gesture = null;
  const states = ["a_fazer", "em_andamento", "concluida"];
  board.querySelectorAll(".kanban-column").forEach((column, index) => { column.dataset.taskState = states[index]; });

  function cleanup() {
    if (!gesture) return;
    gesture.card.classList.remove("is-dragging");
    board.querySelectorAll(".kanban-column").forEach(column => column.classList.remove("drop-target"));
    gesture = null;
  }
  function start(event) {
    const card = event.target.closest(".task-card[data-task-id]");
    if (!card || event.button > 0 || event.isPrimary === false) return;
    if (event.target.closest("button,input,summary,details,a,select,textarea")) return;
    if (!["mouse","touch","pen"].includes(event.pointerType)) return;
    gesture = { id: card.dataset.taskId, card, pointerId: event.pointerId, pointerType: event.pointerType,
      startX: event.clientX, startY: event.clientY, x: event.clientX, y: event.clientY, active: false };
  }
  function move(event) {
    if (!gesture || event.pointerId !== gesture.pointerId) return;
    gesture.x = event.clientX; gesture.y = event.clientY;
    if (!gesture.active && Math.hypot(event.clientX - gesture.startX, event.clientY - gesture.startY) >= THRESHOLD) {
      gesture.active = true; gesture.card.classList.add("is-dragging");
      gesture.card.dataset.dragPointerType = gesture.pointerType;
    }
    if (!gesture.active) return;
    const target = document.elementFromPoint(event.clientX,event.clientY);
    const column = target?.closest(".kanban-column");
    board.querySelectorAll(".kanban-column").forEach(item => item.classList.toggle("drop-target", item === column));
    event.preventDefault();
  }
  async function end(event) {
    if (!gesture || event.pointerId !== gesture.pointerId) return;
    const current = gesture;
    const target = current.active ? document.elementFromPoint(event.clientX,event.clientY) : null;
    const column = target?.closest(".kanban-column");
    const targetCard = target?.closest(".task-card[data-task-id]");
    cleanup();
    if (!current.active || !column) return;
    const state = column.dataset.taskState;
    const cards = [...column.querySelectorAll(".task-card[data-task-id]")].filter(card => card.dataset.taskId !== current.id);
    let order = cards.length;
    if (targetCard && targetCard.dataset.taskId !== current.id) {
      const rect = targetCard.getBoundingClientRect();
      const before = event.clientY < rect.top + rect.height / 2;
      const index = cards.indexOf(targetCard);
      if (index >= 0) order = index + (before ? 0 : 1);
    }
    try { await onMove({ tarefa_id: current.id, novo_estado: state, nova_ordem: order, pointer_type: current.pointerType }); }
    catch (error) { notify(error.message || "Não foi possível mover a tarefa."); }
  }
  board.addEventListener("pointerdown", start);
  document.addEventListener("pointermove", move, { passive: false });
  document.addEventListener("pointerup", end);
  document.addEventListener("pointercancel", cleanup);
  window.addEventListener("blur", cleanup);
  return () => { cleanup(); board.removeEventListener("pointerdown",start); document.removeEventListener("pointermove",move); document.removeEventListener("pointerup",end); document.removeEventListener("pointercancel",cleanup); window.removeEventListener("blur",cleanup); };
}
