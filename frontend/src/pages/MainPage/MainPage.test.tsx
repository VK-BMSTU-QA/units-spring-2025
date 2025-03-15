import React from 'react';
import { fireEvent, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import * as applyCategories from '../../utils/applyCategories';
import { useProducts } from '../../hooks';

const countProductsByCategory = (categories: string[]): number => {
    const products = useProducts();

    if (categories.length === 0) {
        return products.length;
    }
    
    return products.filter(
        (product) => categories.includes(product.category)
    ).length;
};

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
        const { container } = render(<MainPage />);

        const categories = container.querySelectorAll('.categories__badge');
        const electronicsCategory = Array.from(categories).find(
            (item) => item.textContent === 'Электроника'
        );
        expect(electronicsCategory).toBeInTheDocument();

        expect(spyApplyCategories).toHaveBeenCalledTimes(1);
        fireEvent.click(electronicsCategory!);
        expect(spyApplyCategories).toHaveBeenCalledTimes(2);

        const products = container.querySelectorAll('.product-card');
        expect(products.length).toBe(countProductsByCategory(['Электроника']));
    });

    it('should filter products when multiple categories are selected', () => {
        const spyApplyCategories = jest.spyOn(applyCategories, 'applyCategories');
        const { container } = render(<MainPage />);

        const categories = container.querySelectorAll('.categories__badge');
        
        const clothesCategory = Array.from(categories).find(
            (item) => item.textContent === 'Одежда'
        );
        expect(clothesCategory).toBeInTheDocument();

        expect(spyApplyCategories).toHaveBeenCalledTimes(1);
        fireEvent.click(clothesCategory!);
        expect(spyApplyCategories).toHaveBeenCalledTimes(2);

        const forHomeCategory = Array.from(categories).find(
            (item) => item.textContent === 'Для дома'
        );
        expect(forHomeCategory).toBeInTheDocument();

        expect(spyApplyCategories).toHaveBeenCalledTimes(2);
        fireEvent.click(forHomeCategory!);
        expect(spyApplyCategories).toHaveBeenCalledTimes(3);
        
        const products = container.querySelectorAll('.product-card');
        expect(products.length).toBe(countProductsByCategory(['Одежда', 'Для дома']));
    });
    
    it('should remove product filters when category is unselected', () => {
        const spyApplyCategories = jest.spyOn(applyCategories, 'applyCategories');
        const { container } = render(<MainPage />);

        const categories = container.querySelectorAll('.categories__badge');
        const electronicsCategory = Array.from(categories).find(
            (item) => item.textContent === 'Электроника'
        );
        fireEvent.click(electronicsCategory!);

        expect(spyApplyCategories).toHaveBeenCalledTimes(2);
        fireEvent.click(electronicsCategory!);
        expect(spyApplyCategories).toHaveBeenCalledTimes(3);

        const products = container.querySelectorAll('.product-card');
        expect(products.length).toBe(countProductsByCategory([]));
    });
});
