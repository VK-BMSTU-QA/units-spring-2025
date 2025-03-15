import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import type { Product } from '../../types';
import { getPrice } from '../../utils';

jest.mock('../../utils', () => ({
    getPrice: jest.fn(),
}));

afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    let product: Product;

    beforeEach(() => {
        product = {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        };
    });

    it('should render correctly', () => {
        (getPrice as jest.Mock).mockReturnValue('999 $');
        const rendered = render(<ProductCard {...product} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call getPrice 1 time', () => {
        (getPrice as jest.Mock).mockReturnValue('999 $');
        const productWithRubles: Product = {
            ...product,
        };
        const { getByText } = render(<ProductCard {...productWithRubles} />);
        expect(getPrice).toHaveBeenCalledTimes(1);
        expect(getByText('999 $')).toBeInTheDocument();
    });

    it('should not render image if imgUrl is not provided', () => {
        const productWithoutImage: Product = {
            ...product,
            imgUrl: undefined,
        };
        const { queryByAltText } = render(
            <ProductCard {...productWithoutImage} />
        );
        expect(queryByAltText(product.name)).not.toBeInTheDocument();
    });

    it('should render price correctly without priceSymbol', () => {
        (getPrice as jest.Mock).mockReturnValue('999');

        const productWithoutPriceSymbol: Product = {
            ...product,
            priceSymbol: undefined,
        };
        const { getByText } = render(
            <ProductCard {...productWithoutPriceSymbol} />
        );
        expect(getPrice).toHaveBeenCalledWith(999, undefined);
        expect(getByText('999')).toBeInTheDocument();
    });
});
