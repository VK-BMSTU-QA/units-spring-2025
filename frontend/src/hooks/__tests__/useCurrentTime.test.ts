import { act, renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime test', () => {
    it('has correct initial value', () => {
        const mockDate = new Date(2025, 3, 13, 20, 0, 0);
        jest.spyOn(global, 'Date').mockImplementation(() => mockDate);

        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(mockDate.toLocaleTimeString());

        jest.restoreAllMocks();
    });

    it('updates time', () => {
        jest.useFakeTimers();

        const mockDate = new Date(2025, 3, 13, 20, 0, 0);
        jest.spyOn(global, 'Date').mockImplementation(() => mockDate);
        const hook = renderHook(() => useCurrentTime());
        mockDate.setSeconds(mockDate.getSeconds() + 5);
        act(() => {
            jest.advanceTimersByTime(5000);
        });
        expect(hook.result.current).toBe(mockDate.toLocaleTimeString());

        jest.useRealTimers();
        jest.restoreAllMocks();
    });
});
