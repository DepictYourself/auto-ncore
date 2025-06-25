#!/bin/sh
cd /tmp/mnt/Intenso/auto-ncore/backend
# kill any running uvicorn process
pkill -f "uvicorn main:app" 2>/dev/null

# Export production env variables
export $(cat .env.production | xargs)

# Start backend
nohup /opt/bin/uvicorn main:app --host 0.0.0.0 --port 8000 > /tmp/uvicorn.log 2>&1 &