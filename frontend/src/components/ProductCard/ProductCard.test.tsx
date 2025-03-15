import React from "react";
import '@testing-library/jest-dom';
import { render } from '@testing-library/react';
import { ProductCard } from "./ProductCard";
import { Category, PriceSymbol } from "../../types";

afterEach(jest.clearAllMocks);


describe('ProductCard test', () => {
    const props = {
        name: 'product',
        description: 'product description',
        price: 120,
        priceSymbol: '$' as PriceSymbol,
        category: 'Одежда' as Category,
        imgUrl: '/lamp.png',
        id: 1
    };

    it('should render correctly', () => {
        const rendered = render(<ProductCard {...props}/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should display imgae if its url is given', () => {
        const rendered = render(<ProductCard {...props}/>);
        
        const image = rendered.getByAltText('product');
        expect(image).toBeInTheDocument();
        expect(image).toHaveAttribute('src', props.imgUrl);
    })

    it('should not display imgae if its url isnt given', () => {
        const emptyImgUrlProps = {...props, imgUrl: undefined};
        const rendered = render(<ProductCard {...emptyImgUrlProps}/>);
        
        const image = rendered.queryByAltText('product');
        expect(image).not.toBeInTheDocument();
    })
});