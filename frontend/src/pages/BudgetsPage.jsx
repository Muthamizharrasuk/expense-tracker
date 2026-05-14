import { useExpenses } from "../context/ExpenseContext"
import { useState } from "react"

const BudgetsPage = () => {
  const { budgets, addBudget, removeBudget } = useExpenses()
  const [form, setForm] = useState({ limit: "", month: "", category: "" })

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    await addBudget(form)
    setForm({ limit: "", month: "", category: "" })
  }

  return (
    <div>
      <h1>Budgets</h1>
      <form onSubmit={handleSubmit}>
        <input name="limit" placeholder="Limit" value={form.limit} onChange={handleChange} />
        <input name="month" placeholder="Month" value={form.month} onChange={handleChange} />
        <input name="category" placeholder="Category" value={form.category} onChange={handleChange} />
        <button type="submit">Add Budget</button>
      </form>

      {budgets.map((budget) => (
        <div key={budget._id}>
          <p>{budget.category} — ${budget.limit}</p>
          <button onClick={() => removeBudget(budget._id)}>Delete</button>
        
        </div>

      ))}
    </div>
  )
}

export default BudgetsPage