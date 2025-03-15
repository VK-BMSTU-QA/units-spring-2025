import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';

afterEach(jest.clearAllMocks);

describe('Product card test', () => {
    it('should render correctly', () => {

        const rendered = render(<ProductCard name='name' description='description' price={1} id={1} category='Для дома' priceSymbol='$' imgUrl='img' />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should be correct name and another field', () => {
        const rendered = render(<ProductCard name='name' description='description' price={1} id={1} category='Для дома' priceSymbol='$' imgUrl='img' />);

        expect(rendered.getByText('name')).toHaveClass('product-card__name');
        expect(rendered.getByText('description')).toHaveClass('product-card__description');
        expect(rendered.getByText('1 $')).toHaveClass('product-card__price');
        expect(rendered.getByText('Для дома')).toHaveClass('product-card__category');
        expect(rendered.getByAltText('name')).toHaveClass('product-card__image')
    });
});