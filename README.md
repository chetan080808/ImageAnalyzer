# 🌩️ AI Image Analyzer — Serverless AWS Project (S3 + API Gateway + Lambda + Rekognition)

A fully serverless, free-tier–friendly AWS project that analyzes images using **Amazon Rekognition**.  
This application allows users to upload an image from a browser, sends it to API Gateway → Lambda → Rekognition, and returns AI-generated labels.

Perfect for students, beginners, and anyone learning AWS & serverless development.

---

## 🚀 Features

- 🔍 Image label detection using **Amazon Rekognition**
- 🖥️ Static frontend hosted on **Amazon S3**
- ⚡ API built using **Amazon API Gateway (HTTP API)**
- 🧠 Backend processing with **AWS Lambda (Python)**
- 🌐 Fully serverless, scalable, and free-tier compatible
- 🔓 CORS-enabled communication between S3 and API Gateway

---

## 🧱 Architecture Overview

```
Browser 
   ↓
S3 Static Website Hosting
   ↓
API Gateway (HTTP API)
   ↓
Lambda (Python)
   ↓
Amazon Rekognition
   ↓
JSON Response to Browser
```

---

## 📦 Project Structure

```
├── index.html               # Frontend UI (upload + analyze button)
├── lambda_function.py       # Lambda backend (Rekognition logic + CORS)
└── README.md                # Full setup guide
```

---

# 🛠️ Step-by-Step Setup Guide

Follow these instructions to build the entire system from scratch.

---

# 1️⃣ Create the S3 Static Website (Frontend)

### 1. Create an S3 bucket
1. Go to **AWS Console → S3 → Create bucket**
2. Set:
   - Bucket name: must be globally unique  
   - Region: same region you plan to use for Lambda & API Gateway
3. **Uncheck** “Block all public access”
4. Create bucket

---

### 2. Add public-read bucket policy  
Go to:

**Bucket → Permissions → Bucket policy → Edit**

Replace `BUCKET_NAME` below:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::BUCKET_NAME/*"
    }
  ]
}
```

---

### 3. Enable Static Website Hosting
Go to:

**Bucket → Properties → Static website hosting → Enable**

Set:

- **Index document:** `index.html`

Take note of your website URL:

```
http://BUCKET_NAME.s3-website-REGION.amazonaws.com
```

---

### 4. Upload your frontend
Upload:

- `index.html`

Ensure metadata → **Content-Type: text/html**

---

# 2️⃣ Create the AWS Lambda Function

### 1. Create function
AWS Console → **Lambda → Create function**

- Author from scratch  
- Name: `image-analyzer`
- Runtime: **Python 3.9 or Python 3.10**

---

### 2. Add permissions (IAM role)
Your Lambda role must include:

- `AWSLambdaBasicExecutionRole`
- `AmazonRekognitionReadOnlyAccess`

Add via IAM → Roles → attach both policies.

---

### 3. Add backend code
Paste **lambda_function.py** into the Lambda code editor.

This code includes:
- OPTIONS preflight handling  
- Base64 image decoding  
- Rekognition DetectLabels API call  
- JSON response with CORS headers  

Click **Deploy**.

---

# 3️⃣ Create API Gateway (HTTP API)

### 1. Create API
1. Go to **API Gateway → Create API**
2. Choose **HTTP API → Build**
3. Click **Add integration → Lambda**
4. Select your `image-analyzer` function

---

### 2. Create Route
Add a route:

- Method: **ANY**
- Path: **/**  
- Attach Lambda integration

---

### 3. Enable CORS
Go to **CORS settings**:

- Allowed origins: `*`
- Allowed methods: `POST,OPTIONS`
- Allowed headers: `*`

Save changes.

---

### 4. Deploy the API
Use `$default` stage or create a new one like `prod`.

Copy the **Invoke URL**, example:

```
https://xxxxx1234.execute-api.ap-south-1.amazonaws.com
```

---

# 4️⃣ Connect Frontend to Backend

Open `index.html` and replace:

```js
const apiUrl = "REPLACE_WITH_YOUR_API_GATEWAY_URL";
```

with your actual Invoke URL.

Upload the updated `index.html` to S3 again (overwrite).

---

# 5️⃣ Test Everything

### ✔ Browser Test
Open your S3 website URL and:

1. Upload an image  
2. Click **Analyze**  
3. See AI-generated labels appear instantly  

### ✔ Backend Test (optional)
Using `curl`:

```bash
curl -i -X POST "<API_URL>"   -H "Content-Type: application/json"   -d '{"image":"<BASE64_STRING>"}'
```

---

# 🧩 Troubleshooting

### ❌ “Failed to fetch”
- CORS not configured properly  
- Static website not served from S3  
- Lambda not handling OPTIONS requests

### ❌ Rekognition Access Denied
Add IAM policy:  
`AmazonRekognitionReadOnlyAccess`

### ❌ Lambda not receiving requests
Check:
- Route exists  
- Integration attached  
- API deployed  

### ❌ S3 says “Access Denied”
Fix bucket policy OR enable object public access.

---

# 🧹 Cleanup (Recommended)

Remove resources when finished:

- Delete S3 bucket  
- Delete Lambda function  
- Delete API Gateway API  
- Delete IAM role or detach policies  
- Delete CloudWatch log groups  

---

# 🌟 Next Steps / Extensions

You can extend this project to:
- Perform text extraction (OCR)
- Detect emotions / faces (ethical usage!)
- Save results to DynamoDB  
- Add UI improvements  
- Deploy frontend via CloudFront  
- Create CI/CD using GitHub Actions + SAM/CDK  


---

### 🎉 You now have a fully working AI-powered serverless app on AWS!  
