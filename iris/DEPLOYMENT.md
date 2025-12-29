# Deployment Guide

This guide will help you deploy your Iris Classification application to GitHub and a hosting platform.

## 📦 Step 1: Push to GitHub

### Initialize Git Repository (if not already done)

```bash
git init
git add .
git commit -m "Initial commit: Complete Iris ML pipeline with FastAPI backend"
```

### Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it something like `iris-classification` or `iris-ml-deployment`
3. **Do NOT** initialize with README, .gitignore, or license (we already have these)

### Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

## 🚀 Step 2: Deploy Backend (FastAPI)

### Option A: Deploy to Render (Recommended)

1. **Sign up/Login** to [Render](https://render.com)

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository

3. **Configure Settings:**
   - **Name**: `iris-classification-api` (or your choice)
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: Leave empty (or `./` if needed)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment**: `Python 3`

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (usually 2-5 minutes)
   - Your API will be available at: `https://your-app-name.onrender.com`

5. **Update Frontend**
   - After deployment, note your Render URL
   - The frontend will automatically use the correct URL when served from the same domain
   - If deploying frontend separately, update `static/index.html` API URL

### Option B: Deploy to Railway

1. **Sign up/Login** to [Railway](https://railway.app)

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure**
   - Railway auto-detects FastAPI
   - It will automatically:
     - Install dependencies from `requirements.txt`
     - Run `uvicorn main:app`
   - Your app will be available at: `https://your-app-name.up.railway.app`

4. **Custom Domain (Optional)**
   - Railway provides a free domain
   - You can also add a custom domain

### Option C: Deploy to Vercel (Frontend + Backend)

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Create `vercel.json`**
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "main.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "main.py"
       }
     ]
   }
   ```

3. **Deploy**
   ```bash
   vercel
   ```

## 🌐 Step 3: Deploy Frontend

### Option A: Same Domain (Recommended)

If you deploy the FastAPI app with static files (as configured), the frontend is automatically served at the root URL.

### Option B: Separate Frontend Deployment (Vercel/Netlify)

1. **Update API URL in `static/index.html`**
   ```javascript
   const api_url = "https://your-backend-url.onrender.com/predict";
   ```

2. **Deploy to Vercel**
   - Push `static/index.html` to a separate repo or subdirectory
   - Connect to Vercel
   - Deploy

3. **Deploy to Netlify**
   - Drag and drop the `static` folder
   - Or connect GitHub repo
   - Deploy

## ✅ Step 4: Verify Deployment

1. **Test API Endpoint**
   ```bash
   curl -X POST "https://your-app-url.onrender.com/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "sepal_length": 5.1,
       "sepal_width": 3.5,
       "petal_length": 1.4,
       "petal_width": 0.2,
       "model_choice": "logistic"
     }'
   ```

2. **Test Frontend**
   - Visit your deployed URL
   - Enter sample values:
     - Sepal Length: 5.1
     - Sepal Width: 3.5
     - Petal Length: 1.4
     - Petal Width: 0.2
   - Click "Predict"
   - Should return "Setosa"

## 📝 Submission Checklist

- [ ] GitHub repository created and code pushed
- [ ] Backend deployed and accessible
- [ ] Frontend deployed and working
- [ ] API endpoint tested and working
- [ ] Both GitHub links ready (x2 if needed)
- [ ] Both deployed application links ready (x2 if needed)

## 🔗 Example Submission Format

**GitHub Repository Links:**
1. Main Repository: `https://github.com/YOUR_USERNAME/iris-classification`
2. (If separate frontend repo): `https://github.com/YOUR_USERNAME/iris-frontend`

**Deployed Application Links:**
1. Backend API: `https://your-app.onrender.com`
2. Frontend: `https://your-app.onrender.com` (or separate frontend URL)

## 🐛 Troubleshooting

### Backend Issues

- **Port Error**: Make sure you're using `$PORT` environment variable
- **Model Not Found**: Ensure `models/` folder is committed to Git
- **Import Errors**: Check `requirements.txt` has all dependencies

### Frontend Issues

- **CORS Error**: Backend CORS is configured to allow all origins
- **API Not Found**: Check API URL matches your backend deployment URL
- **Network Error**: Verify backend is running and accessible

### Deployment Issues

- **Build Fails**: Check `requirements.txt` and Python version
- **Timeout**: Render free tier may spin down after inactivity
- **Memory Error**: Consider upgrading plan if models are large

## 📞 Support

If you encounter issues:
1. Check deployment logs in your hosting platform
2. Test API locally first: `uvicorn main:app --reload`
3. Verify all files are committed to Git
4. Check environment variables if needed

