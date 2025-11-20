# Times Tables Quiz App with Google Sheets

The application in this repository is a times tables quiz that is [deployed here](https://if-combined-quiz-json-jgiwxdpztjmpvfnakvakh7.streamlit.app/) on Steamlit Community Cloud. The quiz randomly generates multiplication questions for users.

User results are stored in a [Google Sheet](https://docs.google.com/spreadsheets/d/1Nre44JhGSnAGPaBKMPUw9_9jKS7jcc8ivt4Xt8AujH0), where anyone can view the quiz outcomes.

## How it works

The app has three screens, each implemented in its own module:

- Welcome screen
- Quiz screen
- End screen

## Saving Data to Google Sheets in a Streamlit App

This guide explains how to connect your Streamlit app to a Google Sheet so you can save data such as names, scores, or timestamps.

Follow each step in order.

## Step 1. Create a new Google Sheet

1. Go to [Google Sheets](https://sheets.google.com) 
2. Make a blank sheet.  
3. Copy the Sheet ID from the URL.

Example:

```text
https://docs.google.com/spreadsheets/d/ABC1234567890/edit#gid=0  
Sheet ID → **ABC1234567890**
```

## Step 2. Create a Google Cloud Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a project.  
3. Open **IAM & Admin → Service Accounts**.  
4. Click **Create Service Account**.  
5. Name it anything (for example, `streamlit-app`).  
6. Give it the **Editor** role.  

## Step 3. Create a Service Account Key (JSON)

1. Open your service account.  
2. Go to the **Keys** tab.  
3. Click **Add Key → Create New Key**.  
4. Choose **JSON**.  
5. Download the file.

## Step 4. Share Your Google Sheet

1. Open your Google Sheet.  
2. Click **Share**.  
3. Add the service account email from the JSON file.  
4. Give **Editor** access.

## Add Secrets to Streamlit

Create a folder:

```text
.streamlit
```

Inside it, create:

```text
secrets.toml
```

Paste:

```text
[gcp_service_account]
type = "service_account"
project_id = "YOUR_PROJECT_ID"
private_key_id = "YOUR_PRIVATE_KEY_ID"
private_key = "YOUR_PRIVATE_KEY"
client_email = "YOUR_SERVICE_ACCOUNT_EMAIL"
client_id = "YOUR_CLIENT_ID"

SHEET_ID = "YOUR_SHEET_ID"
```

Replace all values with your own.

## Use the Storage Code

```python
from storage import save_result
save_result(name, score)
```

## Deployment on Streamlit Cloud

1. Open your deployed app’s **Settings**.  
2. Go to **Secrets**.  
3. Paste the same `secrets.toml` content.

Your Streamlit app can now write to your Google Sheet.
