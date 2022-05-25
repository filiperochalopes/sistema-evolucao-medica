
const copyToClipboardButtons = document.querySelectorAll(".copy_to_clipboard")

// Botões de copiar para área de transferência
function copyToClipboard(e) {
  /* Get the text field */
  var copyText = document.getElementById(e.target.dataset.id);

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText.value);
}

// Adicionando eventos individuais
for (let i = 0; i < copyToClipboardButtons.length; i++) {
    copyToClipboardButtons[i].addEventListener("click", copyToClipboard);
  }
