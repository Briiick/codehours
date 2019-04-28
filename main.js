function getAddHours() {
    // On Click [Add Hours] => return the number in the input box
    // if button is clicked
    // send the number in the input field
    // by returning it
    var input_hours = document.getElementById('add_hours').value;
    return Number(input_hours);
}

function getHours() {
    fetch('http://localhost:5000')
        .then(response => {
            return response.json();
        })
        .then(json => {
            console.log(json.hours);
            document.getElementsByClassName('goal')[0].innerHTML = json.hours;
            document.getElementById('amount').style.height = `${json.hours}%`
        });
}

function updateHours() {
    hours = getAddHours();
    fetch(`http://localhost:5000/update?hours=${hours}`)
        .then(response => {
            return response.json();
        })
        .then(json => {
            console.log(json.hours);
            document.getElementsByClassName('goal')[0].innerHTML = json.hours;
            document.getElementById('amount').style.height = `${json.hours}%`;
        });
}

window.onload = getHours();