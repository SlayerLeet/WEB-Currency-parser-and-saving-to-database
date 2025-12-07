async function loadPrices() {
    try {
        const response = await fetch("/api/data");  // подставишь свой эндпоинт
        const data = await response.json();

        const table = document.getElementById("priceTable");
        table.innerHTML = "";

        data.forEach(row => {
            const tr = document.createElement("tr");

            tr.innerHTML = `
                <td>${row.id}</td>
                <td>${row.name}</td>
                <td>${row.exchange}</td>
                <td>${row.price}</td>
            `;

            table.appendChild(tr);
        });

    } catch (err) {
        console.error("Ошибка при загрузке цен:", err);
    }
}

document.getElementById("refreshBtn").addEventListener("click", loadPrices);

loadPrices();
    