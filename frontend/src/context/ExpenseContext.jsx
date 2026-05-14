import { createContext, useContext, useState, useEffect } from "react"
import { getExpenses, createExpense, deleteExpense, getBudgets, createBudget, deleteBudget,updateExpense} from "../services/api"

const ExpenseContext = createContext()

export const ExpenseProvider = ({ children }) => {
  const [expenses, setExpenses] = useState([])
  const [budgets, setBudgets] = useState([])

  useEffect(() => {
    
    getExpenses().then(response => setExpenses(response.data))
    getBudgets().then(response => setBudgets(response.data))
  }, [])

  const addExpense = async (expenseData) => {
  await createExpense(expenseData)
  const response = await getExpenses()
  setExpenses(response.data)
}
  const removeExpense = async (id) => {
    await deleteExpense(id)                         
    setExpenses(expenses.filter(expense => expense._id !== id)) 
  }
 const addBudget = async (budgetData) => {
  await createBudget(budgetData)
  const response = await getBudgets()
  setBudgets(response.data)
}
const removeBudget = async (id) => {
  await deleteBudget(id)
  setBudgets(budgets.filter(budget => budget._id !== id))
}
const updateExpenseItem = async (id, data) => {
  await updateExpense(id, data)
  const response = await getExpenses()
  setExpenses(response.data)
}

  return (
    <ExpenseContext.Provider value={{ expenses, budgets, addExpense, removeExpense, addBudget, removeBudget, updateExpenseItem}}>
      {children}
    </ExpenseContext.Provider>
  )
}

export const useExpenses = () => useContext(ExpenseContext)