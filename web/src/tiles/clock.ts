import {Tile} from './tile';

class ClockTile extends Tile {
    TILE_TYPE = 'CLOCK';
    SAMPLE_CHARS = [
        "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛",
        "🕜", "🕝", "🕞", "🕟", "🕠", "🕡", "🕢", "🕣", "🕤", "🕥", "🕦", "🕧"
    ]
    POWER = 255;
    last_time: number | null;

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
        this.last_time = null;
    }

    startTurn() {
        const currentTime = this.ctx.get_time();
        if (!this.last_time) {
            this.last_time = currentTime;
            return;
        }
        if (currentTime - this.last_time >= 1000) {
            for (let dx = 0; dx < 2; dx++) {
                for (let dy = 0; dy < 2; dy++) {
                    if ((dx == 0 && dy == 0) || (dx != 0 && dy != 0)) {
                        continue;
                    }
                    const targetX = this.x + dx;
                    const targetY = this.y + dy;
                    const targetTile = this.ctx.get_tile(targetX, targetY);
                    if (targetTile) {
                        targetTile.acceptEnergy(this.POWER, this.x, this.y);
                    }
                }
            }
        }
    }
}