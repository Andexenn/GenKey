AOS.init({
  duration: 1000, 
  easing: "ease-in-out", 
  once: true, 
});

function generatePassword(length = 8)
{
  const lowerChars = "abcdefghijklmnopqrstuvwxyz";
  const numberChars = "0123456789";
  const specialChars = "!@#$%^&*()_+~`|}{[]:;?><,./-=";
  const allChars = lowerChars + numberChars + specialChars;


  //* dam bao co it nhat it ky tu moi loai
  let password = "";

  password += lowerChars[Math.floor(Math.random() * lowerChars.length())];
  password += numberChars[Math.floor(Math.random() * numberChars.length())];
  password += specialChars[Math.floor(Math.random() * specialChars.length())];

  for(let i = 3; i <= length; ++i)
  {
    password += allChars[Math.floor(Math.random() * allChars.length())];
  }

  return password;
}

function sendPasswordToServer(password)
{
  fetch('/gen', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({password : password })
  })
  .then(response => response.json())
  .then(data => {
    console.log("Server response: ", data);
  });
}

const password = generatePassword(8);
sendPasswordToServer(password);



