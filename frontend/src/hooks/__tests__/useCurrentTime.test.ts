import React from 'react';
import '@testing-library/jest-dom';
import { act, renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

beforeEach(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date('2005-09-20T20:31:00'));
});

afterEach(jest.useRealTimers);

describe('UseCurrentTime hook test', () => {
    it('should return current time', () => {
        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toEqual('20:31:00');
    });

    it('should update current time every second', () => {
        const { result } = renderHook(() => useCurrentTime());

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).toEqual('20:31:01');
    });

    it('should clear interval on unmount', () => {
        const clearIntervalSpy = jest.spyOn(global, 'clearInterval');

        const { unmount } = renderHook(() => useCurrentTime());

        unmount();

        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
    });
});

