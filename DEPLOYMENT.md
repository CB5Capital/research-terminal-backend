# CB5 Capital Research Terminal - Backend Deployment Guide

This guide will help you deploy your FastAPI backend to various cloud platforms so your Netlify frontend can connect to it.

## Option 1: Railway (Recommended - Free Tier Available)

Railway is the easiest and most reliable option with a generous free tier.

### Steps:

1. **Sign up at [Railway](https://railway.app/)**

2. **Connect your GitHub repository:**
   - Create a new repository on GitHub for your backend
   - Push your backend code to the repository
   - In Railway, click "New Project" → "Deploy from GitHub repo"
   - Select your backend repository

3. **Set environment variables in Railway dashboard:**
   ```
   OPENAI_API_KEY=your_actual_openai_key
   CORS_ORIGINS=["https://your-netlify-app.netlify.app", "https://localhost:3000"]
   ENVIRONMENT=production
   ```

4. **Railway will automatically:**
   - Detect your Python app
   - Install dependencies from requirements.txt
   - Use the railway.toml configuration
   - Deploy your app

5. **Get your API URL:**
   - Railway will provide a URL like: `https://your-app-name.up.railway.app`
   - Test it by visiting: `https://your-app-name.up.railway.app/health`

## Option 2: Render (Free Tier Available)

### Steps:

1. **Sign up at [Render](https://render.com/)**

2. **Create a new Web Service:**
   - Connect your GitHub repository
   - Choose your backend repository
   - Render will detect it's a Python app

3. **Configure the service:**
   - **Name:** cb5-research-api
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python start.py`

4. **Set environment variables:**
   ```
   OPENAI_API_KEY=your_actual_openai_key
   CORS_ORIGINS=["https://your-netlify-app.netlify.app"]
   API_HOST=0.0.0.0
   API_PORT=10000
   ENVIRONMENT=production
   ```

5. **Deploy and get your URL:**
   - Render will provide a URL like: `https://cb5-research-api.onrender.com`

## Option 3: Fly.io (Free Tier Available)

### Steps:

1. **Install flyctl CLI:**
   ```bash
   # macOS
   brew install flyctl
   
   # Or download from https://fly.io/docs/getting-started/installing-flyctl/
   ```

2. **Sign up and authenticate:**
   ```bash
   flyctl auth signup
   flyctl auth login
   ```

3. **Deploy from your backend directory:**
   ```bash
   cd /path/to/your/backend
   flyctl deploy
   ```

4. **Set secrets:**
   ```bash
   flyctl secrets set OPENAI_API_KEY=your_actual_openai_key
   flyctl secrets set CORS_ORIGINS='["https://your-netlify-app.netlify.app"]'
   ```

## Option 4: Heroku (Paid)

### Steps:

1. **Install Heroku CLI and login**

2. **Create Heroku app:**
   ```bash
   cd /path/to/your/backend
   heroku create cb5-research-api
   ```

3. **Set environment variables:**
   ```bash
   heroku config:set OPENAI_API_KEY=your_actual_openai_key
   heroku config:set CORS_ORIGINS='["https://your-netlify-app.netlify.app"]'
   heroku config:set ENVIRONMENT=production
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

## After Deployment

### 1. Update your frontend configuration

In your React app, update the API base URL to point to your deployed backend:

```javascript
// In your frontend's backendService.js or similar file
const API_BASE_URL = 'https://your-deployed-backend-url.com';
```

### 2. Update CORS origins

Make sure to update the `CORS_ORIGINS` environment variable with your actual Netlify URL:

```
CORS_ORIGINS=["https://your-actual-app.netlify.app", "https://localhost:3000"]
```

### 3. Test the connection

1. Visit your backend's health endpoint: `https://your-backend-url/health`
2. Test an API call from your frontend
3. Check browser developer tools for any CORS errors

## Troubleshooting

### Common issues:

1. **CORS errors:** Make sure your Netlify domain is in the CORS_ORIGINS environment variable
2. **Port issues:** The backend will use the PORT environment variable provided by the platform
3. **Missing dependencies:** Ensure all dependencies are in requirements.txt
4. **Environment variables:** Double-check all required environment variables are set

### Environment Variables Checklist:

- ✅ `OPENAI_API_KEY` - Your actual OpenAI API key
- ✅ `CORS_ORIGINS` - Array of allowed origins including your Netlify domain
- ✅ `ENVIRONMENT` - Set to "production"
- ✅ Platform-specific variables (PORT, etc.) are usually set automatically

## Testing Your Deployment

After deployment, test these endpoints:

1. **Health check:** `GET https://your-backend-url/health`
2. **Cases:** `GET https://your-backend-url/api/cases`
3. **Frontend connection:** Make sure your React app can call the backend

## Cost Considerations

- **Railway:** Free tier includes 500 hours/month (enough for most apps)
- **Render:** Free tier with limitations (spins down after inactivity)
- **Fly.io:** Generous free tier
- **Heroku:** Paid plans start at $7/month

**Recommendation:** Start with Railway for its simplicity and reliable free tier.