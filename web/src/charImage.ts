import {createCanvas} from "./canvas";

export function getCharacterImage(character: string): HTMLCanvasElement {
    createCanvas(800, 800);
    const ctx = document.querySelector('canvas').getContext('2d');

    if (!ctx) {
        throw new Error("Canvas context not found");
    }

    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, 800, 800);
    ctx.fillStyle = 'black';
    ctx.font = '48px serif';  // TODO: Use Noto Sans for consistent results with the Python version
    ctx.fillText(character, 0, 0);

    // Crop the image to the character
    // Measure text utilities cannot be used as they often include additional padding
    const imageData = ctx.getImageData(0, 0, 800, 800);
    const data = imageData.data;
    let left = 800, right = 0, top = 800, bottom = 0;

    for (let y = 0; y < 800; y++) {
        for (let x = 0; x < 800; x++) {
            const index = (y * 800 + x) * 4;
            const r = data[index];
            const g = data[index + 1];
            const b = data[index + 2];
            const brightness = (r + g + b) / 3;

            if (brightness < 255) { // Non-white pixel
                if (x < left) left = x;
                if (x > right) right = x;
                if (y < top) top = y;
                if (y > bottom) bottom = y;
            }
        }
    }

    // Create a new canvas to hold the cropped image
    const croppedCanvas = createCanvas(right - left + 1, bottom - top + 1);
    const croppedCtx = croppedCanvas.getContext('2d');
    if (!croppedCtx) {
        throw new Error("Cropped canvas context not found");
    }

    // Draw the cropped image
    croppedCtx.putImageData(imageData, -left, -top);

    return croppedCanvas;
}