import './home.css';
import axios from 'axios';
import { Button, Grid, Input, Typography } from "@mui/material/";


const Home = () =>{
    const handleUpload = async () => {
        try {
          const upload = await axios.post('http://127.0.0.1:8000/logs', { FlowID: "192.168.4.118-203.73.24.75-4504-80-6" })
          await axios.post('http://127.0.0.1:5000/IA', { FlowID: "192.168.4.118-203.73.24.75-4504-80-7" })
        } catch (e) {
          console.log(e)
        }
        alert('Uploading...');
      }

    return (
        <Grid container spacing={0} direction="column" alignItems="center" justifyContent="center" style={{ minHeight: '100vh' }} >
          <Grid item xs={3}>
            <Typography variant="h2" style={{ marginBottom: '30px' }}>
              Enviar o arquivo csv para a inteligencia Artificial 
            </Typography>
            <label htmlFor="contained-button-file">
              <Input onChange={handleUpload} style={{ display: 'none' }} accept="image/*" id="contained-button-file" multiple type="file" />
              <Button variant="contained" component="span">
                Upload
              </Button>
            </label>
          </Grid>
        </Grid>
      );
}

export default Home;