import {OneWayBase} from './oneWayBase';

export class LightBlockTile extends OneWayBase {
    TILE_TYPE = '"LIGHT BLOCK';
    SAMPLE_CHARS = ["⬛", "⯀", "◼", "▮"];

    constructor(ctx: ExecutionContext, x: number, y: number) {
        super(ctx, x, y);
    }

    endTurn() {
        if (this.currentInput) {
            const amount = this.currentInput[0];
            this.ctx.print(String.fromCharCode(amount));
        }
    }
}