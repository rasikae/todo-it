// <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
// $("loginid").onclick = function(){alert("clicked")};
/* global $ */
document.getElementById("loginid").onclick = function(){
	// alert("clicked");
	document.getElementById("loginfid").action("{% url 'home' %}");
};

document.getElementById("signinID").onclick = function(){
	var r = document.getElementById("register");
	var l = document.getElementById("loginfid");

	r.style.display = "none"
	l.style.display = "block";
};

document.getElementById("createID").onclick = function(){
	var r = document.getElementById("register");
	var l = document.getElementById("loginfid");

	l.style.display = "none"
	r.style.display = "block";
};

// $('.message a').click(function(){
//    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
// });