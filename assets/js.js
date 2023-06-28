let tg = window.Telegram.WebApp
let buy = document.getElementById("buy")
let order = document.getElementById("order")
let error= document.getElementById("input_error")
error.style.display="none"
tg.expand() // open the page to full screen
// name input
document.getElementById("input_name").value = tg.initDataUnsafe.user.first_name
document.getElementById("input_surname").value = tg.initDataUnsafe.user.last_name

buy.addEventListener("click", () => {
  document.getElementsByTagName("h1")[0].style.display="block"

  a=["name","surname",'text','mail',"phone"]
  for (i in a){
    if (document.getElementById("input"+i).value.length<=2){
      error.innerText = "Error in" + i
      error.display="block"
    }
      
  }

  let data = {
    name: name + surname,
    email: mail,
    phone: phone,
    mail: mail
  } 
  tg.sendData(JSON.stringify(data)) //make a string 

  tg.close()
  alert("Are you sure?")
})
