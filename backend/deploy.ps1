#--- Configuration ---
$routerIp = "192.168.0.2"
$routerUser = "root"
$localBackendPath = "/mnt/c/Users/keelew/dev/auto-ncore/backend/"
$remoteBackendPath = "/tmp/mnt/Intenso/auto-ncore/backend"

#--- Build  locally ---


# --- Copy backend files to router ---
wsl rsync -avc --exclude-from="$localBackendPath/.deployignore"  "$localBackendPath" "${routerUser}@${routerIp}:$remoteBackendPath"


# --- Start the backend on the router ---
Write-Host "Running backend..."
$cmd = "'$remoteBackendPath/start.sh'"
ssh "$routerUser@$routerIp" $cmd

Write-Host "Done! App should be available at http://" + $routerIp + ":8000"
