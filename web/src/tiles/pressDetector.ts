import {Tile} from './base';

export class PressDetector extends Tile {
    TILE_TYPE = 'PRESS DETECTOR';
    SAMPLE_CHARS = ["␣"];

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
    }

    startTurn() {
        const pressedKey = this.ctx.getPressedKey();
        if (pressedKey !== null) {
            for (let dx = 0; dx < 2; dx++) {
                for (let dy = 0; dy < 2; dy++) {
                    if ((dx == 0 && dy == 0) || (dx != 0 && dy != 0)) {
                        continue;
                    }
                    const targetX = this.x + dx;
                    const targetY = this.y + dy;
                    const targetTile = this.ctx.getTile(targetX, targetY);
                    if (targetTile) {
                        targetTile.acceptEnergy(
                            pressedKey.charCodeAt(0),
                            this.x, this.y
                        );
                    }
                }
            }
        }
    }
}