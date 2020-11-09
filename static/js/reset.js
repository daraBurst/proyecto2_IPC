const recover_pswrd = document.getElementById('recover-pswrd-form');
const return_sign_in_btn = document.getElementById('return_sign_in_btn');
let inputs = document.querySelectorAll("input.hide");

return_sign_in_btn.addEventListener('click',() => {
    window.location="home";
    console.log('Back to home');
});

recover_pswrd.addEventListener('submit', (e) =>{

    e.preventDefault();
    
    var username = document.getElementById('username').value;
    var endpoint = 'http://127.0.0.1:5000/v1/recover-password/'.concat(username);

    fetch(endpoint)
    .then(res => res.json())
    .catch(error => console.error('Error:', error))
    .then(response => {
        if (response.status == 200){
            alert('The password is: ' + response.message);

            inputs.forEach(input => input.value = '');
            document.getElementById('alert-recover-pswrd').innerHTML = "";
            
        } else {
            document.getElementById('alert-recover-pswrd').innerHTML = `${response.message}`
        }});
});
