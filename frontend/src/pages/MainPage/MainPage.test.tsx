import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
    
});


import { screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { useCurrentTime, useProducts } from '../../hooks';
import { applyCategories, getPrice, updateCategories } from '../../utils';
import { Product } from '../../types';

jest.mock('../../hooks', () => ({
    useCurrentTime: jest.fn(),
    useProducts: jest.fn().mockReturnValue([
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
        },])
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn(),
    updateCategories: jest.fn(),
    getPrice: jest.fn()
}));

describe('MainPage', () => {
    beforeEach(() => {
        (useCurrentTime as jest.Mock).mockReturnValue('12:00:00');
        jest.mocked(useProducts).mockReturnValue([
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
        ]);

        (applyCategories as jest.Mock).mockImplementation((products, categories) =>
            products.filter((product: any ) => categories.includes(product.category))
        );
        (updateCategories as jest.Mock).mockImplementation(
            (selectedCategories, clickedCategory) => {
                if (selectedCategories.includes(clickedCategory)) {
                    return selectedCategories.filter((cat: any) => cat !== clickedCategory);
                }
                return [...selectedCategories, clickedCategory];
            }
        );
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    it('should render all products by default', () => {
        render(<MainPage />);

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
        expect(screen.getByText('Настольная лампа')).toBeInTheDocument();
        expect(screen.getByText('Принтер')).toBeInTheDocument();
    });

    it('should filter products when a category is selected', () => {
        render(<MainPage />);

        fireEvent.click(screen.getByText('Электроника'));

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Принтер')).toBeInTheDocument();
        expect(screen.queryByText('Костюм гуся')).not.toBeInTheDocument();
        expect(screen.queryByText('Настольная лампа')).not.toBeInTheDocument();
    });

    it('should update selected categories on category click', () => {
        render(<MainPage />);

        fireEvent.click(screen.getByText('Одежда'));
        expect(updateCategories).toHaveBeenCalledWith([], 'Одежда');

        fireEvent.click(screen.getByText('Электроника'));
        expect(updateCategories).toHaveBeenCalledWith(['Одежда'], 'Электроника');
    });
});