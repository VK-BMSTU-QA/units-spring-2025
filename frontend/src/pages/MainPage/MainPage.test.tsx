import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime, useProducts } from '../../hooks';
import { applyCategories } from '../../utils';

jest.mock('../../hooks', () => ({
    useCurrentTime: jest.fn(),
    useProducts: jest.fn(),
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn(),
    updateCategories: jest.fn((selectedCategories: string[], clickedCategory: string) => {
        if (selectedCategories.includes(clickedCategory)) {
            return selectedCategories.filter((category: string) => category !== clickedCategory);
        }
        return [...selectedCategories, clickedCategory];
    }),
}));

jest.mock('../../components', () => ({
    Categories: ({ selectedCategories, onCategoryClick }: any) => (
        <div>
            <button onClick={() => onCategoryClick('Category1')}>Category1</button>
            <button onClick={() => onCategoryClick('Category2')}>Category2</button>
        </div>
    ),
    ProductCard: ({ name }: any) => <div>{name}</div>,
}));

describe('MainPage test', () => {
    beforeEach(() => {
        (useCurrentTime as jest.Mock).mockReturnValue('12:00:00');
        (useProducts as jest.Mock).mockReturnValue([
            { id: 1, name: 'Product1', category: 'Category1' },
            { id: 2, name: 'Product2', category: 'Category2' },
        ]);
        (applyCategories as jest.Mock).mockImplementation((products, selectedCategories) => {
            if (selectedCategories.length === 0) { 
                return products;
            };
            return products.filter((product: { id: number; name: string; category: string }) =>
                selectedCategories.includes(product.category)
            );
        });
    });

    afterEach(jest.clearAllMocks);

    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render the page title and current time', () => {
        render(<MainPage />);

        expect(screen.getByText('VK Маркет')).toBeInTheDocument();
        expect(screen.getByText('12:00:00')).toBeInTheDocument();
    });

    it('should render all products when no category is selected', () => {
        render(<MainPage />);

        expect(screen.getByText('Product1')).toBeInTheDocument();
        expect(screen.getByText('Product2')).toBeInTheDocument();
    });

    it('should filter products by selected category', () => {
        render(<MainPage />);

        fireEvent.click(screen.getByText('Category1'));

        expect(screen.getByText('Product1')).toBeInTheDocument();
        expect(screen.queryByText('Product2')).not.toBeInTheDocument();

        fireEvent.click(screen.getByText('Category2'));

        expect(screen.getByText('Product1')).toBeInTheDocument();
        expect(screen.getByText('Product2')).toBeInTheDocument();
    });

    it('should clear the filter when the same category is clicked again', () => {
        render(<MainPage />);

        fireEvent.click(screen.getByText('Category1'));

        expect(screen.getByText('Product1')).toBeInTheDocument();
        expect(screen.queryByText('Product2')).not.toBeInTheDocument();

        fireEvent.click(screen.getByText('Category1'));

        expect(screen.getByText('Product1')).toBeInTheDocument();
        expect(screen.getByText('Product2')).toBeInTheDocument();
    });
});
