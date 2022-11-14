const { default: cepApi } = require("config/cepApi");

const zipCodeLengthIsEight = (zipcode) =>
  zipcode.match(/\d+/gi)?.join("").length === 8;

const trasnsformRequestData = (data) => ({
  zipcode: data.cep.match(/\d+/gi)?.join(""),
  complement: data.complemento,
  number: "",
  city: data.localidade,
  uf: data.uf,
  street: data.logradouro,
  neighborhood: data.bairro,
});

const getCepApiAdapter = async (zipcode) => {
  if (zipCodeLengthIsEight(zipcode)) {
    const response = await cepApi.get(`${zipcode}/json`);
    if (response.data.erro) {
      throw new Error("Cep not exist");
    }
    return { ...response, data: trasnsformRequestData(response.data) };
  }
  throw new Error("cep length must equal to 8");
};

export default getCepApiAdapter;
