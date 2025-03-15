import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime test', () => {
    let toLocaleTimeStringMock: jest.SpyInstance;
    let clearIntervalSpy: jest.SpyInstance;

    beforeAll(() => {
        jest.useFakeTimers();
        toLocaleTimeStringMock = jest.spyOn(
            Date.prototype,
            'toLocaleTimeString'
        );
    });

    afterAll(() => {
        jest.useRealTimers();
        toLocaleTimeStringMock.mockRestore();
    });

    it('should return the initial time', () => {
        toLocaleTimeStringMock.mockReturnValue('12:00:00');

        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe('12:00:00');
    });

    it('should update the time every second', () => {
        toLocaleTimeStringMock
            .mockReturnValueOnce('12:00:00')
            .mockReturnValueOnce('12:00:01');

        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe('12:00:00');

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).toBe('12:00:01');
    });

    it('should clear the interval on unmount', () => {
        toLocaleTimeStringMock.mockReturnValue('12:00:00');
        clearIntervalSpy = jest.spyOn(global, 'clearInterval');

        const { unmount } = renderHook(() => useCurrentTime());

        unmount();

        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
        clearIntervalSpy.mockRestore();
    });
});
