import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime test', () => {
    beforeAll(() => {
        jest.useFakeTimers();
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    it('should return the initial time', () => {
        jest.spyOn(Date.prototype, 'toLocaleTimeString').mockReturnValue(
            '12:00:00'
        );

        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe('12:00:00');

        jest.spyOn(Date.prototype, 'toLocaleTimeString').mockRestore();
    });

    it('should update the time every second', () => {
        jest.spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValueOnce('12:00:00')
            .mockReturnValueOnce('12:00:01');

        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe('12:00:00');

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).toBe('12:00:01');

        jest.spyOn(Date.prototype, 'toLocaleTimeString').mockRestore();
    });

    it('should clear the interval on unmount', () => {
        const clearIntervalSpy = jest.spyOn(global, 'clearInterval');
        jest.spyOn(Date.prototype, 'toLocaleTimeString').mockReturnValue(
            '12:00:00'
        );

        const { unmount } = renderHook(() => useCurrentTime());

        unmount();

        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);

        clearIntervalSpy.mockRestore();
        jest.spyOn(Date.prototype, 'toLocaleTimeString').mockRestore();
    });
});
