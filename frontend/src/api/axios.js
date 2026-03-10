import axios from "axios";

const instance = axios.create({
  baseURL: "https://booknest-where-stories-nestle2.onrender.com/api"
});

export default instance;