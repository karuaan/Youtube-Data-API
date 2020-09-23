const express = require('express');
const app = express();
const port = 1000;
const aws = require('aws-sdk');
const { AWS_Keys } = require('./keys.js');;

aws.config.update({
    accessKeyId: AWS_Keys.accessKeyId,
    secretAccessKey: AWS_Keys.secretAccessKey,
    region: AWS_Keys.Region
});

const params = {
    Bucket: AWS_Keys.bucketName,
    Key: AWS_Keys.readFileName
  };

const s3 = new aws.S3();

async function get_latest()
{
    try
    {
        console.log('Reading File:');
        var response = await s3.getObject(params).promise();

        var json = await JSON.parse(response.Body);

        return json;
    }
    catch(err)
    {
        throw new Error("Could not retrieve file from s3: " + err.message);
    }
}

// create a GET route
app.get('/express_backend', async (req, res) => {

  const data = await get_latest();

  res.send(data);
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})