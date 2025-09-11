const listaTarefasDiv = document.querySelectorAll('.projeto').forEach(projeto => {
  const titulo = projeto.querySelector('h3');
  if(titulo && titulo.textContent.includes("Lista de Tarefas")) {


    const tarefaInput = document.createElement("input");
    const botaoAdicionar = document.createElement("button");
    const lista = document.createElement("ul");

    tarefaInput.placeholder = "Digite sua tarefa";
    botaoAdicionar.textContent = "Adicionar Tarefa";


    projeto.appendChild(tarefaInput);
    projeto.appendChild(botaoAdicionar);
    projeto.appendChild(lista);


    botaoAdicionar.addEventListener("click", function() {
      const texto = tarefaInput.value.trim();
      if (texto !== "") {
        const item = document.createElement("li");
        item.textContent = texto;

        item.addEventListener("click", function() {
          item.classList.toggle("done");
        });

        lista.appendChild(item);
        tarefaInput.value = "";
      }
    });
  }
});
