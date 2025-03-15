import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from '../MainPage';
import type { Category, Product } from '../../../types';

jest.mock('../../../hooks', () => ({
    useProducts: jest.fn(() => [
        { id: 1, name: 'Product 1', category: 'Электроника' } as Product,
        { id: 2, name: 'Product 2', category: 'Одежда' } as Product,
        { id: 3, name: 'Product 3', category: 'Для дома' } as Product,
    ]),
    useCurrentTime: jest.fn(() => '12:00:00'),
}));

jest.mock('../../../components/Categories', () => ({
    Categories: ({
        selectedCategories,
        onCategoryClick,
    }: {
        selectedCategories: Category[];
        onCategoryClick?: (category: Category) => void;
    }) => (
        <div data-testid="categories">
            {['Электроника', 'Одежда', 'Для дома'].map((category) => (
                <button
                    key={category}
                    onClick={() => onCategoryClick?.(category as Category)}
                    data-testid={`category-${category}`}
                >
                    {category}
                </button>
            ))}
        </div>
    ),
}));

jest.mock('../../../components/ProductCard', () => ({
    ProductCard: ({ name }: { name: string }) => (
        <div data-testid="product-card">{name}</div> // Добавляем data-testid
    ),
}));

jest.mock('../../../utils', () => ({
    applyCategories: (products: Product[], categories: Category[]) =>
        categories.length
            ? products.filter((p: Product) => categories.includes(p.category))
            : products,
    updateCategories: (current: Category[], changed: Category) =>
        current.includes(changed)
            ? current.filter((c: Category) => c !== changed)
            : [...current, changed],
}));

describe('MainPage test', () => {
    it('should match the snapshot', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render the current time', () => {
        render(<MainPage />);
        expect(screen.getByText('12:00:00')).toBeInTheDocument();
    });

    it('should render the categories', () => {
        render(<MainPage />);
        expect(screen.getByTestId('category-Одежда')).toBeInTheDocument();
        expect(screen.getByTestId('category-Для дома')).toBeInTheDocument();
        expect(screen.getByTestId('category-Электроника')).toBeInTheDocument();
    });

    it('should render all products when no category is selected', () => {
        render(<MainPage />);
        expect(screen.getAllByTestId('product-card')).toHaveLength(3);
    });

    it('should filter products when a category is selected', () => {
        render(<MainPage />);
        fireEvent.click(screen.getByTestId('category-Электроника'));
        expect(screen.getAllByTestId('product-card')).toHaveLength(1);
        expect(screen.getByText('Product 1')).toBeInTheDocument();
    });

    it('should clear the filter when the same category is clicked again', () => {
        render(<MainPage />);
        fireEvent.click(screen.getByTestId('category-Электроника'));
        fireEvent.click(screen.getByTestId('category-Электроника'));
        expect(screen.getAllByTestId('product-card')).toHaveLength(3);
    });
});
