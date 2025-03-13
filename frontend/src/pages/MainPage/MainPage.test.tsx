import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useProducts } from '../../hooks/useProducts';
import { useCurrentTime } from '../../hooks/useCurrentTime';
import { applyCategories, updateCategories } from '../../utils';
import { Product } from '../../types/Product';
import { ProductCard } from "../../components";
import { Category } from "../../types/Category";

jest.mock('../../hooks/useProducts', () => ({
    useProducts: jest.fn(),
}));

jest.mock('../../hooks/useCurrentTime', () => ({
    useCurrentTime: jest.fn(),
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn(),
    updateCategories: jest.fn(),
    getPrice: jest.fn((price: number, symbol: string) => `${price}${symbol}`),
}));

const mockProducts: Array<Product> = [
    {
        id: 1,
        name: 'Product 1',
        description: 'test',
        price: 12,
        priceSymbol: '$',
        imgUrl: './img.png',
        category: 'Одежда',
    },
    {
        id: 2,
        name: 'Product 2',
        description: 'test',
        price: 12,
        priceSymbol: '$',
        imgUrl: './img.png',
        category: 'Электроника',
    },
];

const titleOfPage = 'VK Маркет';
const mockSelectedCategories = ['Одежда'];
const time = '20:22:56';

describe('MainPage Component', () => {
    beforeEach(() => {
        (useProducts as jest.Mock).mockReturnValue(mockProducts);
        (useCurrentTime as jest.Mock).mockReturnValue(time);
        (applyCategories as jest.Mock).mockImplementation(
            (products: Array<Product>, categories) =>
                products.filter((product: Product) =>
                    categories.includes(product.category)
                )
        );

        (updateCategories as jest.Mock).mockImplementation(
            (categories, clickedCategory) =>
                categories.includes(clickedCategory)
                    ? categories.filter((cat: Category) => cat !== clickedCategory)
                    : [...categories, clickedCategory]
        );
    });

    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('renders the title, current time, and categories', () => {
        const { container } = render(<MainPage />);

        expect(screen.getByText(titleOfPage)).toBeInTheDocument();
        expect(screen.getByText(time)).toBeInTheDocument();
        expect(container.getElementsByClassName('categories__badge').length).toBe(3);
    });

    it('updates selected categories when a category is clicked', () => {
        const { container} = render(<MainPage />);

        const categoryButton = container.getElementsByClassName('categories__badge')[0]
        fireEvent.click(categoryButton);

        expect(updateCategories).toHaveBeenCalledWith([], 'Одежда');
    });

    it('filters products based on selected categories', () => {
        const { container} = render(<MainPage />);

        const categoryButton = container.getElementsByClassName('categories__badge')[0]
        fireEvent.click(categoryButton);

        expect(applyCategories).toHaveBeenCalledWith(
            mockProducts,
            mockSelectedCategories
        );

        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.queryByText('Product 2')).not.toBeInTheDocument();
    });

    it('clears selected categories when a selected category is clicked again', () => {
        const { container} = render(<MainPage />);

        const categoryButton = container.getElementsByClassName('categories__badge')[0]
        fireEvent.click(categoryButton);

        fireEvent.click(categoryButton);

        expect(updateCategories).toHaveBeenCalledWith(
            ['Одежда'],
            'Одежда'
        );
    });
});
