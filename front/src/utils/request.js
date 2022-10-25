import axios from "axios";

// 创建 axios 实例
const request = axios.create({
  // API 请求的默认前缀
  // baseURL: "http://localhost:5173/api",
  baseURL: "/api",
  timeout: 5000, // 请求超时时间
});

export const get = async (url, params) => {
  let data = await request.get(url, {params})
  return data
}

export const post = async (url, data) => {
  let res = await request.post(url, data)
  return res
}