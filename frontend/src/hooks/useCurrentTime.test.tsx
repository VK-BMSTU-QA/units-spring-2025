import React from 'react';
import { render, fireEvent, renderHook } from '@testing-library/react';
import '@testing-library/jest-dom';
import { useCurrentTime } from './useCurrentTime';
afterEach(jest.clearAllMocks);


describe("Тестирование счётчика", () => {
    it("Просто выдача времени", () => {
        const myTimeout = jest.spyOn(global, "setInterval").mockImplementation( )
         
        renderHook(useCurrentTime)
        expect(myTimeout).toHaveBeenCalledTimes(1);
        expect(myTimeout).toHaveBeenLastCalledWith(expect.any(Function), 1000);
    })
})