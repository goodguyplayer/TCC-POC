import React, { useState } from "react";
import "./login.css";
import { MdEmail, MdLock } from "react-icons/md";
import { HiEye, HiEyeOff } from "react-icons/hi";
import { Link, useNavigate } from "react-router-dom";
import { withRouter } from "react-router-dom";
import Cadastro from "../Authenticate";


const Login = () => {
    // definindo estados iniciais 
    // [] para manipular o estado das propriedades
    const [error, setError] = useState("");
    const [inputs, setInputs] = useState({});
    const [show, setShow] = useState(false);
    const [email, setEmail] = useState("");
    const [emailConf, setEmailConf] = useState("");
    const [senha, setSenha] = useState("");
    const navigate = useNavigate();
    // const { signup } = useAuth();

    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        // console.log(event.target)

        setInputs(values => ({ ...values, [name]: value }))

    }

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(inputs);
    }

    const handleClick = (e) => {
        e.preventDefault();
        setShow(!show);
    };

    const handleLogin = () => {
        if (!email | !senha) {
            setError("Preencha todos os campos");
            return;
        }
        navigate("/signup");
    };

    return (
        // onSubmit -> envia p formulario
        <form onSubmit={handleSubmit}>
            <div className="login">
                <div className="login-right">
                    <h1>Acessar App</h1>
                    <div className="login-loginInputEmail">
                        <MdEmail />
                        <input
                            type="email"
                            placeholder="Digite um email "
                            name="email"
                            value={inputs.email}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="login-loginInputPassword">
                        <MdLock />
                        <input
                            type={show ? "text" : "password"}
                            placeholder="Digite sua senha"
                            name="password"
                            value={inputs.password}
                            onChange={handleChange}
                        />
                        <div className="login-eye">
                            {show ? (
                                <HiEye size={20} onClick={handleClick} />
                            ) : (
                                <HiEyeOff size={20} onClick={handleClick} />
                            )}
                        </div>
                    </div>
                    <button type="submit">Entrar</button>
                    <h4>Não possui conta?</h4>
                    <Link to="/signup" className="link-cadastro">&nbsp;<em>Cadastre-se </em></Link>

                </div>
            </div>
        </form>
    );
};

export default Login;


