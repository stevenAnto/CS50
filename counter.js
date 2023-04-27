if (!localStorage.getItem('counter')){
  localStorage.setItem('counter',0);

}
function count(){
  let counter= localStorage.getItem('counter');
  counter++;
  document.querySelector('h1').innerHTML = counter;
  localStorage.setItem('counter',counter);
}
//Para esperar a que cargue todo
//DOMContentLoaded 
document.addEventListener('DOMContentLoaded',function (){
  document.querySelector('h1').innerHTML=localStorage.getItem('counter');
  document.querySelector('button').addEventListener('click',count)
  //document.querySelector('button').onclick =count;

});
