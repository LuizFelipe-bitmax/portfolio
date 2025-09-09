// Lista de Tarefas Simples

// Seleciona os elementos do HTML
const tarefaInput = document.createElement("input");
const botaoAdicionar = document.createElement("button");
const lista = document.createElement("ul");

// Configura input e botão
tarefaInput.placeholder = "Digite sua tarefa";
botaoAdicionar.textContent = "Adicionar Tarefa";

// Adiciona input, botão e lista na página
document.getElementById("projetos").appendChild(tarefaInput);
document.getElementById("projetos").appendChild(botaoAdicionar);
document.getElementById("projetos").appendChild(lista);

// Função para adicionar tarefa
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
