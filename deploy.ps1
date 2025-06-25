#--- Configuration ---
$routerIp = "192.168.0.2"
$routerUser = "root"

$localBackendPath = "/mnt/c/Users/keelew/dev/auto-ncore/backend/"
$remoteBackendPath = "/tmp/mnt/Intenso/auto-ncore/backend"

$localFrontendDist = "/mnt/c/Users/keelew/dev/auto-ncore/frontend/dist"
$remoteFrontendPath = "/tmp/mnt/Intenso/www"


# --- Deploy Backend ---
wsl rsync -avc --exclude-from="$localBackendPath/.deployignore"  "$localBackendPath" "${routerUser}@${routerIp}:$remoteBackendPath"

Write-Host "Running backend..."
$cmd = "'$remoteBackendPath/start.sh'"
ssh "$routerUser@$routerIp" $cmd


# --- Deploy Frontend ---
Write-Host "Building frontend..."
wsl bash -c "cd /mnt/c/Users/keelew/dev/auto-ncore/frontend && npm run build -- --mode production"

Write-Host "Deploying frontend..."
wsl rsync -avc "$localFrontendDist/" "${routerUser}@${routerIp}:$remoteFrontendPath"

Write-Host "✅ Deployment complete!"
Write-Host "Frontend: http://$routerIp:85/"
Write-Host "Backend API: http://$routerIp:8000/"
