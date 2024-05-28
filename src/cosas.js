
const buttonSave = document.getElementById("button_save");

buttonSave.addEventListener("click", async function() {
  // Get the value from the input field (assuming you want to save it)
  const form = document.getElementById("formulario").value,
  inputValue = document.getElementById("primero").value;
  
  console.log(inputValue);

  // Prepare the data to send (modify this based on your needs)
  let json = {
    inputValue: inputValue,
    // Add other data properties here if needed
  };

  try {
    const query = await fetch("http://127.0.0.1:8000/otro/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(json),
      mode: "no-cors" // Disables CORS checks
    });

    // ... handle response (be aware of limitations)
  

    if (query.ok) {
      console.log("Data saved successfully:", await query.json());
      // Handle successful saving (e.g., display a confirmation message)
    } else {
      console.error("Error saving data:", await query.text());
      // Handle saving errors (e.g., display an error message)
    }
  } catch (error) {
    console.error("Error:", error);
    // Handle other errors (e.g., network issues)
  }
});