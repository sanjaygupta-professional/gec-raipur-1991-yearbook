# Govt. Engineering College Raipur (M.P.) — B.E. Mechanical 1990-91
## 35th Anniversary Interactive Living Yearbook

An authentic, distortion-free interactive yearbook archive built from the original 1990-91 graduation photograph.

---

### Core Principles
1. **Zero Facial Distortion**: Unlike generic AI face enhancement apps (Remini, GFPGAN, CodeFormer) that hallucinate fake teeth and generic synthetic faces on small crops, this system preserves **100% authentic original optical pixels**.
2. **Interactive Roster & Face Mapping**: Every single one of the 67 professors, dignitaries, and students is mapped to an interactive spotlight hotspot.
3. **"Then & Now" Alumni Profiles**: Classmates can view their 1991 graduation crop side-by-side with their current photo, city, role, and favorite campus memories.
4. **Standalone & Portable**: Self-contained web application with zero external runtime dependencies. Runs immediately in any desktop or mobile browser.

---

### Batch Composition (67 Members)
* **Sitting (Front Row)**: 15 Dignitaries & Faculty (Principal Dr. H. A. Vachhani, H.O.D. Mech Prof. G. S. Verma, Dr. Y. P. Jain, Dr. M. L. Jeswani, Miss S. L. Sinha, and distinguished professors)
* **Standing (1st Row)**: 16 Students (Nishtha Kothuria, Prachee Sthapak, ..., Sanjay Gupta)
* **Standing (2nd Row)**: 17 Students (K. V. Raman Rao, ..., Abhay Agrawal)
* **Standing (3rd Row / Back)**: 19 Students (Vinay Awasthi, ..., Mohan Singh)

---

### How to Run Locally

You can open the project directly in your browser:

```bash
# Option 1: Open the landing page directly
xdg-open /home/sanjayg4/gec-raipur-1991-yearbook/landing.html

# Or open the interactive photo viewer directly
xdg-open /home/sanjayg4/gec-raipur-1991-yearbook/index.html

# Option 2: Run a lightweight local web server
cd /home/sanjayg4/gec-raipur-1991-yearbook
python3 -m http.server 8080
# Then visit: http://localhost:8080/landing.html
```

---

### Multi-Agent QA Verification & Pixel Calibration
To eliminate coordinate drift across the group photo, a rigorous multi-agent QA pipeline was executed:
* **Pixel Ruler Calibration Strips**: Generated high-contrast ruler strips (`assets/ruler_sitting.jpg`, `assets/ruler_standing1.jpg`, `assets/ruler_standing2.jpg`, `assets/ruler_standing3.jpg`) along each row axis with 10px tick marks.
* **Codex QA Agent Inspection**: OpenAI Codex was dispatched across each row strip to independently audit face positions, visual features (hair, spectacles, suits, ties, saris), and precise coordinate centers.
* **Exact Row Spacing**: Calibrated vertical baselines across all 4 rows (Back: Y≈405-430, Middle: Y≈468-475, Front Standing: Y≈535-550, Sitting: Y≈595-626).
* **Zero Missing Faces**: Verified exact coverage for all 67 members, including Miss S. L. Sinha on the far right of the seated row (X=1103, Y=626) and Sanjay Gupta on the far right of the 1st standing row (X=1076, Y=545).
* **Regenerated 67 Face Avatars**: All 67 individual face avatar crops in `assets/avatars/{id}.jpg` were regenerated directly centered on each person's real face.
* **QA Overlay Verification**: See `assets/qa_verification_all_faces.jpg` for complete visual proof with all 67 numbered face circles.

---

### Features & Controls
* **Three Background Appearance Modes (Persistent across pages)**:
  * **Dark (Darkroom Obsidian)**: Low-glare charcoal/titanium ground (`#0b0c0e`), optimized for museum viewing and high-contrast photo inspection.
  * **Linen (Archival Off-White)**: Warm tactile cotton-rag paper tone (`#f5f2eb`) reminiscent of 1991 physical convocation thesis paper and archival mounts.
  * **Light (Studio Pure Light)**: Modern Apple gallery daylight aesthetic (`#f4f5f7`) with crisp white surfaces for bright environments.
* **35th Jubilee Style Themes (Top 5 Reviewed with Codex)**:
  * 🏛️ **Archival Silver-Gelatin**: Museum-grade passe-partout mat, beveled gold inner bevel, and engraved 35th anniversary brass plaque.
  * 📐 **Mechanical Blueprint**: Prussian blue engineering draughting paper with official title block (`DWG NO: GECR-ME-91-01`, `SCALE: 1:1`, `REV: 35YR`, `H.O.D. PROF. G.S. VERMA`).
  * 🎞️ **1991 35mm Contact Sheet**: Kodak Tri-X 400 film rebate, sprockets, frame #35A/36, and red grease-pencil crop marks.
  * 🎬 **1991 Bollywood Card**: Golden cinema marquee border with *"★ यादें 1991 ★"* banner designed for batch WhatsApp sharing.
  * 💻 **AutoCAD R11 Slate**: Early 1990s dark slate CAD screen with precision millimeter coordinate rulers and terminal status readouts.
* **Instant WhatsApp Share Card Export**:
  * Click **📲 Export WhatsApp Card** to download a high-resolution 1520x1212 composite image of any theme ready to share.
* **Live Search**: Type any name (e.g., `Sanjay`, `Jain`, `Tiwari`, `Verma`) to instantly filter the directory and spotlight matching faces on the photograph.
* **Dual Spotlight Interaction**:
  * Hovering/clicking any face on the photo reveals their name and highlights their directory card below.
  * Hovering/clicking any card in the roster spotlights the person's face and smoothly pans/zooms the camera onto them.
* **View Modes**:
  * **Deskewed**: Clean, leveled rectangular crop of the photo.
  * **Enhanced B&W**: Contrast-stretched dynamic range with gentle unsharp-masking (no synthetic hallucination).
  * **Original Mount**: Full scan of the original physical cardboard mount with printed text.
* **"Then & Now" Profile Updates**:
  * Click any person to open their profile drawer.
  * Upload a current 2026 photo.
  * Add current location, company/role, contact/LinkedIn, and hostel/mechanical dept memories.
  * Click **Save Update** (persists in your browser) or **Export Updates** (generates a batch JSON file to share).

---

### Project Structure
```
gec-raipur-1991-yearbook/
├── landing.html            # High-conversion 35th anniversary editorial landing page
├── landing.css             # Landing page design system (Manrope, dark surfaces, tokens)
├── landing.js              # Real-time search, scroll reveals, dynamic face gallery
├── landing-data.js         # Lightweight embedded roster data
├── privacy.html            # Privacy and terms page (local storage & pixel integrity)
├── index.html              # Main interactive yearbook & photo viewer
├── styles.css              # Photo viewer styling (collegiate dark palette)
├── app.js                  # Photo viewer logic (zoom, pan, search, spotlights, modals)
├── verify_landing.py       # Automated Playwright test suite for desktop and mobile
├── README.md               # Documentation
├── data/
│   └── roster.json         # Complete structured roster with calibrated coordinates
└── assets/
    ├── photo_deskewed.jpg  # Leveled rectangular photo
    ├── photo_enhanced.jpg  # Optical high-contrast B&W photo
    ├── photo_original.jpg  # Untouched physical mount scan
    ├── landing_preview_desktop.png   # Full page desktop screenshot
    ├── landing_preview_mobile.png    # Full page mobile screenshot
    └── avatars/            # 67 individual authentic 1991 circular face crops
```
