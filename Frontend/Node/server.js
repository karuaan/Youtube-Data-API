const express = require('express');
const app = express();
const router = new express.Router();
const port = 1000;
const aws = require('aws-sdk');
const { AWS_Keys } = require( './Keys.js' );
const cors = require( 'cors' );
const bodyParser = require( 'body-parser' );
const jsonParser = bodyParser.json();

app.use(
  cors({
    origin: 'http://localhost:1000',
    credentials: true,
  })
);

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

async function uploadFile ( data )
{
  const uploadParams = {
    Bucket: AWS_Keys.bucketName,
    Key: AWS_Keys.channelsListFile,
    Body: data
  }

  s3.upload(params, function(err, new_data) {
    if (err) {
        throw err;
    }
    console.log(`File uploaded successfully. ${new_data.Location}`);
});
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
} );

app.get( '/express_backend', async ( req, res ) =>
{
  res.send( { response: 'Received' } );
  }
)

app.post('/channels_list', jsonParser, async( req, res ) =>
{
  req.setTimeout( 100 );
  console.log( 'channels_list' );
  console.log( req.ody.Channels_List );
  try
  {
    const upload_feed = await uploadFile( req.body );
    return res.status( 200 ).send( upload_feed );
  }
  catch ( err )
  {
    return res.status( 500 ).send( err );
  }
  
} );
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
