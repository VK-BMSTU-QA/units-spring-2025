import { render } from '@testing-library/react';
import React from 'react';
import { MainPage } from '../MainPage';

describe('Test MainPage component', () => {
    it('renders as in shapshot', () => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('1995-12-17T03:24:00'));
        const r = render(<MainPage />);
        expect(r.asFragment()).toMatchSnapshot();
    });
});
