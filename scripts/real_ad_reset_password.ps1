# c:/Users/alial/OneDrive/Desktop/Projects/Help_Desk_Projects/Self Service Password Reset Portal/scripts/real_ad_reset_password.ps1
<#+
.SYNOPSIS
    Securely reset an Active Directory user password and unlock the account.

.DESCRIPTION
    This script is intended for use by the Self Service Password Reset Portal.
    It uses the RSAT Active Directory module to reset a user's password and unlock the account.
    All actions and results are logged as JSON to the specified log file.

.PARAMETER Username
    The sAMAccountName of the user whose password will be reset.

.PARAMETER NewPassword
    The new password to set for the user.

.PARAMETER LogPath
    The path to the log file where the result will be written as a JSON object.

.NOTES
    - This script must be run on a Windows Server joined to the target Active Directory domain.
    - The executing account should have delegated rights to reset passwords and unlock accounts, but should NOT be a Domain Admin.
    - Never run this script as Domain Admin. Always use least-privilege service accounts.
    - Protect this script and log files from unauthorized access.
    - Test thoroughly in a non-production environment before deployment.

.EXAMPLE
    .\real_ad_reset_password.ps1 -Username "jdoe" -NewPassword "P@ssw0rd!" -LogPath "C:\Logs\reset.json"
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$Username,
    [Parameter(Mandatory=$true)]
    [SecureString]$NewPassword,  # Accept as SecureString for security
    [Parameter(Mandatory=$true)]
    [string]$LogPath
)

Import-Module ActiveDirectory -ErrorAction Stop

$timestamp = (Get-Date -Format o)
$ip = $env:REMOTE_ADDR
$status = "fail"
$reason = "unknown"

try {
    # Only call Get-ADUser to validate existence, don't assign to unused variable
    Get-ADUser -Identity $Username -ErrorAction Stop
    Set-ADAccountPassword -Identity $Username -Reset -NewPassword $NewPassword -ErrorAction Stop
    Unlock-ADAccount -Identity $Username -ErrorAction SilentlyContinue
    $status = "success"
    $reason = "reset"
} catch {
    $status = "fail"
    $reason = $_.Exception.Message
}

$log = [PSCustomObject]@{
    timestamp = $timestamp
    username  = $Username
    status    = $status
    reason    = $reason
    ip        = $ip
}

$log | ConvertTo-Json | Out-File -FilePath $LogPath -Encoding UTF8

if ($status -eq "success") {
    exit 0
} else {
    exit 1
}
