const aws = require('aws-sdk');
const { AWS_Keys } = require('./keys.js');
const { LexModelBuildingService } = require('aws-sdk');

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

export async function get_latest()
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


