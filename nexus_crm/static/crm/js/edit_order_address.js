<script>
document.getElementById('edit-address-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    const response = await fetch(form.action, {
        method: 'POST',
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
        },
        body: formData
    });

    if (response.ok) {
        const data = await response.json();
        // Обнови блок с адресом на странице
        document.getElementById('order-address').innerText = data.address;
        bootstrap.Modal.getInstance(document.getElementById('editAddressModal')).hide();
    } else {
        const errorData = await response.json();
        alert(`Ошибка: ${JSON.stringify(errorData.errors)}`);
    }
});
</script>
