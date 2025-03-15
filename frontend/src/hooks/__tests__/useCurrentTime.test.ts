import { renderHook, act } from "@testing-library/react";
import { useCurrentTime } from "../useCurrentTime";

const mockDate = new Date(2004, 9, 12, 20);

describe("useCurrentTime", () => {

  beforeEach(() => {
    jest.useFakeTimers();
    jest.spyOn(global, 'setInterval');
    jest.spyOn(global, 'clearInterval');
    jest.setSystemTime(mockDate);
  });


  it('initial time', () => {
    const { result } = renderHook(() => useCurrentTime());

    expect(setInterval).toHaveBeenCalledTimes(1);
    expect(clearInterval).toHaveBeenCalledTimes(0);
    expect(result.current).toBe("20:00:00");
  });

  it('clearInterval and setInterval by advanceTimer', () => {
      const { result } = renderHook(() => useCurrentTime());
      act(() => {
          jest.advanceTimersByTime(61000);
      });
      expect(result.current).toBe("20:01:01");
      expect(clearInterval).toHaveBeenCalledTimes(1);
      expect(setInterval).toHaveBeenCalledTimes(2);
    });

  it('unmount', () => {
    const { unmount } = renderHook(() => useCurrentTime());
    unmount();
    expect(clearInterval).toHaveBeenCalledTimes(1);
    expect(setInterval).toHaveBeenCalledTimes(1);
  });

});
