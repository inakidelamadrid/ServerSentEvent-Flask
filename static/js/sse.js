let targetContainer = document.getElementById("stream-div");
let eventSource = new EventSource("/stream");

eventSource.onMessage = function(evt){
  targetContainer.innerHTML = evt.data;
}
