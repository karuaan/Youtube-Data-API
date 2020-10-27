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

const userchannelsparams = {
  Bucket: AWS_Keys.bucketName,
  Key: AWS_Keys.mychannelsfile
}

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

async function get_user_channel()
{
    try
    {
        console.log('Reading File:');
        var response = await s3.getObject(userchannelsparams).promise();

        var json = await JSON.parse(response.Body);

        return json;
    }
    catch(err)
    {
        const new_json = {"Last_Update_Time" : "No Channels Added!", "Channel_Details" : {"Name" : "No Channels are available. Please add channels!"}}
        return new_json;
    }
}

// create a GET route
app.get('/express_backend', async (req, res) => {

  const data = await get_latest();

  if (data == "none") {
    res.send([]);
  }

  else
  {
    res.send(data);
  }
});

app.get('/userchannels', async (req, res) => {

  const data = await get_user_channel();

    res.send(data);
});


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})