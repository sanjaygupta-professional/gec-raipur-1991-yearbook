#!/usr/bin/env python3
"""
Generate the 5 distinct theme frame/mat SVG assets for the GEC Raipur 1990-91 Living Yearbook.
Outer Canvas: 1520 x 1212
Inner Photo Opening: x=160, y=160, width=1200, height=892 (transparent cutout)
All facial pixels and coordinates remain 100% authentic and aligned.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path("/home/sanjayg4/gec-raipur-1991-yearbook/assets/themes")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1520
HEIGHT = 1212
PX = 160
PY = 160
PW = 1200
PH = 892

def create_archival_svg():
    """1. Archival Silver-Gelatin: Museum passe-partout mat, beveled gold inner rim, engraved brass plaque."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
  <defs>
    <!-- Mat Texture & Shadows -->
    <radialGradient id="matVignette" cx="50%" cy="50%" r="70%">
      <stop offset="40%" stop-color="#242426"/>
      <stop offset="100%" stop-color="#141416"/>
    </radialGradient>
    <linearGradient id="goldBevel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f5e6a3"/>
      <stop offset="35%" stop-color="#d4af37"/>
      <stop offset="70%" stop-color="#aa8620"/>
      <stop offset="100%" stop-color="#6e530b"/>
    </linearGradient>
    <linearGradient id="brassPlate" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e8cf81"/>
      <stop offset="50%" stop-color="#c9a74e"/>
      <stop offset="100%" stop-color="#8a691e"/>
    </linearGradient>
    <filter id="matShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.8"/>
    </filter>
    <mask id="openingMask">
      <!-- Everything white is kept, black is cut out -->
      <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>
      <rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="2" fill="#000000"/>
    </mask>
  </defs>

  <!-- Solid Outer Mat with Cutout -->
  <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="url(#matVignette)" mask="url(#openingMask)"/>

  <!-- Museum Outer Thin Border -->
  <rect x="30" y="30" width="{WIDTH - 60}" height="{HEIGHT - 60}" fill="none" stroke="#38383c" stroke-width="2"/>
  <rect x="36" y="36" width="{WIDTH - 72}" height="{HEIGHT - 72}" fill="none" stroke="#d4af37" stroke-width="0.8" stroke-opacity="0.4"/>

  <!-- Inner Bevel Rim around Photo -->
  <rect x="{PX - 4}" y="{PY - 4}" width="{PW + 8}" height="{PH + 8}" fill="none" stroke="url(#goldBevel)" stroke-width="4" filter="url(#matShadow)"/>
  <rect x="{PX - 1}" y="{PY - 1}" width="{PW + 2}" height="{PH + 2}" fill="none" stroke="#000000" stroke-width="2" opacity="0.6"/>

  <!-- Top Header - Gold Embossed Typography -->
  <g text-anchor="middle" font-family="'Cinzel', 'Times New Roman', serif">
    <text x="{WIDTH / 2}" y="82" font-size="28" font-weight="700" fill="#f5e6a3" letter-spacing="3">GOVERNMENT ENGINEERING COLLEGE, RAIPUR (M.P.)</text>
    <text x="{WIDTH / 2}" y="118" font-size="16" font-weight="600" fill="#c9a74e" letter-spacing="4">DEPARTMENT OF MECHANICAL ENGINEERING • B.E. CLASS OF 1990-1991</text>
  </g>

  <!-- Bottom Brass Memorial Plaque -->
  <g transform="translate({WIDTH / 2 - 340}, {PY + PH + 24})">
    <!-- Brass Plaque Base -->
    <rect x="0" y="0" width="680" height="96" rx="6" fill="url(#brassPlate)" stroke="#523b09" stroke-width="2" filter="url(#matShadow)"/>
    <rect x="4" y="4" width="672" height="88" rx="4" fill="none" stroke="#fcebb3" stroke-width="1" opacity="0.6"/>

    <!-- Screws at 4 corners -->
    <circle cx="16" cy="16" r="4" fill="#6e530b"/><circle cx="16" cy="16" r="3" fill="#291e03"/><line x1="14" y1="16" x2="18" y2="16" stroke="#c9a74e" stroke-width="1"/>
    <circle cx="664" cy="16" r="4" fill="#6e530b"/><circle cx="664" cy="16" r="3" fill="#291e03"/><line x1="662" y1="16" x2="666" y2="16" stroke="#c9a74e" stroke-width="1"/>
    <circle cx="16" cy="80" r="4" fill="#6e530b"/><circle cx="16" cy="80" r="3" fill="#291e03"/><line x1="14" y1="80" x2="18" y2="80" stroke="#c9a74e" stroke-width="1"/>
    <circle cx="664" cy="80" r="4" fill="#6e530b"/><circle cx="664" cy="80" r="3" fill="#291e03"/><line x1="662" y1="80" x2="666" y2="80" stroke="#c9a74e" stroke-width="1"/>

    <!-- Engraved Plaque Text -->
    <text x="340" y="40" text-anchor="middle" font-family="'Cinzel', 'Times New Roman', serif" font-size="20" font-weight="700" fill="#2a1e05" letter-spacing="2">35th ANNIVERSARY COMMEMORATIVE ARCHIVE</text>
    <text x="340" y="70" text-anchor="middle" font-family="'Inter', sans-serif" font-size="13" font-weight="600" fill="#3d2d0c" letter-spacing="1.5">67 FACULTY, DIGNITARIES &amp; GRADUATING ENGINEERS • 1991 – 2026</text>
  </g>
</svg>'''
    (OUTPUT_DIR / "theme_archival.svg").write_text(svg)
    print("✓ Created theme_archival.svg")

def create_blueprint_svg():
    """2. Mechanical Blueprint: Prussian blue drafting board, white drafting lines, technical title block."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
  <defs>
    <!-- Blueprint Grid Pattern -->
    <pattern id="bpGridSmall" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1c4879" stroke-width="0.75" stroke-opacity="0.5"/>
    </pattern>
    <pattern id="bpGridLarge" width="100" height="100" patternUnits="userSpaceOnUse">
      <rect width="100" height="100" fill="url(#bpGridSmall)"/>
      <path d="M 100 0 L 0 0 0 100" fill="none" stroke="#2562a0" stroke-width="1.5" stroke-opacity="0.8"/>
    </pattern>
    <mask id="bpOpeningMask">
      <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>
      <rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="#000000"/>
    </mask>
  </defs>

  <!-- Blue Draughting Surface -->
  <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="#0a2544" mask="url(#bpOpeningMask)"/>
  <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="url(#bpGridLarge)" mask="url(#bpOpeningMask)"/>

  <!-- Outer Technical Drafting Frame -->
  <rect x="25" y="25" width="{WIDTH - 50}" height="{HEIGHT - 50}" fill="none" stroke="#68b2f8" stroke-width="2.5"/>
  <rect x="35" y="35" width="{WIDTH - 70}" height="{HEIGHT - 70}" fill="none" stroke="#68b2f8" stroke-width="1"/>

  <!-- Technical Zone Marks (A-F, 1-8) -->
  <g font-family="'Consolas', 'Courier New', monospace" font-size="12" font-weight="700" fill="#8ec6fc" text-anchor="middle">
    <text x="200" y="30">1</text><text x="400" y="30">2</text><text x="600" y="30">3</text>
    <text x="800" y="30">4</text><text x="1000" y="30">5</text><text x="1200" y="30">6</text><text x="1350" y="30">7</text>
    <text x="30" y="250">A</text><text x="30" y="500">B</text><text x="30" y="750">C</text><text x="30" y="1000">D</text>
  </g>

  <!-- Photo Opening Inner Technical Border -->
  <rect x="{PX - 2}" y="{PY - 2}" width="{PW + 4}" height="{PH + 4}" fill="none" stroke="#68b2f8" stroke-width="2"/>
  <rect x="{PX - 8}" y="{PY - 8}" width="{PW + 16}" height="{PH + 16}" fill="none" stroke="#3b82c4" stroke-width="0.8" stroke-dasharray="8 4"/>

  <!-- Corner Alignment Brackets -->
  <g stroke="#ffffff" stroke-width="2" fill="none">
    <path d="M {PX - 15} {PY + 20} L {PX - 15} {PY - 15} L {PX + 20} {PY - 15}"/>
    <path d="M {PX + PW + 15} {PY + 20} L {PX + PW + 15} {PY - 15} L {PX + PW - 20} {PY - 15}"/>
    <path d="M {PX - 15} {PY + PH - 20} L {PX - 15} {PY + PH + 15} L {PX + 20} {PY + PH + 15}"/>
    <path d="M {PX + PW + 15} {PY + PH - 20} L {PX + PW + 15} {PY + PH + 15} L {PX + PW - 20} {PY + PH + 15}"/>
  </g>

  <!-- Top Technical Specification Header -->
  <g font-family="'Consolas', 'Courier New', monospace" fill="#ffffff">
    <text x="{PX}" y="85" font-size="24" font-weight="700" letter-spacing="2">ASSEMBLY BLUEPRINT: GEC RAIPUR MECHANICAL ENGG. [1990-1991]</text>
    <text x="{PX}" y="115" font-size="14" fill="#8ec6fc">SUBSYSTEM: 67 FACULTY &amp; ALUMNI NODES • ZERO GEOMETRIC DISTORTION CONTRACT</text>
  </g>

  <!-- Bottom Right Official Engineering Title Block (ISO Standard) -->
  <g transform="translate({WIDTH - 470}, {PY + PH + 12})" font-family="'Consolas', 'Courier New', monospace">
    <!-- Title Box Outer -->
    <rect x="0" y="0" width="435" height="116" fill="#0d2b4d" stroke="#68b2f8" stroke-width="2"/>
    <line x1="0" y1="28" x2="435" y2="28" stroke="#68b2f8" stroke-width="1.5"/>
    <line x1="0" y1="58" x2="435" y2="58" stroke="#68b2f8" stroke-width="1.5"/>
    <line x1="0" y1="88" x2="435" y2="88" stroke="#68b2f8" stroke-width="1.5"/>
    <line x1="220" y1="28" x2="220" y2="116" stroke="#68b2f8" stroke-width="1.5"/>
    <line x1="325" y1="58" x2="325" y2="116" stroke="#68b2f8" stroke-width="1.5"/>

    <!-- Row 1: Org -->
    <text x="12" y="19" font-size="13" font-weight="700" fill="#ffffff">GOVT. ENGG. COLLEGE RAIPUR (M.P.)</text>
    <text x="310" y="19" font-size="11" fill="#8ec6fc">DEPT: MECHANICAL</text>

    <!-- Row 2: Title -->
    <text x="12" y="47" font-size="13" font-weight="700" fill="#ffd166">B.E. FINAL YEAR 1990-91</text>
    <text x="230" y="47" font-size="11" fill="#8ec6fc">DWG: GECR-ME-91-01</text>

    <!-- Row 3: Approvals -->
    <text x="12" y="76" font-size="10" fill="#8ec6fc">H.O.D.: PROF. G.S. VERMA</text>
    <text x="230" y="76" font-size="10" fill="#8ec6fc">SCALE: 1:1</text>
    <text x="335" y="76" font-size="10" fill="#8ec6fc">REV: 35YR</text>

    <!-- Row 4: Date & Status -->
    <text x="12" y="104" font-size="10" fill="#8ec6fc">DATE: APRIL 1991 / 2026</text>
    <text x="230" y="104" font-size="10" fill="#06d6a0" font-weight="700">VERIFIED: AUTHENTIC</text>
    <text x="335" y="104" font-size="10" fill="#ffffff">SHEET 1/1</text>
  </g>
</svg>'''
    (OUTPUT_DIR / "theme_blueprint.svg").write_text(svg)
    print("✓ Created theme_blueprint.svg")

def create_contactsheet_svg():
    """3. 1991 35mm Contact Sheet: Kodak Tri-X 400 film rebate, sprockets, grease pencil crop marks."""
    # Generate sprocket holes
    sprockets_top = []
    sprockets_bot = []
    for x in range(40, WIDTH - 40, 52):
        sprockets_top.append(f'<rect x="{x}" y="30" width="30" height="22" rx="4" fill="#000000" stroke="#333333" stroke-width="1"/>')
        sprockets_bot.append(f'<rect x="{x}" y="{HEIGHT - 52}" width="30" height="22" rx="4" fill="#000000" stroke="#333333" stroke-width="1"/>')
    sprockets_top_str = "\n    ".join(sprockets_top)
    sprockets_bot_str = "\n    ".join(sprockets_bot)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
  <defs>
    <mask id="filmOpeningMask">
      <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>
      <rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="#000000"/>
    </mask>
  </defs>

  <!-- Darkroom Matte Black Photographic Sheet -->
  <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="#111111" mask="url(#filmOpeningMask)"/>

  <!-- Sprocket Holes -->
  <g>
    {sprockets_top_str}
    {sprockets_bot_str}
  </g>

  <!-- 35mm Film Edge Text & Frame Numbers (Amber/Orange Factory Stamp) -->
  <g font-family="'Consolas', 'Courier New', monospace" font-weight="700" fill="#fca311" font-size="15" letter-spacing="3">
    <text x="120" y="90">KODAK SAFETY FILM 5063</text>
    <text x="540" y="90">▶ 34A</text>
    <text x="820" y="90">KODAK TRI-X 400</text>
    <text x="1240" y="90">▶ 35</text>

    <text x="120" y="{HEIGHT - 80}">▶ 35A</text>
    <text x="480" y="{HEIGHT - 80}">KODAK SAFETY FILM</text>
    <text x="920" y="{HEIGHT - 80}">▶ 36</text>
    <text x="1200" y="{HEIGHT - 80}">KODAK 5063</text>
  </g>

  <!-- Film Negative Cut Border -->
  <rect x="{PX - 4}" y="{PY - 4}" width="{PW + 8}" height="{PH + 8}" fill="none" stroke="#222222" stroke-width="4"/>

  <!-- Red Chinagraph / Grease Pencil Photographer Marks -->
  <g stroke="#ff3333" stroke-width="3" stroke-linecap="round" fill="none">
    <!-- Top Left Crop Bracket -->
    <path d="M {PX - 20} {PY + 30} L {PX - 20} {PY - 20} L {PX + 30} {PY - 20}"/>
    <!-- Top Right Crop Bracket -->
    <path d="M {PX + PW + 20} {PY + 30} L {PX + PW + 20} {PY - 20} L {PX + PW - 30} {PY - 20}"/>
    <!-- Bottom Left Crop Bracket -->
    <path d="M {PX - 20} {PY + PH - 30} L {PX - 20} {PY + PH + 20} L {PX + 30} {PY + PH + 20}"/>
    <!-- Bottom Right Crop Bracket -->
    <path d="M {PX + PW + 20} {PY + PH - 30} L {PX + PW + 20} {PY + PH + 20} L {PX + PW - 30} {PY + PH + 20}"/>

    <!-- Photographer Select Tick (Grease Pencil "OK" Checkmark) -->
    <path d="M {PX + PW - 80} {PY - 60} L {PX + PW - 60} {PY - 35} L {PX + PW - 20} {PY - 80}"/>
  </g>

  <!-- White Grease Pencil / Darkroom Chinagraph Note -->
  <g font-family="'Caveat', 'Comic Sans MS', cursive, sans-serif" fill="#ffffff" opacity="0.9">
    <text x="{PX + 20}" y="{PY - 45}" font-size="28" transform="rotate(-1, {PX + 20}, {PY - 45})">G.E.C. Raipur — Mechanical '91 (Final Batch Negative)</text>
    <text x="{PX + 40}" y="{PY + PH + 65}" font-size="24" transform="rotate(0.5, {PX + 40}, {PY + PH + 65})">Roll #12, Frame 35A • Convocation Group • April 1991</text>
  </g>
</svg>'''
    (OUTPUT_DIR / "theme_contactsheet.svg").write_text(svg)
    print("✓ Created theme_contactsheet.svg")

def create_cinema_svg():
    """4. 1991 Bollywood / Retro Cinema Title Card: Celebratory golden marquee, ornate Indian filigree, 'यादें 1991'."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
  <defs>
    <linearGradient id="cinemaVelvet" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#360a14"/>
      <stop offset="50%" stop-color="#1f040b"/>
      <stop offset="100%" stop-color="#120106"/>
    </linearGradient>
    <linearGradient id="goldMarquee" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#d4af37"/>
      <stop offset="25%" stop-color="#fff2a8"/>
      <stop offset="50%" stop-color="#d4af37"/>
      <stop offset="75%" stop-color="#fff2a8"/>
      <stop offset="100%" stop-color="#d4af37"/>
    </linearGradient>
    <mask id="cinemaOpeningMask">
      <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>
      <rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="#000000"/>
    </mask>
  </defs>

  <!-- Royal Velvet Marquee Background -->
  <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="url(#cinemaVelvet)" mask="url(#cinemaOpeningMask)"/>

  <!-- Ornate Golden Borders -->
  <rect x="25" y="25" width="{WIDTH - 50}" height="{HEIGHT - 50}" fill="none" stroke="url(#goldMarquee)" stroke-width="4"/>
  <rect x="35" y="35" width="{WIDTH - 70}" height="{HEIGHT - 70}" fill="none" stroke="#d4af37" stroke-width="1" stroke-dasharray="12 6"/>

  <!-- Cinema Corner Flourishes -->
  <g stroke="#d4af37" stroke-width="2" fill="none">
    <path d="M 45 75 Q 75 75 75 45 M 45 85 Q 85 85 85 45"/>
    <path d="M {WIDTH - 45} 75 Q {WIDTH - 75} 75 {WIDTH - 75} 45 M {WIDTH - 45} 85 Q {WIDTH - 85} 85 {WIDTH - 85} 45"/>
    <path d="M 45 {HEIGHT - 75} Q 75 {HEIGHT - 75} 75 {HEIGHT - 45} M 45 {HEIGHT - 85} Q 85 {HEIGHT - 85} 85 {HEIGHT - 45}"/>
    <path d="M {WIDTH - 45} {HEIGHT - 75} Q {WIDTH - 75} {HEIGHT - 75} {WIDTH - 75} {HEIGHT - 45} M {WIDTH - 45} {HEIGHT - 85} Q {WIDTH - 85} {HEIGHT - 85} {WIDTH - 85} {HEIGHT - 45}"/>
  </g>

  <!-- Photo Opening Golden Inner Frame -->
  <rect x="{PX - 4}" y="{PY - 4}" width="{PW + 8}" height="{PH + 8}" fill="none" stroke="url(#goldMarquee)" stroke-width="4"/>

  <!-- Top Cinema Header -->
  <g text-anchor="middle">
    <!-- Hindi & English Cinema Marquee -->
    <text x="{WIDTH / 2}" y="78" font-family="'Yatra One', 'Arial Black', sans-serif" font-size="34" font-weight="900" fill="url(#goldMarquee)" letter-spacing="4">★ यादें 1991 ★</text>
    <text x="{WIDTH / 2}" y="115" font-family="'Cinzel', 'Georgia', serif" font-size="18" font-weight="700" fill="#ffffff" letter-spacing="5">GEC RAIPUR MECHANICAL PRESENTS : THE CLASS OF 1991</text>
    <text x="{WIDTH / 2}" y="142" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#ffd166" letter-spacing="3">35 YEARS OF BROTHERHOOD &amp; MEMORIES</text>
  </g>

  <!-- Bottom Cinema Credits Block -->
  <g text-anchor="middle" font-family="'Inter', sans-serif" transform="translate(0, {PY + PH + 25})">
    <!-- Star divider -->
    <text x="{WIDTH / 2}" y="20" font-size="14" fill="#ffd166">★ ★ ★ 35th JUBILEE EDITION ★ ★ ★</text>

    <!-- Retro Movie Billing -->
    <text x="{WIDTH / 2}" y="52" font-size="16" font-weight="700" fill="#ffffff" letter-spacing="2">STARRING: 67 LEGENDS • 15 ESTEEMED PROFESSORS • 52 ENGINEERS</text>
    <text x="{WIDTH / 2}" y="78" font-size="13" font-weight="500" fill="#e0a96d" letter-spacing="1.5">LOCATION: RAIPUR, M.P. • PRODUCED BY: TIMELESS FRIENDSHIP • RUNTIME: FOREVER</text>
  </g>
</svg>'''
    (OUTPUT_DIR / "theme_cinema.svg").write_text(svg)
    print("✓ Created theme_cinema.svg")

def create_cad_svg():
    """5. AutoCAD R11 / Engineer Slate: Precision coordinate rulers, dark slate screen, CAD command prompt."""
    # Generate ruler tick marks
    ruler_top = []
    for x in range(PX, PX + PW + 1, 20):
        h = 14 if (x - PX) % 100 == 0 else (8 if (x - PX) % 50 == 0 else 4)
        ruler_top.append(f'<line x1="{x}" y1="{PY - 4}" x2="{x}" y2="{PY - 4 - h}" stroke="#00f0ff" stroke-width="1"/>')
        if (x - PX) % 100 == 0:
            ruler_top.append(f'<text x="{x}" y="{PY - 22}" font-size="9" fill="#00f0ff" text-anchor="middle">{x - PX}</text>')
    ruler_top_str = "\n    ".join(ruler_top)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
  <defs>
    <mask id="cadOpeningMask">
      <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>
      <rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="#000000"/>
    </mask>
  </defs>

  <!-- Dark Slate CAD Workstation Surface -->
  <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="#0b1015" mask="url(#cadOpeningMask)"/>

  <!-- Outer Workstation Bezel -->
  <rect x="20" y="20" width="{WIDTH - 40}" height="{HEIGHT - 40}" fill="none" stroke="#1f2c38" stroke-width="2"/>
  <rect x="26" y="26" width="{WIDTH - 52}" height="{HEIGHT - 52}" fill="none" stroke="#00f0ff" stroke-width="0.75" stroke-opacity="0.4"/>

  <!-- Coordinate Ruler (X-Axis) -->
  <g font-family="'Consolas', monospace">
    <line x1="{PX}" y1="{PY - 4}" x2="{PX + PW}" y2="{PY - 4}" stroke="#00f0ff" stroke-width="1.5"/>
    {ruler_top_str}
  </g>

  <!-- Photo Opening CAD Viewport Frame -->
  <rect x="{PX - 2}" y="{PY - 2}" width="{PW + 4}" height="{PH + 4}" fill="none" stroke="#00f0ff" stroke-width="2"/>
  <rect x="{PX - 1}" y="{PY - 1}" width="{PW + 2}" height="{PH + 2}" fill="none" stroke="#ffb703" stroke-width="0.8"/>

  <!-- Top CAD Application Title & Telemetry Header -->
  <g font-family="'Consolas', 'Courier New', monospace" fill="#ffffff" transform="translate({PX}, 65)">
    <rect x="0" y="0" width="{PW}" height="42" fill="#141e28" stroke="#00f0ff" stroke-width="1"/>
    <text x="16" y="26" font-size="15" font-weight="700" fill="#00f0ff">AUTOCAD R11 (1991) — [GECO91_MECH.DWG]</text>
    <text x="560" y="26" font-size="12" fill="#ffb703">VIEW: ORTHO 2D</text>
    <text x="730" y="26" font-size="12" fill="#8ecae6">LAYER: 0_PEOPLE (67 NODES)</text>
    <text x="1000" y="26" font-size="12" fill="#06d6a0">SNAP: ON  GRID: ON</text>
  </g>

  <!-- Bottom CAD Terminal / Command Prompt -->
  <g font-family="'Consolas', 'Courier New', monospace" transform="translate({PX}, {PY + PH + 18})">
    <rect x="0" y="0" width="{PW}" height="95" fill="#05080b" stroke="#00f0ff" stroke-width="1.5"/>
    <text x="16" y="26" font-size="13" fill="#8ecae6">Command: _OPEN "GEC_RAIPUR_MECH_1990_1991.DWG"</text>
    <text x="16" y="48" font-size="13" fill="#8ecae6">Command: _ZOOM _ALL &gt; Regenerating drawing... 67 entities located.</text>
    <text x="16" y="70" font-size="13" fill="#06d6a0" font-weight="700">Command: _STATUS &gt; FACIAL GEOMETRY LOCKED (100% UNTOUCHED OPTICAL PIXELS)</text>
    <text x="16" y="88" font-size="13" fill="#00f0ff">Command: <tspan fill="#ffffff">_SPOTLIGHT "SANJAY GUPTA"</tspan> <tspan fill="#00f0ff">_</tspan></text>
  </g>
</svg>'''
    (OUTPUT_DIR / "theme_cad.svg").write_text(svg)
    print("✓ Created theme_cad.svg")

if __name__ == "__main__":
    print("Generating 5 style theme assets...")
    create_archival_svg()
    create_blueprint_svg()
    create_contactsheet_svg()
    create_cinema_svg()
    create_cad_svg()
    print("Done! All 5 assets created in assets/themes/")
