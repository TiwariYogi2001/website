// Skeleton Hand Cursor with Blood Drops
const skeletonCursor = document.querySelector('.skeleton-cursor');
const bloodDropsContainer = document.querySelector('.blood-drops-container');

let cursorX = 0;
let cursorY = 0;
let bloodDropInterval = null;
let lastDropTime = 0;

// mouse position tracking
document.addEventListener('mousemove', (e) => {
    cursorX = e.clientX;
    cursorY = e.clientY;

    if (!skeletonCursor) return;

    // keep the hand slightly offset so it points like a real cursor
    skeletonCursor.style.left = (cursorX) + 'px';
    skeletonCursor.style.top = (cursorY) + 'px';
});

// when hovering clickable items, slightly enlarge / tilt the hand
document.addEventListener('mouseover', (e) => {
    const target = e.target;
    if (!skeletonCursor) return;

    if (target.closest('a, button, .btn, .hamburger-menu')) {
        skeletonCursor.classList.add('active');
    }
});

document.addEventListener('mouseout', (e) => {
    const target = e.target;
    if (!skeletonCursor) return;

    if (target.closest('a, button, .btn, .hamburger-menu') === null) {
        skeletonCursor.classList.remove('active');
    }
});



// create a single blood drop with splat effect
function createBloodDrop(x, y) {
    if (window.innerWidth <= 968) return; // skip on mobile

    const drop = document.createElement('div');
    drop.className = 'blood-drop-cursor';

    // jitter the spawn so drops don't all spawn at same pixel
    const jitterX = (Math.random() - 0.5) * 8;
    const jitterY = (Math.random() - 0.5) * 6;

    drop.style.left = (x + jitterX) + 'px';
    drop.style.top = (y + jitterY) + 'px';
    drop.style.transform = `translateY(0) rotate(${(Math.random()-0.5)*20}deg)`;

    bloodDropsContainer.appendChild(drop);

    // create a tiny splat where the drop "lands" (position will be slightly below start)
    const splat = document.createElement('div');
    splat.className = 'blood-splat';

    // set splat position a bit lower than drop start, randomized
    const splatX = x + jitterX + (Math.random() - 0.5) * 12;
    const splatY = y + 60 + (Math.random() * 20);

    splat.style.left = splatX + 'px';
    splat.style.top = splatY + 'px';
    bloodDropsContainer.appendChild(splat);

    // cleanup: remove elements after animation finishes (safe generous timeout)
    setTimeout(() => {
        if (drop.parentElement) drop.parentElement.removeChild(drop);
    }, 1600);

    setTimeout(() => {
        if (splat.parentElement) splat.parentElement.removeChild(splat);
    }, 900);
}

// continuous gentle dripping while the cursor moves (interval-based)
function startBloodDripping() {
    if (bloodDropInterval) return;
    bloodDropInterval = setInterval(() => {
        // throttle drops so they aren't insane
        const now = Date.now();
        if (now - lastDropTime < 140) return;
        createBloodDrop(cursorX, cursorY + 8); // spawn slightly below the fingertip
        lastDropTime = now;
    }, 160);
}

function stopBloodDripping() {
    clearInterval(bloodDropInterval);
    bloodDropInterval = null;
}

// start drip on mouseenter to document and stop when leave window
document.addEventListener('mouseenter', startBloodDripping);
document.addEventListener('mouseleave', stopBloodDripping);

// create a smear when user mouses down (adds realism)
document.addEventListener('mousedown', (e) => {
    if (window.innerWidth <= 968) return;
    const smear = document.createElement('div');
    smear.className = 'blood-smear';

    // place smear where cursor is and give a small random rotation
    smear.style.left = (e.clientX + (Math.random()-0.5)*20) + 'px';
    smear.style.top = (e.clientY + (Math.random()-0.5)*20) + 'px';
    smear.style.transform = `translate(-50%, -50%) rotate(${(Math.random()-0.5)*25}deg)`;

    bloodDropsContainer.appendChild(smear);

    // remove after animation ends
    setTimeout(() => {
        if (smear.parentElement) smear.parentElement.removeChild(smear);
    }, 2200);
});

// Optional: reduce CPU when the tab is hidden
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        stopBloodDripping();
    } else {
        startBloodDripping();
    }
});

// Start dripping immediately when the page loads in desktop view
if (window.innerWidth > 968) startBloodDripping();


// Horror Sound Control
const soundToggle = document.getElementById('soundToggle');
let isSoundPlaying = false;
let audioContext;
let oscillator;
let gainNode;

function createHorrorSound() {
    audioContext = new (window.AudioContext || window.webkitAudioContext)();
    
    // Create a low frequency oscillator for creepy ambience
    oscillator = audioContext.createOscillator();
    gainNode = audioContext.createGain();
    
    oscillator.type = 'sine';
    oscillator.frequency.setValueAtTime(55, audioContext.currentTime); // Low A note
    
    // Create a subtle tremolo effect
    const tremolo = audioContext.createOscillator();
    tremolo.frequency.setValueAtTime(3, audioContext.currentTime);
    const tremoloGain = audioContext.createGain();
    tremoloGain.gain.setValueAtTime(0.3, audioContext.currentTime);
    
    tremolo.connect(tremoloGain);
    tremoloGain.connect(gainNode.gain);
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
    
    return { oscillator, tremolo };
}

soundToggle.addEventListener('click', () => {
    if (!isSoundPlaying) {
        const sound = createHorrorSound();
        sound.oscillator.start();
        sound.tremolo.start();
        isSoundPlaying = true;
        soundToggle.classList.remove('muted');
    } else {
        if (oscillator) {
            oscillator.stop();
            audioContext.close();
        }
        isSoundPlaying = false;
        soundToggle.classList.add('muted');
    }
});

// === Mobile Menu Toggle (replacement) ===
const hamburger = document.getElementById('hamburgerMenu');
const mobileMenu = document.getElementById('mobileMenu');
const mobileMenuOverlay = document.getElementById('mobileMenuOverlay');
const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

// Toggle function (hamburger click toggles open/close)
function toggleMobileMenu() {
    const isActive = mobileMenu.classList.contains('active');
    if (isActive) {
        mobileMenu.classList.remove('active');
        mobileMenuOverlay.classList.remove('active');
        document.body.style.overflow = '';
        hamburger.classList.remove('active');
    } else {
        mobileMenu.classList.add('active');
        mobileMenuOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
        hamburger.classList.add('active');
    }
}

// Open/close on hamburger click (toggle)
hamburger.addEventListener('click', function(e) {
    e.stopPropagation(); // prevent the document click immediately closing it
    toggleMobileMenu();
});

// Close when clicking overlay (transparent outside area)
mobileMenuOverlay.addEventListener('click', function() {
    if (mobileMenu.classList.contains('active')) {
        toggleMobileMenu();
    }
});

// Close when clicking any nav link (keep your existing behavior)
mobileNavLinks.forEach(link => {
    link.addEventListener('click', function() {
        if (mobileMenu.classList.contains('active')) {
            toggleMobileMenu();
        }
    });
});

// Close if the user clicks anywhere outside the menu (anywhere on document)
document.addEventListener('click', function(e) {
    if (!mobileMenu.contains(e.target) && !hamburger.contains(e.target)) {
        if (mobileMenu.classList.contains('active')) {
            toggleMobileMenu();
        }
    }
});

// Also stop clicks inside the menu from bubbling (so a click on menu content does not trigger document click)
mobileMenu.addEventListener('click', function(e) {
    e.stopPropagation();
});


// Smooth scroll functionality
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ 
                behavior: 'smooth', 
                block: 'start' 
            });
        }
    });
});

// Navigation scroll effect and active link
const navbar = document.getElementById('navbar');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    // Update active nav link based on scroll position
    const sections = ['home', 'about', 'skill', 'background', 'projects', 'achievement', 'contact'];
    let currentSection = '';

    sections.forEach(sectionId => {
        const section = document.getElementById(sectionId);
        if (section) {
            const rect = section.getBoundingClientRect();
            if (rect.top <= 150 && rect.bottom >= 150) {
                currentSection = sectionId;
            }
        }
    });

    // Update desktop nav
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSection}`) {
            link.classList.add('active');
        }
    });

    // Update mobile nav
    mobileNavLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSection}`) {
            link.classList.add('active');
        }
    });
});

// Mouse parallax effect for background blobs
let mouseX = 0;
let mouseY = 0;

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    
    const blob1 = document.querySelector('.blob-1');
    const blob2 = document.querySelector('.blob-2');
    const blob3 = document.querySelector('.blob-3');
    
    if (blob1) {
        blob1.style.transform = `translate(${mouseX * 0.02}px, ${mouseY * 0.02}px)`;
    }
    if (blob2) {
        blob2.style.transform = `translate(${mouseX * -0.015}px, ${mouseY * -0.015}px)`;
    }
    if (blob3) {
        blob3.style.transform = `translate(${mouseX * 0.01}px, ${mouseY * -0.01}px)`;
    }
});

// Animate elements on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            entry.target.style.transition = 'all 0.8s ease-out';
        }
    });
}, observerOptions);

// Observe all skill cards, project cards, timeline items, and achievement cards
document.querySelectorAll('.skill-card, .project-card, .timeline-item, .achievement-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(40px)';
    observer.observe(el);
});

// Add loading animation
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.8s ease-in';
        document.body.style.opacity = '1';
    }, 100);
});

// Scroll to top functionality
const backToTopLinks = document.querySelectorAll('a[href="#home"]');
backToTopLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

// Add hover effect to tech tags
document.querySelectorAll('.tech-tag').forEach(tag => {
    tag.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-2px) scale(1.05)';
    });
    
    tag.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// Skill icons rotation on hover
document.querySelectorAll('.skill-icon').forEach(icon => {
    icon.addEventListener('mouseenter', function() {
        this.style.animation = 'spin 0.5s ease-in-out';
    });
    
    icon.addEventListener('animationend', function() {
        this.style.animation = '';
    });
});

// Add CSS animation for skill icon spin
const style = document.createElement('style');
style.textContent = `
    @keyframes spin {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.1); }
        100% { transform: rotate(360deg) scale(1); }
    }
`;
document.head.appendChild(style);

// Project card hover effects
document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        const images = this.querySelectorAll('.project-image');
        images.forEach((img, index) => {
            setTimeout(() => {
                img.style.transform = 'scale(1.05)';
                img.style.transition = 'transform 0.3s ease';
            }, index * 50);
        });
    });
    
    card.addEventListener('mouseleave', function() {
        const images = this.querySelectorAll('.project-image');
        images.forEach(img => {
            img.style.transform = 'scale(1)';
        });
    });
});

// Add click effect to buttons
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function(e) {
        // Create ripple effect
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.style.position = 'absolute';
        ripple.style.borderRadius = '50%';
        ripple.style.background = 'rgba(255, 255, 255, 0.5)';
        ripple.style.transform = 'scale(0)';
        ripple.style.animation = 'ripple 0.6s ease-out';
        ripple.style.pointerEvents = 'none';
        
        this.style.position = 'relative';
        this.style.overflow = 'hidden';
        this.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    });
});

// Add ripple animation
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(rippleStyle);
// EmailJS contact form (with visible on-page success message)
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contactForm');
  const statusEl = document.getElementById('contactStatus');
  const submitBtn = document.getElementById('sendButton');

  if (!form) return;

  function showStatus(message, isSuccess = true) {
    if (!statusEl) return;

    statusEl.textContent = message;

    // Change color
    if (isSuccess) {
      statusEl.classList.remove('error');
    } else {
      statusEl.classList.add('error');
    }

    // Fade in
    statusEl.style.opacity = 1;

    // Auto fade out after 5 sec
    setTimeout(() => {
      statusEl.style.opacity = 0;
    }, 5000);
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Validate
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    // Gather fields
    const templateParams = {
      name: document.getElementById('name').value.trim(),
      email: document.getElementById('email').value.trim(),
      subject: document.getElementById('subject').value.trim(),
      message: document.getElementById('message').value.trim(),
    };

    // Button state
    submitBtn.disabled = true;
    submitBtn.textContent = "Sending...";

    // Send Email
    emailjs.send('service_e3z3alb', 'template_wiu8pvb', templateParams)
      .then(() => {
        showStatus("🎉 Your message has been sent successfully!", true);
        form.reset();

        submitBtn.disabled = false;
        submitBtn.textContent = "Send Message";
      })
      .catch(() => {
        showStatus("❌ Failed to send message. Try again later.", false);

        submitBtn.disabled = false;
        submitBtn.textContent = "Send Message";
      });
  });
});

// Add typing effect for achievement cards on view
const achievementCards = document.querySelectorAll('.achievement-card');
achievementCards.forEach((card, index) => {
    card.style.animationDelay = `${index * 0.1}s`;
});

// Add blood drip randomization
function createBloodDrips() {
    const bloodDrips = document.querySelectorAll('.blood-drip');
    bloodDrips.forEach(drip => {
        // Randomize animation duration between 3-5 seconds
        const duration = 3 + Math.random() * 2;
        drip.style.animationDuration = `${duration}s`;
    });
}
// Bottom Horror Pro — walker controller (randomized start & speeds)
(function() {
  const stage = document.getElementById('bottom-horror-pro');
  if (!stage) return;

  // select walkers
  const walkerA = stage.querySelector('.tiny-zombie.walker.a');
  const walkerB = stage.querySelector('.tiny-zombie.walker.b');

  // configuration (ms)
  const config = {
    walkerA: { duration: 16000, delayRange: [0, 2500], scale: 1.0 },
    walkerB: { duration: 11000, delayRange: [2000, 6000], scale: 0.78 }
  };

  // utility to random in range
  const rand = (min, max) => min + Math.random() * (max - min);

  function animateWalker(el, opts) {
    // randomize seed offsets
    const dur = opts.duration * (0.9 + Math.random()*0.25); // small variability
    const startDelay = rand(opts.delayRange[0], opts.delayRange[1]);

    // starting position (off-screen left)
    el.style.left = `${-240 - Math.random()*120}px`;
    el.style.opacity = (0.42 + Math.random()*0.12).toFixed(2);
    el.style.transform = `scale(${opts.scale})`;

    // set small head bob by toggling .walking class
    el.classList.add('walking');

    // schedule move using transform with translateX
    setTimeout(() => {
      // compute translate length to move across screen plus extra margin
      const screenW = window.innerWidth;
      const translateX = screenW + 520 + Math.random()*300; // variable travel
      el.style.transition = `transform ${dur}ms linear`;
      // preserve scale when animating: translateX(...) scale(...) pattern
      el.style.transform = `translateX(${translateX}px) scale(${opts.scale})`;

      // subtle footstep shadow squash loop
      const footprintInterval = setInterval(() => {
        // squash
        const shadow = el.querySelector('.tz-shadow');
        if (!shadow) { clearInterval(footprintInterval); return; }
        shadow.style.transform = 'scaleY(0.78)';
        shadow.style.opacity = '0.85';
        setTimeout(()=> {
          shadow.style.transform = 'scaleY(1)';
          shadow.style.opacity = '0.62';
        }, 140);
      }, 380);

      // cleanup after finishing travel
      const cleanupTimeout = setTimeout(() => {
        clearInterval(footprintInterval);
        // reset for next cycle: jump back to left and restart with new params
        el.style.transition = '';
        el.style.transform = `translateX(0px) scale(${opts.scale})`;
        // tiny pause before next cycle
        setTimeout(()=> animateWalker(el, opts), rand(1400, 3200));
      }, dur + 200);

      // if tab hidden, cancel timers gracefully (optional)
      document.addEventListener('visibilitychange', function onVis() {
        if (document.hidden) {
          // reduce animations by removing transition
          el.style.transition = '';
        }
      }, { once: true });

    }, startDelay);
  }

  // start both walkers
  animateWalker(walkerA, config.walkerA);
  animateWalker(walkerB, config.walkerB);

  // subtle responsive adjustment on resize (restarts walkers to recalc width)
  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
      // quickly restart walkers (stop by removing element and re-adding clone)
      [walkerA, walkerB].forEach((w)=>{
        if (!w) return;
        // reset transition to avoid stuck state
        w.style.transition = '';
        w.style.transform = '';
      });
    }, 400);
  });
})();

// Call on page load
createBloodDrips();

// Console message
console.log('%c💀 Welcome to the Horror Portfolio!', 'font-size: 20px; font-weight: bold; color: #8b0000;');
console.log('%c🔥 Built with passion and dark magic', 'font-size: 14px; color: #ff4500;');
console.log('%c⚡ Yogesh Tiwari - Data Analyst Portfolio', 'font-size: 12px; color: #b0b0b0;');

// Add performance logging
window.addEventListener('load', () => {
    const loadTime = performance.now();
    console.log(`%c⚡ Page loaded in ${loadTime.toFixed(2)}ms`, 'color: #ff4500; font-weight: bold;');
});