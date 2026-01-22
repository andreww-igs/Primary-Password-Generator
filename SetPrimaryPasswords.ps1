Import-Module ActiveDirectory

$CsvPath = "C:\temp\primary_passwords.csv"
$users = Import-Csv $CsvPath

foreach ($row in $users) {
    try {
        $adUser = Get-ADUser -Filter "UserPrincipalName -eq '$($row.UPN)'" -ErrorAction Stop

        $securePassword = ConvertTo-SecureString $row.Password -AsPlainText -Force

        Set-ADAccountPassword `
            -Identity $adUser.DistinguishedName `
            -NewPassword $securePassword `
            -Reset

        # Re-query pwdLastSet to confirm change
        $updatedUser = Get-ADUser $adUser.DistinguishedName -Properties pwdLastSet
        $pwdLastSet  = [DateTime]::FromFileTime($updatedUser.pwdLastSet)
        $formatted   = $pwdLastSet.ToString("yyyy-MM-dd HH:mm:ss")

        Write-Host "Password set for $($row.UPN) at $formatted"
    }
    catch {
        Write-Warning "Failed for $($row.UPN): $($_.Exception.Message)"
    }
}
