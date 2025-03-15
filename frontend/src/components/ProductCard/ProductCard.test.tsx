import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';

jest.mock('../../utils', () => ({
    getPrice: jest.fn((price, symbol) => `${price} ${symbol}`),
}));

afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const product: Product = {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        };

        const rendered = render(<ProductCard {...product} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render without optional field imgUrl', () => {
        const product: Product = {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        };

        const rendered = render(<ProductCard {...product} />);

        expect(rendered.getByText(product.name)).toBeInTheDocument();
        expect(rendered.getByText(product.description)).toBeInTheDocument();
        expect(rendered.getByText('1000 ₽')).toBeInTheDocument();
        expect(rendered.getByText(product.category)).toBeInTheDocument();

        expect(rendered.queryByAltText(product.name)).toBeNull();
    });

    it('should render with optional field imgUrl', () => {
        const product: Product = {
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            priceSymbol: '$',
            category: 'Для дома',
            imgUrl: '/lamp.png',
        };

        const rendered = render(<ProductCard {...product} />);

        expect(rendered.getByText(product.name)).toBeInTheDocument();
        expect(rendered.getByText(product.description)).toBeInTheDocument();
        expect(rendered.getByText('699 $')).toBeInTheDocument();
        expect(rendered.getByText(product.category)).toBeInTheDocument();

        expect(rendered.queryByAltText(product.name)).toBeInTheDocument();
    });
});
