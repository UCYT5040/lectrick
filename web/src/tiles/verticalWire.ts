import {OneWayBase} from './oneWayBase';

export class VerticalWireTile extends OneWayBase {
    TILE_TYPE = 'VERTICAL WIRE';
    SAMPLE_CHARS = ["|"];

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
    }

    acceptanceFilter(x: number, y: number): boolean {
        return x === this.x
    }

    startTurn() {
        if (!this.currentInput) {
            return;
        }
        const [amount, x, y] = this.currentInput;
        let dy;
        if (y < this.y) {
            dy = -1; // Left
        } else if (y > this.y) {
            dy = 1; // Right
        } else {
            return; // No horizontal movement
        }
        const targetTile = this.ctx.getTile(this.x, this.y + dy);
        if (targetTile) {
            targetTile.acceptEnergy(amount, this.x, this.y);
        }
    }
}