
$input_file = "pixel_values.csv"
if (-Not (Test-Path $input_file)) {
    Write-Host "File $input_file not found!"
    exit 1
}


$formatted_output = ""
$count = 0


Get-Content $input_file | ForEach-Object {
    $value = $_
    if ($value -eq 1) {
        $formatted_output += "*"
    } else {
        $formatted_output += "/"
    }
    $count++
    if ($count % 52 -eq 0) {
        $formatted_output += "`n"
    }
}


Write-Host $formatted_output