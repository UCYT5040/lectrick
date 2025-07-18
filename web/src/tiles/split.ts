import {OneWayBase} from './oneWayBase';

class SplitTile extends OneWayBase {
    TILE_TYPE = 'SPLIT';
    SAMPLE_CHARS = ["÷"];

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
    }

    startTurn() {
        if (!this.currentInput) {
            return;
        }
        const [amount, x, y] = this.currentInput;

        for (let dx = 0; dx < 2; dx++) {
            for (let dy = 0; dy < 2; dy++) {
                if ((dx == 0 && dy == 0) || (dx != 0 && dy != 0)) {
                    continue;
                }
                const targetX = this.x + dx;
                const targetY = this.y + dy;
                if (targetX === x && targetY === y) {
                    continue; // Skip the tile that sent the energy
                }
                const targetTile = this.ctx.getTile(targetX, targetY);
                if (targetTile) {
                    targetTile.acceptEnergy(Math.floor(amount / 2) % 256, this.x, this.y);
                }
            }
        }
    }
}