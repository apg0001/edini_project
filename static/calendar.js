const calendarBody = document.getElementById("calendar-body");

const year = 2025;
const month = 3; // 4월

fetch("/api/stickers")
  .then((res) => res.json())
  .then((data) => {
    const stickerMap = {};

    data.forEach((item) => {
      if (!stickerMap[item.date]) {
        stickerMap[item.date] = [];
      }
      stickerMap[item.date].push(item); // 모든 내역 저장
    });

    const firstDay = new Date(year, month, 1);
    const lastDate = new Date(year, month + 1, 0).getDate();
    const startDay = firstDay.getDay();

    let html = "<tr>";
    for (let i = 0; i < startDay; i++) {
      html += "<td></td>";
    }

    for (let date = 1; date <= lastDate; date++) {
      const fullDate = `${year}-${String(month + 1).padStart(2, "0")}-${String(
        date
      ).padStart(2, "0")}`;
      html += "<td>";
      html += `<strong>${date}</strong>`;

      if (stickerMap[fullDate]) {
        stickerMap[fullDate].forEach((entry) => {
          html += `<span class="sticker">🌟 ${entry.count}개<br><small>${entry.reason}</small></span>`;
        });
      }

      html += "</td>";
      if ((startDay + date) % 7 === 0) html += "</tr><tr>";
    }

    html += "</tr>";
    calendarBody.innerHTML = html;
  });

  