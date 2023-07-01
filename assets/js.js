let tg = window.Telegram.WebApp
let buy = document.getElementById("buy")
let order = document.getElementById("order")
let error= document.getElementById("input_error")
error.style.display="none"
tg.expand() // open the page to full screen
// name input

buy.addEventListener("click", () => {
  const name = document.getElementById("input_name").value;
  const surname = document.getElementById("input_surname").value;
  const mail = document.getElementById("input_mail").value;
  const phone = document.getElementById("input_phone").value;
  document.getElementsByTagName("h1")[0].style.display = "block";

  // Input validation
  if (name.length <= 2 || surname.length <= 2 || mail.length <= 2 || phone.length <= 2) {
    error.innerText = "Error: Please fill in all fields with at least 3 characters.";
    error.style.display = "block";
    return;
  }

  let data = {
    name: name + " " + surname,
    phone: phone,
    mail: mail
  } 
  tg.sendData(JSON.stringify(data)) //make a string 

  tg.close()
  alert("Are you sure?")
})
