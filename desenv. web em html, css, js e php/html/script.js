// Obter o modal do novo formulário
var novoModal = document.getElementById("modalNovoForm");

// Quando o usuário clicar no botão, abrir o novo modal
btn.onclick = function() {
    novoModal.style.display = "block";
}

// Quando o usuário clicar em <span> (x), fechar o novo modal
span.onclick = function() {
    novoModal.style.display = "none";
}

// Quando o usuário clicar fora do novo modal, fechar o novo modal
window.onclick = function(event) {
    if (event.target == novoModal) {
        novoModal.style.display = "none";
    }
}
