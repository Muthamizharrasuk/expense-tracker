import { Routes, Route } from "react-router-dom"
import Dashboard from "../pages/Dashboard"
import ExpensesPage from "../pages/ExpensesPage"
import BudgetsPage from "../pages/BudgetsPage"



const AppRoutes = () => {
    return (
        <Routes>    
            <Route path="/" element={<Dashboard />} />
            <Route path="/expenses" element={<ExpensesPage />} />
            <Route path="/budgets" element={<BudgetsPage />} />
        </Routes>
    )
}

export default AppRoutes