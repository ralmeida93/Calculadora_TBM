const estado = document.querySelector("#select-estado");
const cidade = document.querySelector("#cidade");

const bahia = ["Camaçari", "Ilhéus", "Lauro de Freitas"];
const sergipe = ["Aracaju", "Lagarto", "Boquim"];

function selecionar(e) {
  let markump;
  if (e.target.value === "ba") {
    bahia.forEach((cidade) => {
      markump += `<option>${cidade}</option>`;
    });
    cidade.innerHTML = markump;
  } else if (e.target.value === "se") {
    sergipe.forEach((cidade) => {
        markump += `<option>${cidade}</option>`;
    });
    cidade.innerHTML = markump;
  }
}

estado.addEventListener("change", selecionar);
