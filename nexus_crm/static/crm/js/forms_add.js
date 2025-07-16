 // Обработчик для формы клиента
 function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
 
 
 document.getElementById('add-client-form').addEventListener('submit', async function(event) {
        event.preventDefault();
        const form = event.target;
        const data = new FormData(form);
        const response = await fetch(form.action, {
            method: 'POST',
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            body: data,
             credentials: 'same-origin'
        });

        if (response.ok) {
            const client = await response.json();
            const clientSelect = document.getElementById("id_client");
            const newOption = new Option(client.name, client.id, true, true);
            clientSelect.add(newOption, undefined);
            bootstrap.Modal.getInstance(document.getElementById('addClientModal')).hide();
            form.reset();
        } else {
            const errors = await response.json();
            alert(`Ошибка: ${JSON.stringify(errors.errors)}`);
        }
    });

    // Обработчик для формы услуги
    document.getElementById('add-service-form').addEventListener('submit', async function(event) {
        event.preventDefault();
        const form = event.target;
        const data = new FormData(form);
        const response = await fetch(form.action, {
            method: 'POST',
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            body: data
        });

        if (response.ok) {
            const service = await response.json();
            const serviceSelect = document.getElementById("id_service");
            const newOption = new Option(service.title, service.id, true, true);
            serviceSelect.add(newOption, undefined);
            bootstrap.Modal.getInstance(document.getElementById('addServiceModal')).hide();
            form.reset();
        } else {
            const errors = await response.json();
            alert(`Ошибка: ${JSON.stringify(errors.errors)}`);
        }
    });



    document.addEventListener('DOMContentLoaded', function() {
        // Маска для всех полей с классом phone-input
        Inputmask({ mask: "+7(999)999-99-99" }).mask(".phone-input");
    });