//-------------------------------------------------------MENU LATERAL
document.addEventListener('DOMContentLoaded', function () {
    const menuHam = document.getElementById('menu-ham-svg');
    const nav = document.getElementById('nav');
    const sombra = document.getElementById('sombra');

    let menuVisible = false;  // Variable para rastrear si el menú está visible

    if (window.innerWidth <= 1000) {
        menuHam.addEventListener('click', function () {
            menuVisible = !menuVisible;  // Alternar el estado del menú al hacer clic en el icono

            if (menuVisible) {
                nav.style.display = 'flex';
                sombra.style.display = 'flex';
            } else {
                nav.style.display = 'none';
                sombra.style.display = 'none';
            }
        });
    }
});


//-------------------------------------------------------MODO OSCURO

document.addEventListener('DOMContentLoaded', function () {
    let toggle = document.getElementById('toggle');
    let label_toggle = document.getElementById('label_toggle');
    document.body.classList.toggle('dark', toggle.checked);

    // Función para cambiar el color de los elementos SVG con la clase 'svg-blanco'
    function cambiarColorSvgBlanco(color) {
        const svgsBlancos = document.querySelectorAll('.svg-blanco');
        svgsBlancos.forEach(svg => {
            svg.style.fill = color;
        });
    }

    // Función para cambiar el color de todos los elementos dentro de la clase 'menu-ham-elements'
    function cambiarColorMenuHamElements(color) {
        const menuHamElements = document.querySelectorAll('.menu-ham-elements');
        menuHamElements.forEach(element => {
            // Cambiar color del párrafo
            const parrafo = element.querySelector('p');
            if (parrafo) {
                parrafo.style.color = color;
            }

            // Cambiar color del SVG
            const svg = element.querySelector('svg');
            if (svg) {
                svg.style.fill = color;
            }

            // Cambiar color del enlace (a)
            const enlace = element.querySelector('a');
            if (enlace) {
                enlace.style.color = color;
            }

            // Cambiar color del encabezado (h1)
            const h1 = element.querySelector('h1');
            if (h1) {
                h1.style.color = color;
            }
        });
    }
    function cambiarColorMenuHamAbsolute(color, backgroundColor) {
        const menuHamAbsoluteElements = document.querySelectorAll('.menu-ham-absolute');
        menuHamAbsoluteElements.forEach(element => {
            // Cambiar color del párrafo
            const parrafo = element.querySelector('p');
            if (parrafo) {
                parrafo.style.color = color;
            }
    
            // Cambiar color del SVG
            const svg = element.querySelector('svg');
            if (svg) {
                svg.style.fill = color;
            }
    
            // Cambiar color del encabezado h3
            const h3 = element.querySelector('h3');
            if (h3) {
                h3.style.color = color;
            }
            element.style.backgroundColor = backgroundColor;
        });
    }




    

    // Función para cambiar el color de todos los elementos dentro de la clase 'seccion-opciones2'
    function cambiarColorSeccionOpciones2(color) {
        const seccionOpciones2Elements = document.querySelectorAll('.seccion-opciones2');
        seccionOpciones2Elements.forEach(element => {
            // Cambiar color del párrafo
            const parrafo = element.querySelector('p');
            if (parrafo) {
                parrafo.style.color = color;
            }

            // Cambiar color del SVG
            const svg = element.querySelector('svg');
            if (svg) {
                svg.style.fill = color;
            }
        });
    }

    // Función para cambiar el color de todos los elementos dentro de la clase 'menu-ham-elements2'
    function cambiarColorMenuHamElements2(color) {
        const menuHamElements2 = document.querySelectorAll('.menu-ham-elements2');
        menuHamElements2.forEach(element => {
            // Cambiar color del encabezado h3
            const h3 = element.querySelector('h3');
            if (h3) {
                h3.style.color = color;
            }

            // Cambiar color del encabezado h1
            const h1 = element.querySelector('h1');
            if (h1) {
                h1.style.color = color;
            }
        });
    }

    // Establecer el color negro en la carga inicial
    cambiarColorSvgBlanco('rgba(0, 0, 0, 1)');
    cambiarColorMenuHamElements('rgba(0, 0, 0, 1)'); // Cambia al color predeterminado (negro)
    cambiarColorSeccionOpciones2('rgba(0, 0, 0, 1)'); // Cambia al color predeterminado (negro)
    cambiarColorMenuHamElements2('rgba(0, 0, 0, 1)'); // Cambia al color predeterminado (negro)
    cambiarColorMenuHamAbsolute('rgba(0, 0, 0, 1)', '#fff');  // Cambia al color predeterminado (negro)
    

    toggle.addEventListener('change', (event) => {
        let checked = event.target.checked;
        document.body.classList.toggle('dark', checked);

        if (checked == true) {
            label_toggle.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" viewBox="0 0 24 24" style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;"><path d="M6.995 12c0 2.761 2.246 5.007 5.007 5.007s5.007-2.246 5.007-5.007-2.246-5.007-5.007-5.007S6.995 9.239 6.995 12zM11 19h2v3h-2zm0-17h2v3h-2zm-9 9h3v2H2zm17 0h3v2h-3zM5.637 19.778l-1.414-1.414 2.121-2.121 1.414 1.414zM16.242 6.344l2.122-2.122 1.414 1.414-2.122 2.122zM6.344 7.759 4.223 5.637l1.415-1.414 2.12 2.122zm13.434 10.605-1.414 1.414-2.122-2.122 1.414-1.414z"></path></svg>';
            cambiarColorSvgBlanco('#fff'); // Cambiar color de los elementos SVG con la clase 'svg-blanco' a blanco
            cambiarColorMenuHamElements('#fff'); // Cambiar color de todos los elementos dentro de la clase 'menu-ham-elements' a blanco
            cambiarColorSeccionOpciones2('#fff'); // Cambiar color de todos los elementos dentro de la clase 'seccion-opciones2' a blanco
            cambiarColorMenuHamElements2('#fff'); // Cambiar color de todos los elementos dentro de la clase 'menu-ham-elements2' a blanco
            document.getElementById('logo').src = 'img/logo2.PNG';

            cambiarColorMenuHamAbsolute('#fff', '#5A5D67');

        } else {
            label_toggle.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" viewBox="0 0 24 24" style="fill: rgba(4, 4, 4, 1);transform: ;msFilter:;"><path d="M12 11.807A9.002 9.002 0 0 1 10.049 2a9.942 9.942 0 0 0-5.12 2.735c-3.905 3.905-3.905 10.237 0 14.142 3.906 3.906 10.237 3.905 14.143 0a9.946 9.946 0 0 0 2.735-5.119A9.003 9.003 0 0 1 12 11.807z"></path></svg>';
            cambiarColorSvgBlanco('rgba(0, 0, 0, 1)'); // Cambiar color de los elementos SVG con la clase 'svg-blanco' a negro (u otro color que desees)
            cambiarColorMenuHamElements('rgba(0, 0, 0, 1)'); // Cambiar color de todos los elementos dentro de la clase 'menu-ham-elements' a negro (u otro color que desees)
            cambiarColorSeccionOpciones2('rgba(0, 0, 0, 1)'); // Cambiar color de todos los elementos dentro de la clase 'seccion-opciones2' a negro (u otro color que desees)
            cambiarColorMenuHamElements2('rgba(0, 0, 0, 1)'); // Cambiar color de todos los elementos dentro de la clase 'menu-ham-elements2' a negro (u otro color que desees)
            document.getElementById('logo').src = 'img/logo.PNG';
            cambiarColorMenuHamAbsolute('rgba(0, 0, 0, 1)', '#fff');
        }
    });
});



//--------------------VENTANA EMERGENTE---------------------
document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('modal');
    modal.style.display = 'block';

    const closeModalBtn = document.getElementById('closeModalBtn');
    closeModalBtn.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});

//-----------------------------EJEMPLO DE CARRUSEL

document.addEventListener('DOMContentLoaded', function () {
    const wrapper = document.getElementById('carouselWrapper');
    const slides = document.querySelectorAll('.ventas1');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
  
    // Clonar las primeras secciones y agregarlas al final
    const clonedSlides = [...slides].map(slide => slide.cloneNode(true));
    wrapper.append(...clonedSlides);
  
    let currentIndex = 0;
  
    function updateCarousel() {
        wrapper.style.transform = `translateX(${-currentIndex * (270 + 20)}px)`;
    }
  
    function nextSlide() {
        currentIndex++;
        if (currentIndex >= slides.length + 1) {
            currentIndex = 0;
        }
        updateCarousel();
    }
  
    function prevSlide() {
        currentIndex--;
        if (currentIndex < 0) {
            currentIndex = slides.length;
        }
        updateCarousel();
    }
  
    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);
  
    updateCarousel();
  });
  