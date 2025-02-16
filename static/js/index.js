


document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('.delete').forEach((link)=>{
        link.addEventListener('click',function(e){
            e.preventDefault();
            let res=confirm('Are you sure you want to delete');
            if(res){
                window.location.href=link.href;
            }
        })
    })
});

