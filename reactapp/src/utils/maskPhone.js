function maskPhone(telefone = "") {
  // Remover todos os caracteres não-numéricos
  const numerosTelefone = telefone.replace(/\D/g, "").slice(0, 11);

  let newValue = numerosTelefone.replace(/\D/g, "");
  newValue = newValue.replace(/^(\d{2})(\d+)/g, "($1) $2");
  newValue = newValue.replace(/^\((\d{2})\)\s(\d{4})(\d)/g, "($1) $2-$3");
  newValue = newValue.replace(
    /^\((\d{2})\)\s(\d{4})-(\d)(\d{4})/g,
    "($1) $2$3-$4"
  );

  return newValue;
}

export default maskPhone;
