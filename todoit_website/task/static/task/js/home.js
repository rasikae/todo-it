// Get the modal
var modal = document.getElementById('id01');
var modal2 = document.getElementById('id02');
var modal3 = document.getElementById('id03');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    if(event.target == modal2){
        modal2.style.display = "none";
    }
    if(event.target == modal3){
        modal3.style.display = "none";
    }
};

document.getElementById('user_pic').onclick = function(){
	document.getElementById("thedropdown").classList.toggle("show");
}