import React, { useState } from "react";
import "./authenticate.css";
import { MdEmail, MdLock } from "react-icons/md";
import { HiEye, HiEyeOff } from "react-icons/hi";
import { Link, useNavigate } from "react-router-dom";
import { AiOutlineUnlock } from "react-icons/ai"
import axios from 'axios';

const Cadastro = () => {
    const [email, setInputEmail] = useState("");
    const [senha, setInputSenha] = useState("");
    const [confSenha, setInputConfSenha] = useState("");
    const [showsenha, setShowSenha] = useState(false);
    const [showconfsenha, setShowConfSenha] = useState(false);
    const navigate = useNavigate();
    const serverEndPoint = 'http://127.0.0.1:8000/login';

    const handleChangeEmail = (event) => {
        setInputEmail(event.target.value);
    }

    const handleChangeSenha = (event) => {
        setInputSenha(event.target.value);
    }

    const handleChangeConfSenha = (event) => {
        setInputConfSenha(event.target.value);
    }

    const handleSubmit = (event) => {
        event.preventDefault();
    }

    const handleClickSenha = (e) => {
        e.preventDefault();
        setShowSenha(!showsenha);
    };

    const handleClickConfSenha = (e) => {
        e.preventDefault();
        setShowConfSenha(!showconfsenha);
    };


    const handleCreate = async () => {
        try {
            if (senha !== confSenha) {
                alert("senhas diferentes")
                return;
            }
            if (senha === "" || confSenha === "" || email === "") {
                alert("nao pode ter um ou mais valores dos campos em branco")
                return;
            }
            const get = await axios.get(serverEndPoint);
            for (let i = 0; i < get.data.data[0].length; i++) {
                if (get.data.data[0][i].email === email) {
                    alert("email já cadastrado no sistema!")
                    return;
                }
            }
            await axios.post(`${serverEndPoint}`, { email: email, senha: senha, confsenha: confSenha })
            alert("Usuário cadatrado com sucesso!");
            navigate("/login");
            return;
        } catch (e) {
            console.log(e)
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <div className="login">
                <div className="login-right">
                    <h1>Criar conta</h1>
                    <div className="login-loginInputEmail">
                        <MdEmail />
                        <input
                            type="email"
                            placeholder="Digite um email  "
                            name="email"
                            value={email}
                            onChange={handleChangeEmail}
                        />
                    </div>
                    <div className="login-loginInputPassword">
                        <MdLock />
                        <input
                            type={showsenha ? "text" : "password"}
                            placeholder="Digite sua senha"
                            name="password"
                            value={senha}
                            onChange={handleChangeSenha}
                        />
                        <div className="login-eye">
                            {showsenha ? (
                                <HiEye size={20} onClick={handleClickSenha} />
                            ) : (
                                <HiEyeOff size={20} onClick={handleClickSenha} />
                            )}
                        </div>
                    </div>
                    <div className="login-loginInputPassword">
                        <AiOutlineUnlock />
                        <input
                            type={showconfsenha ? "text" : "password"}
                            placeholder="Confime sua senha"
                            name="confirm_password"
                            value={confSenha}
                            onChange={handleChangeConfSenha}
                        />
                        <div className="login-eye">
                            {showconfsenha ? (
                                <HiEye size={20} onClick={handleClickConfSenha} />
                            ) : (
                                <HiEyeOff size={20} onClick={handleClickConfSenha} />
                            )}
                        </div>
                    </div>
                    <button type="submit" onClick={handleCreate}>Inscrever-se</button>
                    <h4>Já possui uma conta?</h4>
                    <Link to="/login" className="link-cadastro">&nbsp;<em>Entre </em></Link>

                </div>
            </div>
        </form>
    );
}

export default Cadastro;
