import {Tile} from './base';

class ClockTile extends Tile {
    TILE_TYPE = 'CLOCK';
    SAMPLE_CHARS = [
        "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛",
        "🕜", "🕝", "🕞", "🕟", "🕠", "🕡", "🕢", "🕣", "🕤", "🕥", "🕦", "🕧"
    ]
    POWER = 255;
    lastTime: number | null;

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
        this.lastTime = null;
    }

    startTurn() {
        const currentTime = this.ctx.getTime();
        if (!this.lastTime) {
            this.lastTime = currentTime;
            return;
        }
        if (currentTime - this.lastTime >= 1000) {
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
}