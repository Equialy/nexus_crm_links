 // Обработчик для формы клиента
    document.getElementById('add-client-form').addEventListener('submit', async function(event) {
        event.preventDefault();
        const form = event.target;
        const data = new FormData(form);
        const response = await fetch(form.action, {
            method: 'POST',
            headers: {'X-CSRFToken': data.get('csrfmiddlewaretoken')},
            body: data
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
            headers: {'X-CSRFToken': data.get('csrfmiddlewaretoken')},
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