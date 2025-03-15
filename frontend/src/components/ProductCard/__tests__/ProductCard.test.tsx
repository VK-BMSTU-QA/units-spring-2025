import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from '../ProductCard';
import { getPrice } from '../../../utils';
import { PriceSymbol } from '../../../types/Symbol';
import { Category } from '../../../types/Category';

jest.mock('../../../utils', () => ({
    getPrice: jest.fn((price, symbol) => `${symbol}${price}`),
}));

afterEach(jest.clearAllMocks);

const defaultProps = {
    name: 'IPhone 14 Pro',
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$' as PriceSymbol,
    category: 'Электроника' as Category,
    id: 1,
    imgUrl: '/mock-image.jpg',
};

describe('test ProductCard component', () => {
    it('should render correctly and match snapshot', () => {
        const rendered = render(<ProductCard {...defaultProps} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render the product name', () => {
        render(<ProductCard {...defaultProps} />);
        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
    });

    it('should render the product description', () => {
        render(<ProductCard {...defaultProps} />);
        expect(
            screen.getByText('Latest iphone, buy it now')
        ).toBeInTheDocument();
    });

    it('should render the product price with symbol', () => {
        render(<ProductCard {...defaultProps} />);
        expect(screen.getByText('$999')).toBeInTheDocument();
        expect(getPrice).toHaveBeenCalledWith(999, '$');
    });

    it('should render the product category', () => {
        render(<ProductCard {...defaultProps} />);
        expect(screen.getByText('Электроника')).toBeInTheDocument();
    });

    it('should render an image if imgUrl is provided', () => {
        render(<ProductCard {...defaultProps} />);
        const image = screen.getByAltText('IPhone 14 Pro');
        expect(image).toBeInTheDocument();
        expect(image).toHaveAttribute('src', '/mock-image.jpg');
    });

    it('should not render an image if imgUrl is not provided', () => {
        render(<ProductCard {...defaultProps} imgUrl={undefined} />);
        const image = screen.queryByAltText('IPhone 14 Pro');
        expect(image).not.toBeInTheDocument();
    });
});
