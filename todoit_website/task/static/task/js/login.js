// <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
// $("loginid").onclick = function(){alert("clicked")};
/* global $ */
document.getElementById("loginid").onclick = function(){
	// alert("clicked");
	document.getElementById("loginfid").action("{% url 'home' %}");
};

document.getElementById("messageID").onclick = function(){
	// alert("alert.id");
	var x = document.getElementById("form");
	alert("alert.id");
	x.classList.toggle("form");
	// x.animate({height: "toggle", opacity: "toggle"}, "slow"); //should 
	alert("alert.id");

};


// $('.message a').click(function(){
//    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
// });