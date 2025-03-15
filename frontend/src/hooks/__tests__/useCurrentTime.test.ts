import { renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';
import { act } from 'react-dom/test-utils';

describe('test current time', () => {
    const mockDate = Date.now();
    
    beforeEach(() => {
        jest.useFakeTimers();
        jest.spyOn(global, 'setInterval');
        jest.spyOn(global, 'clearInterval');

        jest.setSystemTime(mockDate);
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

    it('should update time every second', () => {
        const { result } = renderHook(() => useCurrentTime());
        
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        expect(result.current).toBe(new Date(mockDate + 1000).toLocaleTimeString('ru-RU'));

        act(() => {
            jest.advanceTimersByTime(1000);
        });
        expect(result.current).toBe(new Date(mockDate + 2000).toLocaleTimeString('ru-RU'));
    });

    it('should clear interval on unmount', () => {
        const { unmount } = renderHook(() => useCurrentTime());
        unmount();

        expect(clearInterval).toHaveBeenCalledTimes(1);
    });
});
