// alert("Today is");

// $("loginid").onclick = function(){alert("clicked")};

document.getElementById("loginid").onclick = function(){
	// alert("clicked");
	document.getElementById("loginfid").action("{% url 'home' %}");
};

document.getElementById("mID").onclick = function(){
	alert("mID clicked");
	document.getElementById("formid").animate({height: "toggle", opacity: "toggle"}, "slow");
};


// $('.message a').click(function(){
//    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
// });