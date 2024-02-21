export default function maskCpf(cpf) {
  if (!cpf) {
    return "";
  }

  let newCpf = cpf;
  newCpf = newCpf.replace(/\D/g, "").slice(0, 11);
  newCpf = newCpf.replace(/(\d{3})(\d)/, "$1.$2");
  newCpf = newCpf.replace(/(\d{3})(\d)/, "$1.$2");
  newCpf = newCpf.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
  return newCpf;
}
