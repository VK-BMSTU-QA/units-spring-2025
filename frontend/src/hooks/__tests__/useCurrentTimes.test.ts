import { useCurrentTime } from '../useCurrentTime';
import React, { useDeferredValue } from 'react';
import { renderHook, act } from '@testing-library/react';

describe('test for use current time', () => {
    const defDate = new Date(1, 1, 1, 1, 0, 0);

    it('should return default date', () => {
        jest.spyOn(global, 'Date').mockImplementation(() => defDate);
        expect(renderHook(() => useCurrentTime()).result.current).toBe('01:00:00');

        jest.restoreAllMocks();
    });

    it('should return date with offset', () => {
        jest.useFakeTimers();
        jest.spyOn(global, 'Date').mockImplementation(() => defDate);

        const hook = renderHook(() => useCurrentTime());
        expect(hook.result.current).toBe('01:00:00')
        defDate.setSeconds(defDate.getSeconds() + 1)
        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(hook.result.current).toBe('01:00:01')
        jest.useRealTimers();
        jest.restoreAllMocks();

    });
});