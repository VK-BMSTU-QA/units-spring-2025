import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { productWithImage, productWithImageAndPriceSymbol, productWithPriceSymbol, simpleProduct } from '../../types/mocks/Products';
import { getPrice } from '../../utils';


describe('test product card', () => {
    it('should render product correctly', () => {    
        const rendered = render(<ProductCard {...simpleProduct} />)        
        
        expect(rendered.getByText(simpleProduct.name)).toBeInTheDocument();
        expect(rendered.getByText(simpleProduct.description)).toBeInTheDocument();
        expect(rendered.getByText(simpleProduct.category)).toBeInTheDocument();
        expect(
            rendered.getByText(
                getPrice(simpleProduct.price, simpleProduct.priceSymbol),
                { trim: false, collapseWhitespace: false },
            )
        ).toBeInTheDocument();

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render product with image correctly', () => {
        const rendered = render(<ProductCard {...productWithImage} />)
        
        expect(rendered.queryByRole('img')).toBeInTheDocument();
    });

    it('should render product with price symbol correctly', () => {
        const rendered = render(<ProductCard {...productWithPriceSymbol} />)

        expect(
            rendered.getByText(
                getPrice(productWithPriceSymbol.price, productWithPriceSymbol.priceSymbol),
                { trim: false, collapseWhitespace: false },
            )
        ).toBeInTheDocument();
    });

    it('should render product with image and price symbol correctly', () => {
        const rendered = render(<ProductCard {...productWithImageAndPriceSymbol} />)
        
        expect(rendered.queryByRole('img')).toBeInTheDocument();
        expect(
            rendered.getByText(
                getPrice(productWithImageAndPriceSymbol.price, productWithImageAndPriceSymbol.priceSymbol),
                { trim: false, collapseWhitespace: false },
            )
        ).toBeInTheDocument();
    });
});
