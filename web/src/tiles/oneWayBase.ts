import {Tile} from "./tile";

type Input = [number, number, number]; // [amount, x, y]

class OneWayBase extends Tile {
    pending_input: Input | null;
    current_input: Input | null;

    acceptanceFilter(x: number, y: number): boolean {
        return true // Overridden in subclasses
    }

    acceptEnergy(amount: number, x: number, y: number): void {
        if (!this.acceptanceFilter(x, y)) {
            return;
        }
        if (this.pending_input !== null) {
            this.ctx.startFire();
            return
        }
    }

    advanceTurn(): void {
        this.current_input = this.pending_input;
        this.pending_input = null;
    }
}