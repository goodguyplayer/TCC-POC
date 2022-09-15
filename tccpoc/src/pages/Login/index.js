import React, { useState } from "react";
import "./login.css";
import { MdEmail, MdLock } from "react-icons/md";
import { HiEye, HiEyeOff } from "react-icons/hi";
import { Link, useNavigate } from "react-router-dom";
import axios from 'axios';


const Login = () => {
    // definindo estados iniciais 
    // [] para manipular o estado das propriedades
    const [inputs, setInputs] = useState({});
    const [show, setShow] = useState(false);
    const navigate = useNavigate();

    var id = "631f3f0bc800c41e97a2dc3a";
    const BaseURL = `http://127.0.0.1:8000/logs/login/${id}`;

    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({ ...values, [name]: value }))
    }

    const handleSubmit = (event) => {
        event.preventDefault();
    }

    const handleClick = (e) => {
        e.preventDefault();
        setShow(!show);
    };

    const handleLogin = async () => {
        var open = false;
        try {
            const get = await axios.get(BaseURL)
            console.log(get.data.data[0].senha);
            if (get.data.data[0].email === inputs.email && get.data.data[0].senha === inputs.password) {
                //setUser({ email, senha });
                navigate("/inicio");
                return;
            } else {
                open = true;
            }
        } catch (e) {
            console.log(e)
        }
    }

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
                    <button type="submit" onClick={handleLogin}>Entrar </button>
                    <h4>Não possui conta?</h4>
                    <Link to="/cadastrar" className="link-cadastro">&nbsp;<em>Cadastre-se </em></Link>
                </div>
            </div>
        </form>
    );
};

export default Login;


