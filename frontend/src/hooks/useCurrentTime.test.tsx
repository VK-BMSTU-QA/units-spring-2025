import React from 'react';
import { render, act } from '@testing-library/react';
import '@testing-library/jest-dom';
import { useCurrentTime } from './useCurrentTime';

const date: string = '2025-13-03T20:12:56';

jest.useFakeTimers().setSystemTime(new Date(date));

const mockDate = new Date(date);

describe('useCurrentTime hook', () => {
    afterEach(() => {
        jest.restoreAllMocks();
    });

    it('should initialize with current time', () => {
        const TestComponent = () => {
            const time = useCurrentTime();
            return <div>{time}</div>;
        };

        const { getByText } = render(<TestComponent />);
        expect(getByText(mockDate.toLocaleTimeString('ru-RU'))).toBeInTheDocument();
    });

    it('should update time every second', () => {
        const TestComponent = () => {
            const time = useCurrentTime();
            return <div>{time}</div>;
        };

        const { getByText } = render(<TestComponent />);

        const initialTime = mockDate.toLocaleTimeString('ru-RU');
        expect(getByText(initialTime)).toBeInTheDocument();

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        const updatedTime = new Date(mockDate.getTime() + 1000).toLocaleTimeString('ru-RU');
        expect(getByText(updatedTime)).toBeInTheDocument();
    });

    it('should clear interval on unmount', () => {
        const clearIntervalSpy = jest.spyOn(window, 'clearInterval');
        const TestComponent = () => {
            useCurrentTime();
            return <div>Test</div>;
        };

        const { unmount } = render(<TestComponent />);
        expect(clearIntervalSpy).not.toHaveBeenCalled();

        unmount();
        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
    });
});
