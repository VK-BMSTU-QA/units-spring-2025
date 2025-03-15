import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { MainPage } from './MainPage';
import { useProducts, useCurrentTime } from '../../hooks';
import { Categories } from '../../components';

// Мокаем хуки и компоненты
jest.mock('../../hooks', () => ({
    useProducts: jest.fn(),
    useCurrentTime: jest.fn(),
}));

jest.mock('../../components', () => ({
    Categories: jest.fn(({ selectedCategories, onCategoryClick }) => (
        <div>
            <button
                onClick={() => onCategoryClick({ id: 1, name: 'Category 1' })}
            >
                Category 1
            </button>
            <button
                onClick={() => onCategoryClick({ id: 2, name: 'Category 2' })}
            >
                Category 2
            </button>
        </div>
    )),
    ProductCard: jest.fn(({ name }) => <div>{name}</div>),
}));

describe('MainPage', () => {
    const mockProducts = [
        { id: 1, name: 'Product 1', categoryId: 1 },
        { id: 2, name: 'Product 2', categoryId: 2 },
        { id: 3, name: 'Product 3', categoryId: 1 },
    ];

    beforeEach(() => {
        (useProducts as jest.Mock).mockReturnValue(mockProducts);
        (useCurrentTime as jest.Mock).mockReturnValue('12:00');
    });

    test('renders MainPage with title and current time', () => {
        render(<MainPage />);

        expect(screen.getByText('VK Маркет')).toBeInTheDocument();
        expect(screen.getByText('12:00')).toBeInTheDocument();
    });

    test('renders Categories component', () => {
        render(<MainPage />);

        expect(screen.getByText('Category 1')).toBeInTheDocument();
        expect(screen.getByText('Category 2')).toBeInTheDocument();
    });

    test('renders product cards based on products', () => {
        render(<MainPage />);

        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.getByText('Product 2')).toBeInTheDocument();
        expect(screen.getByText('Product 3')).toBeInTheDocument();
    });

    test('filters products based on selected categories', () => {
        render(<MainPage />);

        // Изначально отображаются все продукты
        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.getByText('Product 2')).toBeInTheDocument();
        expect(screen.getByText('Product 3')).toBeInTheDocument();

        // Выбираем категорию 1
        fireEvent.click(screen.getByText('Category 1'));

        // Теперь должны отображаться только продукты из категории 1
        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.getByText('Product 3')).toBeInTheDocument();
        expect(screen.queryByText('Product 2')).not.toBeInTheDocument();

        // Выбираем категорию 2
        fireEvent.click(screen.getByText('Category 2'));

        // Теперь должны отображаться только продукты из категории 2
        expect(screen.queryByText('Product 1')).not.toBeInTheDocument();
        expect(screen.queryByText('Product 3')).not.toBeInTheDocument();
        expect(screen.getByText('Product 2')).toBeInTheDocument();
    });

    test('allows multiple category selection', () => {
        render(<MainPage />);

        // Изначально отображаются все продукты
        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.getByText('Product 2')).toBeInTheDocument();
        expect(screen.getByText('Product 3')).toBeInTheDocument();

        // Выбираем категорию 1
        fireEvent.click(screen.getByText('Category 1'));

        // Теперь должны отображаться только продукты из категории 1
        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.getByText('Product 3')).toBeInTheDocument();
        expect(screen.queryByText('Product 2')).not.toBeInTheDocument();

        // Выбираем категорию 2
        fireEvent.click(screen.getByText('Category 2'));

        // Теперь должны отображаться продукты из обеих категорий
        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.getByText('Product 2')).toBeInTheDocument();
        expect(screen.getByText('Product 3')).toBeInTheDocument();
    });

    test('displays no products when no categories are selected', () => {
        render(<MainPage />);

        // Изначально отображаются все продукты
        expect(screen.getByText('Product 1')).toBeInTheDocument();
        expect(screen.getByText('Product 2')).toBeInTheDocument();
        expect(screen.getByText('Product 3')).toBeInTheDocument();

        // Снимаем выбор всех категорий
        fireEvent.click(screen.getByText('Category 1'));
        fireEvent.click(screen.getByText('Category 2'));

        // Теперь не должно отображаться ни одного продукта
        expect(screen.queryByText('Product 1')).not.toBeInTheDocument();
        expect(screen.queryByText('Product 2')).not.toBeInTheDocument();
        expect(screen.queryByText('Product 3')).not.toBeInTheDocument();
    });
});
