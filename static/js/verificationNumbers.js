function showCheck(a){
	var c = document.getElementById("myCanvas");
  	var ctx = c.getContext("2d");
  	ctx.fillStyle = "white";
	ctx.clearRect(0,0,1000,1000);
	ctx.font = "70px 'Microsoft Yahei'";
	ctx.fillText(a,10,100);
}
var code ;    
function createCode(){       
    code = "";      
    var codeLength = 4;
    var selectChar = new Array(1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z');      
    for(var i=0;i<codeLength;i++) {
       var charIndex = Math.floor(Math.random()*60);      
      code +=selectChar[charIndex];
    }      
    if(code.length != codeLength){      
      createCode();      
    }
    showCheck(code);
}
          
function validate () {
    var inputCode = document.getElementById("J_codetext").value.toUpperCase();
    var codeToUp=code.toUpperCase();
    document.getElementById("J_codeinput").style.backgroundColor = "#5cbdaa"; 
    document.getElementById("J_codeinput").setAttribute("value","验证码核验");
    if(inputCode.length <=0) {
		document.getElementById("J_codetext").setAttribute("placeholder","输入验证码");
		createCode();
		return false;
    }
    else if(inputCode != codeToUp ){
        document.getElementById("J_codetext").value="";
        document.getElementById("J_codetext").setAttribute("placeholder","验证码错误");
        createCode();
        return false;
    }
    else{
    	var bg = document.getElementById("J_codeinput");
    	bg.style.backgroundColor = "#00b4ef";
    	bg.setAttribute("value","验证码正确");
    	document.getElementById("myCanvas").onclick = "off";
    	document.getElementById("J_codetext").disabled = "disabled";
        window.open(document.getElementById("J_down").getAttribute("data-link"));
        createCode();
        return true;
    }
}