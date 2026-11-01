// Landing page behaviour: navigation, name search, hero tags, face grid, reveals.
(function () {
  "use strict";

  const people = window.YEARBOOK_PEOPLE || [];
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Name search ---------- */
  const normalise = (s) =>
    s.toLowerCase()
      .replace(/\b(dr|prof|shri|miss|mr|mrs|l & t member)\b\.?/g, " ")
      .replace(/[^a-z\s]/g, " ")
      .replace(/\s+/g, " ")
      .trim();

  const indexed = people.map((p) => ({ ...p, key: normalise(p.name) }));

  function findPeople(query) {
    const q = normalise(query);
    if (!q) return [];
    const exact = indexed.filter((p) => p.key === q);
    if (exact.length) return exact;
    const terms = q.split(" ");
    return indexed.filter((p) => terms.every((t) => p.key.split(" ").some((w) => w.startsWith(t))));
  }

  function viewerUrl(query, matches) {
    const base = "index.html?q=" + encodeURIComponent(query);
    return matches.length === 1 ? base + "#person=" + matches[0].id : base;
  }

  const datalist = document.getElementById("peopleList");
  if (datalist) {
    datalist.innerHTML = people.map((p) => `<option value="${p.name}"></option>`).join("");
  }

  document.querySelectorAll("[data-find-form]").forEach((form) => {
    const input = form.querySelector("input");
    const error = form.querySelector(".form-error");

    const setError = (msg) => {
      error.textContent = msg;
      if (msg) {
        form.setAttribute("data-invalid", "");
        input.setAttribute("aria-invalid", "true");
      } else {
        form.removeAttribute("data-invalid");
        input.removeAttribute("aria-invalid");
      }
    };

    input.addEventListener("input", () => setError(""));

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const value = input.value.trim();
      if (value.length < 2) {
        setError("Type at least 2 letters of a name.");
        input.focus();
        return;
      }
      const matches = findPeople(value);
      if (!matches.length) {
        setError(`No one named "${value}" is in the 1991 photo. Try a surname, like Gupta.`);
        input.focus();
        return;
      }
      window.location.href = viewerUrl(value, matches);
    });
  });

  /* ---------- Navigation ---------- */
  const toggle = document.querySelector(".menu-toggle");
  const menu = document.getElementById("mobileMenu");

  function setMenu(open) {
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    document.body.style.overflow = open ? "hidden" : "";
    if (open) {
      menu.hidden = false;
      const items = menu.querySelectorAll("li");
      const step = Math.min(60, 400 / Math.max(items.length, 1));
      items.forEach((li, i) => { li.style.transitionDelay = `${i * step}ms`; });
      requestAnimationFrame(() => menu.classList.add("is-open"));
    } else {
      menu.classList.remove("is-open");
      menu.querySelectorAll("li").forEach((li) => { li.style.transitionDelay = "0ms"; });
      setTimeout(() => { if (!menu.classList.contains("is-open")) menu.hidden = true; }, 300);
    }
  }

  if (toggle && menu) {
    toggle.addEventListener("click", () => setMenu(toggle.getAttribute("aria-expanded") !== "true"));
    menu.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => setMenu(false)));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") setMenu(false); });
  }

  // Current section indicator in the nav
  const navLinks = document.querySelectorAll(".nav-links a");
  const sectionIO = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      navLinks.forEach((a) => {
        const on = a.getAttribute("href") === "#" + entry.target.id;
        a.classList.toggle("is-current", on);
        if (on) a.setAttribute("aria-current", "location"); else a.removeAttribute("aria-current");
      });
    });
  }, { rootMargin: "-45% 0px -50% 0px" });
  ["photo", "how", "faq"].forEach((id) => {
    const el = document.getElementById(id);
    if (el) sectionIO.observe(el);
  });

  /* ---------- Hero name tags ---------- */
  const stage = document.querySelector("[data-hero-stage]");
  const tagIds = ["std1-01", "sit-08", "std1-16"];
  if (stage) {
    tagIds.forEach((id, i) => {
      const p = people.find((x) => x.id === id);
      if (!p) return;
      const tag = document.createElement("a");
      tag.className = "face-tag";
      tag.href = "index.html#person=" + p.id;
      tag.style.left = p.x + "%";
      tag.style.top = p.y + "%";
      tag.setAttribute("aria-label", `See ${p.name} in the photo viewer`);
      const shortName = p.name.replace(/^(Dr\.|Prof\.|Shri|Miss\.?)\s*/, "");
      tag.innerHTML = `<span class="face-label">${shortName}</span><span class="face-ring"></span>`;
      if (p.x < 15) tag.querySelector(".face-label").style.left = "0";
      if (p.x > 85) tag.querySelector(".face-label").style.right = "0";
      stage.appendChild(tag);
      setTimeout(() => tag.classList.add("is-on"), reduceMotion ? 0 : 600 + i * 400);
    });
  }

  /* ---------- Faces grid ---------- */
  const grid = document.querySelector("[data-face-grid]");
  const shortRow = {
    "Sitting (Front Row)": "Seated",
    "Standing (1st Row)": "First row",
    "Standing (2nd Row)": "Second row",
    "Standing (3rd Row)": "Back row",
  };

  function renderGrid(row) {
    const list = row === "all" ? people : people.filter((p) => p.row === row);
    if (!list.length) {
      grid.innerHTML = `<li class="face-meta">No faces in this row yet.</li>`;
      return;
    }
    grid.innerHTML = list.map((p) => `
      <li>
        <a class="face-card" href="index.html#person=${p.id}">
          <img src="assets/avatars/${p.id}.jpg" alt="${p.name}, 1991" loading="lazy" width="100" height="100">
          <span class="face-name">${p.name}</span>
          <span class="face-meta">${shortRow[p.row] || p.row}, #${p.pos}</span>
        </a>
      </li>`).join("");
  }

  if (grid) {
    renderGrid("all");
    document.querySelectorAll(".row-tabs .chip").forEach((chip) => {
      chip.addEventListener("click", () => {
        document.querySelectorAll(".row-tabs .chip").forEach((c) => {
          c.classList.toggle("is-active", c === chip);
          c.setAttribute("aria-selected", String(c === chip));
        });
        renderGrid(chip.dataset.row);
      });
    });
  }

  /* ---------- Section reveals (B7) ---------- */
  const revealIO = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll(".reveal").forEach((el) => revealIO.observe(el));

  /* ---------- Tagline word reveal (B11) ---------- */
  const tagline = document.querySelector("[data-tagline]");
  if (tagline) {
    const accentWords = new Set(["redrawn.", "invented."]);
    const words = tagline.textContent.trim().split(/\s+/);
    tagline.innerHTML = words
      .map((w) => `<span class="word${accentWords.has(w) ? " is-accent" : ""}">${w}</span>`)
      .join(" ");
    const spans = Array.from(tagline.querySelectorAll(".word"));

    if (reduceMotion) {
      spans.forEach((s) => s.classList.add("is-lit"));
    } else {
      // Words that cross the trigger line together light up one after another.
      let queue = [];
      let timer = null;
      const flush = () => {
        const next = queue.shift();
        if (next) next.classList.add("is-lit");
        timer = queue.length ? setTimeout(flush, 90) : null;
      };
      const wordIO = new IntersectionObserver((entries, obs) => {
        entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => spans.indexOf(a.target) - spans.indexOf(b.target))
          .forEach((e) => { queue.push(e.target); obs.unobserve(e.target); });
        if (!timer && queue.length) flush();
      }, { rootMargin: "0px 0px -35% 0px" });
      spans.forEach((s) => wordIO.observe(s));
    }
  }

  /* ---------- 35-Year Mechanical Timeline (1987-2026) ---------- */
  const milestonesGrid = document.getElementById("milestonesGrid");
  const landingMilestoneModal = document.getElementById("landingMilestoneModal");
  const closeLandingMilestoneBtn = document.getElementById("closeLandingMilestoneBtn");
  const landingMilestoneEra = document.getElementById("landingMilestoneEra");
  const landingMilestoneTitle = document.getElementById("landingMilestoneTitle");
  const landingMilestoneCategory = document.getElementById("landingMilestoneCategory");
  const landingMilestoneSvg = document.getElementById("landingMilestoneSvg");
  const landingMilestoneFormula = document.getElementById("landingMilestoneFormula");
  const landingMilestoneDesc = document.getElementById("landingMilestoneDesc");
  const landingMilestoneMemory = document.getElementById("landingMilestoneMemory");

  if (milestonesGrid) {
    let allMilestones = [];

    const renderMilestones = (items) => {
      milestonesGrid.innerHTML = items.map((m) => `
        <article class="milestone-card" data-id="${m.id}">
          <img class="milestone-card-img" src="${m.svg}" alt="${m.title}" loading="lazy">
          <div class="milestone-card-meta">
            <span>${m.year}</span>
            <span>${m.category}</span>
          </div>
          <div class="milestone-card-title">${m.title}</div>
          <div class="milestone-card-formula">${m.formula}</div>
        </article>
      `).join("");

      milestonesGrid.querySelectorAll(".milestone-card").forEach((card) => {
        card.addEventListener("click", () => {
          const m = allMilestones.find((x) => x.id === card.dataset.id);
          if (!m || !landingMilestoneModal) return;
          landingMilestoneEra.textContent = m.era;
          landingMilestoneTitle.textContent = m.title;
          landingMilestoneCategory.textContent = `${m.category} • ${m.year}`;
          landingMilestoneSvg.src = m.svg;
          landingMilestoneSvg.alt = m.title;
          landingMilestoneFormula.textContent = m.formula;
          landingMilestoneDesc.textContent = m.description;
          landingMilestoneMemory.textContent = `"${m.memory}"`;
          landingMilestoneModal.classList.add("open");
        });
      });
    };

    if (closeLandingMilestoneBtn) {
      closeLandingMilestoneBtn.addEventListener("click", () => {
        landingMilestoneModal.classList.remove("open");
      });
    }
    if (landingMilestoneModal) {
      landingMilestoneModal.addEventListener("click", (e) => {
        if (e.target === landingMilestoneModal) landingMilestoneModal.classList.remove("open");
      });
    }

    // Filter tabs
    const timelineTabs = document.querySelectorAll(".timeline-tabs .chip");
    timelineTabs.forEach((tab) => {
      tab.addEventListener("click", () => {
        timelineTabs.forEach((t) => {
          t.classList.remove("is-active");
          t.setAttribute("aria-selected", "false");
        });
        tab.classList.add("is-active");
        tab.setAttribute("aria-selected", "true");
        const era = tab.dataset.era;
        if (era === "foundations") {
          renderMilestones(allMilestones.filter((m) => m.era.includes("Foundation")));
        } else if (era === "modern") {
          renderMilestones(allMilestones.filter((m) => m.era.includes("Modern")));
        } else {
          renderMilestones(allMilestones);
        }
      });
    });

    if (window.MILESTONES_DATA && window.MILESTONES_DATA.length) {
      allMilestones = window.MILESTONES_DATA;
      renderMilestones(allMilestones);
    } else {
      fetch("data/milestones.json")
        .then((res) => res.json())
        .then((data) => {
          allMilestones = data;
          renderMilestones(data);
        })
        .catch((err) => console.warn("Failed loading milestones:", err));
    }

    /* Ambient Side Reels in Hero */
    const landingReelTrackLeft = document.getElementById("landingReelTrackLeft");
    const landingReelTrackRight = document.getElementById("landingReelTrackRight");
    const milestonesForHero = window.MILESTONES_DATA || [];
    if (landingReelTrackLeft && landingReelTrackRight && milestonesForHero.length) {
      const foundations = milestonesForHero.filter((m) => m.era.includes("Foundation"));
      const modern = milestonesForHero.filter((m) => m.era.includes("Modern"));

      const cardHtml = (m) => `
        <article class="milestone-card" data-id="${m.id}" title="${m.title}">
          <img class="milestone-card-img" src="${m.svg}" alt="${m.title}" loading="lazy">
          <div class="milestone-card-meta">
            <span>${m.year}</span>
            <span>${m.category}</span>
          </div>
          <div class="milestone-card-title">${m.title}</div>
          <div class="milestone-card-formula">${m.formula}</div>
        </article>
      `;

      landingReelTrackLeft.innerHTML = [...foundations, ...foundations].map(cardHtml).join("");
      landingReelTrackRight.innerHTML = [...modern, ...modern].map(cardHtml).join("");

      document.querySelectorAll(".hero-reels-stage .milestone-card").forEach((card) => {
        card.addEventListener("click", () => {
          const m = milestonesForHero.find((x) => x.id === card.dataset.id);
          if (!m || !landingMilestoneModal) return;
          landingMilestoneEra.textContent = m.era;
          landingMilestoneTitle.textContent = m.title;
          landingMilestoneCategory.textContent = `${m.category} • ${m.year}`;
          landingMilestoneSvg.src = m.svg;
          landingMilestoneSvg.alt = m.title;
          landingMilestoneFormula.textContent = m.formula;
          landingMilestoneDesc.textContent = m.description;
          landingMilestoneMemory.textContent = `"${m.memory}"`;
          landingMilestoneModal.classList.add("open");
        });
      });
    }
  }

  /* ---------- Appearance Mode Switcher (Blueprint, Heritage, Flow, Linen, Dark) ---------- */
  const THEME_KEY = "gec_theme_mode";
  function applyThemeMode(mode) {
    document.documentElement.setAttribute("data-theme-mode", mode);
    try { localStorage.setItem(THEME_KEY, mode); } catch (e) {}
    document.querySelectorAll(".appearance-pill").forEach((pill) => {
      pill.classList.toggle("active", pill.dataset.mode === mode);
    });
  }

  let savedMode = "blueprint";
  try { savedMode = localStorage.getItem(THEME_KEY) || "blueprint"; } catch (e) {}
  applyThemeMode(savedMode);

  document.addEventListener("click", (e) => {
    const pill = e.target.closest(".appearance-pill");
    if (!pill) return;
    applyThemeMode(pill.dataset.mode);
  });
})();
