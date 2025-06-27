#--- Configuration ---
$routerIp = "192.168.0.2"
$routerUser = "root"

$localBackendPath = "/mnt/c/Users/keelew/dev/auto-ncore/backend/"
$remoteBackendPath = "/tmp/mnt/Intenso/auto-ncore/backend"

$localFrontendDist = "/mnt/c/Users/keelew/dev/auto-ncore/frontend/dist"
$remoteFrontendPath = "/tmp/mnt/Intenso/www"
$remoteFrontendAssetsPath = "$remoteFrontendPath/assets"

# --- Build Step ---
Write-Host "Building frontend..."
wsl bash -c "cd /mnt/c/Users/keelew/dev/auto-ncore/frontend && npm run build -- --mode production"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Frontend build failed."
    exit 1
}

# --- Clean Remote Assets ---
Write-Host "Cleaning old frontend assets..."
$cleanAssetsCmd = "rm -rf $remoteFrontendAssetsPath/*"
ssh "$routerUser@$routerIp" $cleanAssetsCmd

# --- Rsync All Files ---
Write-Host "Deploying backend..."
wsl rsync -avc --exclude-from="$localBackendPath/.deployignore" "$localBackendPath" "${routerUser}@${routerIp}:$remoteBackendPath"

Write-Host "Deploying frontend..."
wsl rsync -avc "$localFrontendDist/" "${routerUser}@${routerIp}:$remoteFrontendPath"

Start-Sleep -Seconds 2

# --- Start Backend ---
# $startBackendCmd = ".$remoteBackendPath/start.sh"
# Write-Host "Starting backend on router...path: " + $startBackendCmd
# ssh "$routerUser@$routerIp" $startBackendCmd
# --- Start Backend ---
Write-Host "Waiting for router to accept new SSH connections..."

$maxAttempts = 10
$attempt = 1
$sshAvailable = $false

while ($attempt -le $maxAttempts) {
    Write-Host "Checking SSH availability (attempt $attempt)..."

    try {
        # Try a 1-second TCP connection to port 22
        $tcp = New-Object System.Net.Sockets.TcpClient
        $asyncResult = $tcp.BeginConnect($routerIp, 22, $null, $null)
        $wait = $asyncResult.AsyncWaitHandle.WaitOne(1000, $false)

        if ($wait -and $tcp.Connected) {
            $tcp.EndConnect($asyncResult)
            $tcp.Close()
            Write-Host "SSH port is open!"
            $sshAvailable = $true
            break
        } else {
            Write-Host "SSH port still closed..."
        }
        $tcp.Close()
    } catch {
        Write-Host "SSH check error: $($_.Exception.Message)"
    }

    Start-Sleep -Seconds ([math]::Pow(2, $attempt))
    $attempt++
}

if (-not $sshAvailable) {
    Write-Host "SSH is still unavailable after $maxAttempts attempts."
    exit 1
}

# Now try to start the backend
Write-Host "Starting backend on router..."
$startBackendCmd = "'$remoteBackendPath/start.sh'"
ssh "$routerUser@$routerIp" $startBackendCmd

# --- Done ---
Write-Host "Deployment complete!"
Write-Host "Frontend: http://${routerIp}:85/"
Write-Host "Backend API: http://${routerIp}:8000/"