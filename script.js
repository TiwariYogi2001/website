// Skeleton Hand Cursor with Blood Drops
const skeletonCursor = document.querySelector('.skeleton-cursor');
const bloodDropsContainer = document.querySelector('.blood-drops-container');
let cursorX = 0;
let cursorY = 0;
let bloodDropInterval;

// Track mouse movement with proper positioning
document.addEventListener('mousemove', (e) => {
    cursorX = e.clientX;
    cursorY = e.clientY;
    
    if (skeletonCursor) {
        // Position cursor with slight offset to match pointer position
        skeletonCursor.style.left = cursorX + 'px';
        skeletonCursor.style.top = cursorY + 'px';
    }
});

// Add hover effect on clickable elements
document.addEventListener('mouseover', (e) => {
    if (e.target.tagName === 'A' || e.target.tagName === 'BUTTON' || 
        e.target.classList.contains('btn') || e.target.classList.contains('hamburger-menu')) {
        if (skeletonCursor) {
            skeletonCursor.style.transform = 'translate(-15px, -10px) scale(1.1)';
        }
    }
});

document.addEventListener('mouseout', (e) => {
    if (e.target.tagName === 'A' || e.target.tagName === 'BUTTON' || 
        e.target.classList.contains('btn') || e.target.classList.contains('hamburger-menu')) {
        if (skeletonCursor) {
            skeletonCursor.style.transform = 'translate(-15px, -10px) scale(1)';
        }
    }
});

// Create continuous blood drops from cursor
function createBloodDrop() {
    if (window.innerWidth <= 968) return; // Don't create on mobile
    
    const drop = document.createElement('div');
    drop.className = 'blood-drop-cursor';
    drop.style.left = cursorX + 'px';
    drop.style.top = cursorY + 'px';
    
    bloodDropsContainer.appendChild(drop);
    
    setTimeout(() => {
        drop.remove();
    }, 1500);
}

// Start blood drops
bloodDropInterval = setInterval(createBloodDrop, 200);

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

// Mobile Menu Toggle
const hamburger = document.getElementById('hamburgerMenu');
const mobileMenu = document.getElementById('mobileMenu');
const mobileMenuOverlay = document.getElementById('mobileMenuOverlay');
const closeMenu = document.getElementById('closeMenu');
const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

function openMobileMenu() {
    hamburger.classList.add('active');
    mobileMenu.classList.add('active');
    mobileMenuOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeMobileMenu() {
    hamburger.classList.remove('active');
    mobileMenu.classList.remove('active');
    mobileMenuOverlay.classList.remove('active');
    document.body.style.overflow = '';
}

hamburger.addEventListener('click', openMobileMenu);
closeMenu.addEventListener('click', closeMobileMenu);
mobileMenuOverlay.addEventListener('click', closeMobileMenu);

// Close mobile menu when clicking a link
mobileNavLinks.forEach(link => {
    link.addEventListener('click', closeMobileMenu);
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

// Contact form submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form values
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const subject = document.getElementById('subject').value;
        const message = document.getElementById('message').value;
        
        // Show success message
        alert(`Thank you for your message, ${name}! I will get back to you soon at ${email}.`);
        
        // Reset form
        this.reset();
    });
}

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