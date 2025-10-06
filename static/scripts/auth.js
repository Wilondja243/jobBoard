let currentRole = 'candidate';

function selectRole(button, role) {
    currentRole = role;
    document.querySelectorAll('.role-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    button.classList.add('active');
    updateRegistrationFields(role);
}

function updateRegistrationFields(role) {
    const nameField = document.getElementById('name-field');
    const name_input = document.querySelector('#name-field input');
    const name_label = document.querySelector('#name-field label');
    
    if (role === 'candidate') {
        name_input.placeholder = "Nom complet";
        name_label.textContent = "Nom complet";
    } else {
        name_input.placeholder = "Nom de l'entreprise";
        name_label.textContent = "Nom de l'entreprese";
    }
}

document.addEventListener('DOMContentLoaded', () => {
    selectRole(document.querySelector(`[data-role="${currentRole}"]`), currentRole);
});