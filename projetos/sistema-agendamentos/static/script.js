
document.addEventListener('click', function(e) {
  if (e.target.matches('.link-delete')) {
    if (!confirm('Confirmar exclusão?')) e.preventDefault();
  }
});
