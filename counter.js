let counter =0;
let total=0;
function count(){
  counter +=1;
  const heading =document.querySelector('h1');
  heading.innerHTML = counter;
  if(counter % 10===0){
    total += Number(counter)
    heading.innerHTML = total;
    counter =0;
  }
}
//Para esperar a que cargue todo
//DOMContentLoaded 
document.addEventListener('DOMContentLoaded',function (){
  document.querySelector('button').addEventListener('click',count)
  //document.querySelector('button').onclick =count;

});
