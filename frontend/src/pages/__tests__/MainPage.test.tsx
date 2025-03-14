import { render } from '@testing-library/react';
import { MainPage } from '../MainPage';

describe('test MainPage', () => {
    it('should return render snapshot', () => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('2025-03-14T00:00:00Z'));
        const r = render(<MainPage />);
        expect(r.asFragment()).toMatchSnapshot();
    });
});
