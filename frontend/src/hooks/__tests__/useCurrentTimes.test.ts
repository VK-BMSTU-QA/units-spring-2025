import { useCurrentTime } from '../useCurrentTime';
import React, { useDeferredValue } from 'react';
import { renderHook, act } from '@testing-library/react';

describe('test for use current time', () => {
    const defDate = new Date(1, 1, 1, 1, 0, 0);
    beforeEach(() => {
        jest.useFakeTimers();
        jest.spyOn(global, 'Date').mockImplementation(() => defDate);
    });

    afterEach(() => {
        jest.restoreAllMocks();
        jest.useRealTimers();
    });

    it('should return default date', () => {
        expect(renderHook(() => useCurrentTime()).result.current).toBe('01:00:00');
    });

    it('should return date with offset', () => {
        const hook = renderHook(() => useCurrentTime());
        expect(hook.result.current).toBe('01:00:00')
        defDate.setSeconds(defDate.getSeconds() + 1);
        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(hook.result.current).toBe('01:00:01');
    });
});