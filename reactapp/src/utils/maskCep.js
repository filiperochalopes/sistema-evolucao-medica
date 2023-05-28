export default function maskCep(cep) {
  if (!cep) {
    return "";
  }
  let newCep = cep;
  newCep = newCep.replace(/\D/g, "").slice(0, 8);
  newCep = newCep.replace(/(\d{5})(\d)/, "$1-$2");
  return newCep;
}
