import {getCharacterImage} from "./characterImage";
import {createCanvas} from "./canvas";

const SHAPES_PATH = "copied/shapes/";
const SHAPES_EXT = ".png";

function toGrayscaleArray(imageData: ImageData): number[] {
    const arr = [];
    for (let i = 0; i < imageData.data.length; i += 4) {
        // Grayscale: 0.299*R + 0.587*G + 0.114*B
        const gray = 0.299 * imageData.data[i] + 0.587 * imageData.data[i + 1] + 0.114 * imageData.data[i + 2];
        arr.push(gray);
    }
    return arr;
}

export async function compareCharacter(
    character: string,
    shapeName: string
): Promise<number> {
    const shapePath = SHAPES_PATH + character + "/" + shapeName + SHAPES_EXT;
    let imageData;
    try {
        imageData = await fetch(shapePath);
    } catch (error) {
        console.error("Error fetching image:", error);
        return 0.0;
    }
    if (!imageData.ok) {
        console.error("Image not found:", shapePath);
        return 0.0;
    }
    const imageBlob = await imageData.blob();
    const imageBitmap = await createImageBitmap(imageBlob);


    const charImage = await getCharacterImage(character);

    const canvas = createCanvas(
        imageBitmap.width,
        imageBitmap.height
    );

    const ctx = canvas.getContext("2d");

    if (!ctx) {
        throw new Error("Canvas context not found");
    }

    // Stretch the character image to match the shape image size
    ctx.drawImage(
        charImage,
        0,
        0,
        charImage.width,
        charImage.height,
        0,
        0,
        imageBitmap.width,
        imageBitmap.height
    );

    // Get pixel data for both images
    const charImageData = ctx.getImageData(0, 0, imageBitmap.width, imageBitmap.height);

    // Convert both images to grayscale arrays
    const charGray = toGrayscaleArray(charImageData);
    const shapeGray = toGrayscaleArray(shapeImageData);

    // Calculate pixel-wise absolute difference and sum
    let pixelDiff = 0;
    for (let i = 0; i < charGray.length; i++) {
        pixelDiff += Math.abs(charGray[i] - shapeGray[i]);
    }

    const maxDiff = imageBitmap.width * imageBitmap.height * 255.0;
    const dissimilarity = pixelDiff / maxDiff;
    return 1.0 - dissimilarity;
}
