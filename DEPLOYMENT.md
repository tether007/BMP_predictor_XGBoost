# BPM Predictor API - Deployment Guide

## Free Deployment Options

### Option 1: Render (Recommended - Best Free Tier)

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Deploy from GitHub**
   - Push your code to GitHub
   - Connect Render to your GitHub repo
   - Render will auto-detect Python and deploy

3. **Free Tier Details**
   - 750 hours/month (31 days)
   - Sleeps after 15 minutes of inactivity
   - Takes ~30 seconds to wake up

**Pros:** Most generous free tier, easy deployment, automatic HTTPS
**Cons:** Sleeps after inactivity (30s wake-up time)

### Option 2: PythonAnywhere (Always Online)

1. **Create Account**
   - Go to [pythonanywhere.com](https://pythonanywhere.com)
   - Sign up for free account

2. **Upload Files**
   - Upload your project files via web interface
   - Install dependencies in Bash console: `pip3.10 install --user -r requirements.txt`

3. **Configure Web App**
   - Go to Web tab, create new web app
   - Choose "Manual configuration"
   - Edit WSGI file to point to your app

**Pros:** Always online, no sleeping, simple setup
**Cons:** Limited CPU seconds, custom domains cost extra

### Option 3: Fly.io (Free Tier)

1. **Create Account**
   - Go to [fly.io](https://fly.io)
   - Sign up and install flyctl

2. **Deploy**
   ```bash
   flyctl launch
   flyctl deploy
   ```

3. **Free Tier Details**
   - 3 shared-cpu-1x VMs
   - 256MB RAM each
   - Apps sleep when not used

**Pros:** Docker-based, good performance
**Cons:** More complex setup, requires Docker knowledge

### Option 4: Vercel (Serverless)

1. **Create Account**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with GitHub

2. **Deploy**
   - Connect GitHub repo
   - Vercel auto-detects Python

3. **Free Tier Details**
   - 100GB bandwidth/month
   - 1000 serverless function invocations
   - Perfect for APIs

**Pros:** Serverless, scales automatically, fast
**Cons:** Cold starts, 10s execution limit

## Quick Start with Render (Recommended)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "BPM Predictor API ready for deployment"
   git remote add origin https://github.com/yourusername/bmp-predictor.git
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect Python settings
   - Click "Create Web Service"

3. **Get Your URL**
   - Render gives you a URL like: `https://your-app-name.onrender.com`
   - Your API will be available at:
     - `https://your-app-name.onrender.com/predict` (HTML form)
     - `https://your-app-name.onrender.com/docs` (API documentation)

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
| Render | 750 hrs/month | $7/month | Best free tier |
| PythonAnywhere | Limited CPU | $5/month | Always online |
| Fly.io | 3 VMs, 256MB each | $1.94/month | Docker apps |
| Vercel | 100GB bandwidth | $20/month | Serverless APIs |

## Recommendation

**Start with Render** - it has the most generous free tier and is super easy to deploy!
