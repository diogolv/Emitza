// Arquivo: static/js/script.js (VERSÃO FINAL E OTIMIZADA)

document.addEventListener('DOMContentLoaded', () => {

    // --- LÓGICA PARA O MENU HAMBÚRGUER ---
    const menuToggle = document.getElementById('menu-toggle');
    const mainNav = document.getElementById('main-nav');
    
    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', () => {
            mainNav.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });
    }

    // --- LÓGICA PARA AS ABAS (TABS) ---
    const tabContainers = document.querySelectorAll('.services-section');

    tabContainers.forEach(container => {
        const tabButtons = container.querySelectorAll('.tab-button');
        const tabContents = container.querySelectorAll('.tab-content');

        if (tabButtons.length > 0 && tabContents.length > 0) {
            tabButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const targetTabId = button.dataset.tab;
                    const targetContent = container.querySelector(`#${targetTabId}`);

                    tabButtons.forEach(btn => btn.classList.remove('active'));
                    tabContents.forEach(content => content.classList.remove('active'));

                    button.classList.add('active');
                    if (targetContent) {
                        targetContent.classList.add('active');
                    }
                });
            });
        }
    });

    // --- INICIALIZAÇÃO DAS ANIMAÇÕES (AOS) ---
    // MOVEMOS ESTE CÓDIGO PARA DENTRO DO DOMContentLoaded
    try {
        AOS.init({
            duration: 800, // Duração da animação em milissegundos
            once: false,    // A animação acontece apenas uma vez
        });
    } catch (e) {
        console.log('AOS não pôde ser inicializado. Verifique se a biblioteca está sendo carregada corretamente.');
    }

});