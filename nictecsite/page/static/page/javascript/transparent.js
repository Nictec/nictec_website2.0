/**
 * Listen to scroll to change header opacity class
 */  
 
(function (){
    var scrolled = false;
    function winload(event){
        window.removeEventListener('load', winload);
        window.addEventListener('scroll', onscroll);
    } 
   
    
    function onscroll(event){
        if(event.pageY > 90 && !scrolled){
            scrolled = true; 
            console.log(scrolled)
            document.querySelector('#navbar').classList.add("scrolled"); 
     
        } else if(event.pageY == 0){
            scrolled = false; 
            document.querySelector('#navbar').classList.remove("scrolled");
        }
    }
    
    window.addEventListener('load', winload);
})();
