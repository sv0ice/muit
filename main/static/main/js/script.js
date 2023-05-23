function runGitCommand() {
    var command = document.getElementById("git-command").value;
    var output = document.getElementById("output");
    
    // Create a JSON object with the command
    var requestBody = {
      command: command
    };
  
    // Make an HTTP POST request to the API server
    fetch('https://api.example.com/git-commands', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody)
    })
    .then(response => response.json())
    .then(data => {
      // Process the response from the server
      output.innerHTML = data.output;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  