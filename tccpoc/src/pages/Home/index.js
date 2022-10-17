import React, { useEffect, useState } from 'react';
import './home.css';
import axios from 'axios';
import { Button, Grid, Input, Typography } from "@mui/material/";
import Papa from "papaparse";
import { DataTable } from '../../components/Table';

const Home = () => {
  const [data, setData] = useState([])

  const handleUpload = async (event) => {
    try {
      Papa.parse(event.target.files[0], {
        header: true,
        skipEmptyLines: true,
        complete: async function (results) {
          const value = JSON.parse(JSON.stringify(results.data));
          for (let i = 0; i < value.length; i++) {
            await axios.post('http://127.0.0.1:8000/logs', value[i])
          }
          const response = await axios.post('http://127.0.0.1:5000/IA', value)
          const parsedData = JSON.parse(response.data.split('\n'))
          setData(parsedData?.map((value) => ({ value: value[0], type: value[0] >= 0.8 ? 'DDoS' : 'Benign' })))
        },
      });
    } catch (e) {
      console.log(e)
    }
  }

  return (
    <Grid container spacing={2} direction="column" alignItems="top" justifyContent="top" style={{ minHeight: '100vh' }}>
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
        {data?.length ?
          <div style={{ margin: '20px' }}>
            <DataTable rows={data?.filter(({type}) => type === 'DDOS')} />
          </div>
          : null}
        {data?.length ?
          <div style={{ margin: '20px' }}>
            <DataTable rows={data?.filter(({type}) => type === 'Benign')} />
          </div>
          : null}
      </Grid>
    </Grid>
  );
}


export default Home;