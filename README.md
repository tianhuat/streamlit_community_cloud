# Deploying Streamlit Apps to Streamlit Community Cloud

Learn how to deploy your Streamlit applications to Streamlit Community Cloud - a **free** hosting platform that makes your apps accessible to anyone in the world with just a URL.

## Why Streamlit Community Cloud?

**Benefits:**
- 🌍 **Free hosting** - Deploy unlimited public apps at no cost
- 🚀 **Instant deployment** - Direct integration with GitHub
- 🔗 **Public accessibility** - Share your apps with anyone via a simple URL
- 🔄 **Auto-updates** - Apps automatically redeploy when you push to GitHub
- ⚙️ **Easy configuration** - Simple setup with secrets management

**Important Limitations:**
- 1 GB RAM per app with limited CPU resources
- Apps sleep after 7 days of inactivity (wake automatically when accessed)
- All apps are **publicly accessible** - consider authentication for sensitive data
- No persistent storage between sessions
- Shared infrastructure may have occasional performance variations

## What This Tutorial Covers

This tutorial walks you through two main areas:

1. **Local Development Setup** - How to run and test your Streamlit app locally
2. **Deployment to Streamlit Community Cloud** - How to deploy your app for free worldwide access

## 1. Local Development Setup

### Prerequisites

- Python 3.12 or higher
- OpenAI API key

### Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd Streamlit
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   # Copy the example file
   cp env.example .env
   
   # Edit .env file and add your OpenAI API key
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

6. Open your browser and go to `http://localhost:8501`

## 2. Deployment to Streamlit Community Cloud

### Step 1: Prepare Your Repository

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add Streamlit GPT-4o-mini chat app"
   git push origin master
   ```

2. **Important:** Never commit your `.env` file! The `.gitignore` file is configured to exclude it.

### Step 2: Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "Deploy a public app from GitHub"
4. Fill in the deployment form:
   - **Repository:** Select your GitHub repository (e.g., `username/streamlit_community_cloud`)
   - **Branch:** `master`
   - **Main file path:** `streamlit_app.py`
   - **App URL (optional):** Leave as default or customize
5. Click "Advanced settings" if you need to configure additional options
6. Click "Deploy"

### Step 3: Configure Secrets

Since you can't upload `.env` files to GitHub, you need to configure secrets during deployment. **You only need to choose ONE of the following three methods (Method 1 is recommended):**

**Important:** Always include double quotation marks (") around your API key value in TOML format.

1. **During Deployment (Recommended):**
   - Click "Advanced settings" in the deployment form
   - Set **Python version** to `3.12`
   - In the **Secrets** section, add your API key in TOML format:
   ```toml
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```
   - Click "Save" then "Deploy"

2. **After Deployment (Alternative):**
   - Go to your deployed app's page in Streamlit Community Cloud
   - Click the three dots menu (⋮) next to your app
   - Select "Settings" from the dropdown menu
   - In the App settings modal, click on the "Secrets" tab
   - In the text area, add your API key in TOML format:
   ```toml
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```
   - Click "Save changes"
   - Your app will automatically restart with the new secrets

3. **Local Development (Optional):**
   - Create a file named `.streamlit/secrets.toml` (locally only, don't commit)
   - Add your secrets:
   ```toml
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```

### Step 4: Verify Deployment

1. Wait for the app to build and deploy (this may take a few minutes)
2. Once deployed, you should see the **GPT-4o-mini Chat Interface** with:
   - A sidebar showing "Settings" with API key validation status
   - "Chat Statistics" showing total messages
   - "Instructions" for using the app
   - A main chat area with input box and "Send" button
3. Test the functionality:
   - Verify the API key shows as "✅ API Key is valid"
   - Try sending a test message to ensure the chat works
   - Check that responses stream in real-time
4. Your app will be available at the generated Streamlit URL

## Conclusion

Congratulations! 🎉 You've successfully learned how to deploy Streamlit applications to Streamlit Community Cloud. 

**What you've accomplished:**
- ✅ Set up local development environment for Streamlit apps
- ✅ Learned the complete deployment workflow to Streamlit Community Cloud
- ✅ Configured secure secrets management
- ✅ Deployed your app for **free worldwide access**

Your Streamlit app is now live and can be shared with anyone around the world via an URL! 🚀 
