import json
from pathlib import Path

BASE_DIR = Path("/home/sanjayg4/gec-raipur-1991-yearbook")
ASSETS_DIR = BASE_DIR / "assets/milestones"
DATA_FILE = BASE_DIR / "data/milestones.json"

ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# 20 Milestones Data
milestones = [
    # 10 Classical College Foundations (1987-1991)
    {
        "id": "carnot-cycle",
        "title": "Carnot & Rankine Thermodynamic Cycles",
        "category": "Thermodynamics",
        "era": "College Foundation (1987–1991)",
        "year": "1824 / 1988 Lab",
        "formula": "η_th = 1 - (T_C / T_H) = W_net / Q_in",
        "svg": "assets/milestones/carnot_cycle.svg",
        "summary": "The theoretical maximum efficiency limit of heat engines operating between thermal reservoirs.",
        "description": "Every mechanical engineer spent late nights tracing isothermal expansion and isentropic compression paths on P-V and T-S coordinates. Carnot proved that no heat engine could be 100% efficient, establishing the foundational Second Law of Thermodynamics.",
        "memory": "Remember drawing endless Carnot and Rankine cycles with French curves in Heat Engines lab sheets, terrified that the professor would reject the calculation if the areas didn't balance?"
    },
    {
        "id": "navier-stokes",
        "title": "Navier-Stokes & Bernoulli Equations",
        "category": "Fluid Mechanics",
        "era": "College Foundation (1987–1991)",
        "year": "1845 / 1989 Lab",
        "formula": "ρ(∂u/∂t + u·∇u) = -∇p + μ∇²u + f",
        "svg": "assets/milestones/navier_stokes.svg",
        "summary": "The non-linear partial differential equations describing the conservation of momentum in viscous fluid flow.",
        "description": "From laminar flow in cylindrical pipes to boundary layer separation over airfoils, these equations govern every pump, compressor, and hydraulic circuit. In 1989, we solved simplified 1D Bernoulli approximations before CFD existed on PCs.",
        "memory": "Standing next to the fluid mechanics flume with stopwatches, timing mercury manometer meniscus shifts to verify venturimeter discharge coefficients."
    },
    {
        "id": "mollier-chart",
        "title": "Mollier Enthalpy-Entropy (h-s) Steam Tables",
        "category": "Thermal Engineering",
        "era": "College Foundation (1987–1991)",
        "year": "1904 / 1989 Lab",
        "formula": "h = u + pv | s_2 - s_1 = ∫ (dq / T)",
        "svg": "assets/milestones/mollier_chart.svg",
        "summary": "Graphical thermodynamics mapping enthalpy vs entropy for steam turbine expansion calculations.",
        "description": "Before digital simulation, steam power plant cycle analysis relied on fold-out paper Mollier charts with green grid lines. Engineers tracked dryness fraction x, superheat degrees, and turbine isentropic drops with a clear ruler.",
        "memory": "Scrambling through the tattered blue Steam Tables booklet during boiler viva, hoping the external examiner wouldn't ask for interpolation at 42.5 bar dry saturated steam!"
    },
    {
        "id": "mohrs-circle",
        "title": "Mohr's Circle of Stress & Strain",
        "category": "Strength of Materials",
        "era": "College Foundation (1987–1991)",
        "year": "1882 / 1988 Lab",
        "formula": "σ_{1,2} = (σ_x + σ_y)/2 ± √[((σ_x - σ_y)/2)² + τ_xy²]",
        "svg": "assets/milestones/mohr_circle.svg",
        "summary": "Two-dimensional graphical transformation to determine principal stresses and maximum shear planes.",
        "description": "Developed by Christian Otto Mohr, this circle allows graphical determination of normal and shear stress on any plane at angle θ. Crucial for shaft design and structural failure theories (von Mises, Tresca).",
        "memory": "Using compasses and HB pencils on A3 drawing sheets in Mechanics of Solids, proving whether ductile mild steel would yield in shear at 45 degrees under tension."
    },
    {
        "id": "geneva-mechanism",
        "title": "Geneva Drive & 4-Bar Kinematic Linkages",
        "category": "Theory of Machines",
        "era": "College Foundation (1987–1991)",
        "year": "1890 / 1989 Lab",
        "formula": "ω_driven = f(θ_driver, n) | Grashof: s + l ≤ p + q",
        "svg": "assets/milestones/geneva_drive.svg",
        "summary": "Intermittent rotary motion mechanism converting continuous rotation into stepped angular indexing.",
        "description": "From movie projector film steppers to automated assembly indexing tables, the Maltese cross Geneva drive demonstrated pure kinematic geometry. Alongside Chebyshev 4-bar linkages, it formed the core of machine synthesis.",
        "memory": "The mechanical clatter of wooden and brass kinematic linkage models in the TOM lab, measuring quick-return stroke ratios with crank-rocker sliders."
    },
    {
        "id": "fourier-heat",
        "title": "Fourier's Law & LMTD Heat Exchangers",
        "category": "Heat & Mass Transfer",
        "era": "College Foundation (1987–1991)",
        "year": "1822 / 1990 Lab",
        "formula": "q = -k A (dT/dx) | ΔT_lm = (ΔT_1 - ΔT_2) / ln(ΔT_1 / ΔT_2)",
        "svg": "assets/milestones/fourier_heat.svg",
        "summary": "Thermal conduction laws and log mean temperature difference for counter-current heat exchangers.",
        "description": "Governs thermal energy flow through conduction, convection, and radiation. Essential for designing shell-and-tube heat exchangers, automotive radiators, and boiler economizers.",
        "memory": "Adjusting hot water valves and copper thermocouples in the heat transfer lab, waiting 45 minutes for thermal steady state while copying notes."
    },
    {
        "id": "euler-buckling",
        "title": "Euler Critical Buckling in Columns",
        "category": "Machine Design",
        "era": "College Foundation (1987–1991)",
        "year": "1757 / 1989 Lab",
        "formula": "P_cr = (π² E I) / (K L)² | σ_b = M y / I",
        "svg": "assets/milestones/euler_buckling.svg",
        "summary": "Determination of maximum axial load before slender structural columns undergo elastic instability.",
        "description": "Leonhard Euler discovered that slender columns buckle under loads far lower than compressive yield strength. Effective length factors K (0.5 for fixed-fixed, 1.0 for pinned-pinned, 2.0 for cantilever) dictate all structural columns.",
        "memory": "Watching the dial gauge quiver on the Universal Testing Machine (UTM) as a slender steel rod suddenly bowed with a loud thud during compressive buckling tests."
    },
    {
        "id": "involute-gears",
        "title": "Involute Gear Profiles & Epicyclic Trains",
        "category": "Machine Design",
        "era": "College Foundation (1987–1991)",
        "year": "1762 / 1990 Lab",
        "formula": "r_base = r_pitch · cos(φ) | Gear Ratio i = N_1 / N_2",
        "svg": "assets/milestones/involute_gears.svg",
        "summary": "Constant velocity ratio transmission via involute curve teeth profiles and planetary gear systems.",
        "description": "Involute teeth guarantee constant angular velocity even if center distance varies slightly. Combined with epicyclic sun-and-planet gear sets, this allowed compact high-torque transmissions in automobiles and cranes.",
        "memory": "Tracing involute curves tooth-by-tooth on layout paper using pitch circle tangents and normal circles until calluses formed on fingers."
    },
    {
        "id": "hydraulic-turbines",
        "title": "Pelton & Francis Turbine Velocity Triangles",
        "category": "Fluid Machinery",
        "era": "College Foundation (1987–1991)",
        "year": "1880 / 1990 Lab",
        "formula": "P = ρ Q (V_w1 u_1 ± V_w2 u_2) | η_man = H_m / H_gross",
        "svg": "assets/milestones/hydraulic_turbines.svg",
        "summary": "Euler turbomachine equation and impulse-reaction velocity triangles for hydroelectric power.",
        "description": "High-head impulse Pelton wheels with double-hemispherical splitter cups vs medium-head reaction Francis turbines. Analyzing blade entrance and exit velocity vectors $V_1, u_1, V_{r1}$ determined hydraulic efficiency.",
        "memory": "The deafening roar of the Pelton wheel testing rig in the basement lab, with water spray soaking everyone's lab coats as the tachometer climbed to 1500 RPM."
    },
    {
        "id": "workshop-gdt",
        "title": "Lathe Machining & GD&T Tolerances (H7/g6)",
        "category": "Manufacturing Technology",
        "era": "College Foundation (1987–1991)",
        "year": "1991 Workshop",
        "formula": "Tolerance = Upper Limit - Lower Limit | Fit = Hole - Shaft",
        "svg": "assets/milestones/workshop_gdt.svg",
        "summary": "Precision metal removal via HSS single-point cutting tools and ISO limits, fits, and geometric tolerancing.",
        "description": "Every engineer mastered centering a four-jaw chuck, grinding high-speed steel tool rake and clearance angles, knurling, thread chasing, and calculating clearance/interference fits for shaft assemblies.",
        "memory": "Smell of cutting oil and sulfur in the central workshop, sweating in blue aprons under ceiling fans while turning a rough cast iron billet down to exact 25.00mm tolerance."
    },

    # 10 Modern Breakthroughs & Robotics (1991-2026)
    {
        "id": "fea-generative",
        "title": "Non-Linear FEA & Generative Topology",
        "category": "Computational Mechanics",
        "era": "Modern Era (1991–2026)",
        "year": "1995–2024",
        "formula": "[K] {u} = {F} | SIMP: E(ρ) = ρ^p E_0",
        "svg": "assets/milestones/fea_meshing.svg",
        "summary": "Finite element discretization evolving from NASTRAN stiffness matrices into AI-driven generative topology.",
        "description": "Where we once hand-calculated 2x2 stiffness matrices, modern multi-physics FEA models millions of elements under non-linear plastic deformation, dynamic crash impacts, and generative topology optimization removing 40% mass.",
        "memory": "Graduating from punch-card batch scripts and monochrome workstations to cloud-rendered stress contours running millions of tetrahedrons in minutes."
    },
    {
        "id": "mems-sensors",
        "title": "MEMS Micro-Machined Accelerometers & Gyros",
        "category": "Micro-Mechatronics",
        "era": "Modern Era (1991–2026)",
        "year": "1998–2010",
        "formula": "C = ε A / d | ΔC = 2 ε A (x / d²) | m ẍ + c ẋ + k x = F",
        "svg": "assets/milestones/mems_accelerometer.svg",
        "summary": "Silicon etched comb-finger micro-mechanics bringing mechanical inertial guidance into every smartphone and drone.",
        "description": "Mechanical engineering etched onto silicon wafers. Microscopic cantilever beams, comb capacitors, and proof masses replaced 10kg spinning mechanical gyroscopes, making autonomous flight and consumer mobile devices possible.",
        "memory": "Realizing the mechanical mass-spring-damper equations we solved on chalkboards are now inside a 2mm chip in every pocket on Earth."
    },
    {
        "id": "metal-3d-printing",
        "title": "Additive Manufacturing & Laser Powder Bed Fusion",
        "category": "Advanced Manufacturing",
        "era": "Modern Era (1991–2026)",
        "year": "2005–2026",
        "formula": "Volumetric Energy Density E = P / (v · h · t)",
        "svg": "assets/milestones/additive_lattice.svg",
        "summary": "Direct Metal Laser Sintering (DMLS) of titanium and Inconel with conformal cooling internal channels.",
        "description": "Shattered traditional subtractive machining constraints. Rocket engine combustors with internal spiral regenerative cooling passages and biomimetic orthopedic implants grown layer-by-layer at 30-micron laser resolution.",
        "memory": "The shift from 'design for machining' (making sure the mill cutter can reach) to 'design for additive' (printing hollow lattice structures that cast iron never could dream of)."
    },
    {
        "id": "spacex-grid-fins",
        "title": "Reusable Rocket Aerodynamic Hypersonic Grid Fins",
        "category": "Aerospace Mechanics",
        "era": "Modern Era (1991–2026)",
        "year": "2015–2026",
        "formula": "C_N = 2 sin(2α) · (A_web / A_ref) | M > 1 Hypersonic",
        "svg": "assets/milestones/grid_fins.svg",
        "summary": "Titanium lattice grid fins steering orbital rocket boosters during Mach 5 atmospheric reentry to pinpoint touchdown.",
        "description": "Grid fins provide high pitch and yaw control authority with minimal hinge moment across transonic and hypersonic shock regimes. Combined with closed-loop hydraulic screw-jack actuators, they made rocket reusability an operational reality.",
        "memory": "Watching the 2015 Falcon 9 first stage stick its vertical landing on an ocean barge: pure mechanical dynamics, gimbal hydraulics, and supersonic aerodynamics at their finest."
    },
    {
        "id": "dynamic-robotics",
        "title": "Modern Quadruped & Biped Dynamic Legged Robots",
        "category": "Robotics & Kinematics",
        "era": "Modern Era (1991–2026)",
        "year": "2008–2026",
        "formula": "τ = J^T(q) F_ext + M(q)q̈ + C(q,q̇)q̇ + g(q)",
        "svg": "assets/milestones/quadruped_linkage.svg",
        "summary": "Boston Dynamics BigDog to Atlas: hydraulic and quasi-direct drive electric actuators with dynamic whole-body balance.",
        "description": "Transcended rigid industrial factory arms. Modern mobile robots employ model predictive control, zero-moment point dynamics, and custom planetary actuators with 10:1 gear reductions to backflip, sprint, and traverse unstructured disaster terrain.",
        "memory": "Remembering inverted pendulum exercises in Control Systems, now realized in real life as humanoid robots executing gymnastics and agile recovery."
    },
    {
        "id": "digital-twin-iiot",
        "title": "Digital Twins & FFT Vibration Spectral Analysis",
        "category": "Predictive Engineering",
        "era": "Modern Era (1991–2026)",
        "year": "2016–2026",
        "formula": "X(k) = ∑_{n=0}^{N-1} x(n) e^{-j 2π k n / N} | BPFO, BPFI",
        "svg": "assets/milestones/digital_twin_iot.svg",
        "summary": "Real-time edge sensor streaming and physics-informed models predicting machine bearing failure before it occurs.",
        "description": "Tri-axial piezo accelerometers sample industrial turbomachinery at 20 kHz. Fast Fourier Transform spectral decomposition detects ball-pass outer race (BPFO) defect peaks weeks before cataclysmic thermal seizure.",
        "memory": "From placing a copper screwdriver to the motor casing to listen for bearing hum, to digital dashboards alerting an engineer across the world in milliseconds."
    },
    {
        "id": "cfd-aerodynamics",
        "title": "CFD Large Eddy Simulation & Vortex Shedding",
        "category": "Aerodynamics & CFD",
        "era": "Modern Era (1991–2026)",
        "year": "2000–2026",
        "formula": "St = (f_s · L) / U_∞ ≈ 0.21 (1 - 21.2 / Re)",
        "svg": "assets/milestones/cfd_vortex.svg",
        "summary": "High-performance computing modeling unsteady turbulent boundary layer separation and von Kármán vortex streets.",
        "description": "Computes aerodynamic drag reduction, downforce on Le Mans race cars, and wind turbine aeroacoustic blade noise. Replaces multi-million dollar wind tunnel prototypes with GPU-accelerated Navier-Stokes volumetric solvers.",
        "memory": "Watching rainbow-colored velocity streamline animations replace the chalk sketches our professors drew on the lecture blackboard."
    },
    {
        "id": "composite-structures",
        "title": "Carbon-Fiber Monocoques & Honeycomb Sandwich",
        "category": "Advanced Materials",
        "era": "Modern Era (1991–2026)",
        "year": "1995–2026",
        "formula": "D = (E_f t_f d² / 2) + (E_c t_c³ / 12) | Tsai-Hill Yield",
        "svg": "assets/milestones/carbon_monocoque.svg",
        "summary": "Anisotropic composite laminates delivering 5x steel strength at a fraction of aluminum weight.",
        "description": "Autoclave pre-preg carbon fiber tape $[0^\circ / \pm 45^\circ / 90^\circ]$ over Nomex aramid honeycomb cores. Revolutionized modern aircraft (Boeing 787 50% composite) and Formula 1 driver safety survival cells.",
        "memory": "Comparing the heavy welded mild-steel box sections we drilled in 1990 to ultra-rigid carbon monocoques strong enough to survive a 200 mph impact intact."
    },
    {
        "id": "harmonic-drives",
        "title": "Harmonic Strain Wave Gearing in Robotics",
        "category": "Precision Mechatronics",
        "era": "Modern Era (1991–2026)",
        "year": "1991–2026",
        "formula": "Reduction Ratio R = -Z_flex / (Z_circ - Z_flex)",
        "svg": "assets/milestones/harmonic_drive.svg",
        "summary": "Zero-backlash elastic deformation gearing enabling sub-arcsecond precision in surgical and humanoid robotic joints.",
        "description": "An elliptical ball-bearing wave generator flexes a thin-walled steel toothed cup against a circular ring with two more teeth. Delivers 100:1 gear reduction with zero backlash, powering the arms of the Mars Curiosity rover and surgical da Vinci systems.",
        "memory": "Teaching machines to move with sub-millimeter grace, combining classical elasticity theory with micro-precision teeth cutting."
    },
    {
        "id": "lidar-autonomous",
        "title": "Autonomous Vehicle LIDAR & Drive-by-Wire",
        "category": "Autonomous Systems",
        "era": "Modern Era (1991–2026)",
        "year": "2012–2026",
        "formula": "Distance d = (c · Δt) / 2 | Point Cloud: P_i = [x, y, z, I]^T",
        "svg": "assets/milestones/lidar_mechatronics.svg",
        "summary": "Optical time-of-flight solid-state laser point clouds coupled to mechatronic steering and braking actuators.",
        "description": "Mechanical automotive engineering merged with electronic sensor fusion. Millions of laser pulses per second map 360-degree road environments, while redundant brushless electric motors control rack-and-pinion steering without mechanical column linkages.",
        "memory": "From adjusting mechanical steering idler arms and tie rods on Ambassador cars to autonomous vehicles navigating city streets with photon pulses."
    }
]

# Write JSON
with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(milestones, f, indent=2)

print(f"✓ Wrote {len(milestones)} milestones to {DATA_FILE}")

# SVG Generator Dictionary with technical schematics
svg_content = {
    "carnot_cycle.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <path d="M 40 190 L 290 190 M 40 190 L 40 25" stroke="#4A6572" stroke-width="2"/>
  <text x="285" y="208" fill="#8BA9C4" font-family="monospace" font-size="12">V (Volume)</text>
  <text x="15" y="25" fill="#8BA9C4" font-family="monospace" font-size="12">P</text>
  <!-- P-V curve -->
  <path d="M 80 50 Q 140 70 200 100 Q 220 140 230 170 Q 160 160 110 145 Q 85 100 80 50 Z" 
        fill="rgba(232, 163, 23, 0.12)" stroke="#E8A317" stroke-width="2.5"/>
  <!-- State points -->
  <circle cx="80" cy="50" r="4" fill="#22D3EE"/>
  <circle cx="200" cy="100" r="4" fill="#22D3EE"/>
  <circle cx="230" cy="170" r="4" fill="#22D3EE"/>
  <circle cx="110" cy="145" r="4" fill="#22D3EE"/>
  <!-- Labels -->
  <text x="70" y="42" fill="#F4F6F9" font-family="monospace" font-size="11" font-weight="bold">1</text>
  <text x="210" y="98" fill="#F4F6F9" font-family="monospace" font-size="11" font-weight="bold">2</text>
  <text x="240" y="175" fill="#F4F6F9" font-family="monospace" font-size="11" font-weight="bold">3</text>
  <text x="95" y="152" fill="#F4F6F9" font-family="monospace" font-size="11" font-weight="bold">4</text>
  <!-- Heat arrows -->
  <path d="M 120 40 L 145 68" stroke="#F2A08C" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="145" y="45" fill="#F2A08C" font-family="monospace" font-size="11">Q_in (T_H)</text>
  <path d="M 175 160 L 195 190" stroke="#68B2F8" stroke-width="2"/>
  <text x="195" y="195" fill="#68B2F8" font-family="monospace" font-size="11">Q_out (T_C)</text>
  <text x="135" y="125" fill="#E8A317" font-family="monospace" font-size="12" font-weight="bold">W_net</text>
</svg>''',

    "navier_stokes.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Boundary plates -->
  <line x1="30" y1="45" x2="290" y2="45" stroke="#8BA9C4" stroke-width="3"/>
  <line x1="30" y1="175" x2="290" y2="175" stroke="#8BA9C4" stroke-width="3"/>
  <!-- Hatching for stationary walls -->
  <path d="M 40 45 L 30 35 M 70 45 L 60 35 M 100 45 L 90 35 M 130 45 L 120 35 M 160 45 L 150 35 M 190 45 L 180 35 M 220 45 L 210 35 M 250 45 L 240 35 M 280 45 L 270 35" stroke="#4A6572" stroke-width="1.5"/>
  <path d="M 40 185 L 30 175 M 70 185 L 60 175 M 100 185 L 90 175 M 130 185 L 120 175 M 160 185 L 150 175 M 190 185 L 180 175 M 220 185 L 210 175 M 250 185 L 240 175 M 280 185 L 270 175" stroke="#4A6572" stroke-width="1.5"/>
  <!-- Parabolic velocity profile -->
  <line x1="90" y1="45" x2="90" y2="175" stroke="#4A6572" stroke-dasharray="3,3"/>
  <path d="M 90 45 Q 210 110 90 175" fill="rgba(34, 211, 238, 0.15)" stroke="#22D3EE" stroke-width="2.5"/>
  <!-- Velocity vectors -->
  <line x1="90" y1="70" x2="165" y2="70" stroke="#E8A317" stroke-width="1.5"/>
  <polygon points="165,68 172,70 165,72" fill="#E8A317"/>
  <line x1="90" y1="110" x2="210" y2="110" stroke="#E8A317" stroke-width="2"/>
  <polygon points="210,107 218,110 210,113" fill="#E8A317"/>
  <line x1="90" y1="150" x2="165" y2="150" stroke="#E8A317" stroke-width="1.5"/>
  <polygon points="165,148 172,150 165,152" fill="#E8A317"/>
  <text x="225" y="114" fill="#E8A317" font-family="monospace" font-size="12" font-weight="bold">u_max</text>
  <text x="45" y="115" fill="#8BA9C4" font-family="monospace" font-size="11">y</text>
  <text x="90" y="200" fill="#22D3EE" font-family="monospace" font-size="11">Laminar Flow: u(y) = u_max[1 - (2y/h)²]</text>
</svg>''',

    "mollier_chart.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <path d="M 40 190 L 290 190 M 40 190 L 40 25" stroke="#4A6572" stroke-width="2"/>
  <text x="280" y="208" fill="#8BA9C4" font-family="monospace" font-size="12">s (Entropy)</text>
  <text x="15" y="25" fill="#8BA9C4" font-family="monospace" font-size="12">h</text>
  <!-- Vapor dome -->
  <path d="M 50 170 Q 130 50 250 130" fill="none" stroke="#68B2F8" stroke-width="2"/>
  <text x="110" y="60" fill="#68B2F8" font-family="monospace" font-size="10">Critical Pt</text>
  <circle cx="130" cy="65" r="3" fill="#68B2F8"/>
  <!-- Constant pressure lines -->
  <path d="M 70 175 Q 160 110 280 85" fill="none" stroke="rgba(232, 163, 23, 0.4)" stroke-width="1.5"/>
  <path d="M 90 185 Q 180 135 285 115" fill="none" stroke="rgba(232, 163, 23, 0.4)" stroke-width="1.5"/>
  <text x="250" y="80" fill="#E8A317" font-family="monospace" font-size="10">P = 100 bar</text>
  <!-- Expansion line in turbine -->
  <line x1="210" y1="85" x2="210" y2="160" stroke="#F2A08C" stroke-width="2.5" stroke-dasharray="4,2"/>
  <polygon points="207,160 210,166 213,160" fill="#F2A08C"/>
  <circle cx="210" cy="85" r="4" fill="#F2A08C"/>
  <circle cx="210" cy="160" r="4" fill="#F2A08C"/>
  <text x="218" y="125" fill="#F2A08C" font-family="monospace" font-size="11" font-weight="bold">Δh_isen</text>
  <text x="50" y="208" fill="#F4F6F9" font-family="monospace" font-size="11">Mollier Diagram (Steam Tables)</text>
</svg>''',

    "mohr_circle.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <line x1="30" y1="110" x2="290" y2="110" stroke="#4A6572" stroke-width="2"/>
  <line x1="160" y1="20" x2="160" y2="200" stroke="#4A6572" stroke-width="2"/>
  <text x="275" y="105" fill="#8BA9C4" font-family="monospace" font-size="12">σ</text>
  <text x="165" y="32" fill="#8BA9C4" font-family="monospace" font-size="12">τ</text>
  <!-- Mohr's circle -->
  <circle cx="170" cy="110" r="65" fill="rgba(232, 163, 23, 0.1)" stroke="#E8A317" stroke-width="2.5"/>
  <circle cx="170" cy="110" r="3" fill="#F4F6F9"/>
  <!-- Diameter line -->
  <line x1="125" y1="65" x2="215" y2="155" stroke="#22D3EE" stroke-width="1.8"/>
  <circle cx="125" cy="65" r="4" fill="#22D3EE"/>
  <circle cx="215" cy="155" r="4" fill="#22D3EE"/>
  <!-- Labels -->
  <text x="105" y="125" fill="#F4F6F9" font-family="monospace" font-size="11">σ_2</text>
  <text x="238" y="125" fill="#F4F6F9" font-family="monospace" font-size="11">σ_1</text>
  <line x1="170" y1="110" x2="170" y2="45" stroke="#F2A08C" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="175" y="55" fill="#F2A08C" font-family="monospace" font-size="11" font-weight="bold">τ_max</text>
  <text x="50" y="205" fill="#E8A317" font-family="monospace" font-size="11">Principal Stresses &amp; Shear Planes</text>
</svg>''',

    "geneva_drive.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Driven wheel (Maltese Cross with 4 slots) -->
  <circle cx="195" cy="110" r="55" fill="rgba(104, 178, 248, 0.15)" stroke="#68B2F8" stroke-width="2"/>
  <path d="M 195 55 L 195 85 M 195 165 L 195 135 M 140 110 L 170 110 M 250 110 L 220 110" stroke="#0A1628" stroke-width="10"/>
  <path d="M 195 55 L 195 85 M 195 165 L 195 135 M 140 110 L 170 110 M 250 110 L 220 110" stroke="#E8A317" stroke-width="3"/>
  <circle cx="195" cy="110" r="8" fill="#F4F6F9"/>
  <!-- Driving disk -->
  <circle cx="95" cy="110" r="45" fill="none" stroke="#8BA9C4" stroke-width="1.5" stroke-dasharray="4,3"/>
  <circle cx="95" cy="110" r="6" fill="#8BA9C4"/>
  <!-- Driving Pin -->
  <circle cx="140" cy="110" r="6" fill="#22D3EE" stroke="#F4F6F9" stroke-width="1.5"/>
  <!-- Direction arrows -->
  <path d="M 85 60 Q 115 65 125 80" fill="none" stroke="#22D3EE" stroke-width="2"/>
  <polygon points="127,78 128,86 122,82" fill="#22D3EE"/>
  <text x="35" y="200" fill="#E8A317" font-family="monospace" font-size="12">Geneva Intermittent Drive (90° Index)</text>
</svg>''',

    "fourier_conduction.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Wall layers -->
  <rect x="90" y="40" width="60" height="130" fill="rgba(232, 163, 23, 0.15)" stroke="#E8A317" stroke-width="1.5"/>
  <rect x="150" y="40" width="70" height="130" fill="rgba(34, 211, 238, 0.15)" stroke="#22D3EE" stroke-width="1.5"/>
  <!-- Temp gradient profile -->
  <line x1="50" y1="50" x2="90" y2="50" stroke="#F2A08C" stroke-width="2"/>
  <line x1="90" y1="50" x2="150" y2="90" stroke="#F2A08C" stroke-width="2.5"/>
  <line x1="150" y1="90" x2="220" y2="155" stroke="#F2A08C" stroke-width="2.5"/>
  <line x1="220" y1="155" x2="260" y2="155" stroke="#68B2F8" stroke-width="2"/>
  <!-- Heat flux arrow -->
  <line x1="60" y1="120" x2="250" y2="120" stroke="#E8A317" stroke-width="3"/>
  <polygon points="250,115 260,120 250,125" fill="#E8A317"/>
  <text x="135" y="112" fill="#E8A317" font-family="monospace" font-size="12" font-weight="bold">q = -k A (dT/dx)</text>
  <text x="95" y="190" fill="#8BA9C4" font-family="monospace" font-size="10">k_1 (Metal)</text>
  <text x="160" y="190" fill="#8BA9C4" font-family="monospace" font-size="10">k_2 (Insulation)</text>
  <text x="45" y="42" fill="#F2A08C" font-family="monospace" font-size="11">T_hot</text>
  <text x="245" y="172" fill="#68B2F8" font-family="monospace" font-size="11">T_cold</text>
</svg>''',

    "euler_buckling.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Supports -->
  <circle cx="160" cy="35" r="6" fill="#8BA9C4"/>
  <circle cx="160" cy="185" r="6" fill="#8BA9C4"/>
  <!-- Deflected column -->
  <line x1="160" y1="35" x2="160" y2="185" stroke="#4A6572" stroke-dasharray="3,3" stroke-width="1.5"/>
  <path d="M 160 35 Q 225 110 160 185" fill="none" stroke="#22D3EE" stroke-width="3"/>
  <!-- Load vectors -->
  <line x1="160" y1="10" x2="160" y2="28" stroke="#F2A08C" stroke-width="2.5"/>
  <polygon points="156,28 160,34 164,28" fill="#F2A08C"/>
  <text x="170" y="24" fill="#F2A08C" font-family="monospace" font-size="12" font-weight="bold">P_cr</text>
  <line x1="160" y1="210" x2="160" y2="192" stroke="#F2A08C" stroke-width="2.5"/>
  <polygon points="156,192 160,186 164,192" fill="#F2A08C"/>
  <text x="170" y="208" fill="#F2A08C" font-family="monospace" font-size="12" font-weight="bold">P_cr</text>
  <!-- Deflection dimension -->
  <line x1="160" y1="110" x2="225" y2="110" stroke="#E8A317" stroke-width="1.5"/>
  <text x="180" y="105" fill="#E8A317" font-family="monospace" font-size="11">δ_max</text>
  <text x="40" y="115" fill="#8BA9C4" font-family="monospace" font-size="11">L (Length)</text>
  <text x="80" y="170" fill="#22D3EE" font-family="monospace" font-size="11">P_cr = π²EI / (KL)²</text>
</svg>''',

    "involute_gears.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Gear 1 Pitch circle -->
  <circle cx="100" cy="110" r="50" fill="none" stroke="#68B2F8" stroke-width="2" stroke-dasharray="4,2"/>
  <!-- Gear 2 Pitch circle -->
  <circle cx="210" cy="110" r="60" fill="none" stroke="#68B2F8" stroke-width="2" stroke-dasharray="4,2"/>
  <!-- Line of action (tangent at pitch point) -->
  <line x1="55" y1="65" x2="255" y2="155" stroke="#E8A317" stroke-width="2"/>
  <circle cx="150" cy="110" r="4" fill="#F4F6F9"/>
  <text x="145" y="125" fill="#F4F6F9" font-family="monospace" font-size="10">Pitch Pt</text>
  <text x="210" y="175" fill="#E8A317" font-family="monospace" font-size="11">Line of Action (φ=20°)</text>
  <!-- Centers -->
  <circle cx="100" cy="110" r="5" fill="#8BA9C4"/>
  <circle cx="210" cy="110" r="5" fill="#8BA9C4"/>
  <text x="75" y="185" fill="#22D3EE" font-family="monospace" font-size="11">Involute Meshing (Zero Backlash)</text>
</svg>''',

    "hydraulic_turbines.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- High pressure nozzle -->
  <path d="M 30 100 L 75 105 L 75 115 L 30 120 Z" fill="#4A6572" stroke="#8BA9C4" stroke-width="1.5"/>
  <!-- Water jet -->
  <rect x="75" y="108" width="60" height="4" fill="#22D3EE"/>
  <!-- Pelton bucket -->
  <path d="M 135 75 Q 160 110 135 145 Q 150 110 135 75 Z" fill="rgba(232, 163, 23, 0.2)" stroke="#E8A317" stroke-width="2"/>
  <!-- Splitter wedge -->
  <polygon points="135,110 148,105 148,115" fill="#E8A317"/>
  <!-- Deflected jet streams -->
  <path d="M 145 105 Q 165 85 130 65" fill="none" stroke="#22D3EE" stroke-width="2"/>
  <path d="M 145 115 Q 165 135 130 155" fill="none" stroke="#22D3EE" stroke-width="2"/>
  <!-- Velocity vectors -->
  <text x="65" y="98" fill="#22D3EE" font-family="monospace" font-size="11">V_1 (Jet)</text>
  <text x="180" y="80" fill="#F4F6F9" font-family="monospace" font-size="11">V_r1</text>
  <text x="180" y="145" fill="#E8A317" font-family="monospace" font-size="11">u (Bucket Speed)</text>
  <text x="50" y="195" fill="#68B2F8" font-family="monospace" font-size="11">Pelton Impulse: P = ρQ·u·(V_1 - u)(1 + k·cos β)</text>
</svg>''',

    "workshop_gdt.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- 3-jaw chuck -->
  <rect x="35" y="60" width="40" height="100" fill="#36454F" stroke="#8BA9C4" stroke-width="2"/>
  <rect x="75" y="75" width="12" height="70" fill="#4A6572"/>
  <!-- Turned workpiece -->
  <rect x="87" y="85" width="80" height="50" fill="rgba(104, 178, 248, 0.2)" stroke="#68B2F8" stroke-width="2"/>
  <rect x="167" y="95" width="70" height="30" fill="rgba(104, 178, 248, 0.3)" stroke="#68B2F8" stroke-width="2"/>
  <!-- Tool bit -->
  <polygon points="167,135 180,165 155,165" fill="#E8A317" stroke="#F4F6F9" stroke-width="1.5"/>
  <!-- Chip curl -->
  <path d="M 167 130 Q 175 120 185 125" fill="none" stroke="#F2A08C" stroke-width="2"/>
  <text x="145" y="185" fill="#E8A317" font-family="monospace" font-size="11">HSS Tool</text>
  <!-- GD&T Callout box -->
  <rect x="180" y="45" width="105" height="25" fill="#162C4D" stroke="#22D3EE" stroke-width="1.5"/>
  <text x="188" y="62" fill="#22D3EE" font-family="monospace" font-size="11">⌀25 H7 / g6 [⌖]</text>
  <text x="50" y="205" fill="#8BA9C4" font-family="monospace" font-size="11">Engine Lathe Workshop Turning</text>
</svg>''',

    "fea_meshing.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Structural bracket outline with FEA mesh -->
  <polygon points="50,45 220,45 260,120 180,175 50,175" fill="none" stroke="#22D3EE" stroke-width="2"/>
  <!-- Inner hole -->
  <circle cx="110" cy="110" r="25" fill="#0A1628" stroke="#F2A08C" stroke-width="2.5"/>
  <!-- Mesh lines (triangles) -->
  <path d="M 50 45 L 110 85 M 110 85 L 160 45 M 160 45 L 220 45 M 160 45 L 200 90 M 200 90 L 260 120 M 200 90 L 135 110 M 110 135 L 120 175 M 120 175 L 50 175 M 120 175 L 180 175 M 180 175 L 210 140 M 210 140 L 260 120 M 135 110 L 210 140" stroke="rgba(104, 178, 248, 0.4)" stroke-width="1.2"/>
  <!-- Stress concentration contour -->
  <circle cx="110" cy="110" r="35" fill="none" stroke="#F2A08C" stroke-width="1.5" stroke-dasharray="3,2"/>
  <text x="75" y="115" fill="#F2A08C" font-family="monospace" font-size="10" font-weight="bold">σ_vM max</text>
  <!-- Load arrow -->
  <line x1="260" y1="120" x2="295" y2="120" stroke="#E8A317" stroke-width="3"/>
  <polygon points="295,116 305,120 295,124" fill="#E8A317"/>
  <text x="270" y="110" fill="#E8A317" font-family="monospace" font-size="11">F_tensile</text>
  <text x="40" y="202" fill="#22D3EE" font-family="monospace" font-size="11">Non-Linear FEA Topology Meshing</text>
</svg>''',

    "mems_accelerometer.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Central proof mass -->
  <rect x="120" y="60" width="80" height="100" fill="rgba(34, 211, 238, 0.2)" stroke="#22D3EE" stroke-width="2"/>
  <!-- Moving comb fingers -->
  <rect x="80" y="75" width="40" height="8" fill="#22D3EE"/>
  <rect x="80" y="105" width="40" height="8" fill="#22D3EE"/>
  <rect x="80" y="135" width="40" height="8" fill="#22D3EE"/>
  <rect x="200" y="75" width="40" height="8" fill="#22D3EE"/>
  <rect x="200" y="105" width="40" height="8" fill="#22D3EE"/>
  <rect x="200" y="135" width="40" height="8" fill="#22D3EE"/>
  <!-- Stationary fingers -->
  <rect x="60" y="65" width="50" height="6" fill="#E8A317"/>
  <rect x="60" y="95" width="50" height="6" fill="#E8A317"/>
  <rect x="60" y="125" width="50" height="6" fill="#E8A317"/>
  <!-- Micro spring anchor -->
  <path d="M 160 30 L 160 40 L 150 45 L 170 50 L 150 55 L 160 60" fill="none" stroke="#F4F6F9" stroke-width="2"/>
  <path d="M 160 190 L 160 180 L 170 175 L 150 170 L 170 165 L 160 160" fill="none" stroke="#F4F6F9" stroke-width="2"/>
  <text x="35" y="205" fill="#E8A317" font-family="monospace" font-size="11">MEMS Comb-Finger Differential Capacitance</text>
</svg>''',

    "additive_lattice.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Octet truss lattice unit cell -->
  <polygon points="160,35 240,75 160,115 80,75" fill="rgba(104, 178, 248, 0.1)" stroke="#68B2F8" stroke-width="1.8"/>
  <polygon points="160,115 240,155 160,195 80,155" fill="rgba(104, 178, 248, 0.1)" stroke="#68B2F8" stroke-width="1.8"/>
  <line x1="80" y1="75" x2="80" y2="155" stroke="#68B2F8" stroke-width="2"/>
  <line x1="240" y1="75" x2="240" y2="155" stroke="#68B2F8" stroke-width="2"/>
  <line x1="160" y1="35" x2="160" y2="195" stroke="#E8A317" stroke-width="2"/>
  <line x1="80" y1="75" x2="240" y2="155" stroke="#22D3EE" stroke-width="1.5"/>
  <line x1="240" y1="75" x2="80" y2="155" stroke="#22D3EE" stroke-width="1.5"/>
  <!-- Laser sintering beam -->
  <line x1="260" y1="20" x2="160" y2="35" stroke="#F2A08C" stroke-width="2.5"/>
  <circle cx="160" cy="35" r="4" fill="#F2A08C"/>
  <text x="210" y="25" fill="#F2A08C" font-family="monospace" font-size="11">Laser Beam</text>
  <text x="45" y="208" fill="#E8A317" font-family="monospace" font-size="11">Direct Metal Laser Sintering (DMLS)</text>
</svg>''',

    "grid_fins.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Outer fin frame -->
  <polygon points="70,40 250,40 230,170 90,170" fill="rgba(232, 163, 23, 0.1)" stroke="#E8A317" stroke-width="2.5"/>
  <!-- Internal grid lattice -->
  <line x1="110" y1="40" x2="120" y2="170" stroke="#8BA9C4" stroke-width="1.5"/>
  <line x1="150" y1="40" x2="155" y2="170" stroke="#8BA9C4" stroke-width="1.5"/>
  <line x1="190" y1="40" x2="190" y2="170" stroke="#8BA9C4" stroke-width="1.5"/>
  <line x1="75" y1="70" x2="245" y2="70" stroke="#8BA9C4" stroke-width="1.5"/>
  <line x1="80" y1="105" x2="240" y2="105" stroke="#8BA9C4" stroke-width="1.5"/>
  <line x1="85" y1="140" x2="235" y2="140" stroke="#8BA9C4" stroke-width="1.5"/>
  <!-- Actuator hinge -->
  <circle cx="160" cy="40" r="7" fill="#22D3EE"/>
  <line x1="160" y1="15" x2="160" y2="40" stroke="#22D3EE" stroke-width="3"/>
  <text x="175" y="25" fill="#22D3EE" font-family="monospace" font-size="11">Torque Shaft</text>
  <text x="45" y="195" fill="#E8A317" font-family="monospace" font-size="11">Titanium Hypersonic Reentry Grid Fin</text>
</svg>''',

    "quadruped_linkage.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Hip joint / chassis -->
  <rect x="70" y="30" width="60" height="25" fill="#162C4D" stroke="#8BA9C4" stroke-width="2"/>
  <circle cx="100" cy="45" r="8" fill="#22D3EE"/>
  <!-- Upper leg link -->
  <line x1="100" y1="45" x2="170" y2="110" stroke="#22D3EE" stroke-width="4"/>
  <!-- Knee joint -->
  <circle cx="170" cy="110" r="9" fill="#E8A317" stroke="#F4F6F9" stroke-width="2"/>
  <!-- Lower leg link -->
  <line x1="170" y1="110" x2="130" y2="180" stroke="#22D3EE" stroke-width="3.5"/>
  <!-- Foot contact pad -->
  <circle cx="130" cy="180" r="7" fill="#F2A08C"/>
  <!-- Ground reaction force vector -->
  <line x1="130" y1="205" x2="130" y2="180" stroke="#F2A08C" stroke-width="2.5"/>
  <polygon points="126,183 130,175 134,183" fill="#F2A08C"/>
  <text x="142" y="200" fill="#F2A08C" font-family="monospace" font-size="11">F_ground</text>
  <!-- Joint angle annotations -->
  <text x="185" y="105" fill="#E8A317" font-family="monospace" font-size="11">θ_knee</text>
  <text x="45" y="205" fill="#8BA9C4" font-family="monospace" font-size="10">Inverse Kinematics: τ = J^T(q)·F</text>
</svg>''',

    "digital_twin_iot.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Rotating shaft & bearing -->
  <circle cx="95" cy="110" r="45" fill="none" stroke="#68B2F8" stroke-width="2.5"/>
  <circle cx="95" cy="110" r="25" fill="#162C4D" stroke="#8BA9C4" stroke-width="2"/>
  <circle cx="95" cy="110" r="6" fill="#F4F6F9"/>
  <!-- Accelerometer sensor on casing -->
  <rect x="85" y="55" width="20" height="14" fill="#E8A317" stroke="#F4F6F9" stroke-width="1.5"/>
  <!-- Wireless signal waves -->
  <path d="M 115 55 Q 125 50 135 55" fill="none" stroke="#22D3EE" stroke-width="2"/>
  <path d="M 118 62 Q 130 55 142 62" fill="none" stroke="#22D3EE" stroke-width="2"/>
  <!-- FFT Spectral graph -->
  <line x1="170" y1="150" x2="295" y2="150" stroke="#8BA9C4" stroke-width="1.5"/>
  <line x1="170" y1="150" x2="170" y2="60" stroke="#8BA9C4" stroke-width="1.5"/>
  <!-- Spectrum peaks -->
  <polyline points="175,148 190,145 200,85 210,147 235,148 245,65 255,148 280,146" fill="none" stroke="#22D3EE" stroke-width="2"/>
  <text x="240" y="58" fill="#F2A08C" font-family="monospace" font-size="10" font-weight="bold">BPFO Defect</text>
  <text x="175" y="165" fill="#8BA9C4" font-family="monospace" font-size="10">Frequency (Hz)</text>
  <text x="40" y="200" fill="#22D3EE" font-family="monospace" font-size="11">Predictive FFT Vibration Analytics</text>
</svg>''',

    "cfd_vortex.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Airfoil profile -->
  <path d="M 50 110 Q 110 80 180 105 Q 110 120 50 110 Z" fill="rgba(232, 163, 23, 0.2)" stroke="#E8A317" stroke-width="2"/>
  <!-- Incoming streamlines -->
  <path d="M 20 85 Q 50 85 90 75 Q 140 65 190 75" fill="none" stroke="#68B2F8" stroke-width="1.8"/>
  <path d="M 20 135 Q 50 135 90 140 Q 140 145 190 135" fill="none" stroke="#68B2F8" stroke-width="1.8"/>
  <!-- Von Karman vortex shedding in wake -->
  <circle cx="215" cy="90" r="10" fill="none" stroke="#22D3EE" stroke-width="2" stroke-dasharray="3,2"/>
  <circle cx="245" cy="120" r="14" fill="none" stroke="#F2A08C" stroke-width="2" stroke-dasharray="3,2"/>
  <circle cx="280" cy="90" r="18" fill="none" stroke="#22D3EE" stroke-width="2" stroke-dasharray="4,2"/>
  <text x="205" y="55" fill="#22D3EE" font-family="monospace" font-size="11">Vortex Shedding (St ≈ 0.21)</text>
  <text x="40" y="195" fill="#E8A317" font-family="monospace" font-size="11">LES Turbulent Boundary Layer Separation</text>
</svg>''',

    "carbon_monocoque.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Honeycomb core -->
  <path d="M 60 95 L 80 85 L 100 95 L 100 115 L 80 125 L 60 115 Z M 100 95 L 120 85 L 140 95 L 140 115 L 120 125 L 100 115 Z M 140 95 L 160 85 L 180 95 L 180 115 L 160 125 L 140 115 Z M 180 95 L 200 85 L 220 95 L 220 115 L 200 125 L 180 115 Z" fill="rgba(232, 163, 23, 0.15)" stroke="#E8A317" stroke-width="1.8"/>
  <!-- Top Carbon Skin plies [0, 45, 90] -->
  <rect x="50" y="65" width="220" height="14" fill="#1C1C1C" stroke="#22D3EE" stroke-width="1.5"/>
  <line x1="50" y1="72" x2="270" y2="72" stroke="#8BA9C4" stroke-width="1" stroke-dasharray="4,2"/>
  <!-- Bottom Carbon Skin plies -->
  <rect x="50" y="135" width="220" height="14" fill="#1C1C1C" stroke="#22D3EE" stroke-width="1.5"/>
  <line x1="50" y1="142" x2="270" y2="142" stroke="#8BA9C4" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="210" y="55" fill="#22D3EE" font-family="monospace" font-size="10">CFRP Skin [0°/±45°/90°]</text>
  <text x="210" y="165" fill="#E8A317" font-family="monospace" font-size="10">Nomex Honeycomb</text>
  <text x="40" y="200" fill="#68B2F8" font-family="monospace" font-size="11">Composite Sandwich: High Flexural Rigidity</text>
</svg>''',

    "harmonic_drive.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- Outer circular spline (rigid, round) -->
  <circle cx="160" cy="110" r="70" fill="none" stroke="#68B2F8" stroke-width="3"/>
  <!-- Flexspline (elliptically deflected) -->
  <ellipse cx="160" cy="110" rx="66" ry="54" fill="rgba(34, 211, 238, 0.15)" stroke="#22D3EE" stroke-width="2.5"/>
  <!-- Elliptical wave generator -->
  <ellipse cx="160" cy="110" rx="48" ry="36" fill="#162C4D" stroke="#E8A317" stroke-width="2"/>
  <!-- Central input hub -->
  <circle cx="160" cy="110" r="12" fill="#E8A317"/>
  <!-- Meshing zone indicators at major axis -->
  <circle cx="94" cy="110" r="4" fill="#F2A08C"/>
  <circle cx="226" cy="110" r="4" fill="#F2A08C"/>
  <text x="232" y="114" fill="#F2A08C" font-family="monospace" font-size="10">Mesh Pt</text>
  <text x="50" y="195" fill="#22D3EE" font-family="monospace" font-size="11">Zero-Backlash Strain Wave Gear (100:1)</text>
</svg>''',

    "lidar_mechatronics.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <rect width="320" height="220" fill="#0A1628" rx="8"/>
  <!-- LIDAR sensor housing -->
  <rect x="60" y="80" width="50" height="70" fill="#162C4D" stroke="#8BA9C4" stroke-width="2" rx="4"/>
  <rect x="70" y="90" width="30" height="25" fill="#0A1628" stroke="#22D3EE" stroke-width="1.5"/>
  <!-- Laser pulse rays spreading outward -->
  <line x1="100" y1="100" x2="270" y2="40" stroke="#22D3EE" stroke-width="1.8"/>
  <line x1="100" y1="102" x2="280" y2="75" stroke="#22D3EE" stroke-width="1.8"/>
  <line x1="100" y1="105" x2="260" y2="120" stroke="#22D3EE" stroke-width="1.8"/>
  <line x1="100" y1="108" x2="275" y2="160" stroke="#22D3EE" stroke-width="1.8"/>
  <!-- 3D Point cloud targets -->
  <circle cx="270" cy="40" r="3" fill="#E8A317"/>
  <circle cx="280" cy="75" r="3" fill="#E8A317"/>
  <circle cx="260" cy="120" r="4" fill="#F2A08C"/>
  <circle cx="275" cy="160" r="3" fill="#E8A317"/>
  <text x="180" y="180" fill="#E8A317" font-family="monospace" font-size="10">Point Cloud: [x,y,z,I]</text>
  <text x="40" y="198" fill="#22D3EE" font-family="monospace" font-size="11">Time-of-Flight LIDAR Sensor Fusion</text>
</svg>'''
}

for fname, content in svg_content.items():
    file_path = ASSETS_DIR / fname
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"✓ Saved {fname}")

print(f"All {len(svg_content)} SVGs generated successfully!")
