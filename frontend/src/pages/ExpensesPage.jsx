import { useExpenses } from "../context/ExpenseContext"
import { useState } from "react"

const ExpensesPage = () => {
  const { expenses, addExpense, removeExpense, updateExpenseItem } = useExpenses()
  const [form, setForm] = useState({ amount: "", category: "", description: "" })
  const [editingId, setEditingId] = useState(null)

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

const handleSubmit = async (e) => {
  e.preventDefault()
  if (editingId) {
    await updateExpenseItem(editingId, form)
    setEditingId(null)
  } else {
    await addExpense(form)
  }
  setForm({ amount: "", category: "", description: "" })
}

  return (
    <div>
      <h1>Expenses</h1>
      <form onSubmit={handleSubmit}>
        <input name="amount" placeholder="Amount" value={form.amount} onChange={handleChange} />
        <input name="category" placeholder="Category" value={form.category} onChange={handleChange} />
        <input name="description" placeholder="Description" value={form.description} onChange={handleChange} />
        <button type="submit">Add Expense</button>
      </form>

      {expenses.map((expense) => (
        <div key={expense._id}>
          <p>{expense.category} — ${expense.amount}</p>
          <button onClick={() => removeExpense(expense._id)}>Delete</button>
          <button onClick={() => {
  setEditingId(expense._id)
  setForm({ amount: expense.amount, category: expense.category, description: expense.description })
}}>Edit</button>
        </div>
      ))}
    </div>
  )
}

export default ExpensesPage