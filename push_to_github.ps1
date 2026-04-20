# push_to_github.ps1
# Clears the existing repository content and pushes the new structure.
# Run from inside your local ctf-writeups repo directory.
#
# Usage:
#   cd C:\Users\Utilizador\Documents\ctf-writeups\ctf-writeups
#   .\push_to_github.ps1

$ErrorActionPreference = "Stop"

Write-Host "Step 1: Removing existing content..." -ForegroundColor Cyan

# Remove everything except .git folder and this script
Get-ChildItem -Path . -Exclude ".git", "push_to_github.ps1" | Remove-Item -Recurse -Force
Write-Host "  Existing content removed."

Write-Host "Step 2: Copying new content from ZIP..." -ForegroundColor Cyan

# Extract destination — set this to where you extracted ctf-rebuild.zip
$SOURCE = "$env:USERPROFILE\Documents\ctf-rebuild"

if (-not (Test-Path $SOURCE)) {
    Write-Host "ERROR: Source folder not found at $SOURCE" -ForegroundColor Red
    Write-Host "Extract the ctf-rebuild.zip to $env:USERPROFILE\Documents\ and retry." -ForegroundColor Red
    exit 1
}

# Copy all content from the extracted folder
Copy-Item -Path "$SOURCE\*" -Destination . -Recurse -Force
Write-Host "  Content copied."

Write-Host "Step 3: Committing and pushing..." -ForegroundColor Cyan

git add .
git commit -m "docs: complete repository rebuild — SOC Level 1 (14 sections, 67 rooms) + supplementary study"
git push

Write-Host ""
Write-Host "Done. Repository updated." -ForegroundColor Green
Write-Host ""
Write-Host "Next step: run the issues and board script:" -ForegroundColor Yellow
Write-Host "  pip install PyGithub python-dotenv"
Write-Host "  echo GITHUB_TOKEN=your_token > .env"
Write-Host "  python create_issues_and_board.py --repo EduardoRochaFernandes/ctf-writeups"
