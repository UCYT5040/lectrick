import {OneWayBase} from './oneWayBase';

export class HorizontalWireTile extends OneWayBase {
    TILE_TYPE = 'HORIZONTAL WIRE';
    SAMPLE_CHARS = ["-", "‐", "‒"];

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
    }

    acceptanceFilter(x: number, y: number): boolean {
        return y === this.y
    }

    startTurn() {
        if (!this.currentInput) {
            return;
        }
        const [amount, x, y] = this.currentInput;
        let dx;
        if (x < this.x) {
            dx = -1; // Left
        } else if (x > this.x) {
            dx = 1; // Right
        } else {
            return; // No horizontal movement
        }
        const targetTile = this.ctx.getTile(this.x + dx, this.y);
        if (targetTile) {
            targetTile.acceptEnergy(amount, this.x, this.y);
        }
    }
}