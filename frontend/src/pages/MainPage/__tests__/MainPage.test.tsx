import { render } from '@testing-library/react';
import React from 'react';
import { MainPage } from '../MainPage';

describe('Test MainPage component', () => {
    it('renders as in shapshot', () => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('2004-07-10'));
        const r = render(<MainPage />);
        expect(r.asFragment()).toMatchSnapshot();
    });
});
