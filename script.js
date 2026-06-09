/* =========================
   LISTA DE TAREFAS
========================= */
document.querySelectorAll('.projeto').forEach(projeto => {
  const titulo = projeto.querySelector('h3');

  if (titulo && titulo.textContent.includes("Lista de Tarefas")) {
    const input = document.createElement("input");
    const botao = document.createElement("button");
    const lista = document.createElement("ul");

    input.placeholder = "Digite sua tarefa";
    botao.textContent = "Adicionar";

    projeto.appendChild(input);
    projeto.appendChild(botao);
    projeto.appendChild(lista);

    botao.addEventListener("click", () => {
      const texto = input.value.trim();

      if (texto !== "") {
        const item = document.createElement("li");
        item.textContent = texto;

        item.addEventListener("click", () => {
          item.classList.toggle("done");
        });

        lista.appendChild(item);
        input.value = "";
      }
    });
  }

  /* =========================
     SISTEMA DE AGENDAMENTOS
  ========================= */
  if (titulo && titulo.textContent.includes("Sistema de Agendamentos")) {
    const linkDemo = document.createElement("a");
    const linkGit = document.createElement("a");

    linkDemo.href = "projetos/sistema-agendamentos/templates/index.html";
    linkDemo.textContent = "🌐 Ver Demo";
    linkDemo.target = "_blank";

    linkGit.href = "https://github.com/LuizFelipe-bitmax/portfolio/tree/main/projetos/sistema-agendamentos";
    linkGit.textContent = "🔗 GitHub";
    linkGit.target = "_blank";

    const espaco = document.createTextNode(" ");

    projeto.appendChild(linkDemo);
    projeto.appendChild(espaco);
    projeto.appendChild(linkGit);

    const aviso = document.createElement("p");
    aviso.innerHTML =
      "<em>Obs: projeto Flask precisa ser executado localmente.</em>";

    projeto.appendChild(aviso);
  }
});
