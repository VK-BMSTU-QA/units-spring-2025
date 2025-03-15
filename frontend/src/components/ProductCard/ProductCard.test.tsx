import React from 'react';
import { render, screen } from '@testing-library/react';
import { ProductCard } from './ProductCard';
import { getPrice } from '../../utils';
import { Product } from '../../types/Product';
import '@testing-library/jest-dom';

jest.mock('../../utils', () => ({
    getPrice: jest.fn((price, symbol) => `${price}${symbol}`),
}));

describe('ProductCardTest', () => {
    const product:Product = {
        id: 10,
        name: 'Test Product',
        description: 'Test Description',
        price: 100,
        priceSymbol: '₽',
        imgUrl: 'https://example.com/image.jpg',
        category: 'Электроника',
    };
    it('should render correctly', () => {
        const rendered = render(<ProductCard {...product} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
    test('рендерит имя, описание, цену и категорию', () => {
        render(<ProductCard {...product} />);

        expect(screen.getByText('Test Product')).toBeInTheDocument();
        expect(screen.getByText('Test Description')).toBeInTheDocument();
        expect(screen.getByText('100₽')).toBeInTheDocument();
        expect(screen.getByText('Электроника')).toBeInTheDocument();
    });

    test('рендерит изображение, если передан imgUrl', () => {
        render(<ProductCard {...product} />);
        const image = screen.getByRole('img');
        expect(image).toHaveAttribute('src', 'https://example.com/image.jpg');
        expect(image).toHaveAttribute('alt', 'Test Product');
    });

    test('не рендерит изображение, если imgUrl не передан', () => {
        const { container } = render(<ProductCard {...product} imgUrl={undefined} />);
        expect(container.querySelector('img')).toBeNull();
    });

    test('вызывает getPrice с правильными аргументами', () => {
        render(<ProductCard {...product} />);
        expect(getPrice).toHaveBeenCalledWith(100, '₽');
    });
});
