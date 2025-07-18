import {OneWayBase} from './oneWayBase';

class NotTile extends OneWayBase {
    TILE_TYPE = 'NOT';
    SAMPLE_CHARS = ["≠", "≄", "≉"];
    POWER = 255;

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
    }

    acceptanceFilter(x: number, y: number): boolean {
        return y === this.y;
    }

    startTurn() {
        let amount;
        if (!this.currentInput || this.currentInput[0] === 0) {
            amount = self.POWER;
        } else {
            amount = 0;
        }
        const [_, x, y] = this.currentInput;
        for (let dx = -1; dx < 2; dx += 2) {
            const targetTile = this.ctx.getTile(this.x + dx, this.y);
            if (targetTile) {
                targetTile.acceptEnergy(amount, this.x, this.y);
            }
        }
    }
}