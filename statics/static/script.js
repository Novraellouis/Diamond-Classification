function predictImage() {
  let fileInput = document.getElementById("fileInput");
  let file = fileInput.files[0];
  let formData = new FormData();
  formData.append("file", file);

  fetch("/predict", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      // Process prediction result
      document.getElementById("predictionResult").innerText = JSON.stringify(data);
    })
    .catch((error) => console.error("Error:", error));
}
