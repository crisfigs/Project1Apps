const startButtonOverlay = document.getElementById("start_button_overlay");
const startButton = document.getElementById("start_button_img");
let startButtonCallback;

const showStartButtonOverlay = (callback) => {
    startButtonOverlay.style.visibility = "visible";
    startButtonCallback = callback;
}

const hideStartButtonOverlay = () => {
    startButtonOverlay.style.visibility = "hidden";
    startButtonCallback();
}

startButton.addEventListener('click', hideStartButtonOverlay, false);