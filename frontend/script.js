document.addEventListener("DOMContentLoaded", () => {
  const checkBtn = document.getElementById("checkBtn");
  const output = document.getElementById("output");
  const loader = document.getElementById("loader");

  checkBtn.addEventListener("click", async () => {
    const input = document.getElementById("textInput").value.trim();
    if (!input) return;

    output.innerHTML = "";
    loader.classList.remove("hidden");

    const response = await fetch(
      "https://toxicity-predictor-5.onrender.com/predict",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: input }),
      }
    );

    const result = await response.json();
    loader.classList.add("hidden");

    const labels = Object.entries(result).filter(([label]) => label !== "safe");

    labels.forEach(([label, value]) => {
      const div = document.createElement("div");
      div.classList.add("trait");

      // Apply color based on % range
      if (value < 30) div.classList.add("green");
      else if (value < 70) div.classList.add("yellow");
      else div.classList.add("red");

      div.innerHTML = `<div>${label.toUpperCase()}</div><div>${value}%</div>`;
      output.appendChild(div);
    });

    if (result.safe) {
      const safeTag = document.createElement("p");
      safeTag.style.marginTop = "20px";
      safeTag.style.color = "green";
      safeTag.style.fontWeight = "bold";
      safeTag.textContent = "✅ This text seems safe!";
      output.appendChild(safeTag);
    }
  });
});
