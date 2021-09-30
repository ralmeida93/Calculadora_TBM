const btnAbrirModal = document.querySelector('#abrirModal');
const btnFecharModal = document.querySelector('#fecharModal');
const containerModal = document.querySelector('.modal-container');

function AbreModal() {
  const modal = document.getElementById('modal-promocao');
  modal.classList.add('mostrar');
}

function FechaModal() {
  const modal = document.getElementById('modal-promocao');
  modal.classList.remove('mostrar');
}

btnAbrirModal.addEventListener('click', AbreModal);
btnFecharModal.addEventListener('click', FechaModal);
// containerModal.addEventListener('click', FechaModal);
