import React from 'react';
import '@testing-library/jest-dom';
import { render, act } from '@testing-library/react';
import { useCurrentTime } from './useCurrentTime';

function TestComponent() {
    const currentTime = useCurrentTime();
    return <div>{currentTime}</div>;
}

beforeEach(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date('2025-03-15T01:00:00'));
});

afterEach(jest.useRealTimers);

describe('UseCurrentTime hook test', () => {
    it('should return corret current time', () => {
        const component = render(<TestComponent />);

        expect(component.getByText('01:00:00')).toBeInTheDocument();
    })

    it('should return corret current time every second', () => {
        const component = render(<TestComponent />);

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(component.getByText('01:00:01')).toBeInTheDocument();
    });

    it('should clear interval on unmount', () => {
        const clearIntervalSpy = jest.spyOn(window, 'clearInterval');

        const { unmount } = render(<TestComponent />);

        unmount();
        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
    });
});
