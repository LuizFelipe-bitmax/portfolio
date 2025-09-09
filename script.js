// Lista de Tarefas Simples

// Seleciona o elemento da seção "projetos"
const projetosSecao = document.getElementById("projetos");

// Cria input, botão e lista
const tarefaInput = document.createElement("input");
const botaoAdicionar = document.createElement("button");
const lista = document.createElement("ul");

tarefaInput.placeholder = "Digite sua tarefa";
botaoAdicionar.textContent = "Adicionar Tarefa";

// Adiciona elementos na seção de projetos
projetosSecao.appendChild(tarefaInput);
projetosSecao.appendChild(botaoAdicionar);
projetosSecao.appendChild(lista);

// Função para adicionar tarefas
botaoAdicionar.addEventListener("click", function() {
    const texto = tarefaInput.value.trim();
    if (texto !== "") {
        const item = document.createElement("li");
        item.textContent = texto;

        // Ao clicar no item, ele é riscado
        item.addEventListener("click", function() {
            item.style.textDecoration = "line-through";
        });

        lista.appendChild(item);
        tarefaInput.value = "";
    }
});
