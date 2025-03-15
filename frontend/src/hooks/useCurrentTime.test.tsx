import {renderHook, act, render} from '@testing-library/react';
import { useCurrentTime } from './useCurrentTime';

jest.useFakeTimers();

describe('useCurrentTime', () => {
    test('возвращает корректное время при инициализации', () => {
        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
    });

    test('обновляет время каждую секунду', () => {
        const { result } = renderHook(() => useCurrentTime());

        const initialTime = result.current;
        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).not.toBe(initialTime);
    });

    test('очищает интервал при размонтировании', () => {
        const clearIntervalSpy = jest.spyOn(global, 'clearInterval');
        const { unmount } = renderHook(() => useCurrentTime());

        unmount();

        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
        clearIntervalSpy.mockRestore();
    });
});
