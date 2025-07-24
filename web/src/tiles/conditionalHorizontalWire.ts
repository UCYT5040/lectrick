import {Tile} from './base';
import {Input} from './oneWayBase';

export class ConditionalHorizontalWireTile extends Tile {
    TILE_TYPE = 'CONDITIONAL HORIZONTAL WIRE';
    SAMPLE_CHARS = [
        "T"
    ];
    pendingInput: Input | null;
    currentInput: Input | null;
    pendingVerticalInput: number | null;
    currentVerticalInput: number | null;

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
        this.pendingVerticalInput = null;
        this.currentVerticalInput = null;
    }

    acceptEnergy(amount: number, x: number, y: number) {
        if (y === this.y) {
            // Horizontal input
            if (this.pendingInput !== null) {
                // Already has a pending input
                this.ctx.startFire();
                return;
            }
            this.pendingInput = [amount, x, y];
        } else if (x === this.x) {
            // Vertical input
            if (this.pendingVerticalInput !== null) {
                // Already has a pending vertical input
                this.ctx.startFire();
                return;
            }
            this.pendingVerticalInput = amount;
        }
    }

    advanceTurn() {
        this.currentInput = this.pendingInput;
        this.pendingInput = null;
        this.currentVerticalInput = this.pendingVerticalInput;
        this.pendingVerticalInput = null;
    }

    startTurn() {
        if (this.currentInput !== null && this.currentVerticalInput !== null) {
            if (this.currentVerticalInput <= 0) {
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
}