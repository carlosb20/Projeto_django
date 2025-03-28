

document.getElementById('meuForm').addEventListener('submit',function(event){
    event.preventDefault()

    let formData = new FormData(this);

    fetch("{% url 'index' %}", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": "{{ csrf_token }}"  // Adiciona o CSRF Token
        }
    })
   
});








