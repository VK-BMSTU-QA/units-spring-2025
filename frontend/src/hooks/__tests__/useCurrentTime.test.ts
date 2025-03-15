import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

jest.useFakeTimers()

describe('useCurrentTime', () => {

    it('should return the correct initial time', () => {
        jest.setSystemTime(new Date('2025-03-15T00:00:00'));
        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
    });

    it('should update time every second', () => {
        jest.setSystemTime(new Date('2025-03-15T00:00:00'));
        const { result } = renderHook(() => useCurrentTime());

        const initialTime = result.current;

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).not.toEqual(initialTime);
        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
    });

    it('should clear interval on unmount', () => {
        jest.spyOn(global, 'clearInterval');
        const { unmount } = renderHook(() => useCurrentTime());
        unmount();
        expect(clearInterval).toHaveBeenCalledTimes(1);
    });
});

