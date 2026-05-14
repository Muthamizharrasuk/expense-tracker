import { BrowserRouter } from "react-router-dom"
import AppRoutes from "./routes/AppRoutes"
import { ExpenseProvider } from "./context/ExpenseContext"
import { Link } from "react-router-dom"

function App() {
  return (
    <BrowserRouter>
      <ExpenseProvider>
        <nav>
          <Link to="/">Dashboard</Link> | 
          <Link to="/expenses">Expenses</Link> | 
          <Link to="/budgets">Budgets</Link>
        </nav>
        <AppRoutes /> 
      </ExpenseProvider>
    </BrowserRouter>
  )
}

export default App    