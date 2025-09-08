# BPM Predictor API - Deployment Guide

## Free Deployment Options

### Option 1: Railway (Recommended - Easiest)

1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy from GitHub**
   - Push your code to GitHub
   - Connect Railway to your GitHub repo
   - Railway will auto-detect Python and deploy

3. **Environment Variables**
   - No additional setup needed
   - Railway handles everything automatically

**Pros:** Super easy, automatic HTTPS, custom domains
**Cons:** 500 hours/month free, then $5/month

### Option 2: Render (Free Tier)

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create Web Service**
   - Connect your GitHub repo
   - Choose "Web Service"
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

3. **Free Tier Limits**
   - 750 hours/month
   - Sleeps after 15 minutes of inactivity
   - Takes ~30 seconds to wake up

### Option 3: Heroku (Free Tier Discontinued)

Heroku no longer offers free hosting, but you can use:
- **Heroku Eco Plan**: $5/month
- Same deployment process as before

### Option 4: PythonAnywhere (Free Tier)

1. **Create Account**
   - Go to [pythonanywhere.com](https://pythonanywhere.com)
   - Sign up for free account

2. **Upload Files**
   - Upload your project files
   - Install dependencies in Bash console

3. **Configure Web App**
   - Create new web app
   - Point to your WSGI file

**Pros:** Always online, no sleeping
**Cons:** Limited CPU seconds, custom domains cost extra

## Quick Start with Railway

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/bmp-predictor.git
   git push -u origin main
   ```

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically deploy!

3. **Get Your URL**
   - Railway gives you a URL like: `https://your-app-name.railway.app`
   - Your API will be available at:
     - `https://your-app-name.railway.app/predict` (HTML form)
     - `https://your-app-name.railway.app/docs` (API documentation)

## Testing Your Deployed API

Once deployed, test with:

```bash
# Test the form endpoint
curl https://your-app-name.railway.app/predict

# Test the API endpoint (if you add it back)
curl -X POST https://your-app-name.railway.app/predict_json \
  -H "Content-Type: application/json" \
  -d '{
    "RhythmScore": 0.42,
    "AudioLoudness": -7.3,
    "VocalContent": 0.61,
    "AcousticQuality": 0.35,
    "InstrumentalScore": 0.18,
    "LivePerformanceLikelihood": 0.05,
    "MoodScore": 0.72,
    "TrackDurationMs": 210000.0,
    "Energy": 0.8
  }'
```

## Custom Domain (Optional)

1. **Railway**: Add custom domain in project settings
2. **Render**: Add custom domain in service settings
3. **Both**: Free SSL certificates included

## Monitoring & Logs

- **Railway**: Built-in logs and metrics
- **Render**: Logs available in dashboard
- **Both**: Health check at `/health` endpoint

## Cost Comparison

| Platform | Free Tier | Paid Plans | Best For |
|----------|-----------|------------|----------|
| Railway | 500 hrs/month | $5/month | Easy deployment |
| Render | 750 hrs/month | $7/month | Always-on apps |
| PythonAnywhere | Limited CPU | $5/month | Learning/prototyping |

## Recommendation

**Start with Railway** - it's the easiest and most reliable for your use case!
