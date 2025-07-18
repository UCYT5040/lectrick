class Tile {
    TILE_TYPE: string;
    SAMPLE_CHARS: string[];
    ctx: ExecutionContext;
    x: number;
    y: number;
    tiles: Tile[];
    pendingInput: any | null;
    currentInput: any | null;

    constructor(ctx: ExecutionContext, x: number, y: number) {
        this.ctx = ctx;
        this.x = x;
        this.y = y;
        this.pendingInput = null;
        this.currentInput = null;
    }

    equals(other: Tile | [number, number]): boolean {
        if (Array.isArray(other)) {
            return this.x === other[0] && this.y === other[1];
        }
        return (
            this.x === other.x &&
            this.y === other.y &&
            this.TILE_TYPE === other.TILE_TYPE
        )
    }

    acceptEnergy(amount: number, x: number, y: number): void {
        // To be implemented in subclasses
    }

    startTurn(): void {
        // To be implemented in subclasses
    }

    endTurn(): void {
        // To be implemented in subclasses
    }

    advanceTurn(): void {
        // To be implemented in subclasses
    }
}