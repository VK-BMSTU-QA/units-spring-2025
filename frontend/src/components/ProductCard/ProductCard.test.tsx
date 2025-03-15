import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { getPrice } from '../../utils';

afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard id={1} name="name" description="description" price={1} priceSymbol='$' category="Для дома" imgUrl='imgUrl' />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should have all and image ', () => {
        const rendered = render(<ProductCard id={1} name="name" description="description" price={1} priceSymbol='$' category="Для дома" imgUrl='/imgUrl.png' />);

        expect(rendered.getByText('name')).toHaveClass(
            'product-card__name'
        );
        expect(rendered.getByText('description')).toHaveClass(
            'product-card__description'
        );
        expect(rendered.getByText('1 $')).toHaveClass(
            'product-card__price'
        );
        expect(rendered.getByText('Для дома')).toHaveClass(
            'product-card__category'
        );
        expect(rendered.getByAltText('name')).toHaveClass(
            'product-card__image'
        );

    });

    it('should have all but img', () => {
        const rendered = render(<ProductCard id={1} name="name" description="description" price={1} priceSymbol='₽' category="Для дома"/>);

        expect(rendered.getByText('name')).toHaveClass(
            'product-card__name'
        );
        expect(rendered.getByText('description')).toHaveClass(
            'product-card__description'
        );
        expect(rendered.getByText('1 ₽')).toHaveClass(
            'product-card__price'
        );
        expect(rendered.getByText('Для дома')).toHaveClass(
            'product-card__category'
        );
        expect(rendered.queryByAltText('name')).not.toBeInTheDocument();

    });

});
