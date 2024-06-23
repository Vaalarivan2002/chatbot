import { Route, Routes } from "react-router-dom"
import HomePage from "../pages/HomePage/HomePage"
import AddQuestion from "../pages/AddQuestion/AddQuestion"

const AllRoutes = () => {
    return (<Routes>
        <Route path="/add-question" element={<AddQuestion/>}></Route>
        <Route path='/' element={<HomePage />}></Route>
    </Routes>);
};

export default AllRoutes;