fetch("/api/statistics")
  .then((res) => res.json())
  .then((data) => {
    const chartData = data.monthly_chart;
    const labels = Object.keys(chartData);
    const values = Object.values(chartData);

    new Chart(document.getElementById("chart"), {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: "스티커 수",
            data: values,
            backgroundColor: "#f8a5c2",
          },
        ],
      },
    });

    // 누적 수 표시
    document.getElementById(
      "month-total"
    ).innerText = `📅 이번 달 스티커: ${data.this_month}개`;
    document.getElementById(
      "week-total"
    ).innerText = `🗓 이번 주 스티커: ${data.this_week}개`;
  });
