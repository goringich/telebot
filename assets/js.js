let tg=window.Telegram.WebApp
let buy = document.getElementById("buy")
let order = document.getElementById("order")

buy.addEventListener("click", () => {
  document.getElementsByTagName("h1").style.display="block"
  alert("Are you sure?")
  document.getElementById("input_name").value = tg.initDataUnsafe.first_name+" " + tg.initData.last_name
})