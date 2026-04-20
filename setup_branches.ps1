# setup_branches.ps1
# Creates one branch per path, each containing only its own content + README.
# Run from inside your local ctf-writeups repo directory.
#
# Usage:
#   cd C:\Users\Utilizador\Documents\ctf-writeups\ctf-writeups
#   .\setup_branches.ps1

$ErrorActionPreference = "Stop"

# ── Helper ────────────────────────────────────────────────────────────
function New-Branch {
    param($BranchName, $Folder)

    Write-Host ""
    Write-Host "Creating branch: $BranchName" -ForegroundColor Cyan

    # Start fresh from main
    git checkout main -q
    git checkout -b $BranchName -q

    # Remove everything except .git, README.md, scripts, and the target folder
    Get-ChildItem -Path . -Exclude ".git", "README.md", ".gitignore", $Folder | Remove-Item -Recurse -Force

    git add -A
    git commit -m "chore($BranchName): isolate $Folder content" -q
    git push origin $BranchName -q

    Write-Host "  Pushed: $BranchName" -ForegroundColor Green

    # Return to main
    git checkout main -q
}

# ── Main branch: README only ──────────────────────────────────────────
Write-Host "Preparing main branch..." -ForegroundColor Cyan
git checkout main -q

# On main, keep only README + .gitignore — remove all path folders
Get-ChildItem -Path . -Exclude ".git", "README.md", ".gitignore", "*.ps1", "*.py" | Remove-Item -Recurse -Force

git add -A
git commit -m "chore(main): root branch — README and scripts only"
git push origin main

# ── Create each path branch ───────────────────────────────────────────
# We need to restore each folder from the full backup first.
# Extract from the ctf-v2 zip if needed.

$SOURCE = "$env:USERPROFILE\Documents\ctf-v2\ctf-v2"

if (-not (Test-Path $SOURCE)) {
    Write-Host ""
    Write-Host "ERROR: Source not found at $SOURCE" -ForegroundColor Red
    Write-Host "Make sure ctf-v2.zip is extracted to $env:USERPROFILE\Documents\ctf-v2\" -ForegroundColor Red
    exit 1
}

$branches = @(
    @{ Name = "soc-level-1";       Folder = "soc-level-1" },
    @{ Name = "soc-level-2";       Folder = "soc-level-2" },
    @{ Name = "soc-level-3";       Folder = "soc-level-3" },
    @{ Name = "security-engineer"; Folder = "security-engineer" },
    @{ Name = "devsecops";         Folder = "devsecops" },
    @{ Name = "supplementary";     Folder = "supplementary" }
)

foreach ($b in $branches) {
    # Restore the folder from backup onto main temporarily
    git checkout main -q
    Copy-Item -Path "$SOURCE\$($b.Folder)" -Destination . -Recurse -Force
    Copy-Item -Path "$SOURCE\README.md" -Destination . -Force

    git add -A
    git commit -m "temp: restore $($b.Folder) for branch creation" -q

    # Create branch and push
    New-Branch -BranchName $b.Name -Folder $b.Folder

    # Remove the temp commit from main
    git checkout main -q
    git reset --hard HEAD~1 -q
    git push origin main --force -q
}

Write-Host ""
Write-Host "All branches created and pushed." -ForegroundColor Green
Write-Host ""
Write-Host "Branches:"
Write-Host "  main              -> README only"
Write-Host "  soc-level-1       -> soc-level-1/ + README"
Write-Host "  soc-level-2       -> soc-level-2/ + README"
Write-Host "  soc-level-3       -> soc-level-3/ + README"
Write-Host "  security-engineer -> security-engineer/ + README"
Write-Host "  devsecops         -> devsecops/ + README"
Write-Host "  supplementary     -> supplementary/ + README"
