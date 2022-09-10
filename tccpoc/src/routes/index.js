import { Fragment } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "../pages/Login";
import Cadastro from "../pages/Authenticate";
import Home from "../pages/Home";

// so tera acesso a home qdo der o login -> por isso é uma rota privada
const Private = ({ Item }) => {

    const signed = true;

    return signed > 0 ? <Item /> : <Cadastro />;
};

const RoutesApp = () => {
    return (
        <BrowserRouter>
            <Fragment>
                <Routes>
                    <Route exact path="/login" element={<Private Item={Login} />} />
                    <Route path="/signup" element={<Cadastro />} />
                    <Route path="/home" element={<Home />}/>
                </Routes>
            </Fragment>
        </BrowserRouter>
    );
};

export default RoutesApp;