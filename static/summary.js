fetch("/api/sticker-summary")
  .then((res) => res.json())
  .then((data) => {
    document.getElementById("total-sticker").innerText = `${data.total}개`;
    document.getElementById("current-badge").innerText = data.badge;
  })
  .catch((err) => {
    console.error("요약 불러오기 실패:", err);
  });
