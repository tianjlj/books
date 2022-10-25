import { get, post } from "@/utils/request";

const apis_api = {
  get_apis: "/apis/get_apis",
  get_type: "/apis/get_type",
};

export const get_apis = async (params) => {
  let res = await get(apis_api.get_apis, params);
  return res
};

export const get_type = async () => {
    let res = await get(apis_api.get_type)
    return res
}
