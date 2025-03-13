import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types/Product';

const product: Product = {
    id: 1,
    name: 'Test Product',
    description: 'Test Description',
    price: 100,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: 'test-image.jpg',
};

describe('ProductCard', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard {...product} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('renders all product details correctly', () => {
        const { getByText, getByAltText } = render(<ProductCard {...product} />);

        expect(getByText(product.name)).toBeInTheDocument();
        expect(getByText(product.description)).toBeInTheDocument();
        expect(getByText('100 $')).toBeInTheDocument();
        expect(getByText(product.category)).toBeInTheDocument();

        const image = getByAltText(product.name);
        expect(image).toHaveAttribute('src', product.imgUrl);
        expect(image).toHaveClass('product-card__image');
    });

    it('does not render image when imgUrl is missing', () => {
        const productWithoutImage = { ...product, imgUrl: undefined };
        const { queryByRole } = render(<ProductCard {...productWithoutImage} />);

        expect(queryByRole('img')).not.toBeInTheDocument();
    });

    it('applies correct CSS classes', () => {
        const { container } = render(<ProductCard {...product} />);

        expect(container.firstChild).toHaveClass('product-card');
        expect(container.querySelector('.product-card__text')).toBeInTheDocument();
        expect(container.querySelector('.product-card__name')).toBeInTheDocument();
        expect(container.querySelector('.product-card__description')).toBeInTheDocument();
        expect(container.querySelector('.product-card__price')).toBeInTheDocument();
        expect(container.querySelector('.product-card__category')).toBeInTheDocument();
    });

    it('formats price correctly with symbol', () => {
        const customProduct: Product = { ...product, price: 50, priceSymbol: '₽' };
        const { getByText } = render(<ProductCard {...customProduct} />);

        expect(getByText('50 ₽')).toBeInTheDocument();
    });

    it('formats price correctly without symbol', () => {
        const customProduct: Product = { ...product, price: 50, priceSymbol: undefined };
        const { getByText } = render(<ProductCard {...customProduct} />);

        expect(getByText('50 ₽')).toBeInTheDocument();
    });
});