var myHeaders = new Headers();
myHeaders.append("apikey", "LZqfG4sJMMkZm3NmAiAojwWo0IeIlbeo");

var requestOptions = {
  method: 'GET',
  redirect: 'follow',
  headers: myHeaders
};

let objetor;
fetch("https://api.apilayer.com/exchangerates_data/convert?to=GBP&from=EUR&amount=24", requestOptions)
  .then(response => response.json())
  .then(data=>{
    console.log(data)
    objetor=data
    const resultado =data.result;
    document.querySelector('body').innerHTML=`1 ${data.query.from} to ${data.query.to} is ${data.result}` 
  })
  .catch(error => console.log('error', error));

