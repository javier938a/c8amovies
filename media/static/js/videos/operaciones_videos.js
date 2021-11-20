
function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

let video=document.getElementById('videoPlayer');
video.addEventListener('contextmenu', function(evt){
	evt.preventDefault();
});

video.addEventListener('timeupdate', function(evt){
	let idvideo=document.getElementById('pk_video').value;
	let segundo_actual = video.currentTime;
	let id_db_video=document.getElementById("pk_video").value;
	let datos={
		'id_video':id_db_video,
		'segundo_actual':segundo_actual
	};
	(async ()=>{
		let url=document.getElementById('url_view').value;
		try{
			console.log(url)
			const csrftoken=getCookie('csrftoken');
			var init={
				method:'POST',
				headers:{
					'X-CSRFToken':csrftoken,
					'X-Requested-Width':"XMLHttpRequest",
					'content-Type':'application/json'
				},
				body:JSON.stringify(datos)
			}

			var response=await fetch(url, init);
			if(response.ok){

			}

		}catch(err){
			console.log('Error al realizar peticion ajax'+err.message);
		}
	})();

})