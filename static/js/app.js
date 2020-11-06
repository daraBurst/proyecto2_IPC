const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener('click',() => {
    container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener('click',() => {
    container.classList.remove("sign-up-mode");
});

const register = document.getElementById('sign-up-form');
const signin = document.getElementById('sign-in-form');
const forgot_pswrd_btn = document.getElementById('forgot_pswrd');

forgot_pswrd_btn.addEventListener('click',() => {
    window.location="recover-password";
    console.log('Forgot pswrd');
});

register.addEventListener('submit', (e) =>{

    e.preventDefault();
    
    var username = document.getElementById('username-in-form').value;
    var name = document.getElementById('name-in-form').value;
    var password = document.getElementById('password-in-form').value;
    var confirm_pswrd = document.getElementById('confirm_pswrd-in-form').value;

    var object = {
        'username': username,
        'name': name,
        'password': password,
        'confirm_pswrd': confirm_pswrd
    }

    console.log(object);

    fetch('http://127.0.0.1:5000/v1/signup', {
        method: 'POST',
        body: JSON.stringify(object),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(res => res.json())
    .catch(error => console.error('Error:', error))
    .then(response => console.log('Success:', response));
});

signin.addEventListener('submit', (e) =>{
    
    e.preventDefault();
    
    var username = document.getElementById('username-s').value;
    var password = document.getElementById('password-s').value;

    var objecto = {
        'username': username,
        'password': password
    }

    console.log(objecto);

    fetch('http://127.0.0.1:5000/v1/signin', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(objecto)
    }).then(res => res.json())
    .catch(error => console.error('Error:', error))
    .then(res => console.log('Success:', res));
});