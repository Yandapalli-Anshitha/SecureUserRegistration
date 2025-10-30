document.getElementById("registerForm").addEventListener("submit", function(event){
  event.preventDefault();

  let password = document.getElementById("password").value;
  
  if(password.length < 8){
    alert("Password must be at least 8 characters!");
    return;
  }

  alert("Registration Successful!");
});
