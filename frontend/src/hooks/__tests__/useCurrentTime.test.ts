import { fireEvent, renderHook } from "@testing-library/react";
import { useCurrentTime } from "../useCurrentTime";

describe("useCurrentTime", () => {
  it("should useCurrentTime correct", () => {
    const date = new Date(2004, 9, 12, 20);
    const spy = jest.spyOn(global, 'Date').mockImplementation(() => date);
    const useCurrentTimeResult  = (renderHook(() => useCurrentTime())).result.current;
    expect(spy).toBeCalledTimes(1);
    expect(useCurrentTimeResult).toBe(date.toLocaleTimeString('ru-RU'))
    spy.mockRestore();
  });
}); 