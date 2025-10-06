


window.addEventListener('DOMContentLoaded', (e)=> {
    e.preventDefault()

    let links = document.querySelectorAll('.link');
    console.log(links)
    links.forEach(link =>{
        if(window.location.href == link.href){
            console.log(window.location.href)
            link.style.cssText = "color: var(--bs-text);background: var(--bs-card-opacity)"
        }
    })

    // const modal = document.getElementById('shareModal');
    // const openBtn = document.getElementById('openShareModalBtn');
    // const closeBtn = document.getElementById('closeShareModalBtn');

    // if (modal) {
    //     openBtn.addEventListener('click', () => {
    //         modal.showModal();
    //     });

    //     closeBtn.addEventListener('click', () => {
    //         modal.close();
    //     });

    //     modal.addEventListener('click', (e) => {
    //         const dialogDimensions = modal.getBoundingClientRect();
    //         if (
    //             e.clientX < dialogDimensions.left ||
    //             e.clientX > dialogDimensions.right ||
    //             e.clientY < dialogDimensions.top ||
    //             e.clientY > dialogDimensions.bottom
    //         ) {
    //             modal.close();
    //         }
    //     });
    // }
})