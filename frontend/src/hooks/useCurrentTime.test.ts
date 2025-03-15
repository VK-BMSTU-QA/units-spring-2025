import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from './useCurrentTime';

describe('useCurrentTime', () => {
    beforeAll(() => {
        jest.useFakeTimers(); // Используем фейковые таймеры
    });

    afterAll(() => {
        jest.useRealTimers(); // Возвращаем настоящие таймеры
    });

    it('should return the current time', () => {
        const { result } = renderHook(() => useCurrentTime());

        // Проверяем, что хук возвращает строку с текущим временем
        expect(result.current).toBeDefined();
        expect(typeof result.current).toBe('string');
    });

    it('should update the time every second', () => {
        const { result } = renderHook(() => useCurrentTime());

        const initialTime = result.current;

        // Перемещаем время вперед на 1 секунду
        act(() => {
            jest.advanceTimersByTime(1000);
        });

        const updatedTime = result.current;

        // Проверяем, что время обновилось
        expect(updatedTime).not.toBe(initialTime);
    });

    it('should clear the interval on unmount', () => {
        const { unmount } = renderHook(() => useCurrentTime());

        // Спаиваемся, что setInterval был вызван
        expect(jest.getTimerCount()).toBe(1);

        // Размонтируем хук
        unmount();

        // Проверяем, что интервал был очищен
        expect(jest.getTimerCount()).toBe(0);
    });
});
