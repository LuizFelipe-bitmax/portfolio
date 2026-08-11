// ========================================
// ANIMAÇÃO DE ENTRADA
// ========================================

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  },
  {
    threshold: 0.1
  }
);

document
  .querySelectorAll(
    "section, .projeto-card, .skill-card, .contato-card, .projeto-destaque"
  )
  .forEach((element) => {
    element.classList.add("fade-in");
    observer.observe(element);
  });


// ========================================
// NAV ATIVO
// ========================================

const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-links a");

const sectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {

      if (entry.isIntersecting) {

        navLinks.forEach((link) => {
          link.classList.remove("active");
        });

        const activeLink = document.querySelector(
          `.nav-links a[href="#${entry.target.id}"]`
        );

        if (activeLink) {
          activeLink.classList.add("active");
        }
      }
    });
  },
  {
    threshold: 0.5
  }
);

sections.forEach((section) => {
  sectionObserver.observe(section);
});