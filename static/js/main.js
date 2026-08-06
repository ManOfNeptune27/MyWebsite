// Smooth scroll behavior for better UX
document.querySelectorAll('a[href^="#"], a[href^="/#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        const isHomeAnchor = href.startsWith('/#');

        if (isHomeAnchor && window.location.pathname !== '/') {
            return;
        }

        e.preventDefault();
        const targetSelector = isHomeAnchor ? href.slice(1) : href;
        const target = document.querySelector(targetSelector);
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Highlight active nav link on scroll
function updateActiveNavLink() {
    const navLinks = document.querySelectorAll('.nav-links a');
    const currentPath = window.location.pathname;
    const isHomePage = currentPath === '/';
    const scrollPosition = window.scrollY + 160;
    let activeHash = '';

    navLinks.forEach(link => {
        link.classList.remove('active');
    });

    if (isHomePage) {
        document.querySelectorAll('main section[id]').forEach(section => {
            const sectionTop = section.offsetTop;
            if (sectionTop <= scrollPosition) {
                activeHash = `#${section.id}`;
            }
        });

        if (activeHash) {
            const activeLink = document.querySelector(`.nav-links a[href="/${activeHash}"]`);
            if (activeLink) {
                activeLink.classList.add('active');
                return;
            }
        }

        const homeLink = document.querySelector('.nav-links a[href="/"]');
        if (homeLink) {
            homeLink.classList.add('active');
        }
        return;
    }

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

window.addEventListener('scroll', updateActiveNavLink);

// Set active nav link on page load
document.addEventListener('DOMContentLoaded', () => {
    updateActiveNavLink();
});

// Add hover effects to favorite items
document.querySelectorAll('.favorite-item').forEach(item => {
    item.addEventListener('mouseenter', function() {
        this.style.cursor = 'pointer';
    });
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animationPlayState = 'running';
        }
    });
}, observerOptions);

document.querySelectorAll('.favorites-section, .card').forEach(el => {
    el.style.animation = 'fadeIn 0.5s ease forwards';
    el.style.animationPlayState = 'paused';
    observer.observe(el);
});
