const projetosSecao = document.getElementById("projetos");

const tarefaInput = document.createElement("input");
const botaoAdicionar = document.createElement("button");
const lista = document.createElement("ul");

tarefaInput.placeholder = "Digite sua tarefa";
botaoAdicionar.textContent = "Adicionar Tarefa";

projetosSecao.appendChild(tarefaInput);
projetosSecao.appendChild(botaoAdicionar);
projetosSecao.appendChild(lista);

botaoAdicionar.addEventListener("click", function() {
    const texto = tarefaInput.value.trim();
    if (texto !== "") {
        const item = document.createElement("li");
        item.textContent = texto;

        item.addEventListener("click", function() {
            item.style.textDecoration = "line-through";
        });

        lista.appendChild(item);
        tarefaInput.value = "";
    }
});
