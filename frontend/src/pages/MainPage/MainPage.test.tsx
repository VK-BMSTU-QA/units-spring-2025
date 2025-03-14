import React from 'react';
import { fireEvent, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import * as applyCategories from '../../utils/applyCategories';

const currentTime = '12:00:00';

jest.mock('../../hooks/useCurrentTime', () => ({
    useCurrentTime: jest.fn(() => currentTime),
}));

afterEach(jest.clearAllMocks);

describe('test main page', () => {
    it('should render main page correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render current time', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getByText(currentTime)).toBeInTheDocument();
    });

    it('should filter products when category is selected', () => {
        const spyApplyCategories = jest.spyOn(applyCategories, 'applyCategories');
        const rendered = render(<MainPage />);

        const electronicsCategory = rendered.getAllByText('Электроника');
        expect(electronicsCategory.length).toBe(3);

        expect(spyApplyCategories).toHaveBeenCalledTimes(1);
        fireEvent.click(electronicsCategory[0]);
        expect(spyApplyCategories).toHaveBeenCalledTimes(2);

        const clothesCategory = rendered.getAllByText('Одежда');
        expect(clothesCategory.length).toBe(1);
    });
});
