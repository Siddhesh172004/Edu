
//  add to cart logic started
function addtocart(id, name) {
  console.log("Added " + name);
  var cart = JSON.parse(localStorage.getItem("cart"));

  if (cart) {
    if (cart[id]) {
      cart[id] = { name: name, value: cart[id].value + 1 };

    } else {
      cart[id] = { name: name, value: 1 };
    }
  } else {
    cart = { [id]: { name: name, value: 1 } };

  }
  localStorage.setItem("cart", JSON.stringify(cart));

  // logic to manipluate cart
  var cartvalue = JSON.parse(localStorage.getItem("cart"));
  console.log(Object.keys(cartvalue).length);

  document.getElementById("carthai").innerHTML =
    Object.keys(cartvalue).length;
    
  // console.log(just.length)
}
//  add to cart logic ended\

//  add to cart when page loads and fecthes the values from the local storage
var cart = JSON.parse(localStorage.getItem("cart"));
var cartvalue = JSON.parse(localStorage.getItem("cart"));
// console.log(Object.keys(cartvalue).length);

document.getElementById("carthai").innerHTML =
  Object.keys(cartvalue).length;

//  add to cart when page loads and fecthes the values from the local storage ended

// showing values in cart model code started
const additemhai=(id)=>{
  var cart = JSON.parse(localStorage.getItem("cart"));
  
 console.log("add"+cart[id].value)
cart[id]={...cart[id],value:cart[id].value+1}
localStorage.setItem("cart", JSON.stringify(cart));
 // updating cart number
cartpopupfun();

}
const removeitem=(id)=>{
  var cart = JSON.parse(localStorage.getItem("cart"));
  
 console.log("remove"+cart[id].value)

  cart[id]={...cart[id],value:cart[id].value-1}
  var slug =  cart[id].value

  if(slug<=0){
    delete cart[id]
  }

  localStorage.setItem("cart",JSON.stringify(cart))
  // updating cart number
  cartpopupfun();
}


//checkoutlogic started
const addHiddenVal=()=>{
  var input = document.getElementById("card-hidden");
  console.log(JSON.parse(localStorage.getItem("cart")))
  console.log(input)
	input.value = localStorage.getItem("cart");

}



const cartpopupfun = () => {

  // var cart1=JSON.parse(localStorage.getItem("cart")) optional if we use cart1 then we have to change the cart1[items]
  var cart = JSON.parse(localStorage.getItem("cart"));
  var cartpopkrnahai = JSON.parse(localStorage.getItem("cart"))
  var htmlstr = ""
  addHiddenVal();
  Object.keys(cartpopkrnahai).map(items => {

    htmlstr = htmlstr + " " + `<li class="list-group-item d-flex justify-content-between">${cart[items].name}<span style="cursor:pointer" onclick="additemhai(${items})">+</span><span class="badge p-2 badge-primary">${cart[items].value}</span><span style="cursor:pointer" onclick="removeitem(${items})">-</span></li>`

  })
  document.getElementById("cartpopupfun").innerHTML = htmlstr
  console.log(htmlstr)
}

const additem = (id) => {
  console.log(id)
}
  // showing values in cart model code ended


