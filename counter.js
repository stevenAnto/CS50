let counter =0;
function count(){
  counter +=1;
  document.querySelector('h1').innerHTML = counter;
  if(counter % 10===0){
    alert('Count is now ${counter}');
  }
}
//Para esperar a que cargue todo
document.addEventListener('DOMContentLoaded',function (){
  document.querySelector('button').onclick =count;

});
