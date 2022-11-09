accountMenuOptions = [
    "my_posts", "account_details", "settings"
]

function manageMenu(selected) {
    for (let i = 0; i < accountMenuOptions.length; i++){
        if (accountMenuOptions[i] == selected) {
            document.getElementById(accountMenuOptions[i] + '_button').style.fontWeight = 'bold';
            document.getElementById(accountMenuOptions[i]).style.display = 'block';
            if (selected == 'my_posts') {
                MyPostsDefault();
            }
        } else {
            document.getElementById(accountMenuOptions[i] + '_button').style.fontWeight = 'normal';
            document.getElementById(accountMenuOptions[i]).style.display = 'none';
        }
    }
}

function MyPostsDefault() {
    el = document.getElementById('content-8');
    if (el != null && el.textContent.trim() === '') {
        el.innerHTML = '<p class="no_posts">No posts yet. Make your first post today! </p>';
    }
}

window.onload = (event) => {
    MyPostsDefault();
}

// repeat password validation in sign-up form
function matchPassword() {  
    var pw1 = document.getElementById("pswd1").value;  
    var pw2 = document.getElementById("pswd2").value;  
    if(pw1 != pw2) {  
        document.getElementById("message2").innerHTML = "**Passwords do not match! Please re-enter your password again.";  
    } 
    else {  
        alert ("Your password created successfully");  
        document.write("Your account has been created successfully");  
    }
}  

