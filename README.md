# GPT-4o-mini Chat Interface

A Streamlit web application that provides a chat interface to interact with OpenAI's GPT-4o-mini model.

## Features

- 🤖 Real-time chat with GPT-4o-mini
- 💬 Streaming responses for better user experience
- 🎨 Beautiful, responsive UI with custom styling
- 📊 Chat statistics and message history
- 🔒 Secure API key handling
- 🗑️ Clear chat history functionality

## Local Development Setup

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
   streamlit run app.py
   ```

6. Open your browser and go to `http://localhost:8501`

## Deployment to Streamlit Community Cloud

### Step 1: Prepare Your Repository

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add Streamlit GPT-4o-mini chat app"
   git push origin main
   ```

2. **Important:** Never commit your `.env` file! The `.gitignore` file is configured to exclude it.

### Step 2: Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "Create app"
4. Select your repository and branch
5. Set the main file path: `app.py`
6. Click "Deploy"

### Step 3: Configure Secrets

Since you can't upload `.env` files to GitHub, you need to configure secrets in Streamlit Cloud:

1. **In Streamlit Cloud Dashboard:**
   - Go to your app settings
   - Click on "Secrets" in the sidebar
   - Add your secrets in TOML format:
   ```toml
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```

2. **Alternative Method - Using Streamlit Secrets:**
   - Create a file named `.streamlit/secrets.toml` (locally only, don't commit)
   - Add your secrets:
   ```toml
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```

### Step 4: Verify Deployment

1. Wait for the app to build and deploy
2. Test the chat functionality
3. Check that the API key validation works

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

## File Structure

```
5_MLOps/Streamlit/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── env.example           # Environment variables template
├── .gitignore           # Git ignore rules
├── README.md            # This file
└── .streamlit/
    └── config.toml      # Streamlit configuration
```

## Restrictions and Considerations

### Streamlit Community Cloud Limitations

1. **Resource Limits:**
   - 1 GB RAM per app
   - Limited CPU resources
   - Apps sleep after 7 days of inactivity

2. **API Rate Limits:**
   - Subject to OpenAI's rate limits
   - Consider implementing rate limiting for production use

3. **Security:**
   - Never commit API keys to GitHub
   - Use Streamlit secrets for sensitive data
   - The app runs on public URLs (consider authentication for sensitive use)

4. **Storage:**
   - No persistent storage between sessions
   - Chat history is lost when the app restarts

### Best Practices

1. **API Key Security:**
   - Always use environment variables or Streamlit secrets
   - Never hardcode API keys in your code
   - Use `.gitignore` to exclude `.env` files

2. **Error Handling:**
   - The app includes comprehensive error handling
   - API failures are gracefully handled with user feedback

3. **Performance:**
   - Streaming responses improve perceived performance
   - Consider adding rate limiting for production use

## Troubleshooting

### Common Issues

1. **API Key Not Working:**
   - Verify your OpenAI API key is valid
   - Check that you have sufficient credits
   - Ensure the key has the correct permissions

2. **App Not Deploying:**
   - Check that all files are committed to GitHub
   - Verify the file path in Streamlit Cloud settings
   - Check the deployment logs for errors

3. **Secrets Not Loading:**
   - Ensure secrets are properly formatted in TOML
   - Restart the app after adding secrets
   - Check for typos in secret names

### Getting Help

- Check the Streamlit Community forum
- Review OpenAI API documentation
- Check the deployment logs in Streamlit Cloud

## License

This project is open source and available under the MIT License.

