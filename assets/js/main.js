(() => {
  "use strict";

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

  /* ---------- header: shadow on scroll, mobile menu ---------- */
  const header = $(".site-header");
  const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  const menuBtn = $(".menu-btn");
  const nav = $("#site-nav");
  const setMenu = (open) => {
    nav.classList.toggle("open", open);
    menuBtn.setAttribute("aria-expanded", String(open));
    menuBtn.textContent = open ? "Close" : "Menu";
  };
  menuBtn.addEventListener("click", () => setMenu(!nav.classList.contains("open")));

  /* ---------- reveal on scroll ---------- */
  const revealEls = $$(".card, .pillar, .exp, .skill-group, .cert, .steps li, .funnel li");
  if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    revealEls.forEach((el) => el.classList.add("reveal"));
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -6% 0px" });
    revealEls.forEach((el) => io.observe(el));
  }

  /* ---------- project filters (work.html) ---------- */
  const grid = $("#project-grid");
  if (grid) {
    const cards = $$(".card", grid);
    const buttons = $$(".filter");
    const apply = (key) => {
      buttons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.filter === key)));
      cards.forEach((c) => { c.hidden = key !== "all" && c.dataset.cat !== key; });
      if (history.replaceState) history.replaceState(null, "", key === "all" ? location.pathname : `#${key}`);
    };
    buttons.forEach((b) => b.addEventListener("click", () => apply(b.dataset.filter)));
    const initial = location.hash.slice(1);
    if (buttons.some((b) => b.dataset.filter === initial)) apply(initial);
  }

  /* ---------- SQL syntax highlighting ---------- */
  const KW = "SELECT|FROM|WHERE|JOIN|ON|GROUP|BY|ORDER|HAVING|LIMIT|AS|AND|OR|NOT|NULL|IS|DESC|ASC|OVER|PARTITION|IN|LEFT|INNER|WITH|CASE|WHEN|THEN|ELSE|END";
  const FN = "SUM|COUNT|AVG|ROUND|RANK|MIN|MAX|DENSE_RANK|ROW_NUMBER";
  const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const token = new RegExp(`(--[^\\n]*)|\\b(${FN})(?=\\s*\\()|\\b(${KW})\\b|\\b(\\d+(?:\\.\\d+)?)\\b`, "gi");
  $$("code.sql").forEach((code) => {
    const src = code.textContent;
    let out = "", last = 0;
    src.replace(token, (m, com, fn, kw, num, idx) => {
      out += esc(src.slice(last, idx));
      const cls = com ? "com" : fn ? "fn" : kw ? "kw" : "num";
      out += `<span class="${cls}">${esc(m)}</span>`;
      last = idx + m.length;
      return m;
    });
    code.innerHTML = out + esc(src.slice(last));
  });

  /* ---------- lightbox ---------- */
  const box = $("#lightbox");
  const boxImg = $("img", box);
  $$("[data-full]").forEach((btn) => {
    btn.addEventListener("click", () => {
      boxImg.src = btn.dataset.full;
      boxImg.alt = $("img", btn)?.alt || "";
      if (typeof box.showModal === "function") box.showModal();
      else window.open(btn.dataset.full, "_blank", "noopener");
    });
  });
  $(".lightbox-close", box).addEventListener("click", () => box.close());
  box.addEventListener("click", (e) => { if (e.target === box) box.close(); });

  /* ---------- count-up numbers ---------- */
  const counters = $$("[data-count]");
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const runCount = (el) => {
    const target = Number(el.dataset.count), suffix = el.dataset.suffix || "", t0 = performance.now(), dur = 1400;
    const fmt = (n) => n.toLocaleString("en-US");
    const tick = (now) => {
      const p = Math.min(1, (now - t0) / dur), eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(Math.round(target * eased)) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if (counters.length && !reduced && "IntersectionObserver" in window) {
    const co = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { runCount(e.target); co.unobserve(e.target); } });
    }, { threshold: 0.4 });
    counters.forEach((el) => co.observe(el));
  }

  /* ---------- cursor spotlight ---------- */
  if (matchMedia("(hover: hover)").matches) {
    document.addEventListener("pointermove", (e) => {
      const el = e.target.closest(".card, .pillar, .board-card");
      if (!el) return;
      const r = el.getBoundingClientRect();
      el.style.setProperty("--mx", `${e.clientX - r.left}px`);
      el.style.setProperty("--my", `${e.clientY - r.top}px`);
    }, { passive: true });
  }

  /* ---------- horror theme: cursor glow ---------- */
  const glowEl = $(".cursor-glow");
  if (glowEl && matchMedia("(hover: hover)").matches) {
    document.addEventListener("pointermove", (e) => { glowEl.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`; }, { passive: true });
  }

  /* ---------- footer year ---------- */
  $$("[data-year]").forEach((el) => { el.textContent = new Date().getFullYear(); });

  /* ---------- contact form (FormSubmit) ---------- */
  const form = $("#contact-form");
  if (!form) return;
  const TO = "yogeshtiwari8974@gmail.com";
  const status = $("#form-status");
  const submit = $("button[type=submit]", form);
  const say = (msg, kind) => { status.textContent = msg; status.className = `form-status ${kind || ""}`; };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    let firstBad = null;
    $$("input:not(#honey), textarea", form).forEach((f) => {
      f.value = f.value.trim();
      const bad = !f.checkValidity();
      f.setAttribute("aria-invalid", String(bad));
      if (bad && !firstBad) firstBad = f;
    });
    if (firstBad) {
      say(firstBad.type === "email" && firstBad.value ? "Please enter a valid email address." : "Please fill in every field.", "err");
      firstBad.focus();
      return;
    }
    const data = {
      name: $("#name").value, email: $("#email").value, subject: $("#subject").value, message: $("#message").value,
      _subject: `Portfolio enquiry: ${$("#subject").value}`, _template: "table", _captcha: "false", _honey: $("#honey").value,
    };

    submit.disabled = true;
    submit.textContent = "Sending…";
    say("");
    try {
      const res = await fetch(`https://formsubmit.co/ajax/${TO}`, {
        method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data),
      });
      const out = await res.json().catch(() => ({}));
      if (!res.ok || String(out.success) !== "true") throw new Error(out.message || `HTTP ${res.status}`);
      form.reset();
      $$("[aria-invalid]", form).forEach((f) => f.removeAttribute("aria-invalid"));
      say("Thanks — your message is on its way. I'll reply soon.", "ok");
    } catch (err) {
      // Service down or blocked — hand the visitor a pre-filled mailto so nothing is lost.
      const subject = encodeURIComponent(data.subject);
      const body = encodeURIComponent(`${data.message}\n\n— ${data.name} (${data.email})`);
      status.className = "form-status err";
      status.innerHTML = "";
      const why = err && err.message === "Failed to fetch"
        ? "Sending was blocked (an ad-blocker, VPN or network filter is stopping formsubmit.co). "
        : `Sending failed (${err && err.message ? err.message : "unknown error"}). `;
      status.append(why);
      const a = document.createElement("a");
      a.href = `mailto:${TO}?subject=${subject}&body=${body}`;
      a.textContent = "Send it from your email app instead →";
      status.append(a);
      console.warn("Form error:", err);
    } finally {
      submit.disabled = false;
      submit.textContent = "Send message";
    }
  });
})();
