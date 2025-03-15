import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Category, PriceSymbol } from '../../types';
import { getPrice } from '../../utils';

jest.mock('../../utils', () => ({
    getPrice: jest.fn((price, symbol) => `${price} ${symbol}`),
}));

afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    const symbol: PriceSymbol = '$';
    const category: Category = 'Для дома';
    const product = {
        id: 1,
        name: 'Product',
        description: '',
        price: 1,
        priceSymbol: symbol,
        category: category,
        imgUrl: 'test.png'
    }

    it('should render correctly', () => {
        const rendered = render(<ProductCard {...product} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should correctly show price', () => {
        const rendered = render(<ProductCard {...product} />);

        expect(getPrice).toHaveBeenCalledTimes(1);
        expect(getPrice).toHaveBeenCalledWith(product.price, product.priceSymbol);
        expect(rendered.getByText('1 $')).toBeInTheDocument();
    });

    it('should display the product image if imgUrl is provided', () => {
        const rendered = render(<ProductCard {...product} />);
        const image = rendered.getByAltText('Product');

        expect(image).toBeInTheDocument();
        expect(image).toHaveAttribute('src', 'test.png');
    });

    it('shouldnt display an image if imgUrl is not provided', () => {
        const productWithoutImage = { ...product, imgUrl: '' };
        const rendered = render(<ProductCard {...productWithoutImage} />);
        
        const image = rendered.queryByAltText('Product');
        expect(image).not.toBeInTheDocument();
    });
});
