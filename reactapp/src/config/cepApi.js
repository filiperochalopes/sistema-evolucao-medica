import axios from "axios";

const cepApi = axios.create({
  baseURL: process.env.REACT_APP_API_CEP_URL,
});

export default cepApi;
