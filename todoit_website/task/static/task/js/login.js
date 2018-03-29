document.getElementById("loginid").onclick = function(){
	document.getElementById("loginfid").action("{% url 'home' %}");
};

document.getElementById("signinID").onclick = function(){
	var r = document.getElementById("register");
	var l = document.getElementById("loginfid");

	r.style.display = "none"
	l.style.display = "block";
};

document.getElementById("registerID").onclick = function(){
	var r = document.getElementById("register");
	var l = document.getElementById("loginfid");

	l.style.display = "none"
	r.style.display = "block";
};