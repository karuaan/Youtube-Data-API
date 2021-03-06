Youtube-Data-API
===

Technologies Used:
---

__AWS S3__ (Stored Feeds into the S3 Bucket through code).

__AWS Lambda Functions__ (Ran the code through a Lambda Function in AWS using Console).

__Youtube API__ (Pulled Channel information through Youtube Data API).

__Python3__ (Backend API for ETL Processes).

__NodeJS__ (Backend Web Interface to get data from S3 Bucket).

__ReactJS__ (Frontend Dashboard to present data pulled from S3 Bucket).

Application Data Architecture
---

![Image of Data Architecture](Youtube_Data_API_Architecture_Diagram.png "Data Architecture!")

Functionality:
---

1. Get Latest Subscriber Count and Video Count of Top 11 Channels Every 3 Hours.
2. Get Top 5 (By Video Score) Latest Videos Uploaded Every 3 Hours.
3. Get Video Score (View Count + Comment Count Relative to Like Percentage and Time in Minutes) of Videos.
4. Get Change in Subscriber Count and Video Count Every 3 Hours.

How to Run:
---

1. Clone the Repo from Github.
2. Create a Virtual Environment:

*__Make Virtual Environment:__ `python3 -m venv /path/to/new/virtual/environment`

*__Activate Virtual Environment:__ `\path\to\new\virtual\environment\Scripts\activate`

3. Install all packages in requirement.txt:

`pip install -r requirements.txt`

`pip freeze > requirements.txt`

4. Create a Google API Key: `https://console.developers.google.com/`
5. Enable Youtube Data API for Google API Keys.
6. Replace AWS Keys in Keys and Google API Keys in Keys.py.
7. Make an S3 Bucket.
8. (Optional) To run code on local machine, please run channelsBySubscribers.py. (Optional)
9. Create a Lambda in AWS and upload the code to AWS.
10. Profit!!!

Future Plans:
---

1. Project Emails once a day listing latest videos.

