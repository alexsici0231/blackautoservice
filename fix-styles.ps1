$file = 'c:\Users\Alex\Desktop\blackautoservice\site\index.html'
$content = Get-Content $file -Raw

$content = $content -replace 'style="margin-top:28px;justify-content:center;font-size:16px;padding:17px;"', 'class="btn-phone"'
$content = $content -replace 'style="display:inline-flex;width:18px;height:18px;color:var\(--red\)"', 'class="icon-inline-18"'
$content = $content -replace 'style="display:flex;align-items:center;justify-content:center;width:24px;height:24px;color:var\(--red\)"', 'class="icon-flex-24"'
$content = $content -replace 'style="display:inline-flex;width:28px;height:28px;color:var\(--red\);margin-bottom:14px"', 'class="icon-inline-28"'
$content = $content -replace 'style="display:inline-flex;width:14px;height:14px;color:var\(--red\)"', 'class="icon-inline-14"'
$content = $content -replace 'style="width:100%;justify-content:center;padding:16px;"', 'class="btn-form"'
$content = $content -replace 'style="background:var\(--bg\)"', 'class="blog-section"'
$content = $content -replace 'style="display:grid;grid-template-columns:repeat\(3,1fr\);gap:20px"', 'class="blog-grid"'

Set-Content $file $content -Encoding UTF8
Write-Host "Done!"
