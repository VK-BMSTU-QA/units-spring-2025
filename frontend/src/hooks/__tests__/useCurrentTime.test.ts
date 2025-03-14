import { renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime hook test', () => {
    beforeAll(() => {
        jest.useFakeTimers().setSystemTime(new Date('1979-01-01T00:00:00Z'));
    });

    afterAll(() => {
        jest.useRealTimers();
        jest.restoreAllMocks();
    });

    it('should correctly initialize time and set an interval for updates', () => {
        jest.spyOn(global, 'setInterval');
        const oldDate = Date;
        const mockDate = jest
            .spyOn(global, 'Date')
            .mockImplementation((val) => {
                return new oldDate(val);
            });
        renderHook(() => useCurrentTime());
        expect(setInterval).toHaveBeenCalledTimes(1);
        expect(mockDate).toHaveBeenCalledTimes(1);
    });
});
