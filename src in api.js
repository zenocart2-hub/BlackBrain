import axios from "axios";

/* ---------------------------------------
   BASE CONFIG
---------------------------------------- */
const API_BASE_URL = "http://127.0.0.1:8000";

/* ---------------------------------------
   AXIOS INSTANCE
---------------------------------------- */
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json"
  }
});

/* ---------------------------------------
   REQUEST INTERCEPTOR (JWT)
---------------------------------------- */
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

/* ---------------------------------------
   AUTH APIs
---------------------------------------- */
export const signup = (data) => {
  return api.post("/auth/signup", data);
};

export const login = (data) => {
  return api.post("/auth/login", data);
};

/* ---------------------------------------
   BRAIN APIs
---------------------------------------- */
export const askBrain = (question, mode = "basic") => {
  return api.post("/brain/ask", {
    question,
    mode
  });
};

/* ---------------------------------------
   HISTORY APIs
---------------------------------------- */
export const getHistory = (limit = 20, skip = 0) => {
  return api.get(`/history?limit=${limit}&skip=${skip}`);
};

export const clearHistory = () => {
  return api.delete("/history/clear");
};

/* ---------------------------------------
   SUBSCRIPTION / PAYMENT APIs
---------------------------------------- */
export const getPlans = () => {
  return api.get("/subscription/plans");
};

export const createPaymentOrder = (plan_code) => {
  return api.post("/subscription/create-order", {
    plan_code
  });
};

export const verifyPayment = (data) => {
  return api.post("/subscription/verify", data);
};

export const getSubscriptionStatus = () => {
  return api.get("/subscription/status");
};

/* ---------------------------------------
   USER / PROFILE APIs
---------------------------------------- */
export const getMyProfile = () => {
  return api.get("/settings/me");
};

export const updateSettings = (settings) => {
  return api.post("/settings/update", settings);
};

/* ---------------------------------------
   LOGOUT HELPER
---------------------------------------- */
export const logout = () => {
  localStorage.removeItem("token");
  window.location.href = "/login";
};

export default api;