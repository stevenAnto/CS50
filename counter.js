let counter =0;
function count(){
  counter ++;
  document.querySelector('h1').innerHTML = counter;
}
//Para esperar a que cargue todo
//DOMContentLoaded 
document.addEventListener('DOMContentLoaded',function (){
  document.querySelector('button').addEventListener('click',count)
  setInterval(count,1000);
  //document.querySelector('button').onclick =count;

});
