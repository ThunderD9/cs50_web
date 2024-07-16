

if (!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0)
}
function z(){
    document.querySelector('h1').innerHTML = 0;
    localStorage.setItem('counter', 0)
}
function count(){
    let counter = localStorage.getItem('counter');
    counter++ ;
    const heading = document.querySelector('h1');
    heading.innerHTML = counter;
    localStorage.setItem('counter', counter)
}



// For event listening
document.addEventListener('DOMContentLoaded', function(){ 
    //loads all the page and runs so we can avoid the inability to run written in the bottom lines
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
    document.querySelector('#zero').onclick = z;

    setInterval(count, 100); //run count function for every one second
});