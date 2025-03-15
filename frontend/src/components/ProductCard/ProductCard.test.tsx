import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';
import { getPrice } from '../../utils';

afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    const products : Product[] = [
        {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        },
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
        {
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            category: 'Для дома',
            imgUrl: '/lamp.png',
        },
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
    ];


    it('should render correctly', () => {
        const card = render(<ProductCard {...products[0]} />);
        expect(card.asFragment()).toMatchSnapshot();
    });

    it('should show product data', () => {

        render(<ProductCard {...products[0]} />)

        expect(document.querySelector('.product-card__name')?.textContent).toEqual(products[0].name);
        expect(document.querySelector('.product-card__description')?.textContent).toEqual(products[0].description);
        expect(document.querySelector('.product-card__price')?.textContent).toEqual(getPrice(products[0].price, products[0].priceSymbol));
        expect(document.querySelector('.product-card__category')?.textContent).toEqual(products[0].category);
    });

    it('should render without image', () => {
        const rendered = render(<ProductCard {...products[1]} />);
        expect(rendered.queryByRole('img')).toBeNull();
    });

    it('should render without default symbol', () => {
        const rendered = render(<ProductCard {...products[2]} />);
        const price: string = getPrice(products[2].price);
        expect(rendered.getByText(price)).toBeInTheDocument();
      });
});
