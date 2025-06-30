
document.addEventListener('DOMContentLoaded', function() {
  const input = document.getElementById('id_photo');
  const preview = document.querySelector('.profile-image');
  if (input && preview) {
    input.addEventListener('change', function() {
      const [file] = input.files;
      if (file) {
        preview.src = URL.createObjectURL(file);
      }
    });
  }
});
