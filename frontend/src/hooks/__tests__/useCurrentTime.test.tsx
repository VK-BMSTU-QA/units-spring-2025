import { useCurrentTime } from '../useCurrentTime';
import { act, renderHook } from '@testing-library/react';

describe('Test useCurrentTime hook', () => {
    beforeAll(() => {
        jest.useFakeTimers().setSystemTime(new Date('2025-03-15 00:00:00'));
    });

    afterAll(() => {
        jest.setSystemTime();
    });

    it('should return current time', () => {
        const renderedHook = renderHook(() => useCurrentTime());
        expect(renderedHook.result.current).toEqual('00:00:00');
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        renderedHook.rerender();
        expect(renderedHook.result.current).toEqual('00:00:01');
    });
});