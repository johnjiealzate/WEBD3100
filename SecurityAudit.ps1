$logFile = "C:\Logs\SecurityAudit.txt"

function Write-Log {
    param([string]$message)
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - $message" | Out-File -Append -FilePath $logFile
}

try {
    # Check and enable Defender real-time protection
    if (Get-Command -Name Set-MpPreference -ErrorAction SilentlyContinue) {
        Set-MpPreference -DisableRealtimeMonitoring $false
        Write-Output "Windows Defender real-time protection is enabled."
        Write-Log "Defender real-time protection enabled."
    } else {
        Write-Output "Windows Defender not found."
        Write-Log "Error: Windows Defender not installed."
    }

    # Check for outdated definitions
    $lastUpdate = (Get-MpComputerStatus).AntivirusSignatureLastUpdated
    if ($lastUpdate -lt (Get-Date).AddDays(-7)) {
        Write-Output "Defender signatures are outdated!"
        Write-Log "Warning: Defender definitions outdated."
    } else {
        Write-Output "Defender signatures are up to date."
        Write-Log "Defender definitions up to date."
    }

    # Check and enable Windows Firewall
    if ((Get-NetFirewallProfile -Profile Domain,Public,Private).Enabled -contains $false) {
        Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
        Write-Output "Windows Firewall enabled."
        Write-Log "Windows Firewall enabled."
    } else {
        Write-Output "Windows Firewall is already enabled."
        Write-Log "Windows Firewall was already enabled."
    }
} catch {
    Write-Output "Error in security audit script: $_"
    Write-Log "Error: $_"
}