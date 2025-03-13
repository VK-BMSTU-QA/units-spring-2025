import { fireEvent, renderHook } from "@testing-library/react";
import { useCurrentTime } from "../useCurrentTime";

describe("useOutsideClick", () => {
  test("should handle outside click", () => {
    const target = document.createElement("div");
    document.body.appendChild(target);

    const outside = document.createElement("div");
    document.body.appendChild(outside);

    const ref = {
      current: target,
    };
    const callback = jest.fn();

    const view = renderHook(() => useCurrentTime());

    expect(callback).toHaveBeenCalledTimes(0);
    fireEvent.click(outside);
    expect(callback).toHaveBeenCalledTimes(1);

    // Тестируем, что "removeEventListener" работает корректно,
    // проверяя после размонтирования, что коллбэк вызывался только один раз.
    jest.spyOn(document, "removeEventListener");

    view.unmount();
    expect(document.removeEventListener).toHaveBeenCalledTimes(1);

    fireEvent.click(outside);
    expect(callback).toHaveBeenCalledTimes(1);
  });
});