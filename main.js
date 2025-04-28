const viewBtn = document.getElementById("view-code-btn");
const codeDisplay = document.getElementById("code-display");
const loading = document.getElementById("loading");

viewBtn.addEventListener("click", () => {
  loading.style.display = "block";
  codeDisplay.classList.add("hidden");

  fetch("assest/main.py")
    .then((response) => response.text())
    .then((data) => {
      loading.style.display = "none";
      codeDisplay.textContent = data;
      codeDisplay.classList.remove("hidden");
    })
    .catch((error) => {
      loading.textContent = "Gagal memuat file.";
      console.error("Error:", error);
    });
});
