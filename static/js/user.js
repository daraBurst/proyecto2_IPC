const logout = document.getElementById('return_sign_in_btn');
const current_usr = document.getElementById('user');

logout.addEventListener('click', () =>{
    window.location="/";
});

/*
current_usr.addEventListener('click',(e) => {
    fetch('http://127.0.0.1:5000/v1/users/all').then(
        res => {
            res.json().then(
                data => {
                    console.log(data);
                    if(data.length > 0){
                        var temp = "";
                        var cont = 1;
                        //--- start for loop
                        data.forEach((x) => {
                            temp +="<tr>";
                            temp +="<th scope='row'>" + (cont) + "</th>";
                            temp +="<td>" + x.username + "</td>";
                            temp +="<td>" + x.name + "</td>";
                            temp +="<td>" + x.password + "</td></tr>";
                            cont++;
                        });
    
                        //--- end for loop
    
                        document.getElementById('data').innerHTML = temp;
                    }
                }
            )
        }
    )
});
*/