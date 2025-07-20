export interface TestWindow extends Window {
    tests: {
        [key: string]: () => void;
    }
}

export function ensureTests(window: Window | TestWindow) {
    window = window as TestWindow;
    if (!window.tests) {
        window.tests = {};
    }
}