import shutil
from pathlib import Path

ROOT = Path("/home/sanjayg4/gec-raipur-1991-yearbook")
DIST = ROOT / "dist"

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir(parents=True)

# Copy core web assets
files_to_copy = [
    "index.html",
    "landing.html",
    "privacy.html",
    "styles.css",
    "landing.css",
    "app.js",
    "landing.js",
    "landing-data.js",
    "milestones-data.js",
]

for f in files_to_copy:
    src = ROOT / f
    if src.exists():
        shutil.copy2(src, DIST / f)
        print(f"✓ Copied {f}")

# Copy data folder
shutil.copytree(ROOT / "data", DIST / "data")
print("✓ Copied data/")

# Copy assets folder (excluding test screenshots and QA temp files)
DIST_ASSETS = DIST / "assets"
DIST_ASSETS.mkdir(parents=True)

# Copy avatars
shutil.copytree(ROOT / "assets/avatars", DIST_ASSETS / "avatars")
print("✓ Copied assets/avatars/")

# Copy milestones
shutil.copytree(ROOT / "assets/milestones", DIST_ASSETS / "milestones")
print("✓ Copied assets/milestones/")

# Copy themes
shutil.copytree(ROOT / "assets/themes", DIST_ASSETS / "themes")
print("✓ Copied assets/themes/")

# Copy key main photos
core_photos = [
    "photo_deskewed.jpg",
    "photo_enhanced.jpg",
    "photo_original.jpg",
    "mount_text_highres.jpg"
]
for cp in core_photos:
    src = ROOT / "assets" / cp
    if src.exists():
        shutil.copy2(src, DIST_ASSETS / cp)
        print(f"✓ Copied assets/{cp}")

print("--- Build Complete in dist/ ---")
