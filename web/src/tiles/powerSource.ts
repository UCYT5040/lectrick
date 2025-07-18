import {Tile} from './base';

class PowerSourceTile extends Tile {
    TILE_TYPE = 'POWER SOURCE';
    SAMPLE_CHARS = ["🗲", "⚡", "⌁"];
    POWER = 255;
    hasSentPower: boolean;

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
        this.hasSentPower = false;
    }

    startTurn() {
        if (!this.hasSentPower) {
            for (let dx = 0; dx < 2; dx++) {
                for (let dy = 0; dy < 2; dy++) {
                    if ((dx == 0 && dy == 0) || (dx != 0 && dy != 0)) {
                        continue;
                    }
                    const targetX = this.x + dx;
                    const targetY = this.y + dy;
                    const targetTile = this.ctx.getTile(targetX, targetY);
                    if (targetTile) {
                        targetTile.acceptEnergy(this.POWER, this.x, this.y);
                    }
                }
            }
            this.hasSentPower = true;
        }
    }
}