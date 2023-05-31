let state = false

function active() {
    if (state === false) {
        state = true;
        getShow()
    }
    else {
        state = false
        getHide()
    }
}

function getShow(){
	document.getElementById("i").style.display = "";
}

function getHide(){
	document.getElementById("i").style.display = "none";
}
