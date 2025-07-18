import {Tile} from "./base";

export type Input = [number, number, number]; // [amount, x, y]

class OneWayBase extends Tile {
    pendingInput: Input | null;
    currentInput: Input | null;

    acceptanceFilter(x: number, y: number): boolean {
        return true // Overridden in subclasses
    }

    acceptEnergy(amount: number, x: number, y: number): void {
        if (!this.acceptanceFilter(x, y)) {
            return;
        }
        if (this.pendingInput !== null) {
            this.ctx.startFire();
            return
        }
    }

    advanceTurn(): void {
        this.currentInput = this.pendingInput;
        this.pendingInput = null;
    }
}