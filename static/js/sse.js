console.log("Perra");
let targetContainer = document.getElementById("stream-div");
let eventSource = new EventSource("/stream");

eventSource.onmessage = function(evt){
  var content = targetContainer.innerHTML;
  var newContent = content + "\n" + evt.data;
  targetContainer.innerHTML = newContent;
}
