import { Fragment } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "../pages/Login";
import Cadastro from "../pages/Authenticate";
import Home from "../pages/Home";
import Alterar from "../pages/Alterar";

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
                    <Route path="/cadastrar" element={<Cadastro />} />
                    <Route path="/inicio" element={<Home />}/>
                    <Route path="/alterar" element={<Alterar />} />
                    <Route path="*" element={<Login />} />
                </Routes>
            </Fragment>
        </BrowserRouter>
    );
};

export default RoutesApp;