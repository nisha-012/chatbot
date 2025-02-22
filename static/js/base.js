document.addEventListener("DOMContentLoaded", () => {
    const initNav = (navClass) => {
        const nav = document.querySelector(`.${navClass}`);
        if (!nav) return; // Ensure element exists

        const navLinks = nav.querySelectorAll(".nav__link");
        const slideRect = nav.querySelector(".nav__slider-rect");

        // Function to update active link based on URL
        const setActiveLink = () => {
            const currentPath = window.location.pathname;
            let activeLink = null;

            navLinks.forEach((link) => {
                if (link.getAttribute("href") === currentPath) {
                    activeLink = link;
                }
            });

            if (activeLink) {
                navLinks.forEach((item) => item.classList.remove("nav__link_active"));
                activeLink.classList.add("nav__link_active");

                // Ensure data-transform exists
                const transformValue = activeLink.dataset.transform ? parseInt(activeLink.dataset.transform) : 0;
                slideRect.style.transform = `translateX(${transformValue}%)`;
            }
        };

        // Set active link on page load
        setActiveLink();

        // Handle navigation clicks
        nav.addEventListener("click", (evt) => {
            if (!evt.target.classList.contains("nav__link")) return;

            // Allow actual navigation for valid hrefs
            if (evt.target.getAttribute("href") !== "#") {
                return;
            }

            evt.preventDefault(); // Prevent only if it's a placeholder link

            navLinks.forEach((item) => item.classList.remove("nav__link_active"));
            evt.target.classList.add("nav__link_active");

            const transformValue = evt.target.dataset.transform ? parseInt(evt.target.dataset.transform) : 0;
            slideRect.style.transform = `translateX(${transformValue}%)`;
        });
    };

    initNav("js-nav");  // Initialize first navigation
    initNav("js-nav2"); // Initialize second navigation
});
