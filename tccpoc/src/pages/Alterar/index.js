import React, { useState } from "react";
import "./alterar.css";
import { MdEmail, MdLock } from "react-icons/md";
import { HiEye, HiEyeOff } from "react-icons/hi";
import { Link, useNavigate } from "react-router-dom";
import axios from 'axios';


const Alterar = () => {
    const [email, setInputEmail] = useState("");
    const [senha, setInputSenha] = useState("");
    const [show, setShow] = useState(false);
    const navigate = useNavigate();
    const serverEndPoint = 'http://127.0.0.1:8000/login'
    const BaseURL = `${serverEndPoint}`;

    const handleChangeEmail = (event) => {
        setInputEmail(event.target.value);
    }

    const handleChangeSenha = (event) => {
        setInputSenha(event.target.value);
    }

    const handleSubmit = (event) => {
        event.preventDefault();
    }

    const handleClick = (e) => {
        e.preventDefault();
        setShow(!show);
    };

    const handleChangePassword = async () => {
        try {
            const get = await axios.get(BaseURL)
            for (let i = 0; i < get.data.data[0].length; i++) {
                if (get.data.data[0][i].email === email) {
                    await axios.put(`${serverEndPoint}/${get.data.data[0][i].id}`, { senha: senha })
                    alert('senha trocada com sucesso!')
                    navigate("/login");
                    return;
                }
            }
            alert('email não cadastrado no sistema')
        } catch (e) {
            console.log(e)
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <div className="login">
                <div className="login-right">
                    <h1>Trocar Senha</h1>
                    <div className="login-loginInputEmail">
                        <MdEmail />
                        <input
                            type="email"
                            placeholder="Digite um email"
                            name="email"
                            value={email}
                            onChange={handleChangeEmail}
                        />
                    </div>
                    <div className="login-loginInputPassword">
                        <MdLock />
                        <input
                            type={show ? "text" : "password"}
                            placeholder="Digite sua senha nova senha"
                            name="password"
                            value={senha}
                            onChange={handleChangeSenha}
                        />
                        <div className="login-eye">
                            {show ? (
                                <HiEye size={20} onClick={handleClick} />
                            ) : (
                                <HiEyeOff size={20} onClick={handleClick} />
                            )}
                        </div>
                    </div>
                    <button type="submit" onClick={handleChangePassword}>Trocar Senha</button>
                    <h4>Já possui uma conta?</h4>
                    <Link to="/login" className="link-cadastro">&nbsp;<em>Entre </em></Link>
                </div>
            </div>
        </form>
    );
};

export default Alterar;


