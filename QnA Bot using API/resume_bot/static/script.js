function request_server(){
    var question = document.getElementById('question').value;
    if (question !== ""){

        // Sending a Request
        var host = window.location.host;
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("GET", "https://"+host+"/ask/" + question, false);
        xmlHttp.send(null);
        var response = xmlHttp.responseText;

        // Adding the content to the chat
        var prev = document.getElementById('chat').innerHTML;
        var new_message = `
            <div class="alert alert-success">
                ` + question + `
            </div>
            <div class="alert alert-secondary">
                ` + response + `
            </div>
            
        `;

        document.getElementById('question').value = "";
        document.getElementById('chat').innerHTML = prev + new_message;
    }
}