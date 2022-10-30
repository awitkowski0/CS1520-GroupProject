accountMenuOptions = [
    "my_posts", "account_details", "settings"
]

function manageMenu(selected) {
    for (let i = 0; i < accountMenuOptions.length; i++){
        if (accountMenuOptions[i] == selected) {
            document.getElementById(accountMenuOptions[i] + '_button').style.fontWeight = 'bold';
            document.getElementById(accountMenuOptions[i]).style.display = 'block';
        } else {
            document.getElementById(accountMenuOptions[i] + '_button').style.fontWeight = 'normal';
            document.getElementById(accountMenuOptions[i]).style.display = 'none';
        }
    }
}