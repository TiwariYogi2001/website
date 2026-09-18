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
  $$("a", nav).forEach((a) => a.addEventListener("click", () => setMenu(false)));

  /* ---------- active nav link ---------- */
  const links = new Map($$(".site-nav a[href^='#']").map((a) => [a.getAttribute("href").slice(1), a]));
  if ("IntersectionObserver" in window) {
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        links.forEach((a) => a.classList.remove("active"));
        links.get(e.target.id)?.classList.add("active");
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    links.forEach((_, id) => { const s = document.getElementById(id); if (s) spy.observe(s); });
  }

  /* ---------- reveal on scroll ---------- */
  const revealEls = $$(".case, .sql-card, .build, .timeline li, .skill-group, .cert");
  if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    revealEls.forEach((el) => el.classList.add("reveal"));
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    revealEls.forEach((el) => io.observe(el));
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

  /* ---------- footer year ---------- */
  $("#year").textContent = new Date().getFullYear();

  /* ---------- contact form (EmailJS) ---------- */
  const EMAILJS = { publicKey: "gQ0EXxX2i41Id_lLn", service: "service_e3z3alb", template: "template_wiu8pvb" };
  const form = $("#contact-form");
  const status = $("#form-status");
  const submit = $("button[type=submit]", form);
  const say = (msg, kind) => { status.textContent = msg; status.className = `form-status ${kind || ""}`; };

  if (window.emailjs) emailjs.init({ publicKey: EMAILJS.publicKey });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    let firstBad = null;
    $$("input, textarea", form).forEach((f) => {
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
    if (!window.emailjs) {
      say("The form couldn't load. Please reach me on LinkedIn instead.", "err");
      return;
    }

    submit.disabled = true;
    submit.textContent = "Sending…";
    say("");
    try {
      await emailjs.send(EMAILJS.service, EMAILJS.template, {
        name: $("#name").value, email: $("#email").value, subject: $("#subject").value, message: $("#message").value,
      });
      form.reset();
      $$("[aria-invalid]", form).forEach((f) => f.removeAttribute("aria-invalid"));
      say("Thanks — your message is on its way. I'll reply soon.", "ok");
    } catch {
      say("Something went wrong sending that. Please try again, or message me on LinkedIn.", "err");
    } finally {
      submit.disabled = false;
      submit.textContent = "Send message";
    }
  });
})();
