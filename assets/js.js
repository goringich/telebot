let tg=window.Telegram.WebApp
let buy = document.getElementById("buy")
let order = document.getElementById("order")
tg.expend() // open the page to full screen

buy.addEventListener("click", () => {
  document.getElementsByTagName("h1").style.display="block"
  alert("Are you sure?")
  // name input
  console.log("hello world!")
  document.getElementById("input_name").value = tg.initDataUnsafe.user.first_name+" " + tg.initData.user.last_name
})
