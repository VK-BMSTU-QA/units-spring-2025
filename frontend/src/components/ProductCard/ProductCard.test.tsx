import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import '@testing-library/jest-dom';

import { ProductCard } from './ProductCard';
import { Product } from '../../types';

afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    const productCardDescription = 'ProductCardDescription';
    const productCardPrice = 123;
    const productCardPriceSymbol = '₽';
    const productCardCategory = 'Электроника';

    const productCardProps: Product = {
        id: 1,
        name: 'ProductCardName',
        description: productCardDescription,
        price: productCardPrice,
        priceSymbol: productCardPriceSymbol,
        category: productCardCategory,
        imgUrl: '/iphone.png',
    };

    it('should render correctly', () => {
        const rendered = render(
            <ProductCard {...productCardProps}></ProductCard>
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should have correct name', () => {
        const rendered = render(
            <ProductCard {...productCardProps}></ProductCard>
        );
        const productCardNameElement = screen.getByText('ProductCardName');

        expect(productCardNameElement).toBeInTheDocument();
    });

    it('should have correct description', () => {
        const rendered = render(
            <ProductCard {...productCardProps}></ProductCard>
        );
        const productCardDescriptionElement = screen.getByText(
            productCardDescription
        );

        expect(productCardDescriptionElement).toBeInTheDocument();
    });

    it('should have correct price', () => {
        const rendered = render(
            <ProductCard {...productCardProps}></ProductCard>
        );
        const productCardPriceElement = screen.getByText(
            `${productCardPrice} ${productCardPriceSymbol}`
        );

        expect(productCardPriceElement).toBeInTheDocument();
    });

    it('should have correct category', () => {
        const rendered = render(
            <ProductCard {...productCardProps}></ProductCard>
        );
        const productCardCategoryElement =
            screen.getByText(productCardCategory);

        expect(productCardCategoryElement).toBeInTheDocument();
    });
});
