import {TILES_LIST} from "./tilesList";
import {compareCharacter} from "./compare";

export async function lookup(character: string) {
    let bestMatch = null;
    let bestScore = 0;
    for (const tile of TILES_LIST) {
        const similarity = await compareCharacter(character, tile.TILE_TYPE);
        if (similarity > bestScore) {
            bestScore = similarity;
            bestMatch = tile;
        }
    }
    if (bestMatch) {
        return {
            tile: bestMatch,
            score: bestScore
        };
    } else {
        return null;
    }
}