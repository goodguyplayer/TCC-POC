import React, { useState } from "react";
import "./authenticate.css";
import { MdEmail, MdLock } from "react-icons/md";
import { HiEye, HiEyeOff } from "react-icons/hi";
import { Link, useNavigate } from "react-router-dom";
import { withRouter } from "react-router-dom";
import { AiOutlineUnlock } from "react-icons/ai"

const Cadastro = () => {
    const [error, setError] = useState("");
    const [inputs, setInputs] = useState({});
    const [show, setShow] = useState(false);
    const [email, setEmail] = useState("");

    const [senha, setSenha] = useState("");
    const [senhaConf, setSenhaConf] = useState("");
    const navigate = useNavigate();

    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;

        console.log("event.target: ", event.target)
        console.log("name: ", name)
        console.log("value: ", value)

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

    return (
        // onSubmit -> envia p formulario
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
                    <button type="submit">Criar</button>
                    <h4>Já possui uma conta?</h4>
                    <Link to="/login" className="link-cadastro">&nbsp;<em>Entre </em></Link>

                </div>
            </div>
        </form>
    );
}

export default Cadastro;
