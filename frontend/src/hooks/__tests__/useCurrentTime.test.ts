import { act } from "react-dom/test-utils";
import { useCurrentTime } from "../useCurrentTime";
import { renderHook } from "@testing-library/react";

// We use some obscure timezone manipulations to
// ensure that in local time we got 00:00:00.
// and our tests are timezone independent
const timezoneOffsettedDate = new Date('2025-01-01');
const mockDate = new Date(timezoneOffsettedDate.getTime() + timezoneOffsettedDate.getTimezoneOffset() * 60 * 1000);

jest.useFakeTimers();
jest.setSystemTime(mockDate);
jest.spyOn(global, 'setInterval');

describe("testing use current time hook", () => {

    it('sets one second update interval', () => {
        renderHook(() => useCurrentTime());
        expect(setInterval).toHaveBeenCalledTimes(1);
        expect(setInterval).toHaveBeenLastCalledWith(expect.any(Function), 1000);
    })

    it('return current time', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe('00:00:00');
    });

    it('updates current time every second', () => {
        const { result } = renderHook(() => useCurrentTime());

        act(() => {
            jest.advanceTimersByTime(1000);
        });
        expect(result.current).toBe('00:00:01');

        act(() => {
            jest.advanceTimersByTime(1000);
        });
        expect(result.current).toBe('00:00:02');
    });
})
