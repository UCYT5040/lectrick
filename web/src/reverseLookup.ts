import {lookup} from "./lookup";

type RangePart = number | [number, number];
type Range = RangePart | RangePart[];

export async function reverseLookup(tileType: string, range: Range): Promise<string[]> {
    if (!Array.isArray(range)) {
        range = [range];
    }
    const results: string[] = [];
    for (const part of range) {
        if (Array.isArray(part)) {
            const [start, end] = part;
            for (let i = start; i <= end; i++) {
                const char = String.fromCharCode(i);
                const result = await lookup(char);
                if (result && result.tile === tileType) {
                    results.push(char);
                }
            }
        } else {
            const char = String.fromCharCode(part);
            const result = await lookup(char);
            if (result && result.tile === tileType) {
                results.push(char);
            }
        }
    }
    return results;
}