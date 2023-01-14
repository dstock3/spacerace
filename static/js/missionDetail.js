let linkContainer = document.querySelector('.mission-link-container')
let links = Array.from(linkContainer.children)
if (links.length === 1) {
    links[0].classList.add('single')
}