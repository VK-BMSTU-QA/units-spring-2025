import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import type { Product } from '../../types';

afterEach(jest.clearAllMocks);
jest.mock('../../utils', () => {
    return {
        getPrice: jest.fn(() => '1 $'),
    }
})

const product: Product = {
    id: 1,
    price: 1,
    name: 'name',
    description: 'description',
    category: 'Для дома',
    priceSymbol: '$',
    imgUrl: 'img'
}

describe('Product card test', () => {

    it('should render correctly', () => {
        const rendered = render(<ProductCard {...product} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should be correct field and check getPrice', () => {
        const { getPrice } = jest.requireMock('../../utils');
        const rendered = render(<ProductCard {...product} />);

        expect(rendered.getByText('name')).toHaveClass('product-card__name');
        expect(rendered.getByText('description')).toHaveClass('product-card__description');
        expect(rendered.getByText('1 $')).toHaveClass('product-card__price');
        expect(rendered.getByText('Для дома')).toHaveClass('product-card__category');
        expect(rendered.getByAltText('name')).toHaveClass('product-card__image');

        expect(getPrice).toHaveBeenCalledTimes(1);
        expect(getPrice).toHaveBeenLastCalledWith(1, '$');
        expect(getPrice).toHaveReturnedWith('1 $');
    });

    it('render without img', () => {
        const rendered = render(<ProductCard name={product.name} description={product.description} price={product.price}
            id={product.id} category={product.category} priceSymbol={product.priceSymbol} />);

        expect(rendered.container.querySelector('.product-card__image')).not.toBeInTheDocument();
    });
});