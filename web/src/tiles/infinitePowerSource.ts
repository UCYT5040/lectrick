import {Tile} from './base';

class InfinitePowerSourceTile extends Tile {
    TILE_TYPE = 'INFINITE POWER SOURCE';
    SAMPLE_CHARS = ["⏻"]
    POWER = 255;

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
    }

    startTurn() {
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
    }
}