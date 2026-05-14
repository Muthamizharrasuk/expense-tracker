import { useExpenses } from "../context/ExpenseContext"

const Dashboard = () => {
  const { expenses, budgets } = useExpenses()
  const total = expenses.reduce((sum, expense) => sum + expense.amount, 0)

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Total spent: ${total}</p>
      <p>Number of expenses: {expenses.length}</p>
      <p>Number of budgets: {budgets.length}</p>

      <h2>Budget Alerts</h2>
      {budgets.map((budget) => {
        const categoryExpenses = expenses.filter(e => e.category === budget.category)
        const totalSpent = categoryExpenses.reduce((sum, expense) => sum + expense.amount, 0)

        return (
          <div key={budget._id}>
            <p>{budget.category} — Spent: ${totalSpent} / Limit: ${budget.limit}</p>
            {totalSpent > budget.limit && <p style={{ color: "red" }}>Over budget!</p>}
            {totalSpent >= budget.limit * 0.8 && totalSpent < budget.limit && <p style={{color: "yellow"}}>Approaching budget!</p>}
          </div>
        )
      })}
    </div>
  )
}

export default Dashboard
        