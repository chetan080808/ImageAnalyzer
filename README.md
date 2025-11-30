🤖 AI Image Analyzer — Serverless AWS Project
AWS
Python
License

A fully serverless, production-ready AI image analysis application built on AWS. Upload any image and get instant AI-powered object detection using Amazon Rekognition.

Perfect for: DevOps Engineers, Cloud Enthusiasts, Students learning AWS & Serverless Architecture

🎥 Project Walkthrough
<!-- ADD YOUR YOUTUBE VIDEO HERE -->
📹 YouTube Tutorial: Coming Soon - Subscribe to my channel!

📄 LinkedIn Article: Read my detailed implementation story

🚀 Live Demo
Try it out: Live Application (Add your S3 website URL)

✨ Features
🔍 AI-Powered Object Detection - Identifies objects, scenes, and concepts in images

🎨 Modern UI/UX - Beautiful gradient design with smooth animations

📸 Image Preview - See your image before analysis

⚡ Real-time Results - Get instant feedback with confidence scores

🌐 100% Serverless - No servers to manage, scales automatically

💰 Free Tier Friendly - Stay within AWS free tier limits

📱 Responsive Design - Works on desktop, tablet, and mobile

🎯 Drag & Drop - Easy file upload with drag-and-drop support

🏗️ Architecture
text
┌─────────────┐
│   Browser   │
│  (User UI)  │
└──────┬──────┘
       │ 1. Upload Image (Base64)
       ↓
┌──────────────────────┐
│   Amazon S3 Bucket   │
│ (Static Web Hosting) │
└──────┬───────────────┘
       │ 2. POST Request
       ↓
┌───────────────────────┐
│  API Gateway (HTTP)   │
│   CORS Enabled API    │
└──────┬────────────────┘
       │ 3. Invoke Lambda
       ↓
┌───────────────────────┐
│   AWS Lambda Python   │
│  (Business Logic)     │
└──────┬────────────────┘
       │ 4. Analyze Image
       ↓
┌───────────────────────┐
│ Amazon Rekognition    │
│   (AI/ML Service)     │
└──────┬────────────────┘
       │ 5. Return Labels
       ↓
┌─────────────┐
│   Browser   │
│ (Display)   │
└─────────────┘
🛠️ Tech Stack
Component	Technology	Purpose
Frontend	HTML, CSS, JavaScript	User interface & interactions
Hosting	Amazon S3	Static website hosting
API	API Gateway (HTTP API)	RESTful API endpoint
Backend	AWS Lambda (Python 3.10)	Serverless compute
AI/ML	Amazon Rekognition	Image analysis & object detection
Monitoring	CloudWatch	Logs and metrics
Security	IAM Roles & Policies	Access management
📦 Project Structure
text
ImageAnalyzer/
├── index.html              # Frontend UI with modern design
├── lambda_function.py      # Lambda backend with CORS handling
├── README.md              # Project documentation (you're here!)
└── assets/                # Screenshots and demo images
    ├── architecture.png
    ├── demo.gif
    └── screenshots/
🚀 Quick Start Guide
Prerequisites
AWS Account (Free Tier eligible)

Basic knowledge of AWS services

A web browser

Deployment Steps
1️⃣ Set Up S3 Static Website
Create S3 Bucket:

bash
# Replace 'your-unique-bucket-name' with your chosen name
aws s3 mb s3://your-unique-bucket-name --region us-east-1
Configure Bucket Policy:

json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-unique-bucket-name/*"
    }
  ]
}
Enable Static Website Hosting:

Index document: index.html

Note your S3 website endpoint

Upload Frontend:

bash
aws s3 cp index.html s3://your-unique-bucket-name/ --content-type "text/html"
2️⃣ Create Lambda Function
Via AWS Console:

Go to Lambda → Create function

Choose Author from scratch

Settings:

Function name: image-analyzer

Runtime: Python 3.10

Architecture: x86_64

Add IAM Permissions:

Attach these policies to your Lambda execution role:

AWSLambdaBasicExecutionRole (auto-attached)

AmazonRekognitionReadOnlyAccess (manual)

Deploy Code:

Paste the content from lambda_function.py and click Deploy.

3️⃣ Set Up API Gateway
Create HTTP API:

Go to API Gateway → Create API

Choose HTTP API → Build

Add Integration:

Type: Lambda

Function: image-analyzer

Version: 2.0

Configure Route:

Method: ANY

Path: /

Integration: image-analyzer

Enable CORS:

Allowed origins: *

Allowed methods: POST, OPTIONS

Allowed headers: *

Deploy API:

Stage: $default (auto-deploy enabled)

Copy your Invoke URL

4️⃣ Connect Frontend to Backend
Update index.html:

javascript
const apiUrl = "https://YOUR-API-ID.execute-api.us-east-1.amazonaws.com";
Re-upload to S3:

bash
aws s3 cp index.html s3://your-unique-bucket-name/ --content-type "text/html"
5️⃣ Test Your Application
Open your S3 website URL

Upload an image (JPG, PNG, etc.)

Click Analyze

View AI-detected labels with confidence scores!

🧪 Testing
Browser Test
Navigate to your S3 website URL

Upload a test image

Verify results display correctly

API Test (Optional)
bash
# Test with curl
curl -X POST "https://YOUR-API-ID.execute-api.us-east-1.amazonaws.com" \
  -H "Content-Type: application/json" \
  -d '{"image":"BASE64_ENCODED_IMAGE_HERE"}'
🐛 Troubleshooting
Common Issues & Solutions
Issue	Cause	Solution
"Failed to fetch"	CORS not configured	Enable CORS in API Gateway & Lambda
404 Not Found	Wrong API URL or stage disabled	Use $default stage URL, ensure auto-deploy enabled
403 Access Denied	S3 bucket policy missing	Add public read policy to S3 bucket
Rekognition Access Denied	Missing IAM permission	Attach AmazonRekognitionReadOnlyAccess to Lambda role
No labels detected	Low confidence threshold	Adjust MinConfidence in Lambda code
Debug Checklist
✅ S3 bucket is public

✅ Static website hosting enabled

✅ Lambda has Rekognition permissions

✅ API Gateway CORS configured

✅ Correct API URL in index.html

✅ API deployed to $default stage

💰 Cost Estimation
AWS Free Tier (First 12 Months)
Service	Free Tier	Your Usage	Cost
S3	5 GB storage, 20K GET, 2K PUT	~5 MB, 100 requests/day	$0.00
Lambda	1M requests, 400K GB-seconds	~50 requests/day	$0.00
API Gateway	1M requests/month	~50 requests/day	$0.00
Rekognition	5,000 images/month	~50 images/day	$0.00
CloudWatch	5 GB logs	Minimal	$0.00
Total Monthly Cost: $0.00 (within free tier limits)

Beyond Free Tier
Rekognition: $1.00 per 1,000 images

Lambda: $0.20 per 1M requests

API Gateway: $1.00 per 1M requests

📊 Monitoring & Cost Control
Set Up Billing Alerts
bash
# Go to AWS Billing Dashboard
# Enable: "Receive Free Tier Usage Alerts"
# Create: Budget Alert ($5 threshold)
Monitor Free Tier Usage
Dashboard: AWS Console → Billing → Free Tier

Check daily for Rekognition usage

Set CloudWatch alarms for cost thresholds

🎓 What I Learned
Building this project taught me:

✅ Serverless architecture design patterns

✅ AWS service integration (S3, Lambda, API Gateway, Rekognition)

✅ CORS configuration for cross-origin requests

✅ IAM roles and security best practices

✅ Base64 encoding for image transmission

✅ Error handling and troubleshooting in cloud

✅ Cost optimization in AWS

✅ Modern frontend design with vanilla JavaScript

🚀 Future Enhancements
Ideas to extend this project:

🎯 Recommended Next Steps:
Accessibility Helper - Add text-to-speech for visually impaired users

Smart Grocery Manager - Identify food items and track pantry inventory

Plant Care Assistant - Identify plant species and provide care instructions

🔧 Technical Improvements:
 Add user authentication (Cognito)

 Store analysis history (DynamoDB)

 Batch image processing

 Export results as PDF/CSV

 CloudFront CDN for faster delivery

 CI/CD pipeline with GitHub Actions

 Infrastructure as Code (Terraform/CDK)

 Text extraction (OCR) capability

 Face detection and analysis

 Custom ML model integration

📚 Learning Resources
AWS Documentation
Amazon Rekognition

AWS Lambda

API Gateway

Amazon S3

Tutorials I Found Helpful
AWS Serverless Architecture Whitepaper

AWS Well-Architected Framework

Serverless Stack (SST) Documentation

🤝 Contributing
Contributions are welcome! Feel free to:

🐛 Report bugs

💡 Suggest new features

📖 Improve documentation

🔧 Submit pull requests

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 About Me
Chetan Namane
DevOps Engineer | Cloud Enthusiast | AWS Learner

Building projects to learn AWS, Terraform, Docker, and DevOps practices. Passionate about serverless architectures and cloud-native development.

🔗 Connect With Me
LinkedIn
GitHub
YouTube
Portfolio

🙏 Acknowledgments
Original project inspiration from YadneshN/ImageAnalyzer

AWS Free Tier for making learning accessible

The DevOps and AWS communities for knowledge sharing

📧 Contact
Have questions or suggestions? Reach out:

📧 Email: your-email@example.com

💼 LinkedIn: Your Profile

🐦 Twitter: @yourusername

<div align="center">
⭐ If you found this project helpful, please give it a star!
Built with ❤️ using AWS Serverless Technologies

</div>
📸 Screenshots
Application Interface
Application Screenshot
Modern, responsive UI with gradient design

Analysis Results
Results Screenshot
AI-detected labels with confidence scores

Architecture Diagram
Architecture
Complete serverless architecture on AWS

📝 Changelog
Version 1.0.0 (Current)
✅ Initial release

✅ Basic image analysis functionality

✅ Modern UI with animations

✅ CORS-enabled API

✅ Free tier optimized

Upcoming (v1.1.0)
🔜 User authentication

🔜 Analysis history

🔜 Batch processing

🔜 Export functionality
