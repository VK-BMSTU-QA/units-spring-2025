import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';
import { getPrice } from '../../utils';

afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    it('should show product data', () => {
        const product : Product = {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
        }

        render(<ProductCard 
            id={product.id} 
            name={product.name} 
            description={product.description}
            price={product.price}
            priceSymbol={product.priceSymbol}
            category={product.category} />)

        expect(document.querySelector('.product-card__name')?.textContent).toEqual(product.name);
        expect(document.querySelector('.product-card__description')?.textContent).toEqual(product.description);
        expect(document.querySelector('.product-card__price')?.textContent).toEqual(getPrice(product.price, product.priceSymbol));
        expect(document.querySelector('.product-card__category')?.textContent).toEqual(product.category);

    });
});
