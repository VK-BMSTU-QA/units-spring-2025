import { renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('test current time', () => {
    beforeEach(() => {
        jest.useFakeTimers();
        jest.spyOn(global, 'setInterval');
        jest.spyOn(global, 'clearInterval');
    });

    afterEach(() => {
        jest.useRealTimers();
        jest.restoreAllMocks();
    });

    it('should return initial time', () => {
        const { result } = renderHook(() => useCurrentTime());
        
        expect(setInterval).toHaveBeenCalledTimes(1);
        expect(result.current).toBe(new Date().toLocaleTimeString('ru-RU'));
    });

    it('should clear interval on unmount', () => {
        const { unmount } = renderHook(() => useCurrentTime());
        unmount();

        expect(clearInterval).toHaveBeenCalledTimes(1);
    });
});
