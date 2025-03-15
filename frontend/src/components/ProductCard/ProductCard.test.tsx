import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';

afterEach(jest.clearAllMocks);

describe('Product card test', () => {
    it('should render correctly', () => {
        const rendered = render(
            <ProductCard
                name="Test Card"
                description="Card for testing"
                price={1234}
                priceSymbol="$"
                category="Для дома"
                id={1234}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should not contain image when no imgUrl', () => {
        const rendered = render(
            <ProductCard
                name="Test Card"
                description="Card for testing"
                price={1234}
                priceSymbol="$"
                category="Для дома"
                id={1234}
            />
        );

        expect(rendered.baseElement).not.toContainHTML('img');
    });

    it('should contain image when imgUrl is provided', () => {
        const rendered = render(
            <ProductCard
                name="Test Card"
                description="Card for testing"
                price={1234}
                priceSymbol="$"
                category="Для дома"
                id={1234}
                imgUrl="/iphone.png"
            />
        );
        expect(rendered.baseElement).toContainHTML('img');
    });
});
