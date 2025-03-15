import { act, renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime hook test', () => {
    beforeAll(() => {
        jest.useFakeTimers().setSystemTime(new Date('1979-01-01T00:00:00Z'));
    });

    beforeEach(() => {
        let seconds = 55;
        jest.spyOn(Date.prototype, 'toLocaleTimeString').mockImplementation(
            () => {
                seconds++;
                return `12:34:${String(seconds).padStart(2, '0')}`;
            }
        );
    });

    afterAll(() => {
        jest.useRealTimers();
        jest.restoreAllMocks();
    });

    it('should correctly initialize time and set an interval for updates', () => {
        const setIntervalSpy = jest.spyOn(global, 'setInterval');
        const { result } = renderHook(() => useCurrentTime());
        expect(setIntervalSpy).toHaveBeenCalledTimes(1);
        expect(result.current).toBe('12:34:56');
    });

    it('should clear the interval when unmounting', () => {
        const clearIntervalSpy = jest.spyOn(global, 'clearInterval');
        const { unmount } = renderHook(() => useCurrentTime());
        unmount();
        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
    });

    it('must update the time every 1000ms', () => {
        const { result } = renderHook(() => useCurrentTime());
        const initialTime = result.current;
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        expect(result.current).not.toEqual(initialTime);
        expect(result.current).toBe('12:34:57');
    });
});
