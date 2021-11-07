var video = document.getElementById('videoPlayer');

function playPause(){
	if(video.pause){
		video.play();
	}else{
		video.pause();
	}
}

function reload(){
	video.load();
}

function makeLarge(){
	video.width=1000;
}

function makeSmall(){
	video.width=250;
}

function makeNormal(){
	video.width=500;
}