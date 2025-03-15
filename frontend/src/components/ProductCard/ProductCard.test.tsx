import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { getProducts } from '../../mocks/productMocks';
import { Product } from '../../types';
import { getPrice } from '../../utils';

describe('Product card test', () => {
    const products: Product[] = getProducts();

    it('rendered with image and price symbol', () => {
        const card = render(<ProductCard {...products[0]} />);
        expect(card.asFragment()).toMatchSnapshot();
    });

    it('rendered without image', () => {
        const card = render(<ProductCard {...products[1]} />);
        const price: string = getPrice(
            products[1].price,
            products[1]?.priceSymbol ?? '₽'
        );
        expect(card.asFragment()).toMatchSnapshot();
        expect(card.queryByRole('img')).toBeNull();
        expect(
            card.getByText(price, { trim: false, collapseWhitespace: false })
        ).toBeInTheDocument();
    });

    it('rendered without default symbol', () => {
        const card = render(<ProductCard {...products[2]} />);
        const price: string = getPrice(products[2].price);
        expect(card.asFragment()).toMatchSnapshot();
        expect(card.queryByRole('img')).toBeInTheDocument();
        expect(
            card.getByText(price, { trim: false, collapseWhitespace: false })
        ).toBeInTheDocument();
    });
});
