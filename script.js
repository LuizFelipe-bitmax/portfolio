// Lista de tarefas interativa no card
const input = document.getElementById('task-input');
const btn = document.getElementById('task-btn');
const lista = document.getElementById('task-list');

function adicionarTarefa() {
  const texto = input.value.trim();
  if (!texto) return;
  const li = document.createElement('li');
  li.textContent = texto;
  li.addEventListener('click', () => li.classList.toggle('done'));
  lista.appendChild(li);
  input.value = '';
  input.focus();
}

if (btn && input) {
  btn.addEventListener('click', adicionarTarefa);
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') adicionarTarefa();
  });
}

// Fade-in ao rolar a página
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('section, .projeto-card, .skill-card, .contato-card, .projeto-destaque')
  .forEach(el => {
    el.classList.add('fade-in');
    observer.observe(el);
  });

// Nav ativo
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => link.classList.remove('active'));
      const active = document.querySelector(`.nav-links a[href="#${entry.target.id}"]`);
      if (active) active.classList.add('active');
    }
  });
}, { threshold: 0.5 });

sections.forEach(s => sectionObserver.observe(s));
