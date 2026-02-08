document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".counter");

  counters.forEach(counter => {
    const target = +counter.dataset.target;
    const hasPlus = counter.innerText.includes("+");

    let current = 0;
    const duration = 1200;
    const stepTime = Math.max(Math.floor(duration / target), 20);

    const update = () => {
      current += Math.ceil(target / (duration / stepTime));
      if (current >= target) {
        current = target;
        counter.innerText = hasPlus ? `${current}+` : current;
      } else {
        counter.innerText = hasPlus ? `${current}+` : current;
        setTimeout(update, stepTime);
      }
    };

    update();
  });
});