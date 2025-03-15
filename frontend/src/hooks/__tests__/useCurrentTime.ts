import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime', () => {
    beforeEach(() => {
        jest.useFakeTimers();
        jest.spyOn(global, 'setInterval');
        jest.spyOn(global, 'clearInterval');
    });

    afterEach(() => {
        jest.useRealTimers();
        jest.restoreAllMocks();
    });

    it('return initial value', () => {
        const { result } = renderHook(useCurrentTime);
        expect(global.setInterval).toHaveBeenCalledTimes(1);
        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
    });

    it('time changing', () => {
        const { result } = renderHook(useCurrentTime);
        const initialTime = result.current;
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        expect(global.setInterval).toHaveBeenCalledTimes(2);
        expect(result.current).not.toBe(initialTime);
    });

    it('clearInterval on unmount', () => {
        const { unmount } = renderHook(useCurrentTime);
        unmount();
        expect(global.clearInterval).toHaveBeenCalled();
    });
});

