import React, { useState } from "react";
import "./authenticate.css";
import { MdEmail, MdLock } from "react-icons/md";
import { HiEye, HiEyeOff } from "react-icons/hi";
import { Link, useNavigate } from "react-router-dom";
import { AiOutlineUnlock } from "react-icons/ai"
import axios from 'axios';

const Cadastro = () => {
    const [inputs, setInputs] = useState({});
    const [show, setShow] = useState(false);
    const navigate = useNavigate();
    const serverEndPoint = 'http://127.0.0.1:8000/login';

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

    const handleCreate = async () => {
        try {
            const get = await axios.get(serverEndPoint);
            if (get.data.data[0].find(input => input.email === inputs.email) != undefined) {
                alert("email já cadastrado no sistema!")
            } else {
                const upload = await axios.post(`${serverEndPoint}`, { email: inputs.email, senha: inputs.password, confsenha: inputs.confirm_password })
                alert("Usuário cadatrado com sucesso!");
                navigate("/inicio");
            }
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
                    <div className="login-loginInputPassword">
                        <AiOutlineUnlock />
                        <input
                            type={show ? "text" : "password"}
                            placeholder="Confime sua senha"
                            name="confirm_password"
                            value={inputs.confirm_password}
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
                    <button type="submit" onClick={handleCreate}>Inscrever-se</button>
                    <h4>Já possui uma conta?</h4>
                    <Link to="/login" className="link-cadastro">&nbsp;<em>Entre </em></Link>

                </div>
            </div>
        </form>
    );
}

export default Cadastro;
