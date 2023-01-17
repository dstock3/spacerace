const timelineItems = document.querySelectorAll('.timeline-item');

timelineItems.forEach(item => {
    item.addEventListener('click', e => {
        const anchor = item.querySelector('a');
        const href = anchor.getAttribute('href');
        window.location.href = href;
    });
});