document.addEventListener('DOMContentLoaded', function() {
    const contactModal = document.getElementById('contactModal');
    const contactModalOverlay = document.getElementById('contactModalOverlay');
    const contactModalClose = document.getElementById('contactModalClose');
    const contactModalCancel = document.getElementById('contactModalCancel');
    const contactButton = document.getElementById('contact-button');

    function openContactModal() {
        contactModal.classList.add('active');
        contactModalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeContactModal() {
        contactModal.classList.remove('active');
        contactModalOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    if (contactButton) {
        contactButton.addEventListener('click', openContactModal);
    }

    if (contactModalClose) {
        contactModalClose.addEventListener('click', closeContactModal);
    }

    if (contactModalCancel) {
        contactModalCancel.addEventListener('click', closeContactModal);
    }

    if (contactModalOverlay) {
        contactModalOverlay.addEventListener('click', closeContactModal);
    }

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && contactModal.classList.contains('active')) {
            closeContactModal();
        }
    });

    if (contactButton) {
        contactButton.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        contactButton.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    }
});