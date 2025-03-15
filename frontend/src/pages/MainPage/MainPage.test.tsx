import React from 'react';
import { fireEvent, render, within } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { Category, Product } from '../../types';
import { applyCategories, updateCategories } from '../../utils';

jest.mock('../../hooks', () => ({
    useCurrentTime: jest.fn(() => '20:31:00'),
    useProducts: jest.fn(() => [
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
    ]),
}));

jest.mock('../../utils', () => ({
    updateCategories: jest.fn((categories: Category[], category: Category) => {
        if (categories.includes(category)) {
            return categories.filter((c) => c !== category);
        }
        return [...categories, category];
    }),
    applyCategories: jest.fn((products: Product[], categories: Category) => {
        if (!categories.length) return products;
        return products.filter((product) =>
            categories.includes(product.category)
        );
    }),
    getPrice: jest.fn((price, symbol) => `${price} ${symbol}`),
}));

afterEach(jest.clearAllMocks);

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should update selected categories and display filtered products', () => {
        const rendered = render(<MainPage />);

        const parametersContainer =
            rendered.container.querySelector<HTMLElement>(
                '.main-page__parameters'
            );
        expect(parametersContainer).not.toBeNull();

        if (!parametersContainer) {
            throw new Error('Контейнер .main-page__parameters не найден');
        }

        expect(updateCategories).toHaveBeenCalledTimes(0);
        expect(applyCategories).toHaveBeenCalledTimes(1);

        fireEvent.click(within(parametersContainer).getByText('Электроника'));

        expect(updateCategories).toHaveBeenCalledTimes(1);
        expect(applyCategories).toHaveBeenCalledTimes(2);
    });
});
