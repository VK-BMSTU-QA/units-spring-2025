import { renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime hook test', () => {
    it('should call date and setTimeout', async () => {
        jest.useFakeTimers().setSystemTime(new Date('1979-01-01'));
        jest.spyOn(global, 'setTimeout');
        jest.spyOn(global, 'setInterval');
        const oldDate = Date;
        const myDate = jest.spyOn(global, 'Date').mockImplementation((stri) => {
            return new oldDate(stri);
        });

        renderHook(useCurrentTime);

        expect(setInterval).toHaveBeenCalledTimes(1);
        expect(myDate).toHaveBeenCalledTimes(1);
    });
});
