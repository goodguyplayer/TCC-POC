import axios from 'axios';
import { Button, Grid, Input, Typography } from "@mui/material/";

function App() {

  const handleUpload = async () => {
    try {
      const upload = await axios.post('http://127.0.0.1:8000/logs', { FlowID: "192.168.4.118-203.73.24.75-4504-80-6" })
      console.log(upload)
    } catch (e) {
      console.log(e)
    }
    alert('Uploading...');
  }

  return (
    <Grid container spacing={0} direction="column" alignItems="center" justifyContent="center" style={{ minHeight: '100vh' }} >
      <Grid item xs={3}>
        <Typography variant="h2" style={{ marginBottom: '30px' }}>
          Page to send an api
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


export default App;
