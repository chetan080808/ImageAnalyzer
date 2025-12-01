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
- 🎨 Modern, responsive UI with image preview
- ⚡ Real-time AI analysis with confidence scores

---

---

## 🏗️ Architecture

![Architecture Diagram](./Output%20images/diagram.gif)

### System Flow.

1. **User** uploads an image through the web interface
2. **Amazon S3** serves the static website and converts image to Base64
3. **API Gateway** receives the POST request with encoded image data
4. **AWS Lambda** processes the request:
   - Decodes Base64 image
   - Calls Amazon Rekognition API
5. **Amazon Rekognition** analyzes the image using AI/ML
6. **Lambda** formats the response with detected labels and confidence scores
7. **API Gateway** returns JSON response to the browser
8. **User** sees real-time analysis results with confidence percentages

### AWS Services Used

- **Amazon S3** - Static website hosting
- **API Gateway** - RESTful API endpoint (HTTP API)
- **AWS Lambda** - Serverless compute (Python 3.10)
- **Amazon Rekognition** - AI-powered image analysis
- **IAM** - Security and access management
- **CloudWatch** - Logging and monitoring

---


## 📦 Project Structure

```
├── index.html               # Frontend UI (modern design + image preview)
├── lambda_function.py       # Lambda backend (Rekognition logic + CORS)
└── README.md                # Full setup guide
```

---

## 🎥 Project Walkthrough

> **📹 YouTube Tutorial:** [Watch the complete walkthrough](#) *(Coming Soon)*

> **💼 LinkedIn Post:** [Read about my learnings](#) *(Coming Soon)*

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
3. **Uncheck** "Block all public access"
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
- Runtime: **Python 3.10**

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

### ❌ "Failed to fetch"
- CORS not configured properly  
- Static website not served from S3  
- Lambda not handling OPTIONS requests
- Wrong API URL in `index.html`

### ❌ Rekognition Access Denied
Add IAM policy:  
`AmazonRekognitionReadOnlyAccess`

### ❌ Lambda not receiving requests
Check:
- Route exists  
- Integration attached  
- API deployed to `$default` stage
- Stage is enabled (not disabled)

### ❌ S3 says "Access Denied"
Fix bucket policy OR enable object public access.

### ❌ 404 Not Found on API
- Ensure you're using `$default` stage URL
- Check if `prod` stage is disabled
- Remove `/prod` from URL if using HTTP API

---

# 🧹 Cleanup (Recommended)

Remove resources when finished:

- Delete S3 bucket  
- Delete Lambda function  
- Delete API Gateway API  
- Delete IAM role or detach policies  
- Delete CloudWatch log groups  

---

# 💰 Cost Estimation (AWS Free Tier)

This project is designed to stay **completely within AWS Free Tier**.

| Service | Free Tier Limit | Expected Usage | Cost |
|---------|----------------|----------------|------|
| **S3** | 5 GB storage, 20K GET, 2K PUT | ~5 MB, 100 requests/day | $0.00 |
| **Lambda** | 1M requests, 400K GB-seconds | ~50 requests/day | $0.00 |
| **API Gateway** | 1M requests/month | ~50 requests/day | $0.00 |
| **Rekognition** | 5,000 images/month | ~50 images/day | $0.00 |
| **CloudWatch** | 5 GB logs, 5 GB storage | Minimal | $0.00 |

**Total Monthly Cost:** **$0.00** ✅

---

# 🌟 Next Steps / Extensions

You can extend this project to:

### 🎯 Recommended Extensions
- **Accessibility Helper** — Add text-to-speech for visually impaired users
- **Smart Grocery Manager** — Identify food items and create inventory
- **Plant Care Assistant** — Identify plants and provide care instructions
- **Fashion Style Analyzer** — Detect clothing items and suggest outfits

### 🔧 Technical Improvements
- Perform text extraction (OCR)
- Detect emotions / faces (ethical usage!)
- Save results to DynamoDB  
- Add user authentication (Cognito)
- Batch image processing
- Deploy frontend via CloudFront  
- Create CI/CD using GitHub Actions + SAM/CDK  

---

# 🎓 What I Learned

Building this project taught me:
- Serverless architecture patterns
- AWS service integration and orchestration
- CORS configuration for secure cross-origin requests
- IAM roles and security best practices
- Cost optimization in AWS free tier
- Modern frontend design with vanilla JavaScript
- Debugging production issues (CORS, API Gateway stages)

---

# 👨‍💻 About Me

**Chetan Namane**  
DevOps Engineer | Cloud Enthusiast | AWS Learner

Building projects to master AWS, Terraform, Docker, and DevOps practices.  
Passionate about serverless architectures and cloud-native development.

### 🔗 Connect With Me

- 💼 **LinkedIn:** [chetannamane](https://www.linkedin.com/in/chetan-namane/)
- 🐙 **GitHub:** [chetan080808](https://github.com/chetan080808)
- 📹 **YouTube:** [codewithchetan](https://youtu.be/YYDqEHEs69k)
- 📧 **Email:** chetannamne2609@gmail.com

---

# 🙏 Acknowledgments

- Original project inspiration: [YadneshN/ImageAnalyzer](https://github.com/YadneshN/ImageAnalyzer)
- AWS Free Tier for making learning accessible
- The DevOps and AWS communities

---

### 🎉 You now have a fully working AI-powered serverless app on AWS!

---

**Built with ❤️ using AWS Serverless Technologies**

*Last Updated: November 30, 2025*
