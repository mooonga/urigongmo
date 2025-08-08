(() => {
  const slider = document.querySelector('.hero-slider');
  if (!slider) return;

  const track   = slider.querySelector('.hero-track');
  const prevBtn = slider.querySelector('.hero-arrow.prev');
  const nextBtn = slider.querySelector('.hero-arrow.next');
  const dotsWrap= slider.querySelector('.hero-dots');

  // 원본 슬라이드 수집
  let baseSlides = Array.from(track.children);   // <li>들
  const REAL = baseSlides.length;
  if (REAL === 0) return;

  // 앞뒤 클론으로 무한 루프 구성
  const firstClone = baseSlides[0].cloneNode(true);
  const lastClone  = baseSlides[REAL - 1].cloneNode(true);
  track.appendChild(firstClone);
  track.insertBefore(lastClone, baseSlides[0]);

  // 다시 수집(클론 포함)
  let slides = Array.from(track.children);

  // 시작 위치: 첫 번째 실제 슬라이드
  let index = 1;
  const DURATION = 600;
  const intervalMs = 5000;
  let timer = null;
  let animating = false;

  // 점 네비 생성(실제 슬라이드 기준)
  dotsWrap.innerHTML = '';
  for (let i = 0; i < REAL; i++) {
    const dot = document.createElement('button');
    if (i === 0) dot.className = 'active';
    dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
    dot.addEventListener('click', () => goExact(i + 1, true)); // i+1 => 클론 보정
    dotsWrap.appendChild(dot);
  }
  const dots = Array.from(dotsWrap.children);

  // 초기 위치 세팅
  track.style.transition = 'none';
  translate();
  requestAnimationFrame(() => track.style.transition = '');

  // 높이 맞춤(크롭 방지 세로 자동)
  function fitHeight() {
    const img = slides[index]?.querySelector('img');
    if (!img) return;
    if (!img.complete) { img.addEventListener('load', fitHeight, { once: true }); return; }
    // 현재 렌더된 높이를 그대로 사용
    // slider.style.height = img.getBoundingClientRect().height + 'px';
  }
  // window.addEventListener('resize', fitHeight);

  function translate() {
    track.style.transform = `translateX(-${index * 100}%)`;
    fitHeight();
    // 점 네비 활성화(클론 제외한 실제 인덱스 계산)
    const realIdx = ((index - 1) % REAL + REAL) % REAL;
    dots.forEach((d, i) => d.classList.toggle('active', i === realIdx));
  }

  function goExact(toIndex, user = false) {
    if (animating) return;
    animating = true;
    index = toIndex;
    translate();
    if (user) resetTimer();
  }

  function next() { goExact(index + 1, false); }
  function prev() { goExact(index - 1, false); }

  // 전환 종료 후 클론에서 실제로 점프(애니메이션 없이)
  track.addEventListener('transitionend', () => {
    // 마지막 실제 다음(=firstClone)에 도달하면 → 실제 첫 번째로 점프
    if (index === slides.length - 1) {
      track.style.transition = 'none';
      index = 1;
      translate();
      // 다음 프레임에 트랜지션 되살리기
      requestAnimationFrame(() => track.style.transition = `transform ${DURATION}ms ease`);
    }
    // 첫 번째 실제 이전(=lastClone)에 도달하면 → 실제 마지막으로 점프
    if (index === 0) {
      track.style.transition = 'none';
      index = slides.length - 2;
      translate();
      requestAnimationFrame(() => track.style.transition = `transform ${DURATION}ms ease`);
    }
    animating = false;
  });

  // 버튼/키보드
  prevBtn.addEventListener('click', () => goExact(index - 1, true));
  nextBtn.addEventListener('click', () => goExact(index + 1, true));
  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft')  goExact(index - 1, true);
    if (e.key === 'ArrowRight') goExact(index + 1, true);
  });

  // 자동재생
  function startTimer() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    timer = setInterval(next, intervalMs);
  }
  function resetTimer() { clearInterval(timer); startTimer(); }

  // 탭 비활성화 시 멈춤
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) clearInterval(timer);
    else resetTimer();
  });

  // 시작
  requestAnimationFrame(() => {
    track.style.transition = `transform ${DURATION}ms ease`;
    translate();
    startTimer();
  });
})();
