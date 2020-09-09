Youtube-Data-API
===

Technologies Used:
---

*__AWS S3__ (Stored Feeds into the S3 Bucket through code).

*__AWS Lambda Functions__ (Ran the code through a Lambda Function in AWS using Console).

*__Youtube API__ (Pulled Channel information through Youtube Data API).

*__Python3__ (Backend API for ETL Processes).

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

__Windows:__ `python3 -m venv /path/to/new/virtual/environment`

__Activate Virtual Environment:__ `\path\to\new\virtual\environment\Scripts\activate`

    3. Install all packages in requirement.txt:

        1. `pip install -r requirements.txt`

        2. `pip freeze > requirements.txt`
    
    4. Create a Google API Key: `https://console.developers.google.com/`

    5. Enable Youtube Data API for Google API Keys.

    6. Replace AWS Keys in Keys and Google API Keys in Keys.py.

    7. Make an S3 Bucket.

    8. (Optional) To run code on local machine, please run channelsBySubscribers.py. (Optional)

    9. Create a Lambda in AWS and upload the code to AWS.

    10. Profit.

Future Plans:
---

    1. Make a Dashboard for this application.
    
    2. Let users provide channels they are interested in.
    
    3. Provide users updates on those channels.
    
    4. Project Emails once a day listing latest videos.

