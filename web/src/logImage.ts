import {ensureTests, TestWindow} from "./testWindow";

export function logImage(message: string, imageUrl: string) {
    console.log(`%c${message}`, `background: url(${imageUrl}) no-repeat; background-size: contain; background-position: 0 1.2em; width: 100px; height: calc(100px + 1.2em); display: inline-block;`);
}

ensureTests(window);
(window as TestWindow).tests.logImage = () => {
    const canvas = document.createElement('canvas');
    canvas.width = 100;
    canvas.height = 100;
    const ctx = canvas.getContext('2d');
    if (!ctx) {
        throw new Error("Canvas context not found");
    }
    for (let x = 0; x < 100; x++) {
        for (let y = 0; y < 100; y++) {
            ctx.fillStyle = `rgb(${x * 2.55}, ${y * 2.55}, 150)`;
            ctx.fillRect(x, y, 1, 1);
        }
    }
    const imageUrl = canvas.toDataURL();
    logImage("Test Image", imageUrl);
};
