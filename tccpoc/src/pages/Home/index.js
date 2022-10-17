import './home.css';
import axios from 'axios';
import { Button, Grid, Input, Typography } from "@mui/material/";
import { useState } from 'react';
import React from 'react';
import Papa from "papaparse";

const Home = () => {
  const [parsedData, setParsedData] = useState([]);
  //State to store table Column name
  const [tableRows, setTableRows] = useState([]);
  //State to store the values
  const [values, setValues] = useState([]);

  const [myDDosList, setDDosList] = useState([]);
  const [myBenignLists, setBenignLists] = useState([]);

  const handleUpload = async (event) => {
    try {
      Papa.parse(event.target.files[0], {
        header: true,
        skipEmptyLines: true,
        complete: async function (results) {
          const rowsArray = [];
          const valuesArray = [];
          results.data.map((d) => {
            rowsArray.push(Object.keys(d));
            valuesArray.push(Object.values(d));
          });
          setParsedData(results.data);
          setTableRows(rowsArray[0]);
          setValues(valuesArray);

          var value = JSON.parse(JSON.stringify(results.data));
          for (let i = 0; i < value.length; i++) {
            const upload = await axios.post('http://127.0.0.1:8000/logs', value[i])
          }
          const resposta = await axios.post('http://127.0.0.1:5000/IA', value)
          var splitResposta = resposta.data.split(' ')
          var parse = JSON.parse(splitResposta)

          for (let i = 0; i < parse.length; i++) {
            if (parse[i] >= 0.8) {
              myDDosList.push({ DDoS: parse[i][0] })
            } else {
              myBenignLists.push({ Benign: parse[i][0] })
            }
          }
          
          setDDosList(myDDosList)
          setBenignLists(myBenignLists)
          console.log(myDDosList)
          console.log(myBenignLists)
        },
      });
    } catch (e) {
      console.log(e)
    }
  }

  return (
    <Grid container spacing={0} direction="column" alignItems="center" justifyContent="center" style={{ minHeight: '100vh' }} >
      <Grid item xs={3}>
        <Typography variant="h2" style={{ marginBottom: '30px' }}>
          Enviar o arquivo csv para a inteligencia Artificial
        </Typography>
        <label htmlFor="contained-button-file">
          <Input onChange={handleUpload} style={{ display: 'none' }} accept=".csv" id="contained-button-file" multiple type="file" />
          <Button variant="contained" component="span">
            Upload
          </Button>
        </label>
      </Grid>
    </Grid>
  );
}



export default Home;