import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';

afterEach(jest.clearAllMocks);

describe('Product card test', () => {
    it('should render correctly', () => {
        const rendered = render(
            <ProductCard
                name="Mazda"
                description="Best Japan auto"
                price={9999494}
                priceSymbol="$"
                category="Электроника"
                id={1001}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should not contain image when no imgUrl', () => {
        const rendered = render(
            <ProductCard
                name="Dodge"
                description="Best American auto"
                price={983453}
                priceSymbol="$"
                category="Электроника"
                id={1002}
            />
        );

        expect(rendered.baseElement).not.toContainHTML('img');
    });

    it('should contain image when imgUrl is provided', () => {
        const rendered = render(
            <ProductCard
                name="BelAZ"
                description="Best Belarus auto"
                price={98765432}
                priceSymbol="$"
                category="Электроника"
                id={1003}
                imgUrl="/belaz.jpg"
            />
        );
        expect(rendered.baseElement).toContainHTML('img');
    });
});
