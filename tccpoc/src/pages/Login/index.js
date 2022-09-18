import React, { useState } from "react";
import "./login.css";
import { MdEmail, MdLock } from "react-icons/md";
import { HiEye, HiEyeOff } from "react-icons/hi";
import { Link, useNavigate } from "react-router-dom";
import axios from 'axios';


const Login = () => {
    const [inputs, setInputs] = useState({});
    const [show, setShow] = useState(false);
    const navigate = useNavigate();
    const serverEndPoint = 'http://127.0.0.1:8000/login'
    const BaseURL = `${serverEndPoint}`;

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
        try {
            const get = await axios.get(BaseURL);
            if (get.data.data[0].find(input => input.email === inputs.email) && get.data.data[0].find(input => input.senha === inputs.password)) {
                navigate("/inicio");
                return;
            } else {
                alert('email ou senha inválidos!')
            }
        } catch (e) {
            console.log(e)
        }
    }

    return (
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
                    <h4>Esqueceu sua senha?</h4>
                    <Link to="/alterar" className="link-cadastro">&nbsp;<em>resetar senha? </em></Link>
                </div>
            </div>
        </form>
    );
};

export default Login;


