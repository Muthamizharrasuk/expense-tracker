import axios from "axios"

const api = axios.create({
  baseURL: "http://127.0.0.1:8000"
})


export const getExpenses = () => api.get("/expenses")
export const createExpense = (data) => api.post("/expenses", data)
export const updateExpense = (id, data) => api.put(`/expenses/${id}`, data)
export const deleteExpense = (id) => api.delete(`/expenses/${id}`)

export const getBudgets = () => api.get("/budgets")
export const createBudget = (data) => api.post("/budgets", data)
export const updateBudget = (id, data) => api.put(`/budgets/${id}`, data)
export const deleteBudget = (id) => api.delete(`/budgets/${id}`)