import {Tile} from './base';

export class OneWayRightTile extends Tile {
    TILE_TYPE = 'ONE WAY RIGHT';
    SAMPLE_CHARS = [">"];

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
    }

    acceptEnergy(amount: number, x: number, y: number) {
        if (y !== this.y || x <= this.x) {
            return false; // Only accept energy from the left
        }
        self.pendingInput = amount;
    }

    advanceTurn() {
        self.currentInput = self.pendingInput;
        self.pendingInput = null;
    }

    startTurn() {
        if (!self.currentInput) {
            return
        }
        const targetTile = this.ctx.getTile(this.x + 1, this.y);
        if (targetTile) {
            targetTile.acceptEnergy(this.currentInput, this.x, this.y);
        }
    }
}