import { useCurrentTime } from "./useCurrentTime";
import { renderHook, act } from "@testing-library/react";

jest.useFakeTimers();

afterAll(() => {
    jest.useRealTimers();
});

describe('test useCurrentTime hook', () => {
    it('should return correct current time', () => {
        const result = renderHook(() => useCurrentTime());
        const initTime = new Date().toLocaleTimeString('ru-RU');
        expect(result.result.current).toBe(initTime);
    });

    it('should update time every second', ()=> {
        const result = renderHook(() => useCurrentTime());
        const initTime = new Date().toLocaleTimeString('ru-RU');
        expect(result.result.current).toBe(initTime);

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        const newTime = new Date().toLocaleTimeString('ru-RU');
        expect(result.result.current).toBe(newTime);
    });

    it('should clear the interval on unmount', () => {
        const clearIntervalSpy = jest.spyOn(global, 'clearInterval');
        const { unmount } = renderHook(() => useCurrentTime());

        unmount();
        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
        clearIntervalSpy.mockRestore(); 
    });
});