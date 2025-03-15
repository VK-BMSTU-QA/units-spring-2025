import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

afterEach(jest.clearAllMocks);

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should show output without filter', () => {
        const rendered = render(<MainPage />);

        const categories = ['Одежда', 'Для дома', 'Электроника'];
        const productCategories = document.querySelectorAll('.product-card__category');
        productCategories.forEach((category) => {
            expect(categories).toContain(category.textContent);
        })
    });

    it('should filter output by one category', () => {
        const rendered = render(<MainPage />);

        fireEvent.click(rendered.getByTestId('Одежда'));
        const productCategories = document.querySelectorAll('.product-card__category');
        productCategories.forEach((category) => {
            expect(category.textContent).toBe("Одежда");
        })
    });

    it('should filter output by multiple categories', () => {
        const rendered = render(<MainPage />);

        fireEvent.click(rendered.getByTestId('Одежда'));
        fireEvent.click(rendered.getByTestId('Электроника'));
        const productCategories = document.querySelectorAll('.product-card__category');
        productCategories.forEach((category) => {
            expect(['Одежда', 'Электроника']).toContain(category.textContent);
        })
    });

    it('should show correct time', () => {
        jest.useFakeTimers().setSystemTime(new Date('2025-03-15T00:00:00'));
    
        const rendered = render(<MainPage />);
    
        expect(rendered.getByTestId("time").textContent).toBe("00:00:00");
    });
});
